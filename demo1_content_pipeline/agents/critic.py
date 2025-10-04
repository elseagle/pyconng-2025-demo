"""Critic agent for quality review."""

from autogen import AssistantAgent
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import CRITIC_CONFIG, CRITIC_SYSTEM_MESSAGE


def create_critic_agent() -> AssistantAgent:
    return AssistantAgent(
        name="Critic",
        system_message=CRITIC_SYSTEM_MESSAGE,
        llm_config=CRITIC_CONFIG,
        max_consecutive_auto_reply=3,
        human_input_mode="NEVER",
    )
