# json

import urllib.parse

API_KEY = {
    "api-key": "a577a94f-33e4-46a1-8e7a-cad952b7e191"  # Lê Quý An
    # "api-key": "e029fb83-aa9d-47a6-ae4c-b66d2d117f41"  # Xa Bảo Sơn
    # "api-key": "3f5a70b1-52d2-4f67-8a1e-22d935f25c05" # Trần Nguyễn Nhựt Trường
}

url = {
    "metadata_v2_url": "https://pro-api.coinmarketcap.com/v2/cryptocurrency/info",
    # Coinmarketcap API url to retrieve metadata
    "quotes_latest_v2_url": "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest",
    # Coinmarketcap API url to retrieve information about all coin categories available on CoinMarketCap
    "cmc_id_map_url": "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"
    # Coinmarketcap API url to retrieve information about a mapping of all cryptocurrencies to unique CoinMarketCap ids
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
    "mongodb_url": "mongodb+srv://anlequy:" + urllib.parse.quote(
        "hsgsMCB@03") + "@cluster0.ccdse.mongodb.net/?retryWrites=true&w=majority",
    # "mongo_db_url": "mongodb+srv://MCBlu2k3:MCBlu2k3pro@cluster0.lvv6j.mongodb.net/?retryWrites=true&w=majority",
    "myDataBase": "CoinMarketCap",
    "myCollection": "CryptoCurrencyData"
}
