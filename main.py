from requests import Request, Session
import json
import pprint
import config
import getCoinsList

def getInfo():
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config.API_KEY["api-key"]
    }

    session = Session()
    session.headers.update(headers)

    coinsList = getCoinsList.getCoinsList()
    value = ','.join([coin for coin in coinsList])
    if value.isupper():
        parameters = {
            'symbol': value
        }
    else:
        value.lower()
        parameters = {
            'slug': value
        }

    response1 = session.get(config.url["metadata_v2_url"], params=parameters)
    info1 = json.loads(response1.text)

    response2 = session.get(config.url["quotes_latest_v1_url"], params=parameters)
    info2 = json.loads(response2.text)


    output = {}
    for coin in info1['data']:
        coin_categories = []
        for coin_category in info1['data'][coin][0]:
            if coin_category != 'tag-names' \
                    and coin_category != 'tag-groups' \
                    and coin_category != 'tags' \
                    and coin_category != 'name' \
                    and coin_category != 'platform' \
                    and coin_category != 'slug' \
                    and coin_category != 'symbol' \
                    and coin_category != 'id':
                coin_categories.append({f"{coin_category}": info1['data'][coin][0][coin_category]})

        coin_categories.append(info2['data'][coin])

        output.update({f"{coin}": coin_categories})

    return output


