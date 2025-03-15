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

AWS_ACCESS_KEY_ID = parser.get('aws', 'aws access key id')
AWS_SECRET_KEY= parser.get('aws', 'aws secret key')
AWS_SESSION_TOKEN = parser.get('aws', 'aws session token')
AWS_REGION = parser.get('aws', 'aws region')
S3_BUCKET_NAME = parser.get('aws', 's3 bucket name')

POST_FIELDS = (
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)