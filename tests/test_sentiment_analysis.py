import unittest
import sqlite3
from scripts.fetch_reviews import create_reviews_table  # Import create_reviews_table function
from scripts.sentiment_analysis import create_sentiment_results_table, analyze_sentiment

class TestSentimentAnalysis(unittest.TestCase):
    
    def setUp(self):
        # Create temporary databases in memory for testing
        self.conn_reviews = sqlite3.connect(':memory:')
        self.conn_results = sqlite3.connect(':memory:')
        self.c_reviews = self.conn_reviews.cursor()
        self.c_results = self.conn_results.cursor()
        
        # Create reviews table and insert test data
        create_reviews_table(self.conn_reviews)  # Call create_reviews_table function
        self.c_reviews.execute("INSERT INTO reviews (id, customer_id, review_text) VALUES (1, 1, 'Great product')")
        self.c_reviews.execute("INSERT INTO reviews (id, customer_id, review_text) VALUES (2, 2, 'Not satisfied')")
        self.conn_reviews.commit()
        
        # Create sentiment_results table
        create_sentiment_results_table(self.conn_results)
    
    def tearDown(self):
        # Close connections and clean up
        self.conn_reviews.close()
        self.conn_results.close()
    
    def test_analyze_sentiment(self):
        # Call analyze_sentiment function
        analyze_sentiment(self.conn_reviews, self.conn_results)
        
        # Verify that sentiment results are inserted correctly
        self.c_results.execute('SELECT * FROM sentiment_results')
        results = self.c_results.fetchall()
        
        # Assert statements to verify expected results
        self.assertEqual(len(results), 2)  # Adjust expected count based on input data
        self.assertEqual(results[0][1], 1)  # Example: Check review_id of first sentiment result
        self.assertEqual(results[0][2], 'positive')  # Example: Check sentiment

if __name__ == '__main__':
    unittest.main()
