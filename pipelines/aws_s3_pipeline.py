from utils import connect_to_s3, create_bucket_if_not_exits, upload_to_s3
from utils import S3_BUCKET_NAME

def s3_upload(ti):

    file_path = ti.xcoms_pull(task_id = 'reddit_extraction',
    key = 'return_value')

    s3 = connect_to_s3()

    create_bucket_if_not_exits(s3, S3_BUCKET_NAME)
    upload_to_s3(s3, file_path, S3_BUCKET_NAME, '.csv')