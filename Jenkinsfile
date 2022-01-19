def StackID = "myStack"
def RepositoryHTTP = "https://github.com/Figaro555/DeployProcessor.git"

pipeline {
    agent any

    stages {
        stage('Creating Infrastucture') {
            steps {
                echo '-------------Creating Infrastructure---------'
                sh """sudo rm -rf /home/ubuntu/Project"""
                sh """mkdir -p /home/ubuntu/Project"""
                sh """ git clone ${RepositoryHTTP} /home/ubuntu/Project"""

                 withAWS(credentials: 'aws-creds', region: 'us-east-1'){

                    sh """aws cloudformation create-stack \
                    --stack-name ${StackID} \
                    --template-body file:///home/ubuntu/Project/DeployProcessor/1.yaml \
                    --capabilities CAPABILITY_NAMED_IAM"""

                    sh """aws cloudformation wait stack-create-complete \
                    --stack-name ${StackID}"""
                 }
            }
        }
        stage('Updating Infrastucture') {
            steps {
                echo '-------------Updating Infrastructure---------'

                 withAWS(credentials: 'aws-creds', region: 'us-east-1'){
                    sh """aws cloudformation update-stack \
                    --stack-name ${StackID} \
                    --template-body file:///home/ubuntu/Project/DeployProcessor/creatingServices.yaml \
                    --no-use-previous-template \
                    --capabilities CAPABILITY_NAMED_IAM"""

                    sh """aws cloudformation wait stack-update-complete \
                    --stack-name ${StackID}"""
                 }
            }
        }
        stage('Deploying code') {
            steps {
                echo '-------------Deploying Code---------'

                sh """zip /home/ubuntu/Project/DeployProcessor/MChannelSender1.zip /home/ubuntu/Project/DeployProcessor/MChannelSender"""
                sh """zip /home/ubuntu/Project/DeployProcessor/MS3Uploader1.zip /home/ubuntu/Project/DeployProcessor/MS3Uploader1"""

                 withAWS(credentials: 'aws-creds', region: 'us-east-1'){

                    sh """aws lambda update-function-code \
                        --function-name  MChannelSender1 \
                        --zip-file fileb:///home/ubuntu/Project/DeployProcessor/MChannelSender1.zip"""

                    sh """aws lambda update-function-code \
                        --function-name  MS3Uploader1 \
                        --zip-file fileb:///home/ubuntu/Project/DeployProcessor/MS3Uploader1.zip"""


                 }
            }
        }
        stage('Deleting Stack') {
            steps {
                echo '-------------Deleting Stack---------'
                sh 'sleep 30'

                 withAWS(credentials: 'aws-creds', region: 'us-east-1'){

                    sh """aws cloudformation delete-stack \
                    --stack-name ${StackID}"""
                 }
            }
        }

    }
}