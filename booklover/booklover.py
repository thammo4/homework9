import pandas as pd;
import numpy as np;

class BookLover:
	def __init__(self, name, email, fav_genre, num_books=0, book_list=pd.DataFrame({'book_name':[], 'book_rating':[]})):
		self.name 		= name;
		self.email 		= email;
		self.fav_genre 	= fav_genre;
		self.num_books 	= num_books;
		self.book_list 	= book_list;

	def add_book (self, book_name=str(), rating=int()):
		'''Append a book to the book_list['book_name']'''
		print('book list'); print(self.book_list); print("\n\n\n\n\n");
		if not book_name:
			return 'Need a book';
		if not rating:
			print('Rating will be zero.');

		if not (not [x for x in list(self.book_list['book_name']) if x == book_name]):
			return 'book already read.';

		new_book = pd.DataFrame({'book_name':[book_name], 'book_rating':[rating]});
		self.book_list = pd.concat([self.book_list, new_book], ignore_index=True);

		print(self.book_list);

	def has_read (self, book_name):
		'''Check if the book_name currently exists in the book_list.book_name list'''
		for x in self.book_list['book_name']:
			if x.lower() == book_name.lower():
				return True;
		return False;

	def num_books_read (self):
		'''Return a count of the number of book names in the book_list dataframe'''
		return len(self.book_list['book_name']);

	def fav_books (self):
		'''Return all books whose rating exceeds three'''
		return self.book_list[self.book_list['book_rating'] > 3];
