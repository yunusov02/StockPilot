from app.db.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, comment="Category ID")

    name: Mapped[str] = mapped_column(nullable=False, comment="Category name")

    parent_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"), nullable=True, comment="Parent category ID"
    )

    def __str__(self) -> str:
        return f"Category(id={self.id}, name='{self.name}', parent_id={self.parent_id})"

    def __repr__(self) -> str:
        return f"Category(id={self.id}, name='{self.name}', parent_id={self.parent_id})"
