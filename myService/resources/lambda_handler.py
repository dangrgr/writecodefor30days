import os
import json

def lambda_handler(event, context):
    message = '{}{}'.format(event['string'], event['punctuation'])  
    return { 
        'message' : message
    }


# test
event = {
    "string": "Hello World",
    "punctuation": "!"
}

print(lambda_handler(event,0))