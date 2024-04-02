from bs4 import BeautifulSoup
import requests

def fetch_html(url):
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        return response.text
    else:
        return None

url = 'https://www.archives.gov/founding-docs/constitution-transcript'

html = fetch_html(url)

if html is not None:
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find the main part of the document within <div> with class 'legacy-content'
    main_part = soup.find('div', {'class': 'legacy-content'})

    # Extract and print the text from the main part
    if main_part is not None:
        main_text = main_part.get_text(strip=True)
        print(main_text)
    else:
        print('Failed to find main part.')
else:
    print('Failed to retrieve data.')
