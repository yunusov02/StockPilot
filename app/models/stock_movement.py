from app.db.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class StockMovement(Base):
    __tablename__ = "stock_movements"

    id: Mapped[int] = mapped_column(primary_key=True, comment="Stock Movement ID")
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"), nullable=False, comment="Product ID"
    )
    delta: Mapped[int] = mapped_column(nullable=False, comment="Change in stock quantity")
    movement_type: Mapped[str] = mapped_column(
        nullable=False, comment="Type of stock movement (e.g., 'in', 'out')"
    )
    created_by: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False, comment="User ID who created the stock movement"
    )

    def __str__(self) -> str:
        return (
            f"StockMovement(id={self.id}, product_id={self.product_id},"
            f"delta={self.delta}, movement_type='{self.movement_type}',"
            f"created_by={self.created_by})"
        )

    def __repr__(self) -> str:
        return (
            f"StockMovement(id={self.id}, product_id={self.product_id},"
            f"delta={self.delta}, movement_type='{self.movement_type}',"
            f"created_by={self.created_by})"
        )
