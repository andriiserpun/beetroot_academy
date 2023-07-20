import aiohttp
import asyncio
import json
async def fetch_comments(session, url):
    async with session.get(url) as response:
        return await response.json()
async def fetch_all_comments(subreddit):
    base_url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}"
    all_comments = []
    async with aiohttp.ClientSession() as session:
        try:
            while True:
                url = f"{base_url}&size=100&{'&before=' + (all_comments[-1]['created_utc']) if all_comments else ''}"
                data = await fetch_comments(session, url)
                comments = data.get('data')
                if not comments:
                    break
                all_comments.extend(comments)
                print(f"Uploaded {len(all_comments)} comments.")
        except Exception as e:
            print(f"an error occurred while uploading comments: {e}")
    return all_comments
async def main():
    subreddit = "your_selected_subreddit"
    comments = await fetch_all_comments(subreddit)
    with open(f"{subreddit}_comments.json", "w") as file:
        json.dump(comments, file, ensure_ascii=False, indent=2)
    print("comments loaded to file")

if __name__ == "__main__":
    asyncio.run(main())
