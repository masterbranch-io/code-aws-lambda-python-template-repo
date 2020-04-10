import json
from datetime import datetime as dt


def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(f'Hello from Lambda @ {dt.now()}!')
    }
