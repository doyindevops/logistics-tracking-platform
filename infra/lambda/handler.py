import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def lambda_handler(event, context):
    http_method = event.get("httpMethod")
    if http_method == "POST":
        body = json.loads(event['body'])
        parcel_id = body.get('parcel_id')
        status = body.get('status', 'created')
        table.put_item(Item={
            "parcel_id": parcel_id,
            "status": status
        })
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Parcel tracked!", "parcel_id": parcel_id})
        }
    elif http_method == "GET":
        parcel_id = event["pathParameters"]["id"]
        response = table.get_item(Key={"parcel_id": parcel_id})
        item = response.get("Item")
        if item:
            return {
                "statusCode": 200,
                "body": json.dumps(item)
            }
        else:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Parcel not found"})
            }
    else:
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Method not allowed"})
        }
