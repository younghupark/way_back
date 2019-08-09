import requests
from bs4 import BeautifulSoup

import re
import pandas as pd


from datetime import timedelta, datetime

start_date = datetime(2019, 1, 18,0)
end_date = datetime(2019, 1, 19,2)
delta = timedelta(hours=1)
prevstamp = "10"
while start_date <= end_date:
    URL = "http://archive.org/wayback/available?url=nytimes.com/subscription&timestamp=%s" % start_date.strftime("%Y%m%d%H")
    print(URL)
    r = requests.get(url = URL)
    data=r.json()
    timestamp = data['archived_snapshots']['closest']['timestamp']
    status = data['archived_snapshots']['closest']['status']

    if (prevstamp != timestamp):
        main_url = data['archived_snapshots']['closest']['url']
        result = requests.get(main_url)

        soup = BeautifulSoup(result.text, 'html.parser')
        wrappers = soup.select(".productGBBRibbonTab--activeTab")
        string_divs = set()
        count = 1;
        for wrapper in wrappers:
            stuff = re.findall("<p>(.*)<\/p>", str(wrapper))
            if stuff:
                print(count)
                print(stuff)
            count+=1


            #strings = wrapper.find_all(string=re.compile("\$[0-9]"))
            #labels = wrapper.find_all("p")
            #for string in strings:
            #    div = str(string.find_parent("div"))
            #    stuff = re.findall("<p>(.*)<\/p>", div)
            #    if stuff:
            #        print(stuff)
                #string_divs.add(string.find_parent("div").get_text())
            #print(timestamp)
            #print(string_divs)
            #print(set(labels))
    prevstamp = timestamp
    start_date += delta
