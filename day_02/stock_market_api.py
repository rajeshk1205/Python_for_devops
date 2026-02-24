import requests

api_key = "CX1VA5WUJF5D8VM6"

api_url = "https://www.alphavantage.co/" # Api endpoint

def get_stock_market_details(symbol):
    query = f'query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    response = requests.get(url=api_url+query)
    print(response.json())

    for key, value in response.json().items():
        if key == 'Meta data':
            print(key,value)


symbol=input("Enter the symbol you want for the stock market details eg. AMZN, IBM, GOGL: ")
get_stock_market_details(symbol)