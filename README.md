---
goal:
  words: 600
---
# wordgoal

![Build](https://github.com/cariad/wordgoal/actions/workflows/ci.yml/badge.svg) [![codecov](https://codecov.io/gh/cariad/wordgoal/branch/main/graph/badge.svg?token=1JBzUKfPGr)](https://codecov.io/gh/cariad/wordgoal)

`wordgoal` is a command line tool for graphing your word count toward a goal.

![wordgoal example](https://github.com/cariad/wordgoal/raw/main/example.png)

## Installation

`wordgoal` requires Python 3.8 or later.

```bash
pip install wordgoal
```

## Configuration

`wordgoal` reads configuration from a YAML file named `wordgoal.yml` inside each directory.

For an example, see the [wordgoal.yml](https://github.com/cariad/wordgoal/blob/main/wordgoal.yml) file for this project.

## Describing your word count goals

In order of precedence, a document's word count goal can be described by:

1. A Markdown document's goal can be described in its front matter:

    ```markdown
    ---
    goal:
      words: 400
    ---
    # My 400-word short story

    It was the best of times…
    ```

1. Any file's goal can be described in its directory's `wordgoal.yml`:

    ```yaml
    files:
      short-story.txt:
        goal: 2000
      long-story.txt:
        goal: 80000
    ```

1. To apply the same goal to all the files in a directory, set the default in that directory's `wordgoal.yml`:

    ```yaml
    default:
      goal: 2000
    ```

1. If neither a goal nor a default has been described for a file, a goal of 1,000 words will be assumed.

## Ignoring files and directories

`wordgoal` tracks the following files in each directory and subdirectory:

- `*.markdown`
- `*.md`
- `*.text`
- `*.txt`

To ignore a specific file or subdirectory, add its name to that directory's `wordgoal.yml`:

```yaml
ignore:
  - LICENCE.txt  # file
  - drafts       # subdirectory
```

## Styling the output

Styling options can be set in each directory's `wordgoal.yml`:

```yaml
style:
  fractions: true    # <current word count> / <goal>
  percentages: true
```

## Related packages

`wordgoal` uses:

- [cariad/boringmd](https://github.com/cariad/boringmd) to extract plain text and front matter from Markdown files.
- [cariad/progrow](https://github.com/cariad/progrow) to render progress bars.

## Thank you! 🎉

My name is **Cariad**, and I'm an [independent freelance DevOps engineer](https://cariad.io).

I'd love to spend more time working on projects like this, but--as a freelancer--my income is sporadic and I need to chase gigs that pay the rent.

If this project has value to you, please consider [☕️ sponsoring](https://github.com/sponsors/cariad) me. Sponsorships grant me time to work on _your_ wants rather than _someone else's_.

Thank you! ❤️
