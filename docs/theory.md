## uv

uv is writtene in Rust It is created to replace `pip` `venv` `poerty`


```bash
uv venv                     # create new venv
uv add <package>            # add dependency and update pyproject.toml file
uv add --dev <package>      # add dependency for dev environment
uv sync                     # based on pyproject.toml and uv.lovk install dependencies
uv run <command>            # using venv you can run commands
uv lock                     # update uv.lock
```



## ruff

Linter + formatter

It was created to replace `flake8` + `isort` + `black`


* `E` - pycodestyle
* `F` - pyflakes (unused imports)
* `I` - isort
* `N` - Naming
* `S` - bandit


Usage

```bash
ruff check .            # checking
ruff check --fix .      # fixing errors
ruff format .           # format
```


## mypy 

Static type checker - checking types without running the application only looking type hunting


Usage 
```bash
mypy app/main.py
```



