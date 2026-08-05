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


