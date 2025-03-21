import time
import requests
from tinydb import TinyDB
from datetime import datetime

def extract_data():
    url = "https://api.coinbase.com/v2/prices/spot"
    params = {"currency": "USD"}
    response = requests.get(url, params=params)
    return response.json()['data']

def transform_data_bitcoin(response):
    value = response['amount']
    crypto = response['base']
    currency = response['currency']

    data_transformed = {
        'crypto': crypto,
        'currency': currency,
        'value': value
    }

    return data_transformed

def save_data_tinydb(data, db_path="bitcoin_data.json"):
    db = TinyDB(db_path)
    db.insert(data)
    print(f"Data saved to {db_path}")

if __name__ == "__main__":
    while True:
        data_json = extract_data()
        data_transformed = transform_data_bitcoin(data_json)
        save_data_tinydb(data_transformed)
        time.sleep(15) # 15 seconds


