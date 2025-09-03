from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimeStampMixin


class Link(Base, TimeStampMixin):
    __tablename__ = "links"

    id: Mapped[int] = mapped_column(primary_key=True)
    short_code: Mapped[str] = mapped_column(unique=True, nullable=False)
    long_url: Mapped[str] = mapped_column(nullable=False)
    expires_at: Mapped[str] = mapped_column(nullable=True)
    owner_id: Mapped[int] = mapped_column(nullable=True)
    click_count: Mapped[int] = mapped_column(nullable=False, default=0)

    def __str__(self):
        return f"Link(short_code={self.short_code})"

    def __repr__(self):
        return self.__str__()
