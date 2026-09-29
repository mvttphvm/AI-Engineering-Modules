"""
Exercise: Build Your Own Database
Module 3 | Lesson 1 | ~30 min

Objective:
Connect to a SQLite database, create two related tables,
insert sample data, and query across them with a JOIN.
"""

import sqlite3


# ── Database setup ──────────────────────────────────────────

# Creates music.db if it doesn't already exist.
conn = sqlite3.connect("music.db")

# Enable foreign key enforcement.
conn.execute("PRAGMA foreign_keys = ON")

# Lets us access columns by name: row["title"]
conn.row_factory = sqlite3.Row


# ── Create tables ───────────────────────────────────────────

def create_tables(conn: sqlite3.Connection) -> None:
    """
    Create the artists and albums tables.
    """

    conn.executescript("""
        CREATE TABLE IF NOT EXISTS artists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            genre TEXT
        );

        CREATE TABLE IF NOT EXISTS albums (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            year INTEGER,
            artist_id INTEGER,
            FOREIGN KEY (artist_id) REFERENCES artists(id)
        );
    """)


# ── Insert data ─────────────────────────────────────────────

def insert_data(conn: sqlite3.Connection) -> None:
    """
    Insert at least 3 artists and 5 albums.
    """

    artists_to_insert = [
        ("MVTT PHVM", "EDM"),
        ("Kaskade", "House"),
        ("Z3LLA", "EDM"),
    ]

    albums_to_insert = [
        ("Origin//", 2026, 2),
        ("Back to Life", 2026, 3),
        ("The Day We All Remembered", 2026, 1),
        ("Gravity", 2024, 3),
        ("The Great Awakening", 2028, 1),
        ("Eyes", 2018, 2),
    ]

    conn.executemany(
        "INSERT INTO artists (name, genre) VALUES (?, ?)",
        artists_to_insert
    )

    conn.executemany(
        "INSERT INTO albums (title, year, artist_id) VALUES (?, ?, ?)",
        albums_to_insert
    )

    conn.commit()


# ── Query data ──────────────────────────────────────────────

def query_albums(conn: sqlite3.Connection) -> list:
    """
    Return all albums with their artist names.
    Order by artist name, then year.
    """

    rows = conn.execute("""
        SELECT albums.title, albums.year, artists.name
        FROM albums
        JOIN artists ON albums.artist_id = artists.id
        ORDER BY artists.name, albums.year
    """).fetchall()

    return rows


# ── Run program ─────────────────────────────────────────────

if __name__ == "__main__":
    create_tables(conn)
    insert_data(conn)

    results = query_albums(conn)

    print("Albums by artist:")

    for row in results:
        print(f"  {row['name']} — {row['title']} ({row['year']})")

    conn.close()