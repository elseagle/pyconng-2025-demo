"""Writer agent for content creation."""

from autogen import AssistantAgent
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import WRITER_CONFIG, WRITER_SYSTEM_MESSAGE


def create_writer_agent() -> AssistantAgent:
    return AssistantAgent(
        name="Writer",
        system_message=WRITER_SYSTEM_MESSAGE,
        llm_config=WRITER_CONFIG,
        max_consecutive_auto_reply=3,
        human_input_mode="NEVER",
    )
