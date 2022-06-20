from requests import Request, Session
import json
import config


def getCoinsList():
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config.API_KEY["api-key"]
    }

    session = Session()
    session.headers.update(headers)

    parameters1 = {
        'listing_status': 'active',
        'start': 1,
        'limit': 5000,
        'sort': 'cmc_rank'
    }

    parameters2 = {
        'listing_status': 'active',
        'start': 5001,
        'limit': 5000,
        'sort': 'cmc_rank',
    }

    parameters3 = {
        'listing_status': 'active',
        'start': 10001,
        'limit': 5000,
        'sort': 'cmc_rank'
    }

    response1 = session.get(config.url["cmc_id_map_url"], params=parameters1)
    info1 = json.loads(response1.text)

    response2 = session.get(config.url["cmc_id_map_url"], params=parameters2)
    info2 = json.loads(response2.text)

    response3 = session.get(config.url["cmc_id_map_url"], params=parameters3)
    info3 = json.loads(response3.text)

    try:
        coinsList = []
        for i in range(5000):
            coinsList.append(info1['data'][i]['id'])

        for i in range(5000):
            coinsList.append(info2['data'][i]['id'])

        for i in range(5000):
            coinsList.append(info3['data'][i]['id'])
    except IndexError:
        print("IndexError occurred")

    return coinsList


