import boto3

from application import application


def create_table():
    ddb = boto3.resource('dynamodb', region_name=application.config['AWS_REGION'])
    ddb.create_table(
        TableName=application.config['STARTUP_SIGNUP_TABLE'], 
        AttributeDefinitions=[
            {
                'AttributeName': 'email',
                'AttributeType': 'S'
            }
        ],
        KeySchema=[
            {
                'AttributeName': 'email',
                'KeyType': 'HASH'
            }
        ], 
        BillingMode='PAY_PER_REQUEST'
    )
