"""Entry point for the Claude Code starter project."""


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    if not name.strip():
        raise ValueError("name must not be empty")
    return f"Hello, {name.strip()}. Claude Code is ready."


def main() -> None:
    """Run the starter program."""
    print(greet("Muhammad"))


if __name__ == "__main__":
    main()
