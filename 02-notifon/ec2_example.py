# coding: utf-8
import boto3
session = boto3.Session(profile_name='personal')
ec2 = session.resource('ec2')
key_name = 'py_auto_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('ls', '- py_auto_key.pem')
get_ipython().run_line_magic('ls', '-l py_auto_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
ec2.images.filter(Owners=['amazon'])
images = ec2.images.filter(Owners=['amazon'])
images.name
img = ec2.Image('ami-09693313102a30b2c')
img.name
img = ec2.Image('ami-09693313102a30b2c')
img
img.name
img = ec2.Image('ami-009d6802948d06e52')
img.name
ami_name = 'amzn2-ami-hvm-2.0.20181114-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
img = list(ec2.images.filter(Owners=['amazon'], Filters=filters))
instances = ec2.create_instances(ImageId=img[0].id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key_name)
instances
instances.terminate
instances[0].terminate
inst = instances[0]
inst.terminate
inst.terminate()
instances = ec2.create_instances(ImageId=img[0].id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key_name)
inst = instances[0]
inst.public_dns_name
inst.public_dns_name
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.security_groups
inst.security_groups[0]
inst.security_groups[0]['GroupId']
default_sg_id = inst.security_groups[0]['GroupId']
security_group = ec2.SecurityGroup(default_sg_id)
security_group.authorize_ingress(CidrIp='170.218.0.0/16', FromPort=22, GroupName='SSH_In', IpProtocol='tcp', ToPort=22, DryRun=True)
security_group.authorize_ingress(CidrIp='170.218.0.0/16', FromPort=22, GroupName='default', IpProtocol='tcp', ToPort=22, DryRun=True)
security_group.authorize_ingress(CidrIp='170.218.0.0/16', FromPort=22, IpProtocol='tcp', ToPort=22, DryRun=True)
security_group.authorize_ingress(CidrIp='170.218.0.0/16', FromPort=22, IpProtocol='tcp', ToPort=22)
inst.public_dns_name()
inst.public_dns_name
security_group.authorize_ingress(CidrIp='170.218.0.0/16', FromPort=80, IpProtocol='tcp', ToPort=80)
get_ipython().run_line_magic('history', '')
