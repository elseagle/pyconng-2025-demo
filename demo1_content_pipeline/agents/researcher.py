"""Researcher agent with knowledge base access."""

from autogen import AssistantAgent
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import RESEARCHER_CONFIG, RESEARCHER_SYSTEM_MESSAGE


def create_researcher_agent() -> AssistantAgent:
    return AssistantAgent(
        name="Researcher",
        system_message=RESEARCHER_SYSTEM_MESSAGE,
        llm_config=RESEARCHER_CONFIG,
        max_consecutive_auto_reply=5,
        human_input_mode="NEVER",
    )
