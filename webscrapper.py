# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = "https://www.zoox.com/careers?locations=Boston-or-Foster-City#open-positions"

# Send the request and get the response
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all elements with a specific tag (e.g., <div>)
elements = soup.find_all("div")

# Extract data from each element
for element in elements:
    data = element.get_text()
    # Process the data as needed
    print(data)
    
