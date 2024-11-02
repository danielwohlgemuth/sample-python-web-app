import boto3
import flask


# Create the Flask app
application = flask.Flask(__name__)

# Load config values specified above
application.config.from_object(__name__)

# Load configuration vals from a file
application.config.from_pyfile('application.config', silent=True)

ddb = boto3.resource('dynamodb', region_name=application.config['AWS_REGION'])


def create_table():
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


def store_in_dynamo(signup_data):
    table = ddb.Table(application.config['STARTUP_SIGNUP_TABLE'])
    table.put_item(
        Item=signup_data
    )
