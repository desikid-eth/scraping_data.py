import requests
from bs4 import BeautifulSoup

# Define the URL to be scraped
url = "https://www.martindale.com/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the response was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all email addresses in the page
    emails = [a["href"][7:] for a in soup.select("a[href^='mailto:']")]

    # Print the email addresses
    for email in emails:
        print(email)
else:
    # Print an error message if the response was not successful
    print("Failed to retrieve data from the website. Response code:", response.status_code)
