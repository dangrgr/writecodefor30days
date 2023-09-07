from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
from . import my_service

class MyServiceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        my_service.myService(self, "myAPIService")

        # example resource
        # queue = sqs.Queue(
        #     self, "MyServiceQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
