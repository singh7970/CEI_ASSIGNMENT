import json

# Sample JSON data
json_data = '''
{
    "explanation": "This is a sample explanation.",
    "author": "",
    "title": "Lucid, üç yeni elektrikli model",
    "url": "https://www.donanimhaber.com/lucid-uc-yeni-elektrikli-model-uzerinde-calistigini-onayladi--181017",
    "publishedAt": "2024-08-22T12:32:00Z"
}
'''

# Load the JSON data
data = json.loads(json_data)

# Extract the "explanation" and "title" fields
explanation = data.get("explanation", "No explanation available")
title = data.get("title", "No title available")

# Print the extracted fields
print("Explanation:", explanation)
print("Title:", title)
