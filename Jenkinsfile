pipeline {
    environment {
        registry = "chema545/lab100"
        registryCredential = 'a3500577-ba66-4d5a-9987-9810f477aacc'
        dockerImage = ''
    }

    agent any

    stages {
        stage('Clonado de código fuente') {
            steps {
                git branch: 'main',
                credentialsId: 'GitHub',
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
        stage('Instalacion de requirements') {
            steps {
                sh 'local/bin/pip install -r requirements.txt'
            }
        }
        stage('Ejecución de tests') {
            steps {
                sh '/var/jenkins_home/workspace/lab100/local/bin/coverage run -m pytest'
                sh '/var/jenkins_home/workspace/lab100/local/bin/coverage report -m'
            }
        }
        stage('Proceso de lintado (linting)') {
            steps {
                sh '/var/jenkins_home/workspace/lab100/local/bin/flake8 **/*.py'
            }
        }
        stage('Creación de imagen Docker') {
            steps {
                script {
                    dockerImage = docker.build("$registry:$BUILD_NUMBER")
                    echo "La rama actual es: ${env.BRANCH_NAME}"
                }
            }
        }
        stage('Subida del resultado a Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
