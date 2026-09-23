class Book:
    def __init__(self, title, author, year):
        # make sure year is a positive integer
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer")

        self.title = title
        self.author = author
        self.year = year
        self.checked_out = False

    def check_out(self):
        self.checked_out = True

    def return_book(self):
        self.checked_out = False

    def __repr__(self):
        status = "Checked Out" if self.checked_out else "Available"
        return f"{self.title} by {self.author} - {status}"


# EBook inherits from Book
class EBook(Book):
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb
        self.checkout_count = 0

    # ebooks can have multiple checkouts, this is an override method
    def check_out(self):
        self.checkout_count += 1

    def return_book(self):
        if self.checkout_count > 0:
            self.checkout_count -= 1

    def __repr__(self):
        return f"{self.title} by {self.author} - {self.file_size_mb} MB - {self.checkout_count} checkouts"


class Catalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]

    def search_by_title(self, keyword):
        # lowercase makes the search case-insensitive
        return [book for book in self.books if keyword.lower() in book.title.lower()]

    def get_available(self):
        available = []

        for book in self.books:
            if isinstance(book, EBook):
                available.append(book)
            elif not book.checked_out:
                available.append(book)

        return available

    def summary(self):
        """Print a summary of all books."""
        total = len(self.books)
        available = len(self.get_available())

        print(f"\nCatalog Summary: {available}/{total} available")

        for book in self.books:
            print(f"  {book}")


# Test the classes
catalog = Catalog()
catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
catalog.add_book(EBook("AI Engineering", "Chip Huyen", 2025, 15.2))

# Search
results = catalog.search_by_title("python")
print(results)  # Should find "Python Crash Course"

# Check out
catalog.books[0].check_out()
available = catalog.get_available()
print(f"Available: {len(available)} books")

catalog.summary()