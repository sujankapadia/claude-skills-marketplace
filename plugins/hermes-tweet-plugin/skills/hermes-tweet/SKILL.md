---
name: hermes-tweet
description: Use Hermes Agent for X/Twitter social listening, account context, and approval-gated actions through Hermes Tweet.
disable-model-invocation: true
argument-hint: "[workflow]"
---

Use Hermes Tweet when a Claude Code session needs to hand off X/Twitter work to
Hermes Agent. Hermes Tweet is the native Hermes Agent plugin published as
`hermes-tweet` and maintained at <https://github.com/Xquik-dev/hermes-tweet>.

## Install

Install and enable the plugin in the Hermes runtime:

```bash
hermes plugins install Xquik-dev/hermes-tweet --enable
```

If the plugin package is already installed but disabled:

```bash
hermes plugins enable hermes-tweet
```

Hermes can also install the Python package from PyPI:

```bash
uv pip install --python ~/.hermes/hermes-agent/venv/bin/python hermes-tweet
hermes plugins enable hermes-tweet
```

## Configure

Set the API key only in the Hermes runtime environment:

```bash
export XQUIK_API_KEY="<your-xquik-api-key>"
```

Keep account-changing actions disabled unless the current session needs them:

```bash
export HERMES_TWEET_ENABLE_ACTIONS="false"
```

## Workflow

1. Start with `tweet_explore` to find the right catalog path.
2. Use `tweet_read` for search, account, trend, monitor, media, and draw reads.
3. Use `tweet_action` only after a human approves posting, replies, DMs,
   follows, webhooks, monitors, or media changes.
4. Never paste API keys into prompts, issues, PR comments, or chat messages.

## Good fits

- Morning or launch briefings that need current X/Twitter signal.
- Brand, creator, competitor, trend, or account research.
- Support triage from public mentions and timelines.
- Giveaway, follower, reply, list, and media audits.
- Controlled publishing sessions with explicit action enablement.
