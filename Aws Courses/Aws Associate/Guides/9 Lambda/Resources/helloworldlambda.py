import json

def lambda_handler(event, context):
    print("In lambda handler")

    result = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps("Hello [YOUR NAME HERE]")
    }

    return result