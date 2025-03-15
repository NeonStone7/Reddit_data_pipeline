from utils import OUTPUT_PATH, POST_FIELDS, SECRET, CLIENT_ID, connect_reddit, extract_posts, transform, write_to_csv
import pandas as pd

def reddit_pipeline(file_name:str,
                     subreddit:str,
                     time_filter:str='day',
                     limit:int=None):
    # connect to reddit
    instance = connect_reddit(CLIENT_ID, SECRET, 'etl pipeline')

    # extract data
    posts = extract_posts(instance, subreddit, time_filter, limit)
    
    # transform
    post_df = pd.DataFrame(posts)
    transformed_data = transform(post_df)

    # load to csv
    path = "data/output/data.csv"
    write_to_csv(transformed_data, path)

    return path

print(reddit_pipeline('', 'dataengineering'))