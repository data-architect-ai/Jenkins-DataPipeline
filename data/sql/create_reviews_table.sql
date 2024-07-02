-- SQL script to create reviews table if not exists
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    review_text TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
