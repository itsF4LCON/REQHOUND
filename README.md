# reqhound

Track what your Python script actually imports at runtime, not what's installed.

## The problem

`pip freeze` dumps every package in your environment. `reqhound` only captures what your code actually uses.

## Install

pip install reqhound

## Usage

reqhound run myscript.py   # track imports at runtime
reqhound check             # diff against requirements.txt
reqhound export            # write a clean requirements.txt

## Example output

── reqhound results ──────────────────
  requests
  flask        ← missing from requirements.txt
  numpy        ← in requirements.txt but never imported
──────────────────────────────────────
  1 present  1 missing  1 unused

## Why not pip freeze?

pip freeze lists everything installed in your environment, often 50+ packages when your project uses 5. reqhound gives you a minimal, accurate dependency list based on runtime imports.

---
made by [itsF4LCON](https://github.com/itsf4lcon)