pipeline {
    agent any
    
    stages {

        stage("Code"){
            steps {
                echo "Cloning the code"
                git url: "https://github.com/data-architect-ai/Jenkins-DataPipeline.git", branch: "main"
            }
        }
        stage("build"){
            steps {
                echo "Building the code"
                sh "docker build -t data-pipeline ."
                sh "docker run --detach 'data-pipeline'"
            }
        }
        
                
        stage('Fetch Reviews') {
            steps {
                sh 'python3 scripts/fetch_reviews.py'  // Execute fetch_reviews.py script
                sh 'python3 scripts/sentiment_analysis.py'  // Execute sentiment_analysis.py script
                sh 'python3 scripts/generate_reports.py'  // Execute generate_reports.py script
            }
        }
        
        stage('Run Tests') {
            steps {
                // Run unit tests for fetch_reviews.py
                sh 'python3 -m unittest tests/test_fetch_reviews.py'
                
                // Run unit tests for sentiment_analysis.py
                sh 'python3 -m unittest tests/test_sentiment_analysis.py'
            }
        }
        
        stage('Sentiment Analysis') {
            steps {
                sh 'python3 scripts/sentiment_analysis.py'  // Execute sentiment_analysis.py script
            }
        }
        
        stage('Generate Reports') {
            steps {
                sh 'python3 scripts/generate_reports.py'  // Execute generate_reports.py script
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
