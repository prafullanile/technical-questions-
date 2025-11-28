# Create a class Book with attributes: title, author, and price.
# → Add a method to display book details.
# Library
# Management
# Create
# Book and Library
# classes.The
# Library
#
#
# class should have methods to add, remove, and display available books.


class book:
	def __init__(self, title, author):
		self.title = title
		self.author = author


class library:
	def __init__(self):
		self.books = []

	def add_book(self, book):

		self.books.append(book)
		print(f"{book.title} , {book.author} added succesfully")


	def book_remove(self,title):
		for book in self.books:
			if book.title == title:
				self.books.remove(book)
				print(f"book '{title}' remove successfully")
				return

		else:
			print(f"book'{title}'is not found in library")


	def display_book(self):
		if not self.books:
			print("book not found")
		else:
			for book in self.books:
				print(f"{book.title} , {book.author}")


b1 = book("101python", "dr.prafulla nile")
b2 = book("404java", "dr. chetan patil")

l = library()

l.add_book(b1)
l.add_book(b2)

l.display_book()

l.book_remove("404java")
