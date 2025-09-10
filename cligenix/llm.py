import cohere
import os
from dotenv import load_dotenv

load_dotenv()
# Get the API key from environment variable for security
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Initialize the Cohere client
co = cohere.ClientV2(COHERE_API_KEY)

prompt = """
    You are a helpful assistant. 
    Given a user question about the command line, respond with the most appropriate and concise CLI command only. 
    Do not include explanations or extra text—just the command itself.
"""


def chat_with_llm(query: str) -> str:
    """
    Sends a query to the Cohere LLM and returns the response.

    Args:
        query (str): The user's input query.

    Returns:
        str: The LLM's response.
    """

    response = co.chat(
        model="command-r",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": query},
        ],
    )
    # Extract and return the response text
    return response
