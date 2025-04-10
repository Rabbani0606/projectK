def lambda_handler(event, context):
    # You can print to logs for debugging
    print("Received event:", event)

    # Return a simple JSON response
    return {
        "statusCode": 200,
        "body": "Hello from Lambda!"
    }
