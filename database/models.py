from sqlalchemy import ForeignKey, String, Integer, DateTime, Boolean, Float
from sqlalchemy.orm import Mapped, mapped_column,DeclarativeBase
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    bio: Mapped[str] = mapped_column(String(256), default=None)
    premium: Mapped[bool] = mapped_column(Boolean, default=False)
    register_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    def __repr__(self):
        return f'id: {self.id!r}, name: {self.name!r}, bio: {self.bio!r}, premium: {self.premium!r}'


class Books(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(256))
    author: Mapped[int] = mapped_column(Integer, ForeignKey("authors.id", ondelete='CASCADE'))
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, onupdate=func.now())
    paid: Mapped[bool] = mapped_column(Boolean, default=False)
    visibility: Mapped[bool] = mapped_column(Boolean, default=True)

    def __repr__(self):
        return (f'id: {self.id!r}, name: {self.name!r}, author: {self.author!r}, '
                f'created_at: {self.created_at!r}, updated_at: {self.updated_at!r}, '
                f'premium: {self.premium!r}, paid: {self.paid!r}, price: {self.price!r}, '
                f'visibility: {self.visibility!r}')


class Authors(Base):
    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    def __repr__(self):
        return f'id: {self.id!r}, name: {self.name!r}'



