import requests
import pandas as pd
import time

df = pd.DataFrame(columns=["timestamp", "latitude", "longitude"])

url = "http://api.open-notify.org/iss-now.json"

for i in range(100):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
       
        timestamp = data["timestamp"]
        latitude = data["iss_position"]["latitude"]
        longitude = data["iss_position"]["longitude"]
        
        df = df.append({
            "timestamp": timestamp,
            "latitude": latitude,
            "longitude": longitude
        }, ignore_index=True)
        
        print(f"Record {i+1} collected")
        time.sleep(1)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


df.to_csv("iss_location_data.csv", index=False)

print("Data collection complete. Data saved to 'iss_location_data.csv'.")
 