import os
import ssl
from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise import Tortoise

cfg = ["database"]

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    if "database" in cfg:
        
        pg_env_check = ["PG_HOST", "PG_PORT", "PG_USER", "PG_PASSWORD", "PG_DB"]
        for pg in pg_env_check:
            if os.getenv(pg) is None:
                raise SystemError(f"\n\033[1;31m[❌ Critical startup failure]\nMissing env variable {pg}\033[0m")

        try:
            TORTOISE_ORM = {
                "connections": {
                    "default": {
                        "engine": "tortoise.backends.asyncpg",
                        "credentials": {
                            "host": os.getenv("PG_HOST"),
                            "port": os.getenv("PG_PORT"),
                            "user": os.getenv("PG_USER"),
                            "password": os.getenv("PG_PASSWORD"),
                            "database": os.getenv("PG_DB"),
                            "ssl": False,
                        }
                    }
                },
                "apps": {
                    "models": {
                        "models": ["app.models"],
                        "default_connection": "default",
                    }
                },
            }

            await Tortoise.init(config=TORTOISE_ORM)

        except Exception as e:
            # await kv.close()
            raise SystemError(f"\n\033[1;31m[❌ Critical startup failure]\nFailed to intialize Tortoise ORM!\nDatabase URL:\nError: {e}\033[0m")
                
    yield

    await Tortoise.close_connections()
