from EnCasDeSoif import settings
import requests
import datetime
import json
import os
from dotenv import load_dotenv


def updateTokenVar(token, time):
    os.environ['LAST_API_GENERATE_TIME'] = time.strftime("%Y-%m-%d %H:%M:%S")
    os.environ['LAST_TOKEN'] = token


def generateNewToken():
    privateToken = settings.MAPBOX_PRIVATE_KEY
    login = settings.MAPBOX_LOGIN
    headers = {'content-type': 'application/json'}
    now = datetime.datetime.now()
    delayedNow = now + datetime.timedelta(minutes=30)
    formatedDelayed = delayedNow.strftime("%Y-%m-%d") + "T" + delayedNow.strftime("%H:%M:%S")
    payload = {"expires": formatedDelayed,
               "scopes": ["styles:tiles", "styles:read", "fonts:read", "datasets:read", "vision:read"]}
    url = 'https://api.mapbox.com/tokens/v2/' + login + '?access_token=' + privateToken
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    parsedResponse = r.json()
    token = parsedResponse['token']
    updateTokenVar(token, now)
    return token


def getTemporaryToken():
    # read the last date import
    lastImportTime = os.getenv('LAST_API_GENERATE_TIME')
    lastToken = os.getenv('LAST_TOKEN')
    now = datetime.datetime.now()
    if(lastImportTime == '' or lastToken == ''):
        return generateNewToken()
    else:
        lastImportTime = datetime.datetime.strptime(lastImportTime, "%Y-%m-%d %H:%M:%S")
        if((lastImportTime + datetime.timedelta(minutes=30)) < now):
            # Generate a new token
            return generateNewToken()
        else:
            return os.getenv('LAST_TOKEN')
