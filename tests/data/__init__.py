from pathlib import Path
from typing import Iterator

from yaml import safe_load


def get(suffix: str) -> Iterator[Path]:
    for path in Path(__file__).parent.iterdir():
        if path.suffix == suffix:
            yield path


def expect_count(path: Path) -> int:
    with open(path.with_suffix(".yml"), "r") as stream:
        return int(safe_load(stream)["count"])
