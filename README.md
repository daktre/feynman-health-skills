# feynman-health-skills

Skills to make [Feynman](https://github.com/getcompanion-ai/feynman) useful for public health and HPSR work.

## The problem

[Feynman](https://github.com/getcompanion-ai/feynman) is a genuinely good AI research agent. It searches, reads, synthesises, and drafts. But its entire source layer runs through [AlphaXiv](https://www.alphaxiv.org) (arXiv, basically), which means it knows about comp sci, physics, and quantitative biology. It does not know whether PubMed exists.

For people doing health policy and systems research, epidemiology, or qualitative work, this is unusable. The skills here fix that.

## What's in the box

### [`pubmed-research.md`](./pubmed-research.md)

Tells Feynman to query PubMed first. Teaches it MeSH term logic, study design quality appraisal, and how to weight evidence from low- and middle-income countries differently.

**Test run**: [ASHA programme effectiveness review](https://notes.daktre.com/6.-Index/Effectiveness-of-India's-ASHA-Programme) — pulled 19 sources, all appropriate (PubMed/PMC/grey, zero arXiv), correctly separated pilot evidence from routine programme evidence.

### [`hpsr-epistemology.md`](./hpsr-epistemology.md)

Teaches the agent that qualitative studies, mixed-methods designs, and implementation science papers are first-class evidence. Currently Feynman treats anything non-quantitative as fallback. That breaks HPSR work.

Also encodes that grey literature (WHO reports, government documents, NHSRC papers) is primary source, not supplementary. Context-sensitivity is a feature, not a weakness.

## What's NOT in the box

- **Subscription databases** (Embase, Web of Science, CINAHL, Ovid MEDLINE) are out of scope. Feynman can reach PubMed via free APIs; these require institutional access.
- **A PubMed CLI connector.** Feynman ships with an `alpha` CLI for AlphaXiv. We don't have the equivalent for PubMed yet. This is the next big piece of work (see [Roadmap](#roadmap) below).
- **New workflows.** Skills layer only. If you want `/sysrev`, `/policybrief`, `/appraise` — the code work is separate.

## Installation

Feynman stores skills as Markdown files in `~/.feynman/agent/skills/`. Clone or download this repo and copy the `.md` files there:

```bash
git clone https://github.com/daktre/feynman-health-skills.git
cp feynman-health-skills/*.md ~/.feynman/agent/skills/
```

Then run Feynman as usual. The agent will auto-detect the new skills.

```bash
feynman lit "your research question here"
feynman deepresearch "your topic"
```

The skills will activate automatically when they're relevant to your query.

## How to use these

This is just instructions. The agent decides when to apply them based on your query. If you ask about public health interventions, epidemiology, health systems, or policy, the skills trigger. If you ask about quantum computing, they don't (and Feynman reverts to its default arXiv-first behaviour).

See the [full feynman-health-fork note](https://notes.daktre.com/6.-Index/feynman-health-fork) for detailed thinking on epistemology, source selection, and what's planned next.

## Roadmap

### Short-term (validated)

- `grey-literature.md` skill — explicitly prioritise WHO IRIS, MoHFW, NHSRC, NFHS, parliamentary reports
- `reviewer-appraisal.md` skill — CASP checklists, Cochrane risk-of-bias, GRADE framing

### Medium-term (needs developer)

- **PubMed CLI connector** — wraps NCBI E-utilities (esearch + efetch). This is the structural blocker. If you know Python or Node.js and want to build this, get in touch.
- WHO IRIS connector (OAI-PMH)
- Cochrane REST API wrapper

### Longer-term (design phase)

- Local document ingestion (curated Indian health policy materials, institutional PDFs)
- New workflows: `/sysrev`, `/policybrief`, `/appraise`, `/burden`, `/greylit`

## For HPSR researchers

These skills won't replace protocol-driven systematic reviews (you need Embase, Web of Science, proper screening workflows — use Covidence or Rayyan for that). But they're useful for:

- Rapid evidence reviews
- Scoping review preliminary searches
- Building context sections for grants
- Understanding what's actually published on a health systems topic
- Separating pilot/special intervention evidence from routine programme findings

## Feedback wanted

From HPSR practitioners: Does this actually help? What's missing? What's wrong?

From developers: Is the PubMed CLI something you'd want to build? What would help?

Drop issues on GitHub or email hello@daktre.com.

## Affiliation

Built at [IPH Bengaluru](https://iph.org.in) as part of broader work on AI tooling for health systems research.

## License

MIT. Do what you want with these, including fork and modify. No attribution required, though nice if you mention where it came from.

## See also

- [Full project thinking](https://notes.daktre.com/6.-Index/feynman-health-fork)
- [Original Feynman repo](https://github.com/getcompanion-ai/feynman)
- [ASHA programme test run](https://notes.daktre.com/6.-Index/Effectiveness-of-India's-ASHA-Programme) and [provenance](https://notes.daktre.com/6.-Index/Provenance-Record-for-ASHA-Programme-Effectiveness-India)
