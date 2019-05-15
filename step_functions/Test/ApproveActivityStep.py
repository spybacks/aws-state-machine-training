import boto3
import time
import json

stepfunctions = boto3.client('stepfunctions', region_name="eu-west-1")

if __name__ == '__main__':

    print("stepfunctions")
    task = stepfunctions.get_activity_task(activityArn="replace with activity arn", workerName="preProccess")
    print(task)
    print ("assuming we did a task")
    time.sleep(15)

    # Perform your task here
    # In this example we continue on in the same function,
    # but the continuation could be a separate event,
    # just as long as you can retrieve the task token

    ##TODO: add your pre processing code here

    event = {"run": "Some Data",
             "version": "0.1",
             "running_type": "Testing",
             "s3_bucket": "s3://test/"}
    print(event)
    response = stepfunctions.send_task_success(taskToken=task['taskToken'], output=json.dumps(event))
    print(response)