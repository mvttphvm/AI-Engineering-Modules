"""
Exercise: Contact Manager
Module 3 | Lesson 7 | ~35 min

Objective:
  Build a CRUD contact manager using SQLAlchemy Sessions. Practice
  adding, querying, updating, and deleting ORM objects within session
  context managers.
"""

from sqlalchemy import create_engine, String, Boolean, Integer, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from typing import Optional

engine = create_engine("sqlite:///:memory:", echo=False)


class Base(DeclarativeBase):
    pass


# ── Contact model (provided — do not modify) ──────────────────────────────────
class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    phone: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    favorite: Mapped[bool] = mapped_column(Boolean, default=False)

    def __repr__(self) -> str:
        fav = " [fav]" if self.favorite else ""
        return f"<Contact {self.first_name} {self.last_name} <{self.email}>{fav}>"


# Create tables
Base.metadata.create_all(engine)


def add_contact(
    first_name: str, last_name: str, email: str, phone: str = None
) -> Contact:
    with Session(engine) as session:
        if not session.query(Contact).filter_by(email=email).first():
            contact = Contact(
                first_name=first_name, last_name=last_name, email=email, phone=phone
            )
            session.add(contact)
            session.commit()
            session.refresh(contact)
            return contact
        else:
            raise ValueError(f"A contact with the email {email} already exists.")


def list_contacts() -> list:
    with Session(engine) as session:
        return (
            session.execute(select(Contact).order_by(Contact.last_name)).scalars().all()
        )


def find_contact(email: str) -> Optional[Contact]:
    with Session(engine) as session:
        return (
            session.execute(select(Contact).where(Contact.email == email))
            .scalars()
            .first()
        )


def update_phone(email: str, new_phone: str) -> bool:
    with Session(engine) as session:
        contact = (
            session.execute(select(Contact).where(Contact.email == email))
            .scalars()
            .first()
        )
        if contact:
            contact.phone = new_phone
            session.commit()
            return True
    return False


def toggle_favorite(email: str) -> bool:
    with Session(engine) as session:
        contact = (
            session.execute(select(Contact).where(Contact.email == email))
            .scalars()
            .first()
        )
        if contact:
            contact.favorite = not contact.favorite
            session.commit()
            print(f"Favorite status for {email} has beenupdated to {contact.favorite}!")
            return contact.favorite
        else:
            raise ValueError(f"No contact found with email: {email}")


def delete_contact(email: str) -> bool:
    with Session(engine) as session:
        contact = (
            session.execute(select(Contact).where(Contact.email == email))
            .scalars()
            .first()
        )
        if contact:
            session.delete(contact)
            session.commit()
            return True
    return False


# ── Test block ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Add contacts
    print("Adding contacts...")
    c1 = add_contact("Alice", "Chen", "alice@example.com", "555-0101")
    c2 = add_contact("Bob", "Martinez", "bob@example.com")
    c3 = add_contact("Carol", "Singh", "carol@example.com", "555-0303")
    c4 = add_contact("David", "Kim", "david@example.com", "555-0404")
    c5 = add_contact("Eve", "Johnson", "eve@example.com", "555-0505")
    print(f"  Created: {c1}, {c2}, {c3}, {c4}, {c5}")

    # List all
    print("\nAll contacts:")
    for c in list_contacts():
        print(f"  {c}")

    # Find by email
    print("\nFind alice@example.com:")
    found = find_contact("alice@example.com")
    print(f"  {found}")

    # Update phone
    print("\nUpdate Bob's phone:")
    update_phone("bob@example.com", "555-9999")
    print(f"  {find_contact('bob@example.com')}")

    # Toggle favorite
    print("\nMark Alice as favorite:")
    new_val = toggle_favorite("alice@example.com")
    print(f"  favorite is now: {new_val}")
    print(f"  {find_contact('alice@example.com')}")

    # Delete
    print("\nDelete Carol:")
    delete_contact("carol@example.com")
    print("Remaining contacts:")
    for c in list_contacts():
        print(f"  {c}")

    # List all
    print("\nAll contacts:")
    for c in list_contacts():
        print(f"  {c}")
