-- SQL script to create sentiment_results table if not exists
CREATE TABLE IF NOT EXISTS sentiment_results (
    id INTEGER PRIMARY KEY,
    review_id INTEGER,
    sentiment TEXT
);
