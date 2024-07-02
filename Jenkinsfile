pipeline {
    agent any
    
    stages {
        stage('Setup') {
            steps {
                // Set up environment, install dependencies, etc.
                // Example:
                sh 'pip install -r requirements.txt'  // Install required Python packages
            }
        }
        
        stage('Fetch Reviews') {
            steps {
                sh 'python scripts/fetch_reviews.py'  // Execute fetch_reviews.py script
                sh 'python scripts/sentiment_analysis.py'  // Execute sentiment_analysis.py script
                sh 'python scripts/generate_reports.py'  // Execute generate_reports.py script
            }
        }
        
        stage('Run Tests') {
            steps {
                // Run unit tests for fetch_reviews.py
                sh 'python -m unittest tests/test_fetch_reviews.py'
                
                // Run unit tests for sentiment_analysis.py
                sh 'python -m unittest tests/test_sentiment_analysis.py'
            }
        }
        
        stage('Sentiment Analysis') {
            steps {
                sh 'python scripts/sentiment_analysis.py'  // Execute sentiment_analysis.py script
            }
        }
        
        stage('Generate Reports') {
            steps {
                sh 'python scripts/generate_reports.py'  // Execute generate_reports.py script
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline finished successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
