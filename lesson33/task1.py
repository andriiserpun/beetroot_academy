import requests

def download_robots_txt(url):
    try:
        robots_url = url.rstrip('/') + '/robots.txt'
        response = requests.get(robots_url)
        if response.status_code == 200:
            content = response.text
            with open('robots.txt', 'w', encoding='utf-8') as file:
                file.write(content)
            print("robots.txt downloaded and saved successfully.")
        else:
            print(f"Failed to download robots.txt. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


wikipedia_url = "https://www.wikipedia.org/"
download_robots_txt(wikipedia_url)
