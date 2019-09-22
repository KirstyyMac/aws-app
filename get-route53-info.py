import json
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    return dynamodb.scan(TableName="Route53Records")['Items']