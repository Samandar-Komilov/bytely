from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base, TimeStampMixin


class User(Base, TimeStampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False, default=True)
    is_premium: Mapped[bool] = mapped_column(nullable=False, default=False)

    def __str__(self):
        return f"User(email={self.email})"
    
    def __repr__(self):
        return self.__str__()