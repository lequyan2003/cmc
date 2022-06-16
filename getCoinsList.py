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

    parameters_1 = {
        'start': 1,
        'limit': 5000
    }

    parameters_2 = {
        'start': 5001,
        'limit': 5000
    }

    parameters_3 = {
        'start': 10001,
        'limit': 5000
    }

    response_1 = session.get(config.url["listings_latest_url"], params=parameters_1)
    info_1 = json.loads(response_1.text)

    response_2 = session.get(config.url["listings_latest_url"], params=parameters_2)
    info_2 = json.loads(response_2.text)

    response_3 = session.get(config.url["listings_latest_url"], params=parameters_3)
    info_3 = json.loads(response_3.text)


    try:
        coinsList = []
        for i in range(5000):
            if info_1['data'][i]['quote']['USD']['price'] > 0:
                coinsList.append(info_1['data'][i]['symbol'])

        for i in range(5000):
            if info_2['data'][i]['quote']['USD']['price'] > 0:
                coinsList.append(info_1['data'][i]['symbol'])

        for i in range(5000):
            if info_3['data'][i]['quote']['USD']['price'] > 0:
                coinsList.append(info_3['data'][i]['symbol'])
    except IndexError:
        print("IndexError occurred")

    return coinsList

