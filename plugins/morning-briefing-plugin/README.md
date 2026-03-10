# /morning-briefing

A Claude Code skill that generates a concise morning news briefing from RSS feeds, covering local (Philadelphia), US, world, and finance news.

## What it does

Fetches headlines from 10 RSS sources across four categories, then uses Claude to distill them into a scannable 2-minute briefing — no opinion pieces, no filler, just what happened and why it matters.

## Prerequisites

- [Claude Code](https://code.claude.com) installed and authenticated
- Python 3 (uses only standard library — no packages to install)

## Installation

Copy the skill to your personal skills directory:

```bash
mkdir -p ~/.claude/skills/morning-briefing
cp SKILL.md feeds.json fetch_feeds.py ~/.claude/skills/morning-briefing/
```

Restart Claude Code to pick up the new skill.

## Usage

```
/morning-briefing              # Full briefing (all categories)
/morning-briefing finance      # Finance only
/morning-briefing local        # Philadelphia news only
/morning-briefing us           # US news only
/morning-briefing world        # World news only
```

## Sources

| Category | Sources |
|----------|---------|
| Local (Philadelphia) | 6ABC Philadelphia, WHYY |
| US News | NPR, AP News, NBC News |
| World News | BBC World, NYT Top Stories |
| Finance | MarketWatch, CNBC Business, Yahoo Finance |

## Customization

Edit `feeds.json` to add, remove, or swap sources. The format is:

```json
{
  "category": [
    {"name": "Display Name", "url": "https://example.com/rss/feed.xml"}
  ]
}
```

Any standard RSS or Atom feed URL will work. You can also add new categories — the skill will pick them up automatically.

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Skill instructions for Claude |
| `feeds.json` | Configurable list of RSS feed sources |
| `fetch_feeds.py` | Python script that fetches and parses RSS feeds |

## How it selects stories

The feed fetcher pulls ~80+ headlines from all sources. Claude then curates them down to 10-12 stories using these criteria:

1. **Impact first** — Each section leads with the story that affects the most people. A war driving oil prices and markets ranks above a local school renaming debate.

2. **Deduplication** — Major stories appear across multiple feeds (e.g., a breaking news event might show up in NPR, AP, NBC, BBC, and NYT). These are merged into a single entry rather than repeated.

3. **What gets included**:
   - Breaking news and developing stories
   - Policy changes that affect daily life
   - Major market-moving events
   - Local stories with direct community impact

4. **What gets filtered out**:
   - Opinion and editorial pieces
   - Listicles and lifestyle articles
   - Celebrity and entertainment news
   - Personal finance advice columns
   - Promotional content and event listings
   - Individual stock picks and earnings transcripts
   - Sports (unless historically significant)

5. **Local relevance** — For the local section, stories are prioritized by direct community impact: public safety, infrastructure, and policy over curiosities and feel-good stories.

6. **Finance signal vs. noise** — Broader economic trends and market-moving events are prioritized over individual company analysis or investment advice.

The goal: if someone reads this in 2 minutes over coffee, they walk away knowing the 10-12 things actually worth knowing today.

## Example output

```
# Morning Briefing — Tuesday, March 10, 2026

## Local (Philadelphia)
- **FBI detonations in Bucks County**: Three controlled detonations at a storage
  facility connected to an alleged terror plot.
- **Deadly Germantown crash**: Two teenagers killed in a multi-vehicle crash.

## US News
- **Trump sends mixed signals on Iran war**: No clear end date given despite
  claiming the war is "very complete."
...

📊 Markets: Dow, S&P 500, and Nasdaq wavering; oil sliding.
```
