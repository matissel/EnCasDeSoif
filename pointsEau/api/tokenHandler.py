from EnCasDeSoif import settings
import requests
import datetime
import json
import os

def updateTokenVar(token, time):
    os.environ['LAST_API_GENERATE_TIME'] = time 
    os.environ['LAST_TOKEN'] = token

def generateNewToken():
    privateToken = settings.MAPBOX_PRIVATE_KEY
    headers = {'content-type': 'application/json'}
    now = datetime.datetime.now()
    delayedNow = now + datetime.timedelta(minutes=30)
    formatedDelayed = delayedNow.strftime("%Y-%m-%d") + "T" + delayedNow.strftime("%H:%M:%S") 
    payload = {"expires": formatedDelayed,
                "scopes": ["styles:tiles","styles:read","fonts:read","datasets:read","vision:read"]}
    url = 'https://api.mapbox.com/tokens/v2/matissou?access_token='+privateToken
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    parsedResponse = r.json()
    token = parsedResponse['json']

    updateTokenVar(token, now)

    return parsedResponse['token']


def getTemporaryToken():
    # read the last date import  
    lastImportTime = os.environ.get('LAST_API_GENERATE_TIME')
    now = datetime.datetime.now()
    if(lastImportTime==''):
        os.environ['LAST_API_GENERATE_TIME'] = now
        return generateNewToken()
    else:
        if( (lastImportTime + datetime.timedelta(minutes=30)) < now):
            # Generate a new token 
            return generateNewToken()
        else:
            # return last token used
            if(os.environ.get('LAST_TOKEN') == ''):
                return generateNewToken
            else:
                return os.environ.get('LAST_TOKEN')

