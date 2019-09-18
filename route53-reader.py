import json
import boto3
import re
import uuid
import time
import random
from datetime import datetime

print('Loading function ' + datetime.now().time().isoformat())
route53 = boto3.client('route53')
ec2 = boto3.resource('ec2')
compute = boto3.client('ec2')
dynamodb_client = boto3.client('dynamodb')
dynamodb_resource = boto3.resource('dynamodb')

def lambda_handler(event, context):
    hosted_zones = route53.list_hosted_zones()
    print hosted_zones