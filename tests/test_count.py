from pathlib import Path
from typing import Iterator, Optional

from pytest import mark
from yaml import safe_load

from wordgoal.count import words_in_markdown_file, words_in_string, words_in_text_file


def documents(suffix: str) -> Iterator[Path]:
    for path in Path(__file__).parent.joinpath("documents").iterdir():
        if path.suffix == suffix:
            yield path


def expect(path: Path) -> int:
    with open(path.with_suffix(".yml"), "r") as stream:
        return int(safe_load(stream)["count"])


@mark.parametrize(
    "line, expect",
    [
        (None, 0),
        ("", 0),
        (" ", 0),
        ("foo", 1),
        ("foo bar", 2),
        ("\n", 0),
        (" \n", 0),
        ("\n ", 0),
        (" \n ", 0),
        ("foo\n", 1),
        ("\nfoo", 1),
        ("foo\nbar", 2),
    ],
)
def test_words_in_string(line: Optional[str], expect: int) -> None:
    assert words_in_string(line) == expect


def test_words_in_markdown_file() -> None:
    for path in documents(".md"):
        assert words_in_markdown_file(path) == expect(path)


def test_words_in_text_file() -> None:
    for path in documents(".txt"):
        assert words_in_text_file(path) == expect(path)
