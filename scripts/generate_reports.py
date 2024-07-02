import sqlite3

def generate_reports():
    # Connect to results.db SQLite database
    conn = sqlite3.connect('data/results.db')
    c = conn.cursor()
    
    # Example: Fetch sentiment results
    c.execute('SELECT id, review_id, sentiment FROM sentiment_results')
    results = c.fetchall()
    
    # Example: Generate reports
    for result in results:
        id, review_id, sentiment = result  # Extract id, review_id, and sentiment from result tuple
        # Generate report based on sentiment (replace with your actual reporting logic)
        print(f"ID: {id}, Review ID: {review_id}, Sentiment: {sentiment}")
    
    # Close connection
    conn.close()

if __name__ == '__main__':
    generate_reports()
