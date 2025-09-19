import typer
from .llm import bash_helper

# create a typer app instance
app = typer.Typer()

@app.callback()
def callback():
    """
    Entry point for the CLI application.
    """
    pass

@app.command()
def input_query(
    query: str,
    model: str = typer.Option("ollama", help="Specify the LLM to use: 'cohere' or 'ollama'"),
    ollama_model: str = typer.Option("llama3", help="Ollama model to use: 'llama3' or 'tinyllama'")
):
    """
    Processes a user query to generate a Bash command.
    """
    if model not in ["cohere", "ollama"]:
        print(f"Error: Invalid model specified. Choose 'cohere' or 'ollama'.")
        return
    if model == "ollama" and ollama_model not in ["llama3", "tinyllama"]:
        print(f"Error: Invalid Ollama model. Choose 'llama3' or 'tinyllama'.")
        return

    response = bash_helper(query, model=ollama_model, llm_type=model)
    print(f"Query: {query}")
    print(f"Response: {response}")

def main(name: str):
    """
    Standalone function to greet the user by name.
    """
    print(f"Hello {name}")

if __name__ == "__main__":
    app()


# --------------------------------------------------------------------------------------------

# version 2

# import the Typer library for building CLI applications
# import typer
# from .llm import chat_with_cohere, chat_with_ollama

# # Create a Typer app instance
# app = typer.Typer()


# @app.callback()
# def callback():
#     """
#     Entry point for the CLI application.
#     This function is called before any subcommand is executed.
#     """
#     pass  # No global options or setup needed for now


# @app.command()
# def input_query(
#     query: str,
#     model: str = typer.Option("cohere", help="Specify the model to use: 'cohere' or 'ollama'."),
# ):
#     """
#     Example command that greets the user by name.

#     Args:
#         name (str): The name to greet.
#     """
#     if model == "cohere":
#         response = chat_with_cohere(query)
#     elif model == "ollama":
#         response = chat_with_ollama(query)
#     else:
#         print(f"Error: Invalid model specified. Choose 'cohere' or 'ollama'.")
#         return

#     print(f"Query: {query}")
#     print(f"Response: {response}")


# def main(name: str):
#     """
#     Standalone function to greet the user by name.

#     Args:
#         name (str): The name to greet.
#     """
#     print(f"Hello {name}")


# # If this script is run directly, launch the Typer CLI app
# if __name__ == "__main__":
#     app()


# ---------------------------------------------------------------------------------------------

# initial version
# # Import the Typer library for building CLI applications
# import typer
# from .llm import chat_with_llm

# # Create a Typer app instance
# app = typer.Typer()


# @app.callback()
# def callback():
#     """
#     Entry point for the CLI application.
#     This function is called before any subcommand is executed.
#     """
#     pass  # No global options or setup needed for now


# @app.command()
# def input_query(query: str):
#     """
#     Example command that greets the user by name.

#     Args:
#         name (str): The name to greet.
#     """
#     response = chat_with_llm(query)
#     print(f"Query: {query}")
#     print(f"Response: {response.message.content[0].text}")


# def main(name: str):
#     """
#     Standalone function to greet the user by name.

#     Args:
#         name (str): The name to greet.
#     """
#     print(f"Hello {name}")


# # If this script is run directly, launch the Typer CLI app
# if __name__ == "__main__":
#     app()

# # Running it: python cli.py command1 your_name
