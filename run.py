import requests
from bs4 import BeautifulSoup

URL = "http://archive.org/wayback/available?url=nytimes.com/subscription&timestamp=20060101I"

r = requests.get(url = URL)


data=r.json()


main_url = data['archived_snapshots']['closest']['url']

result = requests.get(main_url)

soup = BeautifulSoup(result.text, 'html.parser')

print(soup.prettify()[:1000])
