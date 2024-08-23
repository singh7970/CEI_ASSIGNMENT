import requests
import json  
url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)


if response.status_code == 200:
  
    data = response.json()

    print(json.dumps(data, indent=4))
else:
   
    print(f"Failed to retrieve data. Status code: {response.status_code}")

