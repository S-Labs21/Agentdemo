from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import gemma as gm
from google.adk.models import Gemini
import os
from litellm import completion

os.environ["GEMINI_API_KEY"] = "your-api-key"

root_agent = Agent(
    name = "simple_chat",
    model=LiteLlm(model="gemini-1.5-flash"),

    description = "A simple conversational AI",
    instruction = "Your name is reno, you are a conversational AI, you will act as a chat buddy"
)
