import sqlite3

# ── Database setup (provided — do not modify) ─────────────────────────────────
conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row

conn.executescript("""
    CREATE TABLE members (
        id   INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        tier TEXT NOT NULL DEFAULT 'standard'  -- 'standard' or 'premium'
    );

    CREATE TABLE books (
        id     INTEGER PRIMARY KEY,
        title  TEXT NOT NULL,
        genre  TEXT NOT NULL,
        pages  INTEGER
    );

    CREATE TABLE checkouts (
        id          INTEGER PRIMARY KEY,
        member_id   INTEGER REFERENCES members(id),
        book_id     INTEGER REFERENCES books(id),
        checkout_date TEXT NOT NULL,       -- stored as 'YYYY-MM-DD' strings
        return_date   TEXT                 -- NULL if not returned
    );

    INSERT INTO members VALUES
      (1, 'Alice Chen',    'premium'),
      (2, 'Bob Martinez',  'standard'),
      (3, 'Carol Singh',   'premium'),
      (4, 'Dan Okafor',    'standard'),
      (5, 'Elena Petrov',  'premium');

    INSERT INTO books VALUES
      (1,  'The Hobbit',               'Fantasy',  310),
      (2,  'Dune',                     'Sci-Fi',   688),
      (3,  'Pride and Prejudice',      'Classic',  432),
      (4,  'Neuromancer',              'Sci-Fi',   271),
      (5,  'Good Omens',               'Fantasy',  413),
      (6,  'Nineteen Eighty-Four',     'Classic',  328),
      (7,  'The Left Hand of Darkness','Sci-Fi',   286),
      (8,  'Jane Eyre',                'Classic',  507),
      (9,  'American Gods',            'Fantasy',  635),
      (10, 'Foundation',               'Sci-Fi',   244);

    INSERT INTO checkouts VALUES
      (1,  1, 1,  '2024-01-05', '2024-01-19'),
      (2,  1, 2,  '2024-01-20', '2024-02-03'),
      (3,  1, 5,  '2024-02-10', '2024-02-24'),
      (4,  2, 3,  '2024-01-08', '2024-01-22'),
      (5,  2, 6,  '2024-02-01', NULL),
      (6,  3, 2,  '2024-01-15', '2024-01-29'),
      (7,  3, 4,  '2024-02-05', '2024-02-19'),
      (8,  3, 7,  '2024-03-01', NULL),
      (9,  4, 10, '2024-01-20', '2024-02-03'),
      (10, 5, 1,  '2024-02-01', '2024-02-15'),
      (11, 5, 9,  '2024-02-20', NULL),
      (12, 1, 8,  '2024-03-05', NULL);
""")
conn.commit()


print("1. How many books are in each genre?")
query1 = """
    SELECT b.genre, COUNT(*) as book_count
    FROM books b
    GROUP BY b.genre
    ORDER BY book_count DESC
 """
for row in conn.execute(query1):
    print(f"   {row['genre']}: {row['book_count']} books")


# Which member has checked out the most books? (GROUP BY + ORDER BY + LIMIT)
print("2. Which member has checked out the most books?")
query2 = """
    SELECT m.name, COUNT(c.book_id) AS book_count
    FROM members m
    LEFT JOIN checkouts c ON m.id = c.member_id
    GROUP BY m.id
    ORDER BY book_count DESC
    LIMIT 1
    """
for row in conn.execute(query2):
    print(
        f"   {row['name']} has checked out the most books at: {row['book_count']} books!"
    )


print("3. What is the average number of checkouts per member?")
query3 = """
    SELECT AVG(checkout_count) AS avg_checkouts
    FROM (
        SELECT COUNT(*) AS checkout_count
        FROM checkouts c
        GROUP BY member_id
    )
"""
for row in conn.execute(query3):
    print(f"   Average checkouts per member: {row['avg_checkouts']}")


print("4. Which genres have more than 3 checkouts?")
query4 = """SELECT b.genre, COUNT(*) AS checkout_counts
    FROM books b
    INNER JOIN checkouts c ON c.book_id = b.id
    GROUP BY b.genre
    HAVING checkout_counts > 3
    ORDER BY checkout_counts DESC
"""
for row in conn.execute(query4):
    print(f"   {row['genre']}: {row['checkout_counts']} checkouts")


print("5. Which books have never been checked out")
query5 = """
    SELECT b.title
    FROM books b
    WHERE b.id NOT IN (SELECT c.book_id
                        FROM checkouts c
                        GROUP BY c.book_id)"""
for row in conn.execute(query5):
    print(f"   {row['title']}: has never been checked out!")


conn.close()
