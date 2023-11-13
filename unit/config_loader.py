import json

def load_config(file_path = 'config.json'):
    try:
        with open(file_path, 'r') as file:
            config_data = json.load(file)
    except FileNotFoundError:
        config_data = {}

    protocol = config_data.get('protocol')
    domain = config_data.get('domain')
    port = config_data.get('port')
    url = f"{protocol}://{domain}:{port}"

    return protocol, domain, port, url

def change_count(file_path = 'config.json'):

    with open(file_path, 'r') as file:
        data = json.load(file)

    count_value = data.get('count', 0)

    new_count_value = count_value + 1
    data['count'] = new_count_value

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f'Current count value for images: {new_count_value}')
    return new_count_value

   