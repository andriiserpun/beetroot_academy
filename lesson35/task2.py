import requests
import json
from multiprocessing import Pool

def fetch_comments(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        return []
def fetch_all_comments(subreddit, start_date, end_date):
    base_url = 'https://api.pushshift.io/reddit/comment/search/'
    params = {
        'subreddit': subreddit,
        'after': start_date,
        'before': end_date,
        'size': 500,
        'sort': 'asc',
        'sort_type': 'created_utc'
    }
    comments = []
    current_url = base_url
    while True:
        response = fetch_comments(current_url)
        if not response:
            break
        comments.extend(response)
        current_url = base_url + f'?after={response[-1]["created_utc"]}&subreddit={subreddit}'
    return comments
def save_comments_to_file(comments, file_path):
    with open(file_path, 'w') as file:
        json.dump(comments, file)

if __name__ == '__main__':
    subreddit = 'YOUR_SUBREDDIT'
    start_date = '2023-07-15'
    end_date = '2023-07-18'
    file_path = 'comments.json'
    comments = fetch_all_comments(subreddit, start_date, end_date)
    with Pool() as pool:
        pool.apply_async(save_comments_to_file, args=(comments, file_path))
        pool.close()
        pool.join()
    print('Done')
