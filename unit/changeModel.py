import requests
from config_loader import load_config

protocol, domain, port, url = load_config()

opt = requests.get(url=f'{url}/sdapi/v1/options')
opt_json = opt.json()
opt_json['sd_model_checkpoint'] = 'uberRealisticPornMerge_urpmv12.safetensors' # change name model
response = requests.post(url=f'{url}/sdapi/v1/options', json=opt_json)
print(response.json())
