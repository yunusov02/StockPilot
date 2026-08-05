## init uv

```bash
uv init
```

this command will initialize uv in current project 

after then we need to install some our dependencies

```bash
uv add fastapi uvicorn sqlalchemy asyncpg alembic pydantic-settings python-dotenv structlog
```

For test/dev we will create new group

```bash
uv add --dev pytest pytest-asyncio ruff mypy httpx factory-boy     
```

```bash
uv sync # synchronize code install dependencies
```



### ruff

**ruff used as linter and formatter**


```bash
uv run ruff check .         # to find problems
uv run ruff check . --fix   # to fix problems

```

**ruff also used like auto-reformat codestlye**

```bash

uv run ruff format .
```


### `mypy`


**mypy is the type checker**


```bash

uv run mypy app

```

Mypy reads type annotations and check whatever you are using consistently
