from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os, sys

# to run commands in the root dir
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

default_args = {
    'owner': 'Oamen Modupe',
    'start_date': datetime(2025, 3, 15)
}

file_postfix = datetime.now().strftime('%Y%m%d')

dag = DAG(
    dag_id = 'etl_reddit',
    default_args = default_args,
    schedule_interval = '@daily',
    catchup = False,
    tags = ['reddit', 'etl', 'pipeline']
)

# extract from reddit
extract = PythonOperator(
    task_id = 'reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs = {
        'file_name': f'reddit_pipeline_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit':100
    }
)

# upload to s3