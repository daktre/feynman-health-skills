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

This is the big ask. If you know Python or Node.js and want to build a CLI wrapper around NCBI E-utilities (esearch + efetch), this would unblock a lot of functionality.

Spec sketch:

```bash
pubmed search --query "malaria AND India" --limit 50 --output json
pubmed fetch --pmid 12345678 --format full
```

Output: JSON with title, authors, abstract, PMID, publication date, journal.

Interested? Open an issue or email hello@daktre.com to discuss.

## New skills

If you think there should be a skill for `grey-literature`, `policy-writing`, or something else HPSR-specific, open an issue with what you think it should teach the agent.

## Code of conduct

Be respectful. This is a small, research-focused project. We're here to make tooling better for health systems work, not to fight.
