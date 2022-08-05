import requests
import config


def getCoinsList():
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config.API_KEY["api-key"]
    }

    parameters = {
        'listing_status': 'active',
        'start': 1,
        'limit': 100,
        'sort': 'cmc_rank'
    }

    info = requests.get(config.url["cmc_id_map_url"], params=parameters, headers=headers).json()

    try:
        coinsList = []
        for i in range(100):
            coinsList.append(info['data'][i]['id'])
    except IndexError:
        print("IndexError occurred")

    return coinsList





