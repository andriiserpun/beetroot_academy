import requests
import json

url = "https://rickandmortyapi.com/api/character/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    comments = data['results']
    sorted_comments = sorted(comments, key=lambda x: x['created'], reverse=False)
    with open('comments.json', 'w', encoding='utf-8') as json_file:
        json.dump(sorted_comments, json_file, ensure_ascii=False, indent=4)
    print("Данные успешно сохранены в файл 'comments.json'")
else:
    print("Произошла ошибка при выполнении запроса:", response.status_code)
