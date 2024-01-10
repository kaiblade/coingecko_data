from pycoingecko import CoinGeckoAPI
import requests
from requests import exceptions as e
import time
from concurrent.futures import ThreadPoolExecutor
import json



def get_price_data(token):
    time.sleep(1.5)
    token_ids_raw = []
    
    for tok in token['token_data']:

            token_ids_raw.append(tok['name'].replace(' ', '-'))
    

    
    token_ids = list(set(token_ids_raw))

        

    network_price_data = {}

    network_price_data['blockchain']= token['blockchain']
    tokens_data = []
    try:
        for token_id in token_ids:
            tokens_prices_data = {}
            tokens_prices_data['token_id'] = token_id
            token_prices_data = cg.get_coin_market_chart_by_id(id=(token_id).lower(),vs_currency='usd',days='7')
            tokens_prices_data['price_data'] = token_prices_data['prices']
            tokens_data.append(tokens_prices_data)
    
    except (ValueError):
        print('price data doesnt exists')
        
    
    network_price_data['tokens_prices'] = tokens_data
    price_data.append(network_price_data)


with open("token_data.json", "r") as file:
    token_data = json.load(file)

cg = CoinGeckoAPI()
price_data = []

with ThreadPoolExecutor(max_workers = 3) as pool:
    pool.map(get_price_data, token_data)

print(f'token_data_len: {len(price_data)}')


with open("price_data.json", "w") as file:
    json.dump(price_data, file)