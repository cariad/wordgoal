#!/bin/bash -e

li="\033[1;34m↪\033[0m "  # List item
ok="\033[0;32m✔️\033[0m "  # OK

echo -e "${li:?}Building..."
echo "${1:--1.-1.-1}" > wordgoal/VERSION
rm -rf build
rm -rf dist
python setup.py bdist_wheel
rm -rf build

echo -e "${ok:?}OK!"
