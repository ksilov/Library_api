from .models import *
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, name: str, password: str, bio: str) -> Users:
        new_user = Users(name=name, password=password, bio=bio)
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user

    async def update_user(self, user_id: int, user_name: str,
                          user_password: str, user_bio, user_premium: bool) -> Users:
        user = await self.get_user_by_id(user_id)
        if user:
            if user_name:
                user.name = user_name
            if user_password:
                user.password = user_password
            if user_bio:
                user.bio = user_bio
            if user_premium:
                user.premium = user_premium
            await self.session.commit()
            await self.session.refresh(user)
            return user

    async def get_user_by_id(self, user_id: int) -> Users:
        user = await self.session.execute(select(Users).where(Users.id == user_id))
        return user.scalar_one_or_none()

    async def delete_user_by_id(self, user_id: int) -> bool:
        user = await self.get_user_by_id(user_id)
        if user:
            await self.session.delete(user)
            await self.session.commit()
            return True
        return False

