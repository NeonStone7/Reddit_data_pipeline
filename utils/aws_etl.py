from utils import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY
import s3fs

def connect_to_s3():

    try: 
        s3 = s3fs.S3FileSystem(
            anon = False,
            key = AWS_ACCESS_KEY_ID,
            SECRET = AWS_SECRET_KEY
        )
        return s3
    
    except Exception as e:
        print('could not connect to s3')
        print(e)
        sys.exit(1)
    

def create_bucket_if_not_exits(s3:  s3fs.S3FileSystem,
        bucket:str):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            print('bucket created')
        else:
            print('bucket already exists')
    
    except Exception as e:
        print(e)

def upload_to_s3(s3: s3fs.S3FileSystem,
        file_path:str, bucket_str, s3_filename:str):
    
    try:
        s3.put(file_path, bucket+'/raw/'+s3_filename)
    except Exception as e:
        print('File not found')
        print(e)
