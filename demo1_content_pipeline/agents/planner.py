"""Planner agent for workflow coordination."""

from autogen import AssistantAgent
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import PLANNER_CONFIG, PLANNER_SYSTEM_MESSAGE


def create_planner_agent() -> AssistantAgent:
    return AssistantAgent(
        name="Planner",
        system_message=PLANNER_SYSTEM_MESSAGE,
        llm_config=PLANNER_CONFIG,
        max_consecutive_auto_reply=10,
        human_input_mode="NEVER",
    )
