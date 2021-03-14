from pathlib import Path

from wordgoal.invoke import invoke, invoke_unsafe


def test_invoke__version() -> None:
    assert invoke(["--version"]) == 0


def test_invoke__invalid_path() -> None:
    assert invoke(["--path", "foo"]) == 1


def test_invoke_unsafe__version() -> None:
    assert invoke_unsafe(["--version"]) == "-1.-1.-1"


def test_invoke_unsafe() -> None:
    with open(Path(".").joinpath("tests").joinpath("this-project.out")) as stream:
        expect = stream.read()
    assert invoke_unsafe([]) + "\n" == expect
