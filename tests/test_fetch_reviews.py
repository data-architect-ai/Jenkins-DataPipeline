import unittest
import sqlite3
from scripts.fetch_reviews import create_reviews_table, fetch_reviews

class TestFetchReviews(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary reviews.db in memory for testing
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()
        create_reviews_table(self.conn)
    
    def tearDown(self):
        # Close the connection and clean up
        self.conn.close()
    
    def test_fetch_reviews(self):
        # Call fetch_reviews function
        fetch_reviews(self.conn)
        
        # Verify that data is inserted correctly
        self.c.execute('SELECT * FROM reviews')
        reviews = self.c.fetchall()
        
        # Assert statements to verify expected results
        self.assertEqual(len(reviews), 3)  # Adjust expected count based on input data
        self.assertEqual(reviews[0][1], 1)  # Example: Check customer_id of first review
        self.assertEqual(reviews[0][2], "Great product, highly recommended!")  # Example: Check review_text

if __name__ == '__main__':
    unittest.main()
