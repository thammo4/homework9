import unittest;
from booklover import BookLover;
import pandas as pd;
import numpy as np;

class BookLoverTestSuite(unittest.TestCase):
	def test_1_add_book (self):
		print('Running Test 1 (add book)\n');
		self.book_lover = BookLover(name='bob', email='bob@bob.com', fav_genre='Victorian Literature', book_list=pd.DataFrame({'book_name':['1984'], 'book_rating':[3]}));

		book = 'For Whom the Bell Tolls';
		self.book_lover.add_book(book, 5);
		self.assertTrue(book in self.book_lover.book_list['book_name'].values);

	def test_2_add_book (self):
		print('Running Test 2 (add book)\n');
		self.book_lover = BookLover(name='bob', email='bob@bob.com', fav_genre='Victorian Literature', book_list=pd.DataFrame({'book_name':['1984'], 'book_rating':[3]}));

		self.book_lover.add_book('Emma', 4);
		self.book_lover.add_book('Emma', 5);
		self.assertEqual(self.book_lover.book_list['book_name'].value_counts()['Emma'], 1);

	def test_3_has_read (self):
		print('Running Test 3 (has read)\n');
		self.book_lover = BookLover(name='bob', email='bob@bob.com', fav_genre='Victorian Literature', book_list=pd.DataFrame({'book_name':['1984'], 'book_rating':[3]}));

		self.book_lover.add_book('Siddhartha');
		self.assertTrue(self.book_lover.has_read('Siddhartha'));

	def test_4_has_read (self):
		print('Running Test 4 (has read)\n');
		self.book_lover = BookLover(name='bob', email='bob@bob.com', fav_genre='Victorian Literature', book_list=pd.DataFrame({'book_name':['1984'], 'book_rating':[3]}));

		self.assertFalse(self.book_lover.has_read('Rich Dad, Poor Dad'));

	def test_5_num_books_read (self):
		print('Running Test 5 (num books read)\n');
		self.book_lover = BookLover(name='bob', email='bob@bob.com', fav_genre='Victorian Literature', book_list=pd.DataFrame({'book_name':['1984'], 'book_rating':[3]}));

		self.assertEqual(self.book_lover.num_books_read(), 1);

	def test_6_fav_books (self):
		print('Running Test 6 (fav books)\n');
		self.book_lover = BookLover(name='bob', email='bob@bob.com', fav_genre='Victorian Literature', book_list=pd.DataFrame({'book_name':['1984'], 'book_rating':[3]}));

		self.book_lover.add_book('The Crucible', 4);
		self.book_lover.add_book('Men of Mathematics', 5);
		self.book_lover.add_book('A Room With A View', 2);

		self.assertTrue((self.book_lover.fav_books()['book_rating'] > 3).all());

		print('\nDone.\n');


if __name__ == '__main__':
    unittest.main()