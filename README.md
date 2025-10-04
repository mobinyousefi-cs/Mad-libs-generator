# Mad Libs Generator

A polished Python **Mad Libs** app with both **CLI** and **Tkinter GUI**.  
Pick a story, fill in prompts (noun, verb, adjective, food, etc.), and generate a funny story.

## Features
- ✅ Multiple built-in stories with metadata (title, difficulty, tags)
- ✅ Dynamic prompt extraction & validation
- ✅ CLI (`madlibs` command) and GUI (`python -m madlibs.gui`)
- ✅ Save final story to a text file
- ✅ `src/` layout, tests with `pytest`, Ruff + Black linting, GitHub Actions CI
- ✅ MIT License

## Quickstart
```bash
# Python 3.10+ recommended
python -m venv .venv && . .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .                               # dev install from pyproject
# OR: pip install -r requirements.txt

# Run CLI
madlibs --list
madlibs --story "Space Picnic"
madlibs --story "Space Picnic" --set noun=rocket verb="zoom" food="sandwich"

# Run GUI
python -m madlibs.gui
