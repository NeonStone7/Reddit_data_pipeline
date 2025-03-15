from utils import SECRET, CLIENT_ID, connect_reddit, extract_posts

def reddit_pipeline(file_name:str,
                     subreddit:str,
                     time_filter:str='day',
                     limit:int=None):
    # connect to reddit
    instance = connect_reddit(CLIENT_ID, SECRET, 'etl pipeline')

    # extract data
    posts = extract_posts(instance, subreddit, time_filter, limit)
    print(posts)
    # transform

    # load to csv
    return None
instance = connect_reddit(CLIENT_ID, SECRET, 'etl pipeline')

# extract data
posts = extract_posts(instance, 'dataengineering', 'day', 100)
print([post for post in posts])