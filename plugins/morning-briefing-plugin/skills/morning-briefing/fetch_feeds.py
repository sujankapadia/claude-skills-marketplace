#!/usr/bin/env python3
"""Fetch RSS feeds and output a consolidated text summary for Claude to summarize."""

import json
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FEEDS_FILE = os.path.join(SCRIPT_DIR, "feeds.json")
MAX_ITEMS_PER_FEED = 8


def fetch_feed(url, timeout=15):
    """Fetch and parse an RSS feed, returning a list of article dicts."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read()
        root = ET.fromstring(data)
    except Exception as e:
        return [], str(e)

    articles = []
    # Standard RSS
    for item in root.iter("item"):
        title = item.findtext("title", "").strip()
        desc = item.findtext("description", "").strip()
        link = item.findtext("link", "").strip()
        pub = item.findtext("pubDate", "").strip()
        if title:
            # Strip HTML tags from description
            import re
            desc = re.sub(r"<[^>]+>", "", desc)
            if len(desc) > 300:
                desc = desc[:300] + "..."
            articles.append({"title": title, "description": desc, "link": link, "published": pub})

    # Atom fallback
    if not articles:
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        for entry in root.findall(".//atom:entry", ns):
            title = entry.findtext("atom:title", "", ns).strip()
            summary = entry.findtext("atom:summary", "", ns).strip()
            if title:
                articles.append({"title": title, "description": summary, "link": "", "published": ""})

    return articles[:MAX_ITEMS_PER_FEED], None


def main():
    categories = sys.argv[1:] if len(sys.argv) > 1 else None

    with open(FEEDS_FILE) as f:
        feeds = json.load(f)

    print(f"# News Briefing — {datetime.now().strftime('%A, %B %d, %Y %I:%M %p')}")
    print()

    for category, sources in feeds.items():
        if categories and category not in categories:
            continue

        label = {"local": "Local (Philadelphia)", "us": "US News", "world": "World News", "finance": "US Finance"}
        print(f"## {label.get(category, category.title())}")
        print()

        for source in sources:
            articles, error = fetch_feed(source["url"])
            if error:
                print(f"**{source['name']}**: ⚠ Feed unavailable ({error})")
                print()
                continue

            print(f"### {source['name']}")
            for art in articles:
                print(f"- **{art['title']}**")
                if art["description"]:
                    print(f"  {art['description']}")
            print()

    print("---")
    print("*Sources fetched from RSS feeds. Articles are from the last 24 hours.*")


if __name__ == "__main__":
    main()
