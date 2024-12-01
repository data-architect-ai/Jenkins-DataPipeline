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
