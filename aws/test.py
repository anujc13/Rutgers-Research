import boto3

region_name = 'us-east-1'
aws_access_key_id = 'AKIAVGWXFZ3AB7C4D2VU'
aws_secret_access_key = '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'

endpoint_url = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'

# Uncomment this line to use in production
# endpoint_url = 'https://mturk-requester.us-east-1.amazonaws.com'

client = boto3.client(
    'mturk',
    endpoint_url=endpoint_url,
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

response = client.list_qualification_types(
    MustBeRequestable=False,
    MustBeOwnedByCaller=True,
    MaxResults=100
)

print(response)