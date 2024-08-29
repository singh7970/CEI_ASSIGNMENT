import pandas as pd
import requests
import json
from datetime import datetime, timedelta

# Function to get data for a specific date
def get_vegetable_data(date):
    url = f"https://vegetablemarketprice.com/api/dataapi/market/uttarpradesh/daywisedata?date={date}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.text)["data"]
    else:
        print(f"Failed to retrieve data for {date}")
        return []

# Initialize a list to store the data
data_list = []

# Define the date range
start_date = datetime(2024, 5, 1)
end_date = datetime(2024, 6, 30)

# Loop through each date in the specified range
current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%d")
    daily_data = get_vegetable_data(date_str)
    
    # Process each entry in the daily data
    for entry in daily_data:
        data_list.append({
            "Date": date_str,
            "State": "Uttar_Pradesh",
            "Vegetable Name": entry.get("vegetablename", "N/A"),
            "Wholesale Price": entry.get("price", "N/A"),
            "Retail Price": entry.get("retailprice", "N/A"),
            "Mall Price": entry.get("shopingmallprice", "N/A"),
            "Unit": entry.get("units", "N/A"),
            "Vegetable Image": entry.get("vegetableimage", "N/A")
        })
    
    current_date += timedelta(days=1)

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data_list)

# Save the DataFrame to a CSV file
df.to_csv("/content/UttarPradeshVegMarketData_May_June_2024.csv", index=False)

# Display the first few rows of the DataFrame
df.head()

print("Data scraping and saving completed.")