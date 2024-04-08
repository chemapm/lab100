pipeline {
    environment {
        registry = "chema545/lab100"
        registryCredential = 'b7c76036-c919-4172-8aa9-0727c30ef20e'
        dockerImage = ''
    }

    agent any

    stages {
        stage('Clonado de código fuente') {
            steps {
                git branch: 'main',
                credentialsId: 'bbc43dbe-0883-4786-9b1b-eed84b178421',
                url: 'https://github.com/chemapm/lab100.git'
            }
        }
        stage('Version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Crear y activar Entorno Virtual') {
            steps {
                //sh 'apt install python3.11-venv'
                sh 'python3 -m venv local'
                sh '. local/bin/activate'
            }
        }
        stage('Ejecución de tests') {
            steps {
                sh 'local/bin/pip install -r requirements.txt'
                sh '/var/jenkins_home/workspace/lab100/local/bin/coverage run -m pytest'
                sh '/var/jenkins_home/workspace/lab100/local/bin/coverage report -m'
            }
        }
        stage('Proceso de lintado (linting)') {
            steps {
                sh 'flake8 .'
            }
        }
        stage('Creación de imagen Docker') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Subida del resultado a Docker Hub') {
            when {
                anyOf {
                    branch 'develop'
                    branch 'master'
                    branch 'main'
                }
            }
            steps {
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
