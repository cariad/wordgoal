from pathlib import Path
from typing import Optional

from yaml import safe_load

from tests.data import expect_count, get
from wordgoal.documents.markdown import markdown_goal, words_in_markdown


def expect_goal(path: Path) -> Optional[int]:
    with open(path.with_suffix(".yml"), "r") as stream:
        goal = safe_load(stream)["goal"]
    return int(goal) if goal else None


def test_markdown_goal() -> None:
    for path in get(".md"):
        assert markdown_goal(path) == expect_goal(path)


def test_words_in_markdown() -> None:
    for path in get(".md"):
        assert words_in_markdown(path) == expect_count(path), path
