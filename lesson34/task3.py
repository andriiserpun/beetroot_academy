import requests
import json
from concurrent.futures import ThreadPoolExecutor
def fetch_comments(subreddit, num_comments=1000, batch_size=100):
    base_url = "https://api.pushshift.io/reddit/comment/search/"
    params = {
        "subreddit": subreddit,
        "size": batch_size,
        "sort": "asc",
        "sort_type": "created_utc",
    }
    comments = []
    total_processed = 0
    while total_processed < num_comments:
        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            comments.extend(data["data"])
            total_processed += len(data["data"])
            if len(data["data"]) < batch_size:
                break
            params["before"] = data["data"][-1]["created_utc"]
        except Exception as e:
            print("Error occurred:", e)
            break
    return comments[:num_comments]
def main():
    subreddit = "YOUR_SUBREDDIT_NAME"
    num_comments = 1000
    with ThreadPoolExecutor() as executor:
        future = executor.submit(fetch_comments, subreddit, num_comments)
        comments = future.result()
    with open("comments.json", "w", encoding="utf-8") as file:
        json.dump(comments, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
