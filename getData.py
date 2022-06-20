import pprint
from requests import Request, Session
import json
import config
import getCoinsList


def getData():
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config.API_KEY["api-key"]
    }

    session = Session()
    session.headers.update(headers)

    coinsList = getCoinsList.getCoinsList()
    output = {}
    for i in range(len(coinsList)):
        parameters = {
            'id': str(coinsList[i])
        }

        response1 = session.get(config.url["metadata_v2_url"], params=parameters)
        info1 = json.loads(response1.text)

        response2 = session.get(config.url["quotes_latest_v2_url"], params=parameters)
        info2 = json.loads(response2.text)

        coin_categories = []
        for coin_category in info1['data'][parameters['id']]:
            if coin_category != 'tag-names' \
                    and coin_category != 'tag-groups' \
                    and coin_category != 'tags' \
                    and coin_category != 'name' \
                    and coin_category != 'platform' \
                    and coin_category != 'slug' \
                    and coin_category != 'symbol' \
                    and coin_category != 'id':
                coin_categories.append({f"{coin_category}": info1['data'][parameters['id']][coin_category]})

        coin_categories.append(info2['data'][parameters['id']])

        output.update({info1['data'][parameters['id']]['name']: coin_categories})

    return output









