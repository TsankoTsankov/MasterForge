# Contributing to MasterForge

First off, thank you for considering contributing to MasterForge! It's people like you that make tools like this great.

## Getting Started
1.  **Fork** the repo on GitHub.
2.  **Clone** the project to your own machine.
3.  **Install dependencies**: `pip install -r requirements.txt`.
4.  **Run the app**: `streamlit run Home.py`.

## Adding a New Tool
We use a modular architecture. To add a new calculator:
1.  Create a new file in `tools/` (e.g., `tools/my_calc.py`).
2.  Define a `show()` function that contains your Streamlit code.
3.  Import your module in `Home.py`.
4.  Add a button in the dashboard to route to your new page.

## Code Style
* Keep logic separate from UI where possible.
* Add comments for complex math formulas.

## Found a Bug?
* **Ensure the bug was not already reported** by searching on GitHub under [Issues].
* If you're unable to find an open issue addressing the problem, open a new one.
