from pathlib import Path

from setuptools import setup

from wordgoal.version import get_version

readme_path = Path(__file__).parent.joinpath("README.md")

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "Environment :: Console",
    "Intended Audience :: Other Audience",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Text Processing",
    "Topic :: Utilities",
    "Typing :: Typed",
]

version = get_version()

if "a" in version:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in version:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@hey.com",
    classifiers=classifiers,
    description="Charts word count toward a goal",
    entry_points={
        "console_scripts": [
            "wordgoal=wordgoal.__main__:cli_entry",
        ],
    },
    include_package_data=True,
    install_requires=[
        "boringmd~=1.0",
        "progrow~=1.0",
    ],
    license="MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="wordgoal",
    packages=[
        "wordgoal",
    ],
    package_data={
        "wordgoal": ["py.typed"],
    },
    python_requires=">=3.8",
    url="https://github.com/cariad/wordgoal",
    version=version,
)
