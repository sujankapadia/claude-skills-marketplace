---
name: morning-briefing
description: Get a brief morning news summary covering local Philadelphia, US, world, and finance news.
disable-model-invocation: true
argument-hint: "[category: local|us|world|finance]"
---

Generate a concise morning news briefing. If $ARGUMENTS specifies a category (local, us, world, finance), only include that section. Otherwise include all four.

## Steps

1. Run the feed fetcher script to pull the latest headlines:

```
python3 ${CLAUDE_SKILL_DIR}/fetch_feeds.py $ARGUMENTS
```

2. From the raw feed output, create a **brief, scannable summary** organized by section:

   - **Local (Philadelphia)**: 2-3 top stories
   - **US News**: 3-4 top stories
   - **World News**: 3-4 top stories
   - **US Finance**: 2-3 top stories, plus mention any major market moves

3. For each story, write **one sentence** — what happened, why it matters. No filler.

4. End with a one-line market snapshot if finance data is available (major indices, direction).

## Format

```
# Morning Briefing — [Day, Date]

## Local (Philadelphia)
- **headline**: one sentence summary
- **headline**: one sentence summary

## US News
- ...

## World News
- ...

## Finance
- ...

📊 Markets: [S&P/Dow/Nasdaq direction if available]
```

## Guidelines

- Keep the entire briefing under 400 words — this should be a 2-minute read
- Lead with the most impactful story in each section
- Skip duplicate stories that appear across multiple feeds
- Skip opinion pieces, listicles, and celebrity news
- Write in plain language — no jargon, no editorializing

## Feed configuration

Feeds are configured in [feeds.json](feeds.json). Edit that file to add, remove, or swap sources.
