pipeline {
    agent any

    stages {
        stage('Clonado de código fuente') {
            steps {
                git credentialsId: 'bbc43dbe-0883-4786-9b1b-eed84b178421', url: 'https://github.com/chemapm/lab100/blob/main/Jenkinsfile.git'
            }
        }
        stage('Ejecución de tests') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'coverage run -m pytest'
                sh 'coverage report -m'
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
                    docker.build('test')
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
                    docker.withRegistry('', 'b7c76036-c919-4172-8aa9-0727c30ef20e') {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
