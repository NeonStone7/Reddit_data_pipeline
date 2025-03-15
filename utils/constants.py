import configparser
import os

parser = configparser.ConfigParser()
# join the dirname with the config.conf path
parser.read(
    os.path.join(os.path.dirname(__file__),
    '../config/config.conf')
)

SECRET = parser.get('api_keys', 'reddit_secret_key')
CLIENT_ID = parser.get('api_keys', 'reddit_client_id')

DATABASE_HOST = parser.get('database', 'database_host')
DATABASE_NAME = parser.get('database', 'database_name')
DATABASE_PORT = parser.get('database', 'database_port')
DATABASE_USERNAME = parser.get('database', 'database_username')
DATABASE_PASSWORD = parser.get('database', 'database_password')

INPUT_PATH = parser.get('file_paths', 'input_path')
OUTPUT_PATH = parser.get('file_paths', 'output_path')

# [aws]
# aws_access_key_id = [aws access key id]
# aws_secret_access_key= [aws secret key]
# aws_session_token= [aws session token]
# aws_region = [aws region]
# aws_bucket_name = [s3 bucket name]

