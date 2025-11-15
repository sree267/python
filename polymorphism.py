# Base class
class Book:
    def __init__(self, title, author):
        self.title = title

        
        self.author = author
    
    def display_info(self):
        print("Book Title:", self.title)
        print("Author:", self.author)


# Derived class
class PythonBook(Book):
    def __init__(self, title, author, pages, price):
        # invoking base class constructor
        super().__init__(title, author)
        self.pages = pages
        self.price = price

    # Method overriding
    def display_info(self):
        # call base class method also (optional)
        super().display_info()
        print("Pages:", self.pages)
        print("Price:", self.price)


# Object creation
pb = PythonBook("Learning Python", "Mark Lutz", 1600, 799)

# Display book details
pb.display_info()
