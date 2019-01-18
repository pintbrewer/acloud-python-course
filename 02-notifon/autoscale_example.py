# coding: utf-8
as_client = session.client('autoscaling')
as_client.describe_auto_scaling_groups()
as_client.describe_policies(AutoScalingGroupName='notifon')
response = as_client.execute_policy(AutoScalingGroupName='notifon', PolicyName='notifon-up')
