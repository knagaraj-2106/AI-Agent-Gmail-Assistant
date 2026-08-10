"""
LLM Configuration

Creates a reusable GPT-4o-mini model instance
for the entire application.
"""

import os

from langchain_openai import ChatOpenAI


class LLMManager:
    """
    Singleton-style LLM Manager.
    """

    _llm = None

    @classmethod
    def get_llm(cls):

        if cls._llm is None:

            cls._llm = ChatOpenAI(
                model="gpt-4o-mini",
                temperature=0,
                api_key=os.getenv("OPENAI_API_KEY"),
            )

        return cls._llm


llm = LLMManager.get_llm()