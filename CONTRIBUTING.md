# Contributing

## Feedback from HPSR researchers

If you use these skills and find they work (or don't), tell us. Open an issue, send an email to hello@daktre.com, or just use the skills and report back informally.

Specifically helpful:
- Do the sources feel right for your work?
- Are there gaps in how the agent understands HPSR?
- Have you used this for a real research task? How did it go?

## Improving the skills

The `.md` files are the agent's instructions. If you think the instructions could be clearer, more accurate, or better targeted at HPSR work, suggest changes.

We're open to pull requests for skill rewrites, but start with an issue first so we can talk through what you're seeing.

## Building the PubMed CLI connector

**Status: Completed.**

This connector is now implemented in `pubmed_cli.py`, which wraps NCBI E-utilities (esearch + efetch) to output standardized JSON. 

*Note: Below was the original specification used for development.*

```bash
pubmed search --query "malaria AND India" --limit 50 --output json
pubmed fetch --pmid 12345678 --format full
```

If you are interested in extending this, please review the current implementation and open an issue to discuss enhancements.

## New skills

If you think there should be a skill for `grey-literature`, `policy-writing`, or something else HPSR-specific, open an issue with what you think it should teach the agent.

## Code of conduct

Be respectful. This is a small, research-focused project. We're here to make tooling better for health systems work, not to fight.
