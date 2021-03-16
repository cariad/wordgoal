from pathlib import Path

from mock import Mock, patch
from pytest import mark

from wordgoal.directory import Directory


@patch("wordgoal.directory.markdown_goal", return_value=600)
@patch("wordgoal.directory.words_in_markdown", return_value=3)
@patch("wordgoal.directory.words_in_text", return_value=7)
def test_analyse_file__markdown(
    words_in_text: Mock,
    words_in_markdown: Mock,
    markdown_goal: Mock,
) -> None:
    root = Path(".")
    file = root.joinpath("foo.md")

    append = Mock()
    rows = Mock()
    rows.append = append

    directory = Directory(root)
    with patch.object(directory, "rows", rows):
        directory.analyse_file(file)

    append.assert_called_with(name="foo.md", current=3, maximum=600)
    markdown_goal.assert_called_with(file)
    words_in_markdown.assert_called_with(file)
    words_in_text.assert_not_called()


@patch("wordgoal.directory.words_in_markdown", return_value=3)
@patch("wordgoal.directory.words_in_text", return_value=7)
def test_analyse_file__text(
    words_in_text: Mock,
    words_in_markdown: Mock,
) -> None:
    root = Path(".")
    file = root.joinpath("foo.txt")

    append = Mock()
    rows = Mock()
    rows.append = append

    directory = Directory(root)
    with patch.object(directory, "rows", rows):
        directory.analyse_file(file)

    append.assert_called_with(name="foo.txt", current=7, maximum=1000)
    words_in_markdown.assert_not_called()
    words_in_text.assert_called_with(file)


@patch("wordgoal.directory.words_in_markdown", return_value=3)
@patch("wordgoal.directory.words_in_text", return_value=7)
def test_analyse_file__unhandled(
    words_in_text: Mock,
    words_in_markdown: Mock,
) -> None:
    root = Path(".")
    file = root.joinpath("foo.bar")

    append = Mock()
    rows = Mock()
    rows.append = append

    directory = Directory(root)
    with patch.object(directory, "rows", rows):
        directory.analyse_file(file)

    append.assert_not_called()
    words_in_markdown.assert_not_called()
    words_in_text.assert_not_called()


@mark.parametrize(
    "directory, name, expect",
    [
        (Path("."), ".git", True),
        (Path("."), "foo", False),
        # The "wordgoal" directory has no configuration file, so no objects
        # should be ignored.
        (Path(".").joinpath("wordgoal"), ".git", False),
    ],
)
def test_ignore(directory: Path, name: str, expect: bool) -> None:
    assert Directory(directory).ignore(name) == expect


def test_root__child() -> None:
    root = Directory(Path(__file__).parent.parent)
    assert Directory(root.directory.joinpath("wordgoal"), root).root == root.directory


def test_root__root() -> None:
    root_path = Path(__file__).parent.parent
    root_dir = Directory(root_path)
    assert root_dir.root == root_path
    assert Directory(root_path.joinpath("wordgoal"), root_dir).root == root_path


@patch("wordgoal.directory.Directory.analyse_file")
def test_walk(analyse_file: Mock) -> None:
    root = Path(".")
    directory = Directory(root)

    with patch("wordgoal.directory.Directory") as directory_maker:
        directory.walk()

    directory_maker.assert_any_call(
        path=root.joinpath("wordgoal"),
        parent=directory,
    )
    analyse_file.assert_any_call(root.joinpath("Pipfile"))
