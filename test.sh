#!/bin/bash -e

li="\033[1;34m↪\033[0m "  # List item
ok="\033[0;32m✔️\033[0m "  # OK

echo -e "${li:?}Running tests..."
pytest

echo -e "${li:?}Running smoke test..."
python -m wordgoal --width 80 > smoke.out
cmp ./tests/this-project.out smoke.out
rm smoke.out

echo -e "${ok:?}OK!"
