
class Book:
    def __init__(self,Title,Author,Published_Year):
        self.Title = Title
        self.author= Author
        self.published = Published_Year
    
book_1 = Book("r","b",1999)

print(book_1.Title)