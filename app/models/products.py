from app.db.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, comment="Product ID")
    sku: Mapped[str] = mapped_column(nullable=False, unique=True, comment="Product SKU")
    name: Mapped[str] = mapped_column(nullable=False, comment="Product name")
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"), nullable=False, comment="Category ID"
    )
    price_cents: Mapped[int] = mapped_column(nullable=False, comment="Product price in cents")
    current_stock: Mapped[int] = mapped_column(nullable=False, comment="Current stock quantity")
    reorder_level: Mapped[int] = mapped_column(nullable=False, comment="Reorder level quantity")

    def __str__(self) -> str:
        return f"Product(id={self.id}, sku='{self.sku}', name='{self.name}')"

    def __repr__(self) -> str:
        return f"Product(id={self.id}, sku='{self.sku}', name='{self.name}')"
