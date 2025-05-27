
# Required installations
# pip install openai-agents
# pip install python-dotenv

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please define it in your .env file.")

# Gemini API client using OpenAI-style wrapper
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Define the model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Configuration
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# 🗣️ Translator Agent
translator = Agent(
    name="Translator Agent",
    instructions="""
    You are a professional translation agent. Your job is to translate any input text
    into the target language provided by the user. Maintain original tone and accuracy.
    
    Format: 
    Translate this into <language>: <text>
    
    Example:
    Translate this into French: Hello, how are you?
    """
)

# Example usage
response = Runner.run_sync(
    translator,
    input="Translate this into Franch: The future of AI is autonomous agents.",
    run_config=config
)

print(response.final_output)








