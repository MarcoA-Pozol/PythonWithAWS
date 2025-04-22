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

def download_from_s3(bucket: str, s3_file: str, local_file: str) -> bool:
    """
    Download a file from an S3 bucket
    
    Args:
    - bucket: Bucket to download from
    - s3_file: S3 object name
    - local_file: File to save to locally
    
    Return:
    - Bool: True if file was downloaded, else False
    """
    s3 = boto3.client('s3')
    
    try:
        s3.download_file(bucket, s3_file, local_file)
        print(f"Download Successful: {local_file}")
        return True
    except Exception as e:
        print(f"Error downloading file: {e}")
        return False

# Example usage
download_from_s3('your-bucket-name', 'images/remote_image.jpg', 'downloaded_image.jpg')