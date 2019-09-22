import json

hosted_zones = """{
  "ResponseMetadata": {
    "RequestId": "b792f4c6-9467-4ab9-ba07-ac3e836c68e5",
    "HTTPStatusCode": 200,
    "HTTPHeaders": {
      "x-amzn-requestid": "b792f4c6-9467-4ab9-ba07-ac3e836c68e5",
      "content-type": "text/xml",
      "content-length": "1154",
      "date": "Sat, 21 Sep 2019 00:01:46 GMT"
    },
    "RetryAttempts": 0
  },
  "HostedZones": [
    {
      "Id": "/hostedzone/Z2O9QZWYBSPMK8",
      "Name": "thecloudcon.net.",
      "CallerReference": "RISWorkflow-RD:c38b42fd-475a-4358-a3ff-9cbea3a004e7",
      "Config": {
        "Comment": "HostedZone created by Route53 Registrar",
        "PrivateZone": false
      },
      "ResourceRecordSetCount": 2
    },
    {
      "Id": "/hostedzone/Z06337433R7I8KFS9UHDR",
      "Name": "local.",
      "CallerReference": "co2b2lxosjew6jzlg2pkwzouvjzjvgmy-jxcjqyzd",
      "Config": {
        "Comment": "Created by AWS Cloud Map namespace with ARN arn:aws:servicediscovery:ap-southeast-2:557710541832:namespace/ns-ssm5u7xnowlgklym",
        "PrivateZone": true
      },
      "ResourceRecordSetCount": 2,
      "LinkedService": {
        "ServicePrincipal": "servicediscovery.amazonaws.com",
        "Description": "arn:aws:servicediscovery:ap-southeast-2:557710541832:namespace/ns-ssm5u7xnowlgklym"
      }
    }
  ],
  "IsTruncated": false,
  "MaxItems": "100"
}"""

route53_dict = json.loads(hosted_zones)
hosted_zones_dict = route53_dict['HostedZones']

for zones in hosted_zones_dict:
    print(zones["Name"])
    print(zones["Id"])
    print(zones["ResourceRecordSetCount"])