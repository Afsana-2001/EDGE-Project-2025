import requests
from bs4 import BeautifulSoup


url = "https://example.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all('p')

    for i, paragraph in enumerate(paragraphs, 1):
        print(f"Paragraph {i}: {paragraph.get_text(strip=True)}")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
