"""
Exercise: Product Catalog Models
Module 3 | Lesson 6 | ~35 min

Objective:
  Define SQLAlchemy 2.0 ORM models for a product catalog and write
  queries using the ORM's select() API instead of raw SQL strings.
"""

from sqlalchemy import (
    create_engine,
    select,
    String,
    Float,
    Boolean,
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from typing import Optional, List

engine = create_engine("sqlite:///product_catalog.db", echo=True)


class Base(DeclarativeBase):
    pass


# ── TODO: Define the Category model ──────────────────────────────────────────
# Table name: "categories"
# Columns:
#   id   — Integer, primary key
#   name — String, required, unique
# Relationship: one category -> many products
class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[Optional[str]] = mapped_column(String(300))
    products: Mapped[list["Product"]] = relationship(
        "Product", back_populates="category"
    )

    def __repr__(self) -> str:
        return f"Category(id = {self.id}, name = '{self.name}', description = '{self.description}')"


# ── TODO: Define the Product model ────────────────────────────────────────────
# Table name: "products"
# Columns:
#   id          — Integer, primary key
#   name        — String, required
#   description — String, optional
#   price       — Float, required
#   in_stock    — Boolean, default True
#   category_id — Integer, ForeignKey("categories.id")
# Relationship: many products -> one category
class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(300))
    price: Mapped[float] = mapped_column(nullable=False)
    in_stock: Mapped[bool] = mapped_column(default=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship("Category", back_populates="products")


# ── Test block ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Create tables (run this once your models are defined)
    Base.metadata.create_all(engine)

    # ── Seed data ─────────────────────────────────────────────────────────────
    with Session(engine) as session:
        electronics = Category(name="Electronics")
        books = Category(name="Books")
        sports = Category(name="Sports")
        session.add_all([electronics, books, sports])
        session.flush()  # assigns IDs without committing

        session.add_all(
            [
                Product(
                    name="Wireless Headphones",
                    price=79.99,
                    in_stock=True,
                    category_id=electronics.id,
                ),
                Product(
                    name="Mechanical Keyboard",
                    price=129.99,
                    in_stock=True,
                    category_id=electronics.id,
                ),
                Product(
                    name="USB-C Hub",
                    price=39.99,
                    in_stock=False,
                    category_id=electronics.id,
                ),
                Product(
                    name="Python Crash Course",
                    price=39.99,
                    in_stock=True,
                    category_id=books.id,
                ),
                Product(
                    name="SQL for Beginners",
                    price=29.99,
                    in_stock=True,
                    category_id=books.id,
                ),
                Product(
                    name="Yoga Mat", price=34.99, in_stock=True, category_id=sports.id
                ),
            ]
        )
        session.commit()

    # ── Query 1: All products in stock ────────────────────────────────────────
    print("Products in stock:")
    with Session(engine) as session:
        stmt = select(Product).where(Product.in_stock.is_(True))
        products = session.execute(stmt).scalars().all()
        for p in products:
            print(f"  {p.name} — ${p.price:.2f}")

    # ── Query 2: Products under $50, ordered by price ─────────────────────────
    print("Products under $50 (cheapest first):")
    with Session(engine) as session:
        stmt = select(Product).where(Product.price < 50).order_by(Product.price)
        products = session.execute(stmt).scalars().all()
        for p in products:
            print(f"  {p.name} — ${p.price:.2f}")

    # ── Query 3: All products with their category name ────────────────────────
    print("All products with category:")
    with Session(engine) as session:
        stmt = select(Product).join(Product.category)
        products = session.execute(stmt).scalars().all()
        for p in products:
            print(f"  {p.name} — {p.category.name}")
