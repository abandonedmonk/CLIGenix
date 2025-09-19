import cohere
import os
import requests
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM

load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# Initialize the Cohere client
co = cohere.ClientV2(COHERE_API_KEY)

# System prompt for command generation
SYSTEM_PROMPT = """
You are a command generator. Given a user question about the command line, respond with ONLY the most concise and accurate CLI command. 
Do not include explanations, extra text or unrelated filters (e.g. specific file extensions unless requested). 
If unsure, output: SEARCH_NEEDED: <query>
"""

# ollama_llm = OllamaLLM(model="tinyllama")

def query_ollama(prompt: str, model: str = "llama3"):
    """
    Sends a query to a local LLM running on Ollama and returns the response.
    """
    ollama_llm = OllamaLLM(model=model)
    full_prompt = f"{SYSTEM_PROMPT}\n{prompt}"
    return ollama_llm.invoke(full_prompt).strip()

def query_cohere(prompt: str):
    """
    Sends a query to the Cohere LLM and returns the response.
    """
    response = co.chat(
        model="command-r",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )
    return response.message.content[0].text

def serper_search(query: str, max_results: int = 3) -> list:
    """
    Performs a search using the Serper API and returns up to max_results snippets.
    """
    if not SERPER_API_KEY:
        raise ValueError("SERPER_API_KEY not found in .env")
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"}
    payload = {"q": query}
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    results = response.json().get("organic", [])[:max_results]
    return [item["snippet"] for item in results]

def bash_helper(query: str, model: str = "llama3", llm_type: str = "ollama") -> str:
    """
    Processes a user query to generate a Bash command, with a fallback to search if needed.
    """
    # Select LLM based on llm_type
    query_fn = query_ollama if llm_type == "ollama" else query_cohere
    llm_output = query_fn(query, model=model) if llm_type == "ollama" else query_fn(query)

    if llm_output.startswith("SEARCH_NEEDED:"):
        search_query = llm_output.replace("SEARCH_NEEDED:", "").strip()
        print(f"LLM is unsure, searching the web for: {search_query}")
        search_results = serper_search(search_query)
        print("Search results:", search_results)
        # Re-query LLM with search context
        enhanced_prompt = (
            f"User asked: {query}\n"
            f"Relevant snippets:\n{search_results}\n"
            f"Provide ONLY the exact Bash command, ensuring it is concise and accurate."
        )
        return query_fn(enhanced_prompt, model=model) if llm_type == "ollama" else query_fn(enhanced_prompt)
    
    return llm_output



# ------------------------------------------------------------------------

# version 2

# import cohere
# import os
# import requests
# from dotenv import load_dotenv
# import json
# from langchain_ollama import OllamaLLM

# load_dotenv()
# COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# # Initialize the Cohere client
# co = cohere.ClientV2(COHERE_API_KEY)

# # Initialize the Ollama client
# ollama_llm = OllamaLLM(model="tinyllama")

# prompt = """
#     You are a helpful assistant.
#     Given a user question about the command line, respond with the most appropriate and concise CLI command only.
#     Do not include explanations or extra text—just the command itself.
# """

# def chat_with_cohere(query: str):
#     """
#     Sends a query to the Cohere LLM and returns the response.
#     """
#     response = co.chat(
#         model="command-r",
#         messages=[
#             {"role": "system", "content": prompt},
#             {"role": "user", "content": query},
#         ],
#     )
#     # extract and return the response text
#     return response.message.content[0].text

# def chat_with_ollama(query: str):
#     """
#     Sends a query to a local LLM running on Ollama and returns the response.
#     """
    
#     # LangChain handles the API call
#     full_prompt = f"{prompt}\n{query}"
#     response = ollama_llm.invoke(full_prompt)
#     return response



    # url = "http://localhost:11434/api/generate"
    # data = {
    #     "model": "llama3", 
    #     "prompt": f"{prompt}\n{query}",
    # }
    # headers = {"Content-Type": "application/json"}
    # response = requests.post(url, json=data, headers=headers)
    # response.raise_for_status() # Raise an exception for bad status codes
    # # Ollama returns a stream of JSON objects, we need to parse the last one
    # response_lines = response.text.strip().split("\n")
    # response_json = [json.loads(line) for line in response_lines]
    # return response_json[-1]["response"]


# ---------------------------------------------------------------------------------

# initial version
# import cohere
# import os
# from dotenv import load_dotenv

# load_dotenv()
# # Get the API key from environment variable for security
# COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# # Initialize the Cohere client
# co = cohere.ClientV2(COHERE_API_KEY)

# prompt = """
#     You are a helpful assistant. 
#     Given a user question about the command line, respond with the most appropriate and concise CLI command only. 
#     Do not include explanations or extra text—just the command itself.
# """


# def chat_with_llm(query: str) -> str:
#     """
#     Sends a query to the Cohere LLM and returns the response.

#     Args:
#         query (str): The user's input query.

#     Returns:
#         str: The LLM's response.
#     """

#     response = co.chat(
#         model="command-r",
#         messages=[
#             {"role": "system", "content": prompt},
#             {"role": "user", "content": query},
#         ],
#     )
#     # Extract and return the response text
#     return response
