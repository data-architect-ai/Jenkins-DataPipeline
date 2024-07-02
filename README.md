# Jenkins-DataPipeline


Jenkins-DataPipeline/
├── .git/                       # Git internal directory
├── README.md                   # Project README
├── .gitignore                  # Git ignore file
├── Jenkinsfile                 # Jenkins pipeline script
├── scripts/                    # Scripts directory
│   ├── fetch_reviews.py        # Script to fetch customer reviews
│   ├── sentiment_analysis.py   # Script for sentiment analysis
│   ├── store_results.py        # Script to store sentiment results
│   └── generate_reports.py     # Script to generate reports
├── tests/                      # Tests directory
│   ├── test_fetch_reviews.py   # Unit tests for fetch_reviews.py
│   ├── test_sentiment_analysis.py  # Unit tests for sentiment_analysis.py
│   └── test_store_results.py   # Unit tests for store_results.py
└── data/                       # Data directory (optional)
    ├── reviews.db              # SQLite database for customer reviews
    ├── results.db              # SQLite database for sentiment results
    └── sql/                    # Directory for SQL scripts
        ├── create_reviews_table.sql          # SQL script to create reviews table
        └── create_sentiment_results_table.sql # SQL script to create sentiment_results table


1. Input Data to DB

cd Jenkins-DataPipeline/data

sqlite3 reviews.db

DROP TABLE IF EXISTS reviews;

CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    review_text TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM reviews;

.exit

sqlite3 results.db

DROP TABLE IF EXISTS sentiment_results;

CREATE TABLE IF NOT EXISTS sentiment_results (
    id INTEGER PRIMARY KEY,
    review_id INTEGER,
    sentiment TEXT
);

SELECT * FROM sentiment_results;

.exit


2. Fetch Data from DB

cd Jenkins-DataPipeline 

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

python3 scripts/fetch_reviews.py

python3 scripts/sentiment_analysis.py

python3 scripts/generate_reports.py

3. Run tests

python3 -m unittest tests.test_fetch_reviews

python3 -m unittest tests.test_sentiment_analysis

4. Jenkins CI/CD pipeline as Container

docker build -t my-jenkins .

docker run -p 8080:8080 -p 50000:50000 my-jenkins

get container_d from
docker ps

docker logs <container_id>
get password 

enterpasswrod and setup at:
http://localhost:8080/

https://github.com/manojbusam/Jenkins-DataPipeline.git

