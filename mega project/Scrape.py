import requests
from lxml import html
import csv
import time

# Input and output CSV file paths
input_csv ='/home/priyanshu/Documents/ASSIGNMENT/mega project/NameLink.csv'

output_csv = 'Scraped_dataA.csv'

# Function to scrape data from a given URL
def scrape_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # Define common XPath queries
    xpaths = {
        "movie_name": '/html/body/section/div/section/h1/span/text()',
        "screenshot_links": '/html/body/section/div/section/main/div/h3/a/img/@src',
        "download_links": (
            '/html/body/section/div/section/main/div/div[4]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/h3/a/@href | '
            '/html/body/section/div/section/main/div/div[4]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/h4/a/@href | '
            '/html/body/section/div/section/main/div/div[4]/h3/a/@href'
        ),
        "ratings": '/html/body/section/div/section/main/div/div[3]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/span/a/text()',
        "trailer_link": '/html/body/section/div/section/main/div/div[5]/iframe/@src',
        "categories": '/html/body/section/div/section/main/div/div[3]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/span/text()'
    }

    try:
        # Send a GET request to the URL with a timeout and headers
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful

        # Parse the content using lxml
        tree = html.fromstring(response.content)

        # Extract data using XPath
        movie_name = tree.xpath(xpaths["movie_name"])
        movie_name = movie_name[0] if movie_name else "N/A"

        screenshot_links = tree.xpath(xpaths["screenshot_links"])
        download_links = tree.xpath(xpaths["download_links"])

        ratings = tree.xpath(xpaths["ratings"])
        ratings = ratings[0] if ratings else "N/A"

        trailer_link = tree.xpath(xpaths["trailer_link"])
        trailer_link = trailer_link[0] if trailer_link else "N/A"

        categories = tree.xpath(xpaths["categories"])
        categories = categories[0] if categories else "N/A"

        # Return the scraped data as a dictionary
        return {
            "Movie Name": movie_name,
            "Screenshot Links": screenshot_links,
            "Source Link": url,
            "Download Links": download_links,
            "Ratings": ratings,
            "Trailer Link": trailer_link,
            "Categories": categories
        }

    except requests.exceptions.Timeout:
        print(f"Timeout error for URL {url}")
        return None
    except requests.exceptions.TooManyRedirects:
        print(f"Too many redirects for URL {url}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error for URL {url}: {e}")
        return None
    except requests.RequestException as e:
        print(f"Request error for URL {url}: {e}")
        return None
    except Exception as e:
        print(f"An error occurred for URL {url}: {e}")
        return None

# Function to read URLs from a CSV file with encoding fallback
def read_urls_from_csv(file_path):
    urls = []
    try:
        # Try reading with UTF-8 encoding first
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            urls = [row['Link'] for row in csv_reader]
    except UnicodeDecodeError:
        print(f"UTF-8 decoding failed for {file_path}. Trying ISO-8859-1 encoding.")
        # If a UnicodeDecodeError occurs, try with 'ISO-8859-1' encoding
        with open(file_path, mode='r', newline='', encoding='ISO-8859-1') as file:
            csv_reader = csv.DictReader(file)
            urls = [row['Link'] for row in csv_reader]
    except FileNotFoundError as e:
        print(f"File not found: {file_path}. Exception: {e}")
    return urls

# Function to write a single row of scraped data to the CSV file
def append_data_to_csv(file_path, data):
    # Define the CSV column headers
    headers = [
        "Movie Name",
        "Screenshot Links",
        "Source Link",
        "Download Links",
        "Ratings",
        "Trailer Link",
        "Categories"
    ]

    try:
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)

            # Check if the file is empty to write the header
            if file.tell() == 0:
                writer.writeheader()  # Write the header only once at the beginning

            writer.writerow(data)  # Write the row of data
    except IOError as e:
        print(f"Error writing to CSV file {file_path}: {e}")

# Main script execution
if __name__ == "__main__":
    # Read URLs from input CSV file
    urls = read_urls_from_csv(input_csv)

    if not urls:
        print("No URLs to scrape. Exiting.")
        exit()

    # Scrape data for each URL and write directly to CSV
    for url in urls:
        print(f"Scraping data for URL: {url}")
        retries = 3
        while retries > 0:
            scraped_data = scrape_data(url)
            if scraped_data:
                append_data_to_csv(output_csv, scraped_data)
                break  # Exit the retry loop if successful
            else:
                retries -= 1
                print(f"Retrying... ({3 - retries} attempts left)")
                time.sleep(5)  # Wait for a few seconds before retrying
        else:
            print(f"Failed to scrape data for URL: {url} after multiple attempts.")
