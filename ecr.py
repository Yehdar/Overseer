import boto3

ecr_client = boto3.client('ecr')

response = ecr_client.create_repository(repositoryName="overseer")

print(response['repository']['repositoryUri'])
