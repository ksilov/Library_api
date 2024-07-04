from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_session
from database.crud import UserRepository
from .schemas import *


''' /users router '''

router = APIRouter()


@router.post('/create')
async def create_user(user: User, session: AsyncSession = Depends(get_session)):
    if not user:
        raise HTTPException(status_code=400, detail="missing user's parameters")

    user_rep = UserRepository(session)
    await user_rep.create_user(
        name=user.name,
        password=user.password,
        bio=user.bio
    )

    return {
        "message": f"user created",
        "user": {
            "name": user.name,
            "password": user.password,
            "bio": user.bio
        }
    }


@router.get('/get')
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_session)):
    if not user_id:
        raise HTTPException(status_code=400, detail='missing user id parameter')

    user_rep = UserRepository(session)
    user = await user_rep.get_user_by_id(user_id)

    return user.scalar_one_or_none()


@router.get('/delete')
async def delete_user_by_id(user_id: int, session: AsyncSession = Depends(get_session)):
    if not user_id:
        raise HTTPException(status_code=400, detail='missing user id parameter')

    user_rep = UserRepository(session)
