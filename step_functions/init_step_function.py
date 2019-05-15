import sys
import logging
import boto3
import os
import time
import json
from datetime import datetime, timedelta

activity = os.getenv("ACTIVITY","")

def lambda_handler(event, context):
    print(json.dumps(event))
    event["testData"]="test"
    # send sqs
    # send     activity

    return event


if __name__ == "__main__":
    event = {"run": "SomeRun",
             "version": "0.1",
             "running_type":"66665",
             "s3_bucket": "s3://tes/"}

    lambda_handler(event, None)