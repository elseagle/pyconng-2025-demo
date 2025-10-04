"""
Knowledge base tools for research.
Simple, local tools without external API dependencies.
"""

from typing import Dict, List, Any


# Simple in-memory knowledge base for demo purposes
KNOWLEDGE_BASE = {
    "python_asyncio": {
        "title": "Python Asyncio Basics",
        "key_points": [
            "asyncio is Python's built-in library for writing concurrent code using async/await syntax",
            "async def defines a coroutine function that can be awaited",
            "await keyword pauses execution until the awaited operation completes",
            "asyncio.run() is the entry point to run async programs",
            "Useful for I/O-bound operations like network requests, file operations",
            "Not helpful for CPU-bound tasks (use multiprocessing instead)",
        ],
        "examples": [
            "async def fetch_data():\n    await asyncio.sleep(1)\n    return 'data'",
            "asyncio.run(main())",
        ],
        "common_pitfalls": [
            "Forgetting to await a coroutine",
            "Mixing blocking and non-blocking code",
            "Not using asyncio-compatible libraries",
        ],
    },
    "autogen_agents": {
        "title": "AutoGen Multi-Agent Systems",
        "key_points": [
            "AutoGen enables building conversational multi-agent systems",
            "Each agent has a role, system message, and optional tools",
            "GroupChat orchestrates turn-taking between agents",
            "Agents can be Assistants (LLM-powered) or UserProxyAgents (human/code executors)",
            "Tool calling allows agents to invoke Python functions",
            "Human-in-the-loop patterns enhance safety and control",
        ],
        "examples": [
            "AssistantAgent for planning and reasoning",
            "UserProxyAgent for executing code and human input",
        ],
        "common_pitfalls": [
            "Too many agents causing confusion",
            "Unclear system messages leading to poor coordination",
            "No maximum round limits causing infinite loops",
        ],
    },
    "machine_learning": {
        "title": "Machine Learning Fundamentals",
        "key_points": [
            "ML is a subset of AI focused on learning from data",
            "Supervised learning uses labeled data (classification, regression)",
            "Unsupervised learning finds patterns in unlabeled data (clustering)",
            "Features are input variables, labels are outputs",
            "Training involves optimizing model parameters to minimize error",
            "Evaluation uses metrics like accuracy, precision, recall, F1-score",
        ],
        "examples": [
            "Linear regression for price prediction",
            "Decision trees for classification",
            "K-means for customer segmentation",
        ],
        "common_pitfalls": [
            "Overfitting to training data",
            "Insufficient or biased training data",
            "Not preprocessing or normalizing features",
        ],
    },
    "api_design": {
        "title": "RESTful API Design Best Practices",
        "key_points": [
            "REST uses HTTP methods: GET (read), POST (create), PUT/PATCH (update), DELETE",
            "Resources are nouns in URLs (e.g., /users, /posts)",
            "Status codes communicate outcomes (200 OK, 404 Not Found, 500 Error)",
            "Versioning ensures backward compatibility (e.g., /v1/users)",
            "Authentication via tokens (JWT, OAuth)",
            "Pagination for large datasets",
        ],
        "examples": [
            "GET /api/v1/users?page=1&limit=20",
            "POST /api/v1/users with JSON body",
            "PUT /api/v1/users/123 to update user",
        ],
        "common_pitfalls": [
            "Using verbs in URLs (e.g., /getUser)",
            "Inconsistent naming conventions",
            "Exposing internal implementation details",
        ],
    },
    "docker_basics": {
        "title": "Docker Containerization Basics",
        "key_points": [
            "Docker packages applications with dependencies into containers",
            "Containers are lightweight, portable, and isolated",
            "Dockerfile defines the container image",
            "Images are built from Dockerfiles, containers run from images",
            "docker-compose orchestrates multi-container applications",
            "Volumes persist data outside containers",
        ],
        "examples": [
            "FROM python:3.10\nCOPY . /app\nRUN pip install -r requirements.txt",
            "docker build -t myapp .",
            "docker run -p 8000:8000 myapp",
        ],
        "common_pitfalls": [
            "Large image sizes due to unnecessary layers",
            "Running containers as root user",
            "Not using .dockerignore to exclude files",
        ],
    },
}


def search_knowledge_base(topic: str) -> Dict[str, Any]:
    """
    Search the knowledge base for information on a given topic.

    This is a read-only, safe tool with no side effects.

    Args:
        topic: The topic to search for (e.g., "python_asyncio", "autogen_agents")

    Returns:
        Dictionary with title, key_points, examples, and common_pitfalls
        Returns error message if topic not found
    """
    topic_normalized = topic.lower().replace(" ", "_").replace("-", "_")

    # Try exact match first
    if topic_normalized in KNOWLEDGE_BASE:
        return {
            "success": True,
            "topic": topic,
            "data": KNOWLEDGE_BASE[topic_normalized],
        }

    # Try partial match
    for key, value in KNOWLEDGE_BASE.items():
        if topic_normalized in key or key in topic_normalized:
            return {"success": True, "topic": topic, "data": value}

    # List available topics if not found
    available_topics = list(KNOWLEDGE_BASE.keys())
    return {
        "success": False,
        "topic": topic,
        "error": f"Topic '{topic}' not found in knowledge base.",
        "available_topics": available_topics,
        "suggestion": "Try one of the available topics or rephrase your query.",
    }


def get_writing_guidelines(content_type: str = "technical_blog") -> Dict[str, Any]:
    """
    Get writing guidelines for different content types.

    This is a read-only tool providing style and structure recommendations.

    Args:
        content_type: Type of content (technical_blog, tutorial, documentation, email)

    Returns:
        Dictionary with structure, style, and checklist guidelines
    """
    guidelines = {
        "technical_blog": {
            "structure": [
                "1. Engaging title",
                "2. Brief introduction (the 'why')",
                "3. Main content with clear sections",
                "4. Code examples with explanations",
                "5. Common pitfalls or gotchas",
                "6. Conclusion and key takeaways",
            ],
            "style": {
                "tone": "Professional yet conversational",
                "sentence_length": "Mix short and medium sentences",
                "code_snippets": "Always include context and output",
                "headings": "Use descriptive, scannable headings",
            },
            "checklist": [
                "Clear target audience?",
                "Code tested and functional?",
                "Jargon explained?",
                "Logical flow?",
                "Actionable takeaways?",
            ],
        },
        "tutorial": {
            "structure": [
                "1. What you'll build",
                "2. Prerequisites",
                "3. Step-by-step instructions",
                "4. Testing/verification",
                "5. Next steps or extensions",
            ],
            "style": {
                "tone": "Patient and encouraging",
                "sentence_length": "Short, clear instructions",
                "code_snippets": "Complete, runnable code",
                "headings": "Action-oriented (e.g., 'Install Dependencies')",
            },
            "checklist": [
                "Prerequisites clearly stated?",
                "Every step tested?",
                "Screenshots or examples?",
                "Troubleshooting section?",
                "Working final result?",
            ],
        },
        "documentation": {
            "structure": [
                "1. Overview/purpose",
                "2. API/function reference",
                "3. Parameters and return values",
                "4. Usage examples",
                "5. Error handling",
            ],
            "style": {
                "tone": "Formal and precise",
                "sentence_length": "Concise and direct",
                "code_snippets": "Minimal, focused examples",
                "headings": "Standardized format",
            },
            "checklist": [
                "All parameters documented?",
                "Types specified?",
                "Edge cases covered?",
                "Examples runnable?",
                "Version information included?",
            ],
        },
        "email": {
            "structure": [
                "1. Clear subject line",
                "2. Greeting",
                "3. Context (1-2 sentences)",
                "4. Main message",
                "5. Call to action",
                "6. Professional sign-off",
            ],
            "style": {
                "tone": "Professional and respectful",
                "sentence_length": "Short paragraphs",
                "code_snippets": "Link to docs instead",
                "headings": "Use bullet points for lists",
            },
            "checklist": [
                "Subject line descriptive?",
                "Purpose clear upfront?",
                "Proofread for errors?",
                "Next steps obvious?",
                "Appropriate tone?",
            ],
        },
    }

    if content_type in guidelines:
        return {
            "success": True,
            "content_type": content_type,
            "guidelines": guidelines[content_type],
        }
    else:
        return {
            "success": False,
            "error": f"Content type '{content_type}' not recognized.",
            "available_types": list(guidelines.keys()),
        }


# Tool schemas for AutoGen registration
TOOL_SCHEMAS = [
    {
        "name": "search_knowledge_base",
        "description": "Search the knowledge base for information on a topic. Returns key points, examples, and common pitfalls.",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "The topic to search (e.g., 'python asyncio', 'autogen agents', 'machine learning')",
                }
            },
            "required": ["topic"],
        },
    },
    {
        "name": "get_writing_guidelines",
        "description": "Get writing guidelines for specific content types including structure, style, and checklists.",
        "parameters": {
            "type": "object",
            "properties": {
                "content_type": {
                    "type": "string",
                    "enum": ["technical_blog", "tutorial", "documentation", "email"],
                    "description": "The type of content to get guidelines for",
                }
            },
            "required": ["content_type"],
        },
    },
]
