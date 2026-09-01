from app.db.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, comment="Order ID")
    status: Mapped[str] = mapped_column(nullable=False, comment="Order status")
    created_by: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False, comment="User ID who created the order"
    )

    def __str__(self) -> str:
        return f"Orders(id={self.id}, status='{self.status}',created_by={self.created_by})"

    def __repr__(self) -> str:
        return f"Orders(id={self.id}, status='{self.status}',created_by={self.created_by})"


class OrderItems(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True, comment="Order Item ID")
    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id"), nullable=False, comment="Order ID"
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"), nullable=False, comment="Product ID"
    )
    quantity: Mapped[int] = mapped_column(
        nullable=False, comment="Quantity of the product in the order"
    )
    unit_price_cents: Mapped[int] = mapped_column(
        nullable=False, comment="Unit price of the product in cents"
    )

    def __str__(self) -> str:
        return (
            f"OrderItems(id={self.id}, order_id={self.order_id},"
            f"product_id={self.product_id}, quantity={self.quantity},"
            f"unit_price_cents={self.unit_price_cents})"
        )

    def __repr__(self) -> str:
        return (
            f"OrderItems(id={self.id}, order_id={self.order_id},"
            f"product_id={self.product_id}, quantity={self.quantity},"
            f"unit_price_cents={self.unit_price_cents})"
        )
