import requests

def extract_data():
    url = "https://api.coinbase.com/v2/prices/spot"
    params = {"currency": "USD"}  # Adding currency parameter for better response
    response = requests.get(url, params=params)
    data = response.json()
    return {
        'status_code': response.status_code,
        'data': data,
        'amount': data['data']['amount'] if 'data' in data and 'amount' in data['data'] else None
    }

result = extract_data()
print("Status Code:", result['status_code'])
print("Data:", result['data'])
print("Amount:", result['amount'])

