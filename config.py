# json

import urllib.parse



API_KEY = {
    #"api-key": "a577a94f-33e4-46a1-8e7a-cad952b7e191"
    "api-key": "eb58dcba-6ffa-4bfd-91ac-db2dd4723860"
}

url = {
    "metadata_v2_url": "https://pro-api.coinmarketcap.com/v2/cryptocurrency/info",
    # Coinmarketcap API url to retrieve metadata
    "quotes_latest_v1_url": "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",
    # Coinmarketcap API url to retrieve information about all coin categories available on CoinMarketCap
    "listings_latest_url": "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    # Coinmarketcap API url to retrieve information about a cryptocurrency with the latest market data
}

cryptoCurrencies = {
    "cryptoCurrency1": "BTC",
    "cryptoCurrency2": "ETH",
    "cryptoCurrency3": "USDT",
    "cryptoCurrency4": "USDC",
    "cryptoCurrency5": "BNB",
    "cryptoCurrency6": "ADA",
    "cryptoCurrency7": "XRP",
    "cryptoCurrency8": "BUSD",
    "cryptoCurrency9": "SOL",
    "cryptoCurrency10": "DOGE"
}


mongodb = {
    "mongodb_url": "mongodb+srv://anlequy:"+urllib.parse.quote("hsgsMCB@03")+"@cluster0.ccdse.mongodb.net/?retryWrites=true&w=majority",
    "myDataBase": "CoinMarketCap",
    "myCollection": "CryptoCurrencyData"
}
