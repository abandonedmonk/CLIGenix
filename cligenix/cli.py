# Import the Typer library for building CLI applications
import typer
from llm import chat_with_llm

# Create a Typer app instance
app = typer.Typer()


@app.callback()
def callback():
    """
    Entry point for the CLI application.
    This function is called before any subcommand is executed.
    """
    pass  # No global options or setup needed for now


@app.command()
def input_query(query: str):
    """
    Example command that greets the user by name.

    Args:
        name (str): The name to greet.
    """
    response = chat_with_llm(query)
    print(f"Query: {query}")
    print(f"Response: {response.message.content[0].text}")


def main(name: str):
    """
    Standalone function to greet the user by name.

    Args:
        name (str): The name to greet.
    """
    print(f"Hello {name}")


# If this script is run directly, launch the Typer CLI app
if __name__ == "__main__":
    app()

# Running it: python cli.py command1 your_name
