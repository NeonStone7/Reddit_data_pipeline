from praw import Reddit
import sys

def connect_reddit(client_id, secret, user_agent)-> Reddit:
    try:
        reddit = Reddit(
            client_id = client_id,
            client_secret = secret,
            user_agent = user_agent
        )
        print('Connection to reddit successful')
        return reddit
    
    except Exception as e:
        print(e)
        sys.exit(1)
    

def extract_posts(instance:Reddit,
                    subreddit:str, 
                    time_filter:str,
                    limit=None):
    subreddit = instance.subreddit(subreddit)
    posts = subreddit.top(time_filter, limit=limit)

    # posts_list = []
    return posts
