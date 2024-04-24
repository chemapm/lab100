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
                checkout scmGit(branches: [[name: '*/main'], [name: '*/develop']], 
                extensions: [], 
                userRemoteConfigs: [[credentialsId: 'GitHub', 
                url: 'https://github.com/chemapm/lab100.git']])
            }
        }
        stage('Imagen python') {
            agent {
                docker {
                    image 'python:3.9-slim'
                }
            }
            steps {
                // Instalación de requerimientos
                sh 'pip install -r requirements.txt'
                
                // Ejecución de tests
                sh 'coverage run -m pytest'
                sh 'coverage report -m'

                // Proceso de lintado
                sh 'flake8 **/*.py'
            }
        }
        stage('Creación de imagen Docker') {
            steps {
                script {
                    dockerImage = docker.build("$registry:$BUILD_NUMBER")
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
