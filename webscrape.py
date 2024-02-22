# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = "https://jnj.com/"

# Send the request and get the response
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all elements with the desired class
elements = soup.find_all("div")

# Extract data from each element
for element in elements:
    data = element.get_text()
    # Process the data as needed
    print(data)