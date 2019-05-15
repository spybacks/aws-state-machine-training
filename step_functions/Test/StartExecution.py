import boto3
import time
import json

stepfunctions = boto3.client('stepfunctions', region_name="eu-west-1")

if __name__ == '__main__':

    print("stepfunctions")
    response = stepfunctions.start_execution(
        stateMachineArn='{rplace with correct arn }',
        name='test',
        input=json.dumps({"run": "SomeRun","version": "0.1","running_type":"sdfsdf","s3_bucket": "s3://test/"}))


    print(response)

