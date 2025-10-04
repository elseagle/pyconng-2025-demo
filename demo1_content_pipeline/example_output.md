# Example Output - Content Creation Pipeline

This file shows what you can expect to see when running the demo.

## Console Output (Abbreviated)

```
======================================================================
  🤖 AutoGen Multi-Agent Content Creation Pipeline
======================================================================

📝 Topic: Python asyncio basics
📄 Content Type: technical_blog
🔄 Max Rounds: 12

──────────────────────────────────────────────────────────────────────
  Creating Agents...
──────────────────────────────────────────────────────────────────────

✓ Planner Agent - Coordinates workflow
✓ Researcher Agent - Gathers information
✓ Writer Agent - Creates content
✓ Critic Agent - Reviews quality
✓ Admin (UserProxy) - Executes tools & oversees

──────────────────────────────────────────────────────────────────────
  Registering Tools...
──────────────────────────────────────────────────────────────────────

✓ Registered search_knowledge_base tool
✓ Registered get_writing_guidelines tool

──────────────────────────────────────────────────────────────────────
  Setting Up Group Chat...
──────────────────────────────────────────────────────────────────────

✓ Group chat configured with 5 participants

──────────────────────────────────────────────────────────────────────
  Starting Multi-Agent Workflow...
──────────────────────────────────────────────────────────────────────

Initial message to Planner:
We need to create a technical_blog about: Python asyncio basics

Please coordinate the team to:
1. Research the topic thoroughly using available tools
2. Create well-structured, engaging content
3. Review and ensure quality standards are met

Let's begin!

---

Admin (to chat_manager):
[Initial message sent]

---

Planner (to chat_manager):

Thank you for the assignment! I'll coordinate the team to create a high-quality 
technical blog post about Python asyncio basics.

Let me break this down:

**Plan:**
1. Researcher will gather comprehensive information on Python asyncio
2. Writer will create an engaging blog post based on the research
3. Critic will review for accuracy, clarity, and quality
4. Once approved, we'll deliver the final content

**Researcher**, please start by gathering information on "Python asyncio basics" 
using the search_knowledge_base tool. We need key concepts, examples, and common 
pitfalls.

---

Researcher (to chat_manager):

I'll search the knowledge base for information on Python asyncio basics.

***** Suggested tool call (call_abc123): search_knowledge_base *****
Arguments:
{
  "topic": "python asyncio"
}
******************************************************************

---

Admin (to chat_manager):

***** Response from calling tool (call_abc123) *****
{
  "success": true,
  "topic": "python asyncio",
  "data": {
    "title": "Python Asyncio Basics",
    "key_points": [
      "asyncio is Python's built-in library for writing concurrent code using async/await syntax",
      "async def defines a coroutine function that can be awaited",
      "await keyword pauses execution until the awaited operation completes",
      "asyncio.run() is the entry point to run async programs",
      "Useful for I/O-bound operations like network requests, file operations",
      "Not helpful for CPU-bound tasks (use multiprocessing instead)"
    ],
    "examples": [
      "async def fetch_data():\n    await asyncio.sleep(1)\n    return 'data'",
      "asyncio.run(main())"
    ],
    "common_pitfalls": [
      "Forgetting to await a coroutine",
      "Mixing blocking and non-blocking code",
      "Not using asyncio-compatible libraries"
    ]
  }
}
****************************************************

---

Researcher (to chat_manager):

Excellent! I've gathered comprehensive information on Python asyncio. Let me also 
get the writing guidelines for a technical blog post.

***** Suggested tool call (call_def456): get_writing_guidelines *****
Arguments:
{
  "content_type": "technical_blog"
}
*********************************************************************

---

Admin (to chat_manager):

***** Response from calling tool (call_def456) *****
{
  "success": true,
  "content_type": "technical_blog",
  "guidelines": {
    "structure": [...],
    "style": {...},
    "checklist": [...]
  }
}
****************************************************

---

Researcher (to chat_manager):

Perfect! I have all the information needed. Here's my research summary for the Writer:

**Research Summary: Python Asyncio Basics**

**Core Concepts:**
- asyncio is Python's built-in library for concurrent programming
- Uses async/await syntax for readable asynchronous code
- async def creates coroutine functions
- await pauses execution until operation completes
- asyncio.run() is the main entry point

**Use Cases:**
- I/O-bound operations (network requests, file I/O)
- NOT for CPU-bound tasks (use multiprocessing instead)

**Code Examples:**
```python
async def fetch_data():
    await asyncio.sleep(1)
    return 'data'

asyncio.run(main())
```

**Common Pitfalls:**
1. Forgetting to await coroutines
2. Mixing blocking and async code
3. Using non-async libraries

**Writer**, please use this research to create an engaging technical blog post 
following the guidelines for structure, tone, and code examples.

---

Writer (to chat_manager):

Thank you, Researcher! I'll create an engaging technical blog post based on your 
excellent research.

# Python Asyncio: Your Gateway to Concurrent Programming

Have you ever wondered how modern Python applications handle multiple tasks 
simultaneously without freezing up? The answer lies in `asyncio`, Python's 
powerful built-in library for asynchronous programming.

## What is Asyncio?

Asyncio is Python's solution for writing concurrent code using the elegant 
`async/await` syntax. Instead of waiting idly for I/O operations to complete, 
your program can juggle multiple tasks, making it perfect for network requests, 
file operations, and other I/O-bound workloads.

## Core Concepts Made Simple

### Defining Async Functions

Creating an asynchronous function is as simple as adding the `async` keyword:

```python
async def fetch_data():
    await asyncio.sleep(1)  # Simulates an I/O operation
    return 'data'
```

### The Power of await

The `await` keyword is where the magic happens. It tells Python, "Hey, this 
operation will take a while—feel free to do other things while waiting!"

### Running Your Async Code

To execute async functions, use `asyncio.run()` as your entry point:

```python
import asyncio

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())
```

## When Should You Use Asyncio?

✅ **Perfect for:**
- Network requests (API calls, web scraping)
- File I/O operations
- Database queries
- Any I/O-bound operations

❌ **Not suitable for:**
- CPU-intensive tasks (use multiprocessing instead)
- Simple scripts without I/O operations

## Common Pitfalls to Avoid

1. **Forgetting to await**: Without `await`, your coroutine won't execute
2. **Mixing blocking code**: Regular blocking calls will freeze your async code
3. **Using non-async libraries**: Ensure your dependencies support asyncio

## Key Takeaways

- Asyncio makes concurrent programming readable and maintainable
- Use it for I/O-bound operations, not CPU-bound tasks
- Master `async def`, `await`, and `asyncio.run()` as your foundation
- Watch out for common pitfalls like forgetting to await coroutines

Ready to make your Python applications more responsive? Start experimenting with 
asyncio in your next project!

**Critic**, I've completed the blog post. Please review it for accuracy, 
clarity, and adherence to technical blog guidelines.

---

Critic (to chat_manager):

Excellent work, Writer! I've reviewed the content carefully against our research 
and guidelines. Here's my assessment:

**Strengths:**
✓ Engaging title and opening hook
✓ Clear structure with logical flow
✓ Code examples are accurate and well-explained
✓ Appropriate use of visual indicators (✅ ❌)
✓ Covers all key points from research
✓ Includes common pitfalls section
✓ Strong conclusion with actionable takeaways
✓ Professional yet conversational tone

**Accuracy Check:**
✓ All technical details match the research
✓ Use cases correctly identified
✓ Pitfalls align with findings
✓ Code examples are functional

**Style Check:**
✓ Scannable headings
✓ Mix of short and medium sentences
✓ Code snippets include context
✓ Target audience clear (developers new to asyncio)

**APPROVED - Content meets quality standards**

The blog post is accurate, engaging, and follows best practices for technical 
content. It's ready for publication!

---

Planner (to chat_manager):

Excellent work, team! We've successfully completed the content creation workflow:

✅ Researcher gathered comprehensive, accurate information
✅ Writer created engaging, well-structured content
✅ Critic verified quality and approved

The technical blog post about Python asyncio basics is complete and meets all 
quality standards. The content is accurate, engaging, and follows best practices 
for technical blogging.

**TASK_COMPLETE**

──────────────────────────────────────────────────────────────────────
  Workflow Complete!
──────────────────────────────────────────────────────────────────────

✓ Total rounds: 8
✓ Check the conversation above for the final content

══════════════════════════════════════════════════════════════════════

🎉 Demo complete!
Check out the multi-agent conversation above!

Try modifying:
  • DEMO_TOPIC variable for different subjects
  • CONTENT_TYPE for different formats
  • Agent system messages in config.py
  • MAX_ROUNDS in .env or config.py
```

## What Just Happened?

### Message Flow

1. **Admin → Planner**: Initial task request
2. **Planner → Researcher**: Assignment to gather info
3. **Researcher → Admin**: Tool call for `search_knowledge_base`
4. **Admin → Researcher**: Tool execution results
5. **Researcher → Admin**: Tool call for `get_writing_guidelines`
6. **Admin → Researcher**: Tool execution results
7. **Researcher → Writer**: Research summary
8. **Writer → Critic**: Draft content for review
9. **Critic → Planner**: Approval message
10. **Planner → All**: TASK_COMPLETE signal

### Key Observations

- **Turn-taking**: GroupChatManager decides who speaks next
- **Tool execution**: Admin (UserProxy) executes tools on behalf of Researcher
- **Structured protocol**: Clear handoffs between agents
- **Termination**: "TASK_COMPLETE" signal ends the chat
- **Quality control**: Built-in review step before completion

## Customization Examples

### Try Different Topics

```python
# In main.py
DEMO_TOPIC = "Docker containerization basics"
# or
DEMO_TOPIC = "machine learning fundamentals"
# or
DEMO_TOPIC = "RESTful API design"
```

### Try Different Content Types

```python
CONTENT_TYPE = "tutorial"  # Step-by-step guide
# or
CONTENT_TYPE = "documentation"  # API reference style
# or
CONTENT_TYPE = "email"  # Professional email format
```

### Adjust Creativity

```python
# In config.py
WRITER_CONFIG = {
    "temperature": 0.9,  # More creative (default: 0.8)
}

PLANNER_CONFIG = {
    "temperature": 0.1,  # More deterministic (default: 0.3)
}
```

## Performance Notes

- **Typical runtime**: 2-3 minutes
- **Rounds used**: 6-10 (out of 12 max)
- **Tool calls**: 2 (search + guidelines)
- **Tokens**: ~3000-4000 (varies by model)
- **Cost**: ~$0.10-0.30 with GPT-4 (less with GPT-3.5)

## Demo Variations for Your Talk

### Variation 1: Show Tool Calling
Pause after Researcher calls `search_knowledge_base` and highlight the function call format.

### Variation 2: Show Revision Flow
Modify the Critic to request one revision, showing the feedback loop.

### Variation 3: Enable Human-in-the-Loop
Set `human_input_mode="ALWAYS"` and approve each step manually.

### Variation 4: Show Failure Handling
Request a topic not in the knowledge base to show error handling.

---

**Ready to run your own demo?**

```bash
poetry run python demo1_content_pipeline/main.py
```

