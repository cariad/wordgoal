from pathlib import Path

from mock import Mock, patch
from pytest import mark

from wordgoal.directory import Directory


@patch("wordgoal.directory.words_in_markdown_file", return_value=3)
@patch("wordgoal.directory.words_in_text_file", return_value=7)
def test_analyse_file__markdown(
    words_in_text_file: Mock,
    words_in_markdown_file: Mock,
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
    words_in_markdown_file.assert_called_with(file)
    words_in_text_file.assert_not_called()


@patch("wordgoal.directory.words_in_markdown_file", return_value=3)
@patch("wordgoal.directory.words_in_text_file", return_value=7)
def test_analyse_file__text(
    words_in_text_file: Mock,
    words_in_markdown_file: Mock,
) -> None:
    root = Path(".")
    file = root.joinpath("foo.txt")

    append = Mock()
    rows = Mock()
    rows.append = append

    directory = Directory(root)
    with patch.object(directory, "rows", rows):
        directory.analyse_file(file)

    append.assert_called_with(name="foo.txt", current=7, maximum=600)
    words_in_markdown_file.assert_not_called()
    words_in_text_file.assert_called_with(file)


@patch("wordgoal.directory.words_in_markdown_file", return_value=3)
@patch("wordgoal.directory.words_in_text_file", return_value=7)
def test_analyse_file__unhandled(
    words_in_text_file: Mock,
    words_in_markdown_file: Mock,
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
    words_in_markdown_file.assert_not_called()
    words_in_text_file.assert_not_called()


def test_analyse_path__directory() -> None:
    with patch("wordgoal.directory.Directory.analyse_file") as analyse_file:
        directory = Directory(Path("."))
        path = directory.directory.joinpath("wordgoal")

        with patch("wordgoal.directory.Directory") as directory_maker:
            directory.analyse_path(path)
            analyse_file.assert_not_called()
            directory_maker.assert_called_with(directory=path, parent=directory)


def test_analyse_path__file() -> None:
    with patch("wordgoal.directory.Directory.analyse_file") as analyse_file:
        directory = Directory(Path("."))
        path = directory.directory.joinpath("Pipfile")

        with patch("wordgoal.directory.Directory") as directory_maker:
            directory.analyse_path(path)
            analyse_file.assert_called_with(path)
            directory_maker.assert_not_called()


def test_analyse_path__ignored() -> None:
    with patch("wordgoal.directory.Directory.analyse_file") as analyse_file:
        directory = Directory(Path("."))

        with patch("wordgoal.directory.Directory") as directory_maker:
            directory.analyse_path(Path(".").joinpath(".git"))
            analyse_file.assert_not_called()
            directory_maker.assert_not_called()


def test_analyse_path__special() -> None:
    with patch("wordgoal.directory.Directory.analyse_file") as analyse_file:
        directory = Directory(Path("."))
        path = Mock()
        path.is_dir = Mock(return_value=False)
        path.is_file = Mock(return_value=False)

        with patch("wordgoal.directory.Directory") as directory_maker:
            directory.analyse_path(path)
            analyse_file.assert_not_called()
            directory_maker.assert_not_called()


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
    root = Directory(Path(__file__).parent)
    assert Directory(root.directory.joinpath("wordgoal"), root).root == root.directory


def test_root__root() -> None:
    root_path = Path(__file__).parent
    root_dir = Directory(root_path)
    assert root_dir.root == root_path
    assert Directory(root_path.joinpath("wordgoal"), root_dir).root == root_path


@patch("wordgoal.directory.Directory.analyse_path")
def test_walk(analyse_path: Mock) -> None:
    root = Path(".")
    Directory(root).walk()
    analyse_path.assert_any_call(root.joinpath("wordgoal"))
    analyse_path.assert_any_call(root.joinpath("Pipfile"))
