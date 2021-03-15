from pytest import mark

from tests.data import expect_count, get
from wordgoal.documents.text import words_in_string, words_in_text


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
def test_words_in_string(line: str, expect: int) -> None:
    assert words_in_string(line) == expect


def test_words_in_text() -> None:
    for path in get(".txt"):
        assert words_in_text(path) == expect_count(path)
