import pulumi
from pulumi_aws import s3
from pulumi_gcp import storage
import os
from pulumi import automation as auto
from dotenv import load_dotenv

load_dotenv()
project_name = "app_bucket_project"

def create_bucket(environment, region, bucket_name, stack_name):
    try:
        stack = auto.create_or_select_stack(stack_name=stack_name,
                                            project_name=project_name,
                                            program=create_program(environment, region, bucket_name))
        stack.workspace.install_plugin("aws", "v5.0.0")
        stack.workspace.install_plugin("gcp", "v5.0.0")
        stack.set_config("aws:region", auto.ConfigValue(region))

        stack.set_config("gcp:region", auto.ConfigValue(region))
        stack.set_config("gcp:project", auto.ConfigValue(os.getenv('GOOGLE_CLOUD_PROJECT')))
        stack.set_config("gcp:credentials", auto.ConfigValue(os.getenv('GOOGLE_CLOUD_KEYFILE_JSON')))
        stack.up(on_output=print)

        # Retrieve the outputs after the up operation
        outputs = stack.outputs()
        
        return "Bucket created successfully", outputs
    except Exception as e:
        return str(e), {}

def destroy_bucket(environment, region, bucket_name, stack_name):
    try:
        stack = auto.create_or_select_stack(stack_name=stack_name,
                                            project_name=project_name,
                                            program=create_program(environment, region, bucket_name))
        stack.destroy(on_output=print)
        stack.workspace.remove_stack(stack_name)
        return "Bucket and stack destroyed successfully"
    except Exception as e:
        return str(e)

def create_program(environment, region, bucket_name):
    def pulumi_program():
        if environment == 'AWS':
            bucket = s3.Bucket(bucket_name)
            pulumi.export('bucketName', bucket.id)
            pulumi.export('region', region)
        elif environment == 'GCP':
            bucket = storage.Bucket(bucket_name, location=region)
            pulumi.export('bucketName', bucket.name)
            pulumi.export('region', region)
    return pulumi_program
