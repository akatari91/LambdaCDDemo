import json


def lambda_handler(event, context):
    response = "Hello from lambda"
    return {"statusCode": 200, "body": json.dumps(response)}