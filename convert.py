import requests
import json


def convert(text):

    url = "https://gsamuel-morse-code-v1.p.rapidapi.com/"

    # text = 'How you doing?'

    payload = "{\n    \"text\": \""+text+"\"\n}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': "0c9fe16e68mshae94b6721541cb9p17183bjsn808deabde345",
        'x-rapidapi-host': "gsamuel-morse-code-v1.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    jsonToPython = json.loads(response.text)

    return (jsonToPython['code'])
