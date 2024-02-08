import aws_cdk as core
import aws_cdk.assertions as assertions

from seedfarmer_demo.seedfarmer_demo_stack import SeedfarmerDemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in seedfarmer_demo/seedfarmer_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SeedfarmerDemoStack(app, "seedfarmer-demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
