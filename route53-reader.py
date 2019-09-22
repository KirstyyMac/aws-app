import boto3

route53 = boto3.client('route53')
dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):
    #get data from route53
    hosted_zones=route53.list_hosted_zones()
    for zone in hosted_zones['HostedZones']:
        dynamodb.put_item(TableName='Route53Records', 
            Item={
                'Id': {'S':zone['Id']},
                'Name': {'S':zone['Name']},
                'ResourceRecordSetCount': {'N':str(zone['ResourceRecordSetCount'])}
            }
        )