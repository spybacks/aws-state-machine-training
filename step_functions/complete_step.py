import sys
import logging
import boto3
import os
import time
import json
from datetime import datetime, timedelta


def lambda_handler(event, context):
    print(json.dumps(event))
    event['completed'] = 'end'
    return event

