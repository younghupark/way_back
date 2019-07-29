import requests
from bs4 import BeautifulSoup



from datetime import timedelta, date

start_date = date(2016, 1, 1)
end_date = date(2017, 1, 1)
delta = timedelta(days=1)
while start_date <= end_date:
    URL = "http://archive.org/wayback/available?url=nytimes.com/subscription&timestamp=%sI" % start_date.strftime("%Y%m%d")

    r = requests.get(url = URL)
    data=r.json()


    main_url = data['archived_snapshots']['closest']['url']

    result = requests.get(main_url)

    soup = BeautifulSoup(result.text, 'html.parser')

    print(soup.prettify()[:1000])
    start_date += delta
