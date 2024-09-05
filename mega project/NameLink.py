import requests
from bs4 import BeautifulSoup
import csv
import time

# Function to fetch and parse a single page
def fetch_page(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

# Base URL with a placeholder for page number
base_url = "https://hdhub4u.contact/page/{}/"

# Open a CSV file to write the output
with open('movies.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Title', 'Link'])  # Write headers to the CSV file

    # Loop through pages from 1 to 863
    for page_number in range(1, 864):
        # Construct the URL for the current page
        url = base_url.format(page_number)
        print(f"Fetching page {page_number}...")

        # Fetch and parse the page
        soup = fetch_page(url)

        # Find all relevant <li> elements with the specified class
        li_elements = soup.find_all('li', class_='thumb col-md-2 col-sm-4 col-xs-6')

        # Extract and write data for each <li> element
        for li in li_elements:
            title = li.find('p').get_text(strip=True)
            link = li.find('a')['href']
            csvwriter.writerow([title, link])

        # Sleep to avoid overwhelming the server
        time.sleep(1)  # Adjust the sleep time as needed

print("Data successfully written to movies.csv")
