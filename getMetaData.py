import requests
import getCoinsList
import config


def getMetaData():
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config.API_KEY["api-key"]
    }

    coinslist = getCoinsList.getCoinsList()
    value = ','.join([str(id) for id in coinslist])
    parameters = {
        "id": value,
        "aux": "urls,logo,description,notice"
    }

    response = requests.get(config.url["metadata_v2_url"], params=parameters, headers=headers).json()
    if response['status']['error_code'] != 0:
        print(response['status']['error_code'])
        return None

    output = {}
    for id in coinslist:
        if str(id) in response['data']:
            output[response['data'][str(id)]['name']] = response['data'][str(id)]

    return output
