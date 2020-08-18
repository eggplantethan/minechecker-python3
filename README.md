# MineChecker - Minecraft name checker

An simple easy way to check the availability of thousands of Minecraft accounts.

## Installation

Download the requests module using pip.

```bash
pip install requests
```

## Usage

1. Dump words/names separated by lines into `words.txt`.
2. Run `index.py`.
3. Words/names that have not been claimed will be added to `unclaimed.txt`.

This python script checks names with a one second interval because of rate limiting. Let the python script run for a few hours if you have a large list of words/names.

View example word lists in examples folder.
