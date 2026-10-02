import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from main import greet  # noqa: E402


def test_greet_returns_message():
    assert greet("Muhammad") == "Hello, Muhammad. Claude Code is ready."


def test_greet_strips_whitespace():
    assert greet("  Ali  ") == "Hello, Ali. Claude Code is ready."


def test_greet_rejects_empty():
    with pytest.raises(ValueError):
        greet("   ")
