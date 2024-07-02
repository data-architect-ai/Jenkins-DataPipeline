import sqlite3

def create_reviews_table(conn):
    # Create reviews table if not exists
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                review_text TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()

def fetch_reviews(conn):
    # Example function to fetch reviews (inserting sample data)
    c = conn.cursor()
    
    # Sample reviews with different sentiments
    reviews = [
            (1, "Great product, highly recommended!"),
            (2, "Disappointed with the quality."),
            (3, "The item was okay, nothing special."),
            (4, "Best purchase ever!"),
            (5, "Terrible experience."),
            (6, "Average product."),
        ]
    
    # Insert sample reviews into the reviews table
    for customer_id, review_text in reviews:
        c.execute("INSERT INTO reviews (customer_id, review_text) VALUES (?, ?)", (customer_id, review_text))
    
    conn.commit()

# Example usage (you can remove this from the script if not needed)
if __name__ == '__main__':
    conn = sqlite3.connect('data/reviews.db')  # Adjust path as needed
    create_reviews_table(conn)
    fetch_reviews(conn)
    conn.close()
