def is_exist(item):
    channel_list = [1, 2, 3, 'name', 'example']

    if item in channel_list:
        return "Yes"
    else:
        return "No"
print(is_exist("name"))