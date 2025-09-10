# Import the Typer library for building CLI applications
import typer

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
def command1(name: str):
    """
    Example command that greets the user by name.

    Args:
        name (str): The name to greet.
    """
    print(f"Hello {name}")


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
