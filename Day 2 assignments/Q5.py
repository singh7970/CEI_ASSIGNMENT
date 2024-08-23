import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)


if response.status_code == 200:
 
    data = response.json()
    
    # Extract latitude, longitude, and timestamp
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    timestamp = data["timestamp"]

    # Print the extracted data
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print(f"Timestamp: {timestamp}")
else:
    
    
    print(f"Failed to retrieve data. Status code: {response.status_code}")
