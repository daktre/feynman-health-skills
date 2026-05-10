# Integration Guide: Adding Skills to Your Agent

This guide covers how to integrate the skills and tools from the `feynman-health-skills` repository into your independent Feynman agent.

### Step 1: Install the PubMed Tool
To allow your agent to use the PubMed connector, ensure the script is accessible as an executable tool.

```bash
# Ensure your agent's tools directory exists
mkdir -p ~/.feynman/tools/

# Copy the script and make it executable
cp pubmed_cli.py ~/.feynman/tools/pubmed_search
chmod +x ~/.feynman/tools/pubmed_search
```

### Step 2: Update Agent Configuration
Open your agent's configuration file (e.g., `~/.feynman/config.json`) and add the `pubmed_search` tool definition:

```json
{
  "tools": {
    "pubmed_search": {
      "command": "~/.feynman/tools/pubmed_search",
      "description": "Searches PubMed for health literature. Requires a query string."
    }
  }
}
```

### Step 3: Add Skills to your Agent
Your agent automatically detects skills by scanning its skill directory. Simply copy the `.md` files into that directory:

```bash
# 1. Ensure the directory exists
mkdir -p ~/.feynman/agent/skills/

# 2. Copy the skill files
cp hpsr-epistemology.md ~/.feynman/agent/skills/
cp pubmed-research.md ~/.feynman/agent/skills/
```

Restart your Feynman agent for the changes to take effect.
