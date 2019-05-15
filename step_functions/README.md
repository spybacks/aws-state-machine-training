# Audit - AWS Lambda Functions

## Creating the Lambda functions Deployment Package to be uploaded via the AWS console

``` bash
# install serverless https://serverless.com/framework/docs/providers/aws/guide/installation/
# serverless plugin install --name serverless-step-functions --stage dev
# npm install --save-dev serverless-pseudo-parameters
# npm install -g serverless


# Create a zip file of the project
$ zip -R  lambda_code.zip *.py


# Deploy the Lambda function
$ serverless deploy --stage dev
```
