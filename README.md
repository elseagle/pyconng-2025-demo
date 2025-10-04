# PyCon NG 2025: AutoGen Multi-Agent Systems Demos

**Speaker**: Oluwasogo Ogundowole  
**Talk**: Autogen 101: Building Your First Multi-Agent System

## Overview

This repository contains beginner-friendly demos showcasing how to build multi-agent systems using Microsoft AutoGen. Each demo illustrates core concepts like agent roles, tool calling, triage/planning, and collaborative workflows.

## Prerequisites

- Python 3.10+
- Poetry (for dependency management)
- OpenAI API key or compatible LLM endpoint

## Setup

1. **Install Poetry** (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. **Install dependencies**:
```bash
poetry install
```

3. **Configure your LLM**:
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_api_key_here
# Or use a local model endpoint
# OPENAI_API_BASE=http://localhost:11434/v1
```

## Demo 1: Content Creation Pipeline

**Location**: `demo1_content_pipeline/`

A multi-agent system for collaborative content creation with role-based specialization.

### Agents

1. **Planner** (Triage): Breaks down content requests into actionable steps
2. **Researcher**: Gathers relevant information using knowledge base tools
3. **Writer**: Creates content based on research findings
4. **Critic**: Reviews content for accuracy, clarity, and quality

### Key Features

- ✅ Simple, no external API dependencies (uses local knowledge base)
- ✅ Clear role separation and triage pattern
- ✅ Tool calling with function schemas
- ✅ Human-in-the-loop for final approval
- ✅ Message protocol with structured turn-taking

### Run the Demo

```bash
poetry run python demo1_content_pipeline/main.py
```

### What to Expect

The system will:
1. Accept a content topic (e.g., "Python async/await basics")
2. Planner decomposes the task and assigns to Researcher
3. Researcher queries knowledge base for relevant facts
4. Writer drafts content based on research
5. Critic reviews and suggests improvements (if needed)
6. System outputs final content with audit trail

## Demo 2: Customer Support Triage _(Coming Soon)_

**Location**: `demo2_customer_support/`

A multi-agent customer support system that routes inquiries to specialized agents.

## Key Concepts Demonstrated

### 1. Agent Roles
Each agent has a clear responsibility, policy (LLM + rules), and tools.

### 2. Triage Pattern
The Planner agent acts as a router, decomposing tasks and assigning to appropriate specialists.

### 3. Tool Design
- **Read-only tools**: Safe knowledge lookups (e.g., `search_knowledge_base`)
- **Action tools**: Side-effect operations with approval gates (e.g., `publish_content`)

### 4. Turn-Taking
GroupChatManager orchestrates who speaks next based on:
- Message content and context
- Agent capabilities and current state
- Custom selection policies

### 5. Safety & Control
- Max rounds to prevent infinite loops
- Human-in-the-loop for critical decisions
- Structured message protocols for predictability

## Project Structure

```
PYCONNG_2025/
├── pyproject.toml              # Poetry dependency management
├── README.md                   # This file
├── .env                        # LLM configuration (create this)
├── demo1_content_pipeline/     # Demo 1: Content creation
│   ├── main.py                 # Entry point
│   ├── config.py               # LLM and agent configuration
│   ├── agents/                 # Agent definitions
│   │   ├── planner.py
│   │   ├── researcher.py
│   │   ├── writer.py
│   │   └── critic.py
│   └── tools/                  # Tool implementations
│       └── knowledge_tools.py
└── demo2_customer_support/     # Demo 2 (future)
```

## Learning Resources

- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [Last Year's Talk: Observability Tools for LLMs](https://youtube.com/...)
- [Speaker's X/LinkedIn](#)

## Troubleshooting

### "No module named 'autogen'"
Run `poetry install` to install dependencies, then use `poetry run python ...` or `poetry shell` to activate the environment.

### Rate limits or API errors
- Reduce `max_consecutive_auto_reply` in agent configs
- Add delays between turns
- Use a local model (Ollama, LM Studio) to avoid API costs

### Agents not collaborating properly
- Check agent system messages for clarity
- Review speaker selection logic in GroupChatManager
- Ensure message protocols are consistent

## License

MIT License - Feel free to use for learning and teaching!

---

**Questions?** Reach out to Oluwasogo Ogundowole at [email] or [@handle]

