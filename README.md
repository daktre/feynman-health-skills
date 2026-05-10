# feynman-health-skills

Skills, tools, and epistemological frameworks to make [Feynman](https://github.com/getcompanion-ai/feynman) useful for public health and Health Policy and Systems Research (HPSR) work.

## The problem

[Feynman](https://github.com/getcompanion-ai/feynman) is a powerful AI research agent designed for general research, relying heavily on [AlphaXiv](https://www.alphaxiv.org) (arXiv). While excellent for computer science, physics, and quantitative biology, it lacks a native understanding of health databases.

For researchers in public health, epidemiology, or health policy, this default behavior is inadequate. This repository provides the necessary skills and tools to bridge that gap.

## What's in the box

- **PubMed CLI Connector (`pubmed_cli.py`):** Direct integration with NCBI databases to fetch clinical and epidemiological evidence.
- **Enhanced HPSR Epistemology (`hpsr-epistemology.md`):** A formal evidence-assessment framework that mandates explicit **Evidence Confidence Scoring** (High/Medium/Low) and **Source Categorization**.
- **Modular Skills Index (`skills_index.yaml`):** A structured way to manage and trigger agent capabilities based on research context.

## Prerequisites

You need [Feynman](https://github.com/getcompanion-ai/feynman) installed. See [Feynman's installation guide](https://github.com/getcompanion-ai/feynman?tab=readme-ov-file#installation) for setup.

## Quick Start: Integrating with your Feynman Agent

1. **Clone this Repository:**
   ```bash
   git clone https://github.com/daktre/feynman-health-skills.git
   cd feynman-health-skills
   ```

2. **Configure the PubMed CLI Tool:**
   Make the script accessible as a tool for your agent:
   ```bash
   mkdir -p ~/.feynman/tools/
   cp pubmed_cli.py ~/.feynman/tools/pubmed_search
   chmod +x ~/.feynman/tools/pubmed_search
   ```

3. **Register Skills:**
   Copy the skill Markdown files into your agent's skills directory:
   ```bash
   mkdir -p ~/.feynman/agent/skills/
   cp hpsr-epistemology.md ~/.feynman/agent/skills/
   cp pubmed-research.md ~/.feynman/agent/skills/
   ```

For detailed setup, see [docs/INTEGRATION.md](./docs/INTEGRATION.md).

## Why these skills matter

### [`pubmed-research.md`](./pubmed-research.md)
Tells Feynman to query PubMed first. Teaches it MeSH term logic, study design quality appraisal, and how to weight evidence from low- and middle-income countries (LMICs) appropriately.

### [`hpsr-epistemology.md`](./hpsr-epistemology.md)
Teaches the agent that qualitative studies, mixed-methods designs, and implementation science papers are first-class evidence. It enforces strict **Evidence Confidence Scoring** (High/Medium/Low) to ensure reliable synthesis, and treats grey literature (WHO reports, government documents) as a primary source.

## Roadmap

### Short-term
- `grey-literature.md` skill — explicitly prioritise WHO IRIS, MoHFW, NHSRC, NFHS, parliamentary reports.
- `reviewer-appraisal.md` skill — CASP checklists, Cochrane risk-of-bias, GRADE framing.

### Medium-term
- WHO IRIS connector (OAI-PMH).
- Cochrane REST API wrapper.

### Longer-term
- Local document ingestion (curated Indian health policy materials, institutional PDFs).
- New workflows: `/sysrev`, `/policybrief`, `/appraise`, `/burden`, `/greylit`.

## Affiliation

Built at [IPH Bengaluru](https://www.iphbengaluru.res.in) as part of broader work on AI tooling for health systems research.

## License

MIT. Do what you want with these, including fork and modify. No attribution required, though nice if you mention where it came from.

## See also

- [Full project thinking](https://notes.daktre.com/6.-Index/feynman-health-fork)
- [Original Feynman repo](https://github.com/getcompanion-ai/feynman)
