import boto3
from botocore.exceptions import NoCredentialsError
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()
BUCKET = os.getenv("S3_BUCKET")

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
    
def create_and_write_txt_file(filename: str, filetitle: str, filetext: str) -> str:
    """
    Create and write a new txt file.
    
    Args:
    - filename: Local name of the file 
    - filetitle: Title of the file
    - filetext: Text of the file

    Return:
    - str: Path to the created file
    """
    directory = "./files/txt/"
    os.makedirs(directory, exist_ok=True) 

    filepath = f"{directory}{filename}.txt"
    
    with open(filepath, "w") as file:
        file.write(f"{filetitle}\n")
        file.write(f"{filetext}\n")
    
    return filepath 

FILE = create_and_write_txt_file(
    filename="WhatIsAWS",
    filetitle="Do you already know what AWS is?",
    filetext="AWS (Amazon Web Services) is a cloud computing platform that offers a wide range of services, including computing power, storage, databases, machine learning, security, and networking. Businesses and developers use AWS to build, deploy, and scale applications without needing physical hardware."
)

print(f"File created at: {FILE}")
upload_to_s3(bucket=BUCKET, local_file=FILE, s3_file="txt/remote_text.txt")