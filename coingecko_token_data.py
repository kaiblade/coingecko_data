from pycoingecko import CoinGeckoAPI
import requests
from requests import exceptions as e
import time
from concurrent.futures import ThreadPoolExecutor
import json



def get_token_data(network):
    time.sleep(1.5)
    token_info = {}
    if network["id"]:

        try:
            response = requests.get(f'https://tokens.coingecko.com/{str(network["id"])}/all.json')
            data = response.json()

            if data['tokens']:
                token_info['blockchain']= network["id"]
                token_info['token_data'] = data['tokens']
                token_data.append(token_info)

                
        except e.JSONDecodeError:
            print(f'Token data unavailable for {network["id"]}')
        print('')
        print('')




cg = CoinGeckoAPI()
network_list = cg.get_asset_platforms()


token_data = []


count = 0

with ThreadPoolExecutor(max_workers = 4) as pool:
    pool.map(get_token_data, network_list)

print(f'token_data_len: {len(token_data)}')


with open("token_data.json", "w") as file:
    json.dump(token_data, file)