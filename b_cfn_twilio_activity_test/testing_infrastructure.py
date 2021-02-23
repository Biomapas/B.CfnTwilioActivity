from aws_cdk.core import Stack

from b_cfn_twilio_activity.function import TwilioActivitySingletonFunction
from b_cfn_twilio_activity.resource import TwilioActivityResource
from b_cfn_twilio_activity.twilio_activity import TwilioActivity


class TestingInfrastructure(Stack):
    def __init__(self, scope: Stack):
        super().__init__(
            scope=scope,
            id=f'TestingStack',
            stack_name=f'TestingStack'
        )

        function = TwilioActivitySingletonFunction(
            scope=self,
            name='TestingFunction',
            twilio_account_sid='Test1',
            twilio_auth_token='Test2',
            twilio_workspace_sid='Test3'
        )

        offline_activity = TwilioActivity(friendly_name='Offline', availability=False, default=True)

        TwilioActivityResource(
            scope=self,
            activity_function=function,
            activities=[offline_activity]
        )
