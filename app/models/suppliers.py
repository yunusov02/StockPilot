from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Supplier(Base):
    __tablename__ = "suppliers"

    id: Mapped[int] = mapped_column(primary_key=True, comment="Supplier ID")
    name: Mapped[str] = mapped_column(nullable=False, unique=True, comment="Supplier name")
    contact_email: Mapped[str] = mapped_column(
        nullable=False, unique=True, comment="Supplier contact email"
    )

    def __str__(self) -> str:
        return f"Supplier(id={self.id}, name='{self.name}', contact_email='{self.contact_email}')"

    def __repr__(self) -> str:
        return f"Supplier(id={self.id}, name='{self.name}', contact_email='{self.contact_email}')"
