# Information

## Overview

This is a league match scoreboard calculation CLI application.

## Enviroment Setup

Create a local python virtual enviroment by following this [guide](https://realpython.com/lessons/creating-virtual-environment/) or you may install this globally, its up to you, but I recommend using a virtual enviroment.

## Development Setup

It is recommanded to install the required packages from `requirements.txt`.
as you may notice in this repo, there is a `requirements.in`, this file was used to generate the `requirements.txt`

these 2 files listed above was created using these 2 packages
```batch
pip3 install pipreqs
pip3 install pip-tools
```

Then it was generated using this command

```batch
pipreqs --savepath=requirements.in && pip-compile
```

# CLI COMMANDS

## Run CLI - version

```batch
python -m league -v
```

## Run CLI - set input file (output to file)

```batch
python -m league load scores.txt output.txt
```

## Run CLI - Unit Testing - Internal

```batch
python -m league test
```

## Run CLI - Unit Testing - Direct

```batch
python -m pytest tests/
```


# Testing and Other Information

A `sample_scores.txt` file is provided which can be used to test this CLI App with

also I'll be using a test suite called PyTest, the tests can be found in the `./test` directory
