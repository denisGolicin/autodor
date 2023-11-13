import requests
from config_loader import load_config

protocol, domain, port, url = load_config()

response = requests.get(url=f'{url}/sdapi/v1/sd-models')
print(response.json())