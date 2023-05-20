import json
with open('phonebook.json', 'r') as json_file:
    phonebook = json.load(json_file)
    print(phonebook)
print([name['last_name'] for name in phonebook['first_name']])