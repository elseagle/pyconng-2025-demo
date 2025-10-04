"""Multi-agent content creation pipeline using AutoGen."""

import sys
import warnings
import logging

warnings.filterwarnings(
    "ignore", message=".*API key specified is not a valid OpenAI format.*"
)
warnings.filterwarnings("ignore", message=".*Model .* is not found.*")
warnings.filterwarnings("ignore", message=".*flaml.automl is not available.*")
warnings.filterwarnings("ignore", category=UserWarning, module="flaml")

from termcolor import colored
from autogen import UserProxyAgent, GroupChat, GroupChatManager

logging.getLogger("autogen.oai.client").setLevel(logging.ERROR)

from agents import (
    create_planner_agent,
    create_researcher_agent,
    create_writer_agent,
    create_critic_agent,
)
from tools.knowledge_tools import search_knowledge_base, get_writing_guidelines
from config import MAX_ROUNDS, LLM_CONFIG, SHOW_COLORS


def print_header(text: str, color: str = "cyan") -> None:
    if SHOW_COLORS:
        print("\n" + colored("=" * 70, color))
        print(colored(f"  {text}", color, attrs=["bold"]))
        print(colored("=" * 70, color) + "\n")
    else:
        print("\n" + "=" * 70)
        print(f"  {text}")
        print("=" * 70 + "\n")


def print_section(text: str, color: str = "yellow") -> None:
    if SHOW_COLORS:
        print(colored(f"\n{'─' * 70}", color))
        print(colored(f"  {text}", color, attrs=["bold"]))
        print(colored(f"{'─' * 70}\n", color))
    else:
        print(f"\n{'─' * 70}")
        print(f"  {text}")
        print(f"{'─' * 70}\n")


def is_termination_message(message: dict) -> bool:
    content = message.get("content", "").upper()
    termination_signals = [
        "TASK_COMPLETE",
        "APPROVED - CONTENT MEETS QUALITY STANDARDS",
        "WORKFLOW COMPLETE",
    ]
    return any(signal in content for signal in termination_signals)


def create_user_proxy() -> UserProxyAgent:
    user_proxy = UserProxyAgent(
        name="Admin",
        system_message="A human administrator overseeing the content creation process.",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=0,
        is_termination_msg=is_termination_message,
        code_execution_config=False,
    )
    return user_proxy


def register_tools(user_proxy: UserProxyAgent, agents: list) -> None:
    for agent in agents:
        if agent.name == "Researcher":
            user_proxy.register_function(
                function_map={
                    "search_knowledge_base": search_knowledge_base,
                    "get_writing_guidelines": get_writing_guidelines,
                }
            )

            if agent.llm_config:
                agent.llm_config["functions"] = [
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
                                    "enum": [
                                        "technical_blog",
                                        "tutorial",
                                        "documentation",
                                        "email",
                                    ],
                                    "description": "The type of content to get guidelines for",
                                }
                            },
                            "required": ["content_type"],
                        },
                    },
                ]


def setup_group_chat(agents: list, user_proxy: UserProxyAgent) -> GroupChat:
    all_agents = agents + [user_proxy]
    group_chat = GroupChat(
        agents=all_agents,
        messages=[],
        max_round=MAX_ROUNDS,
        speaker_selection_method="auto",
    )
    return group_chat


def run_content_pipeline(topic: str, content_type: str = "technical_blog") -> None:
    print_header("AutoGen Multi-Agent Content Creation Pipeline", "cyan")

    print(f"Topic: {colored(topic, 'green', attrs=['bold'])}")
    print(f"Content Type: {colored(content_type, 'green', attrs=['bold'])}")
    print(f"Max Rounds: {colored(MAX_ROUNDS, 'green', attrs=['bold'])}\n")

    print_section("Creating Agents...", "yellow")

    planner = create_planner_agent()
    print(f"✓ {colored('Planner Agent', 'green')} - Coordinates workflow")

    researcher = create_researcher_agent()
    print(f"✓ {colored('Researcher Agent', 'green')} - Gathers information")

    writer = create_writer_agent()
    print(f"✓ {colored('Writer Agent', 'green')} - Creates content")

    critic = create_critic_agent()
    print(f"✓ {colored('Critic Agent', 'green')} - Reviews quality")

    user_proxy = create_user_proxy()
    print(f"✓ {colored('Admin (UserProxy)', 'green')} - Executes tools & oversees")

    agents = [planner, researcher, writer, critic]

    print_section("Registering Tools...", "yellow")
    register_tools(user_proxy, agents)
    print(f"✓ Registered {colored('search_knowledge_base', 'green')} tool")
    print(f"✓ Registered {colored('get_writing_guidelines', 'green')} tool")

    print_section("Setting Up Group Chat...", "yellow")
    group_chat = setup_group_chat(agents, user_proxy)

    manager = GroupChatManager(
        groupchat=group_chat,
        llm_config=LLM_CONFIG,
    )
    print(
        f"✓ Group chat configured with {colored(f'{len(agents) + 1}', 'green')} participants"
    )

    print_section("Starting Multi-Agent Workflow...", "magenta")

    initial_message = f"""We need to create a {content_type} about: {topic}

Please coordinate the team to:
1. Research the topic thoroughly using available tools
2. Create well-structured, engaging content
3. Review and ensure quality standards are met

Let's begin!"""

    print(f"Initial message to Planner:\n{colored(initial_message, 'white')}\n")

    try:
        user_proxy.initiate_chat(
            manager,
            message=initial_message,
        )
    except Exception as e:
        print(colored(f"\n⚠️  Error during execution: {e}", "red"))
        print(colored("This might be due to missing API key or configuration.", "red"))
        sys.exit(1)

    print_section("Workflow Complete!", "green")
    print(f"✓ Total rounds: {colored(len(group_chat.messages), 'green')}")
    print(f"✓ Check the conversation above for the final content")
    print(f"\n{'═' * 70}\n")


def main():
    import os

    print_header("Demo 1: Content Creation Pipeline", "cyan")
    if not os.getenv("OPENAI_API_KEY"):
        print(colored("Warning: OPENAI_API_KEY not found in environment", "yellow"))
        print(colored("Create a .env file with your API key:", "yellow"))
        print(colored("  OPENAI_API_KEY=your_key_here\n", "white"))
        print(colored("Or export it:", "yellow"))
        print(colored("  export OPENAI_API_KEY='your_key_here'\n", "white"))

        response = input(
            colored("Continue anyway to see the structure? (y/n): ", "cyan")
        )
        if response.lower() != "y":
            sys.exit(0)

    DEMO_TOPIC = "Python asyncio basics"
    CONTENT_TYPE = "technical_blog"

    print(colored("\nAvailable topics:", "cyan", attrs=["bold"]))
    print(colored("  1. Python asyncio basics", "white"))
    print(colored("  2. AutoGen agents", "white"))
    print(colored("  3. Machine learning fundamentals", "white"))
    print(colored("  4. RESTful API design", "white"))
    print(colored("  5. Docker containerization basics", "white"))

    try:
        choice = input(
            colored("\nChoose topic (1-5) or press Enter for default [1]: ", "cyan")
        )
        topics = [
            "Python asyncio basics",
            "AutoGen agents",
            "Machine learning fundamentals",
            "RESTful API design",
            "Docker containerization basics",
        ]
        if choice and choice.isdigit() and 1 <= int(choice) <= 5:
            DEMO_TOPIC = topics[int(choice) - 1]
    except (EOFError, KeyboardInterrupt):
        print(colored("\nUsing default topic...", "yellow"))

    print(f"\n{colored('Workflow:', 'cyan', attrs=['bold'])}")
    print(f"  - Planner acts as coordinator")
    print(f"  - Researcher gathers information using tools")
    print(f"  - Writer creates content based on research")
    print(f"  - Critic reviews and provides feedback")
    print(f"  - GroupChatManager orchestrates turn-taking\n")

    try:
        input(colored("Press Enter to start the demo...", "cyan"))
    except (EOFError, KeyboardInterrupt):
        print(colored("\nStarting demo automatically...\n", "cyan"))

    run_content_pipeline(topic=DEMO_TOPIC, content_type=CONTENT_TYPE)

    print(colored("\nDemo complete!", "green", attrs=["bold"]))
    print(colored("Check the conversation above for results.", "green"))
    print(colored("\nCustomization options:", "cyan"))
    print(colored("  - Change DEMO_TOPIC for different subjects", "white"))
    print(colored("  - Modify CONTENT_TYPE for different formats", "white"))
    print(colored("  - Edit agent system messages in config.py", "white"))
    print(colored("  - Adjust MAX_ROUNDS in .env", "white"))


if __name__ == "__main__":
    main()
