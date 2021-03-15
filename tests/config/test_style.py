from pytest import mark

from wordgoal.config import Style


@mark.parametrize(
    "style, expect",
    [
        (Style(parent=None, values=None), True),
        (
            Style(
                parent=Style(parent=None, values={"color": True}),
                values=None,
            ),
            True,
        ),
        (
            Style(
                parent=Style(parent=None, values={"color": False}),
                values=None,
            ),
            False,
        ),
        (
            Style(
                parent=Style(parent=None, values={"color": False}),
                values={"color": True},
            ),
            True,
        ),
        (
            Style(
                parent=Style(parent=None, values={"color": True}),
                values={"color": False},
            ),
            False,
        ),
    ],
)
def test_color(style: Style, expect: int) -> None:
    assert style.color == expect


@mark.parametrize(
    "style, expect",
    [
        (Style(parent=None, values=None), True),
        (
            Style(
                parent=Style(parent=None, values={"fractions": True}),
                values=None,
            ),
            True,
        ),
        (
            Style(
                parent=Style(parent=None, values={"fractions": False}),
                values=None,
            ),
            False,
        ),
        (
            Style(
                parent=Style(parent=None, values={"fractions": False}),
                values={"fractions": True},
            ),
            True,
        ),
        (
            Style(
                parent=Style(parent=None, values={"fractions": True}),
                values={"fractions": False},
            ),
            False,
        ),
    ],
)
def test_fractions(style: Style, expect: int) -> None:
    assert style.fractions == expect


@mark.parametrize(
    "style, expect",
    [
        (Style(parent=None, values=None), False),
        (
            Style(
                parent=Style(parent=None, values={"percentages": True}),
                values=None,
            ),
            True,
        ),
        (
            Style(
                parent=Style(parent=None, values={"percentages": False}),
                values=None,
            ),
            False,
        ),
        (
            Style(
                parent=Style(parent=None, values={"percentages": False}),
                values={"percentages": True},
            ),
            True,
        ),
        (
            Style(
                parent=Style(parent=None, values={"percentages": True}),
                values={"percentages": False},
            ),
            False,
        ),
    ],
)
def test_percentages(style: Style, expect: int) -> None:
    assert style.percentages == expect
