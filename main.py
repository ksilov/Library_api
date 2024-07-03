from fastapi import FastAPI
from asyncio import run
from database.database import create_tables, delete_tables


app = FastAPI()

app.include_router()



async def main():
    await create_tables()


if __name__ == "__main__":
    run(main())
