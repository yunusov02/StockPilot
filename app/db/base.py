from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now, nullable=False, comment="Creation timestamp"
    )

    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
        comment="Last update timestamp",
    )

    deleted_at: Mapped[datetime] = mapped_column(
        default=None, nullable=True, comment="Deletion timestamp"
    )
