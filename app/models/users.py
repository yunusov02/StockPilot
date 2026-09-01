from enum import Enum

from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class UserRole(Enum):
    OWNER = "owner"
    STAFF = "staff"


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, comment="User ID")
    username: Mapped[str] = mapped_column(nullable=False, unique=True, comment="Username")
    email: Mapped[str] = mapped_column(nullable=False, unique=True, comment="User email")
    hashed_password: Mapped[str] = mapped_column(nullable=False, comment="Password hash")
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False, comment="Is user active")
    role: Mapped[UserRole] = mapped_column(
        default=UserRole.STAFF, nullable=False, comment="User role"
    )

    def __str__(self) -> str:
        return (
            f"Users(id={self.id}, username='{self.username}',"
            f"email='{self.email}', is_active={self.is_active}"
        )

    def __repr__(self) -> str:
        return (
            f"Users(id={self.id}, username='{self.username}',"
            f"email='{self.email}', is_active={self.is_active}"
        )
