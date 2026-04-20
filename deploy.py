import boto3

BUCKET_NAME = "your-actual-bucket-name"   # change this

s3 = boto3.client('s3')

try:
    s3.upload_file('index.html', BUCKET_NAME, 'index.html')
    print("✅ File uploaded successfully")
except Exception as e:
    print("❌ Upload failed:", e)
