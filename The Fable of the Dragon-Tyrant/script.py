import requests
from bs4 import BeautifulSoup

url = 'https://nickbostrom.com/fable/dragon.html'
response = requests.get(url)

# Ensure the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Save the parsed content to an HTML file
    with open('webpage.html', 'w', encoding='utf-8') as file:
        file.write(str(soup.prettify()))
