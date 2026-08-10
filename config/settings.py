import os

# ===========================
# OpenAI Configuration
# ===========================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY not found. Please configure it in your Windows Environment Variables."
    )

MODEL_NAME = "gpt-4o-mini"
TEMPERATURE = 0
MAX_TOKENS = 1000