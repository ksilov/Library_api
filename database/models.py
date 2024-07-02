from typing import List, Optional
from sqlalchemy import ForeignKey, String, Integer, DateTime, Boolean, Float
from sqlalchemy.orm import Mapped, DeclarativeBase, relationship, mapped_column
from sqlalchemy.sql import func


Base = DeclarativeBase()


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    bio: Mapped[str] = mapped_column(String(256), default=None)
    premium: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self):
        return f'id: {self.id!r}, name: {self.name!r}, bio: {self.bio!r}, premium: {self.premium!r}'


class Book(Base):
    __tablename__ = 'book'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(256))
    author: Mapped[int] = mapped_column(Integer, ForeignKey("author.id", ondelete='CASCADE'))
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, onupdate=func.now())
    premium: Mapped[bool] = mapped_column(Boolean, default=False)
    paid: Mapped[bool] = mapped_column(Boolean, default=False)
    price: Mapped[float] = mapped_column(Float, default=0.0)
    visibility: Mapped[bool] = mapped_column(Boolean, default=True)

    def __repr__(self):
        return (f'id: {self.id!r}, name: {self.name!r}, author: {self.author!r}, '
                f'created_at: {self.created_at!r}, updated_at: {self.updated_at!r}, '
                f'premium: {self.premium!r}, paid: {self.paid!r}, price: {self.price!r}, '
                f'visibility: {self.visibility!r}')


class Author(Base):
    __tablename__ = 'author'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return f'id: {self.id!r}, name: {self.name!r}'


