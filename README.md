# Reviews Sentiment Jenkins DataPipeline

This repository contains scripts and files for setting up a Jenkins CI/CD pipeline to transform customer reviews into sentiment analysis results.



### 1. Setting Up Data

```
### Input Data to DB

Navigate to the data directory:

```bash
cd Jenkins-DataPipeline/data
```

Open SQLite and create the `reviews` table:

```bash
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
```

Create the `sentiment_results` table:

```bash
sqlite3 results.db

DROP TABLE IF EXISTS sentiment_results;

CREATE TABLE IF NOT EXISTS sentiment_results (
    id INTEGER PRIMARY KEY,
    review_id INTEGER,
    sentiment TEXT
);

SELECT * FROM sentiment_results;

.exit
```

### 2. Fetch Data from DB(Local)

Navigate back to the root directory:

```bash
cd Jenkins-DataPipeline
```

Set up a virtual environment and install dependencies:

```bash
python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt
```

Fetch reviews, perform sentiment analysis, and generate reports:

```bash
python3 scripts/fetch_reviews.py

python3 scripts/sentiment_analysis.py

python3 scripts/generate_reports.py
```

###  3.Running Tests(Local)

Execute unit tests for fetch_reviews and sentiment_analysis:

```bash
python3 -m unittest tests.test_fetch_reviews

python3 -m unittest tests.test_sentiment_analysis
```

### 4. Jenkins CI/CD Pipeline as Container

Build the Docker image for Jenkins:

```bash
docker build -t my-jenkins .
```

Run Jenkins in a Docker container:

```bash
docker run -p 8080:8080 -p 50000:50000 my-jenkins
```

### 5. Access Jenkins 

`http://localhost:8080/`. Retrieve the initial password from Docker logs:

```bash
docker ps
docker logs <container_id>
```

Follow the setup instructions provided by Jenkins to complete the installation.

![Screenshot 2024-07-02 at 2 08 27 AM](https://github.com/manojbusam/Jenkins-DataPipeline/assets/44409170/aad3a392-e1d4-4992-bd89-ae8aab621d60)


## Project Structure

```
Jenkins-DataPipeline/
├── .git/                       # Git internal directory
├── README.md                   # Project README
├── .gitignore                  # Git ignore file
├── Jenkinsfile                 # Jenkins pipeline script
├── Dockerfile                  # Dockerfile for Jenkins pipeline
├── requirements.txt            # Python dependencies for Jenkins pipeline
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
