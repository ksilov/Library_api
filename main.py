from fastapi import FastAPI
from asyncio import run
from api.users import router as users_router
from database.database import create_tables, delete_tables
import uvicorn


app = FastAPI()
app.include_router(users_router, prefix='/users')


@app.get('/')
async def index():
    return {'message': 'hello motherfucker'}


async def main():
    await create_tables()


if __name__ == "__main__":
    run(main())
    uvicorn.run('main:app', reload=True)

