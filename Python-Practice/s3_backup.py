"""
This is a script to take a backup from local to AWS S3 bucket
boto3 -> used to do AWS tasks using python
pip install boto3
"""

import boto3

s3 = boto3.resource("s3")   
def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)


def create_bucket(s3,bucket_name,region):
    s3.create_bucket(Bucket=bucket_name,
                     CreateBucketConfiguration={
                    'LocationConstraint': region,
                     },)
    print("Bucket created successfully")

def upload_backup_s3(s3,file_name,bucket_name,key_name):
    """
    uploads a given backup file path to a given s3 bucket 
    with a new name(key)
    """

    data= open(file_name, 'rb') # file read in binary
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("File uploaded successfully")

bucket_name="Python-Practice"
region="us-east-2"
file_name="C:\\Users\\panka\\OneDrive\\Documents\\Devops\\Python Practice\\backups\\backup_2025-08-14.tar.gz"
key_name="MyDaily-backup.tar.gz"    

upload_backup_s3(s3,file_name,bucket_name,key_name)
create_bucket(s3,bucket_name,region)
show_buckets(s3)