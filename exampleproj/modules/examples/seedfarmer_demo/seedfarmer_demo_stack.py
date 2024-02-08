from aws_cdk import (
    # Duration,
    Stack,
    RemovalPolicy,
    aws_s3 as s3
    # aws_sqs as sqs,
)
from constructs import Construct

class SeedfarmerDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create an S3 bucket
        s3.Bucket(self, "MyS3Bucket",
                   bucket_name="seedfarmer08022024",
                   removal_policy=RemovalPolicy.DESTROY  # This will delete the bucket when the stack is destroyed
                   )
