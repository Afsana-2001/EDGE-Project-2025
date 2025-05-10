import requests
from bs4 import BeautifulSoup

# Function to scrape text from <p> tags on a webpage
def scrape_paragraphs(url):
    try:
        # Send a GET request to the webpage
        response = requests