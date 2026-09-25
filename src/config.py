"""
Chunk 2: LLM setup.

TODO:
- Load ANTHROPIC_API_KEY from .env using python-dotenv (load_dotenv()).
- Instantiate a ChatAnthropic client from langchain_anthropic with:
    model="claude-sonnet-4-5" (or your assigned model), temperature=0.1
  Low temperature matters here: this agent must not "creatively" invent numbers.
- Export the client as `llm` so agent.py can import it.
"""

from dotenv import load_dotenv

load_dotenv()

# TODO: from langchain_anthropic import ChatAnthropic
# TODO: llm = ChatAnthropic(model=..., temperature=0.1)

DB_PATH = "data/budget.db"
CATEGORY_RULES_PATH = "data/category_rules.json"
BUDGET_TEMPLATES_PATH = "data/budget_templates.csv"
