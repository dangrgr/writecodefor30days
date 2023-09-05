import os
import json

def lambda_handler(event, context):
    message = 'Hello {}{}'.format(event['string'], event['punctuation'])  
    return { 
        'message' : message
    }


# test
event = {
    "string": "World",
    "punctuation": "!"
}

print(lambda_handler(event,0))