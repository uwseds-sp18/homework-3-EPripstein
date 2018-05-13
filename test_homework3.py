import unittest
import os
from homework3 import create_dataframe

class create_df_tests(unittest.TestCase):
	
	#Set up
	def setUp(self):
		self.df = create_dataframe('/Users/Eric/Documents/UW/DATA515/Assignments/hw2-EPripstein/class.db')
		
	#Test to ensure a bad path results in a ValueError
	def test_error(self):
		self.bad_path = 'nonsense_path.db'
		if not os.path.exists(self.bad_path):
			error_type = ValueError
			self.assertTrue(error_type == ValueError)
		 
	#Test that there are at least 10 rows in the dataframe
	def test_rows(self):
		self.assertTrue(len(self.df) >= 10)
	
	#Test if the only columns in the df are video_id, category_id, language
	def test_cols(self):
		df_cols = self.df.columns.tolist()
		self.assertTrue((len(df_cols) == 3) & ('video_id' in df_cols) & ('category_id' in df_cols) & ('language' in df_cols))
		
	#Test that the columns video_id and language could be a key
	def test_key(self):
		df_deduped = self.df.drop_duplicates(['video_id', 'language'])
		self.assertTrue(len(df_deduped) == len(self.df))
		
		
if __name__ == '__main__':
	unittest.main()