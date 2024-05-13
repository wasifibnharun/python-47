class Book:
    def __init__(self,book_name,author,pages,edition):
        self.book=book_name
        self.author=author
        self.pages=pages
        self.edition=edition
        print(f"The book,'{self.book}' is written by {self.author},it contains {self.pages} pages and the {self.edition} edition of it has been published")
        
    def updated_edition(self,new_edition):
        self.edition=new_edition
        print(f"The {self.edition} edition of the book is available now")
        
book1=Book("The Alchemist","Paulo Coelho",161,"1st")
book1.updated_edition("2nd")