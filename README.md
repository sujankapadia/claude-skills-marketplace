# sujan-skills

A Claude Code plugin marketplace with practical skills for daily life and productivity.

## Available Plugins

| Plugin | Command | Description |
|--------|---------|-------------|
| **morning-briefing** | `/sujan-skills:morning-briefing` | Concise morning news briefing from RSS feeds — local (Philadelphia), US, world, and finance |
| **umms-lunch-menu** | `/sujan-skills:umms-lunch-menu` | Check the Upper Merion Middle School lunch menu for today or a specific date |

## Installation

Add the marketplace:

```
/plugin marketplace add sujankapadia/claude-skills-marketplace
```

Install a plugin:

```
/plugin install morning-briefing@sujan-skills
/plugin install umms-lunch-menu@sujan-skills
```

## Prerequisites

- [Claude Code](https://code.claude.com) installed and authenticated
- Python 3 (standard library only — no packages to install)
- `poppler` for the lunch menu skill (`brew install poppler`)

## Plugin Details

### morning-briefing

Fetches headlines from 10 RSS sources across four categories (local Philadelphia, US, world, finance), then uses Claude to distill them into a scannable 2-minute briefing.

```
/sujan-skills:morning-briefing              # Full briefing
/sujan-skills:morning-briefing finance      # Finance only
/sujan-skills:morning-briefing local        # Local news only
```

See [morning-briefing README](plugins/morning-briefing-plugin/README.md) for full details on sources, customization, and how stories are selected.

### umms-lunch-menu

Fetches the monthly lunch menu PDF from the Upper Merion Area School District website, converts it to images, and reads the calendar to find what's being served on a given day.

```
/sujan-skills:umms-lunch-menu              # Today's menu
/sujan-skills:umms-lunch-menu March 15     # Specific date
```
