pipeline {
    agent {
        docker { 
            image 'python:3.8'
            args '--network=host'
        }
    }
    environment {
        HOME = "${env.WORKSPACE}@tmp"
        BIN_PATH = "${HOME}/.local/bin/"
    }
    stages {
        stage('Git Clone') {
            steps {
                git changelog: false, url: 'http://gitlab.devops.ru/lollolol/fastapi-calculator.git'
            }
        }
        stage('Prepare') {
            steps {

                sh 'python --version'
                sh 'pip install virtualenv'
                sh "${BIN_PATH}virtualenv venv"
                sh 'bash -c "source venv/bin/activate"'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps{
                
                sh 'python -m pytest'
                sh "${BIN_PATH}flake8 ."
                sh 'python -m mypy src --explicit-package-bases'
            }
        }
    }
}
