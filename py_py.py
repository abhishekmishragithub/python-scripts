class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    def __repr__(self):
        return f"title={self.title}, author={self.author}, price={self.price}"

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author and self.price == other.price
        return False

    def __hash__(self):
        return hash((self.title, self.author, self.price))

    def book_info(self):
        return f"{self.title} by {self.author}"


book1 = Book("Harry Potter", "JK Rowling", 39.95)
print(book1)
print(book1.book_info())
print(book1.__dict__)
print(book1.__hash__())
print(hash(book1))
print(hash(book1.__repr__()))
