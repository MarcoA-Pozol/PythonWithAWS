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

def list_s3_files(bucket: str, prefix: str = '') -> None:
    """
    List files in an S3 bucket
    
    Args:
    - bucket: Bucket name
    - prefix: Only list files with this prefix (like a directory)
    
    Return:
    - None: Prints the list of files
    """
    s3 = boto3.client('s3')
    
    try:
        response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
        if 'Contents' in response:
            print(f"Files in {bucket}/{prefix}:")
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print(f"No files found in {bucket}/{prefix}")
    except Exception as e:
        print(f"Error listing files: {e}")

# Example usage
list_s3_files('your-bucket-name', 'images/')

def delete_s3_file(bucket: str, s3_file: str) -> None:
    """
    Delete a file from an S3 bucket
    
    Args:
    - bucket: Bucket name
    - s3_file: File to delete
    
    Return:
    - None: Prints success/error message
    """
    s3 = boto3.client('s3')
    
    try:
        s3.delete_object(Bucket=bucket, Key=s3_file)
        print(f"Successfully deleted {s3_file} from {bucket}")
    except Exception as e:
        print(f"Error deleting file: {e}")

# Example usage
delete_s3_file('your-bucket-name', 'images/remote_image.jpg')