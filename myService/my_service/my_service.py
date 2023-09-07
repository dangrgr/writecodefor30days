import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (aws_apigateway as apigateway,
                     aws_s3 as s3,
                     aws_lambda as lambda_)

class myService(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        bucket = s3.Bucket(self, "myServiceStore-05593820188734")

        handler = lambda_.Function(self, "LambdaHandler",
                    runtime=lambda_.Runtime.PYTHON_3_10,
                    code=lambda_.Code.from_asset("resources"),
                    handler="lambda_handler",
                    environment=dict(
                        BUCKET=bucket.bucket_name)
                    )

        bucket.grant_read_write(handler)

        api = apigateway.RestApi(self, "api-service",
                  rest_api_name="My API Service",
                  description="My API service.")

        get_service_integration = apigateway.LambdaIntegration(handler,
                request_templates={"application/json": '{ "statusCode": "200" }'})

        api.root.add_method("GET", get_service_integration)   # GET /