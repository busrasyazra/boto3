import boto3    
s3 = boto3.resource('s3')
bucket = s3.Bucket('busra-boto3-bucket')
bucket.delete()

for bucket in s3.buckets.all():
    print(bucket.name)