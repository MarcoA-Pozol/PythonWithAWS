import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(local_file, bucket, s3_file) -> bool:
    """
    Upload a file to an S3 bucket
    
	Args:
    - local_file: File to upload
	- bucket: Bucket to upload to
    - s3_file: S3 object name
    
	Return:
	- Bool: True if file was uploaded, else False
    """
    s3 = boto3.client('s3')
    
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print(f"Upload Successful: {s3_file}")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

# Example usage
upload_to_s3('local_image.jpg', 'your-bucket-name', 'images/remote_image.jpg')