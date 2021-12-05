import requests
import json
import pandas as pd

api_key = 'PUT_YOUR_API_KEY' # your windsor.ai api-key from https://onboard.windsor.ai

# URL listing the fields you want to pull
api_url = 'https://connectors.windsor.ai/facebook?date_preset=last_7d&fields=date,campaign,clicks,spend&api_key=' + api_key


res = requests.get(api_url).json()
df = pd.DataFrame.from_dict(res['data'])
print(df)

