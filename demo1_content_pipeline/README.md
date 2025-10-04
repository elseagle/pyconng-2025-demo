# Demo 1: Content Creation Pipeline

A beginner-friendly multi-agent system demonstrating collaborative content creation using AutoGen.

## What This Demo Shows

This demo illustrates key AutoGen concepts perfect for a live demonstration:

1. **Triage/Planning Pattern**: A Planner agent that acts as a coordinator
2. **Role Specialization**: Four distinct agents with clear responsibilities
3. **Tool Calling**: Simple, local knowledge base tools (no external APIs)
4. **Turn-Taking**: GroupChat orchestration with automatic speaker selection
5. **Quality Control**: Built-in review and approval workflow
6. **Structured Workflow**: Clear message protocols and termination signals

## Architecture

```
┌─────────────┐
│   Planner   │  ← Triage agent (coordinates workflow)
└──────┬──────┘
       │ Assigns tasks to specialists
       ├─────────────┬──────────────┬────────────┐
       ▼             ▼              ▼            ▼
┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐
│Researcher│  │  Writer  │  │  Critic  │  │  Admin  │
│(Tools)   │  │          │  │(Review)  │  │(Human)  │
└──────────┘  └──────────┘  └──────────┘  └─────────┘
```

### Agent Roles

1. **Planner** (Triage Agent)
   - Understands the content request
   - Breaks down tasks into steps
   - Assigns work to appropriate agents
   - Monitors progress and signals completion

2. **Researcher** (Worker Agent)
   - Uses `search_knowledge_base` tool to gather facts
   - Uses `get_writing_guidelines` for structure advice
   - Synthesizes findings into organized summaries
   - Passes structured research to Writer

3. **Writer** (Worker Agent)
   - Takes research findings as input
   - Creates well-structured, engaging content
   - Follows guidelines for the content type
   - Hands off to Critic for review

4. **Critic** (Review Agent)
   - Reviews content against guidelines and research
   - Checks accuracy, clarity, structure, style
   - Provides specific feedback or approves
   - Can request revisions if needed

5. **Admin** (UserProxy)
   - Executes tool calls on behalf of agents
   - Can provide human-in-the-loop oversight
   - Manages workflow initiation

## Key Features for Your Talk

### 1. Simple Tools (No External APIs)
- `search_knowledge_base`: Local knowledge lookup
- `get_writing_guidelines`: Style and structure recommendations
- Safe, read-only operations perfect for demos

### 2. Clear Message Protocol
- Agents communicate with structured messages
- Termination signals: "TASK_COMPLETE", "APPROVED"
- Easy to follow conversation flow

### 3. Configurable Behavior
- Temperature settings per role (Planner=0.3, Writer=0.8)
- Max rounds to prevent infinite loops
- Human-in-the-loop mode (change `human_input_mode`)

### 4. Observable Workflow
- Color-coded console output
- Clear section headers showing each phase
- Full conversation history visible

## Running the Demo

### Quick Start

```bash
# From the project root
poetry install
poetry run python demo1_content_pipeline/main.py
```

### Step-by-Step

1. **Install dependencies**:
   ```bash
   poetry install
   ```

2. **Configure your LLM** (create `.env` in project root):
   ```env
   OPENAI_API_KEY=your_api_key_here
   MODEL_NAME=gpt-4
   MAX_ROUNDS=12
   ```

3. **Run the demo**:
   ```bash
   poetry run python demo1_content_pipeline/main.py
   ```

4. **Watch the agents collaborate**! 🎉

## Customizing for Your Demo

### Change the Topic
Edit `DEMO_TOPIC` in `main.py`:
```python
DEMO_TOPIC = "Docker containerization basics"  # Pick from knowledge base
```

### Change Content Type
```python
CONTENT_TYPE = "tutorial"  # Options: technical_blog, tutorial, documentation, email
```

### Add New Topics to Knowledge Base
Edit `tools/knowledge_tools.py` and add to `KNOWLEDGE_BASE`:
```python
KNOWLEDGE_BASE = {
    "your_topic": {
        "title": "Your Topic Title",
        "key_points": [...],
        "examples": [...],
        "common_pitfalls": [...]
    }
}
```

### Enable Human-in-the-Loop
In `main.py`, change:
```python
human_input_mode="NEVER"  →  human_input_mode="ALWAYS"
```

### Adjust Temperature
In `config.py`, modify agent configs:
```python
WRITER_CONFIG = {
    **LLM_CONFIG,
    "temperature": 0.9,  # More creative
}
```

## File Structure

```
demo1_content_pipeline/
├── main.py                 # Entry point and orchestration
├── config.py               # LLM configs and system messages
├── README.md               # This file
├── agents/                 # Agent definitions
│   ├── __init__.py
│   ├── planner.py         # Triage/coordinator
│   ├── researcher.py      # Info gatherer with tools
│   ├── writer.py          # Content creator
│   └── critic.py          # Quality reviewer
└── tools/                  # Tool implementations
    ├── __init__.py
    └── knowledge_tools.py  # Simple knowledge base
```

## What Happens During Execution

1. **Setup Phase**
   - Creates 4 specialized agents + Admin
   - Registers tools with Researcher
   - Configures GroupChat with all participants

2. **Workflow Phase**
   - Admin sends initial task to Planner
   - Planner analyzes and assigns to Researcher
   - Researcher calls `search_knowledge_base` tool
   - Researcher summarizes findings
   - Planner assigns to Writer
   - Writer creates content using research
   - Planner assigns to Critic
   - Critic reviews and either approves or requests revisions
   - If revisions needed, Writer updates content
   - Planner announces "TASK_COMPLETE"

3. **Completion**
   - Termination signal detected
   - GroupChat ends
   - Summary displayed

## Live Demo Tips

### Before the Demo
- ✅ Test with your API key
- ✅ Choose a topic from the knowledge base
- ✅ Run once to see typical flow
- ✅ Note typical completion time (2-3 minutes)

### During the Demo
1. **Show the file structure first** - emphasize modularity
2. **Walk through agent definitions** - highlight system messages
3. **Show the tools** - emphasize simplicity (no external APIs)
4. **Run the demo** - let it complete or interrupt at interesting points
5. **Highlight key moments**:
   - When Planner assigns tasks
   - When Researcher calls tools
   - When Critic provides feedback
   - When termination signal is sent

### After the Demo
- Show how to customize (change topic, content type)
- Discuss temperature settings per role
- Mention human-in-the-loop patterns
- Connect to slides about orchestration patterns

## Troubleshooting

### "No module named 'autogen'"
```bash
poetry install
poetry shell  # Or use 'poetry run python ...'
```

### API Key Errors
Check `.env` file exists with valid `OPENAI_API_KEY`

### Agents Keep Looping
- Reduce `MAX_ROUNDS` in `.env`
- Strengthen termination signals in system messages
- Check `is_termination_message` function

### Tools Not Being Called
- Verify tool registration in `main.py`
- Check function schemas match tool signatures
- Ensure Researcher's `llm_config` includes functions

## Next Steps

After this demo, attendees can:
1. Modify agent system messages for different behaviors
2. Add new tools to the knowledge base
3. Change orchestration patterns (speaker selection)
4. Add more agents for additional roles
5. Implement human-in-the-loop at critical steps

## Connection to Your Slides

This demo directly illustrates concepts from:
- **Slide 3**: Agent components (role, policy, tools, messaging)
- **Slide 5**: AutoGen features (conversation, roles, tools, control)
- **Slide 8-9**: Demo flow matches your planned workflow
- **Slide 10**: Shows supervisor-worker + router patterns
- **Slide 11**: Safety via max rounds and controlled tools
- **Slide 13**: Turn-taking with GroupChatManager

Perfect for a beginner-friendly, code-first presentation! 🚀

