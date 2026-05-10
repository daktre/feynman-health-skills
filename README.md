# Feynman Health Skills

A collection of domain-specific skills, tools, and epistemological frameworks designed to turn your Feynman agent into a robust Health Policy and Systems Research (HPSR) engine.

## Features
- **PubMed CLI Connector:** Direct integration with NCBI databases to fetch clinical and epidemiological evidence.
- **Enhanced HPSR Epistemology:** A formal evidence-assessment framework that mandates confidence scoring and source categorization.
- **Modular Skills Index:** A structured way to manage agent capabilities.

## Quick Start: Integrating with your Feynman Agent

These skills are designed to live alongside your existing Feynman agent configuration.

### 1. Clone this Repository
```bash
git clone https://github.com/daktre/feynman-health-skills.git
cd feynman-health-skills
```

### 2. Configure the PubMed CLI Tool
To allow your agent to use the PubMed connector, link the script to your agent's tools directory and make it executable:

```bash
# Ensure your agent's tools directory exists
mkdir -p ~/.feynman/tools/

# Copy/Link the script
cp pubmed_cli.py ~/.feynman/tools/pubmed_search
chmod +x ~/.feynman/tools/pubmed_search
```

### 3. Register the Skill
Follow the [Detailed Integration Guide](./docs/INTEGRATION.md) to register these skills and the tool within your agent's configuration files.

## HPSR Epistemology
Health Policy and Systems Research (HPSR) operates with a different epistemology from clinical medicine. This skill teaches the agent to retrieve, evaluate, and synthesise HPSR evidence with explicit **Evidence Confidence Scoring** (High/Medium/Low).

## Roadmap
- [ ] Implementation of **WHO IRIS / Cochrane REST API** connectors.
- [ ] Development of **Policy Writer** and **Grey Literature Appraisal** skills.
