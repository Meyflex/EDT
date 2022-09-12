from ssl import SSLSession
from requests_html import HTMLSession

from bs4 import BeautifulSoup
from icalendar import Calendar, Event, vCalAddress, vText
import pytz
from datetime import datetime
import os
from pathlib import Path
session=HTMLSession()

url="https://intranet.polytech.universite-paris-saclay.fr/planning.html#"
url_app5_info="https://ade-planning.polytech.universite-paris-saclay.fr/direct/?data=5e3670a1af648401000482f65ebb1c4e51e7ab85056895b4cf55c89501c3748af5fe262b0b0938f81c1a3c30b54b9c65a1fff1df12d753d0f40f34e833a103db3fa636948ec0c7765b03a789de2f58aad102b01eed60a8b514847b385457efed"
url_peip1='https://ade-planning.polytech.universite-paris-saclay.fr/direct/?data=5e3670a1af648401000482f65ebb1c4e51e7ab85056895b4cf55c89501c3748af5fe262b0b0938f87a9882e74a3f76e0b760d181e6772c6df15f60700e60a742b2ed5e3c27118796ba1d70a4827aadb7ef015f9604cfa310b7b0dae73ff76118'


response = session.get(url_app5_info)
response.html.render(sleep=2 ,keep_page=True)

i=0
dataSession=[]

for i in range(0,100):

    string="#inner"+str(i)
    dataSession.append(response.html.find(string))
    Data=str(dataSession[i]).split("'")[len(str(dataSession[i]).split("'"))-2]
    Data=Data.split("null")
    if len(Data)>1:
        print(Data)




    

#print(video)

