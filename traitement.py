from requests_html import HTMLSession
from jour import Jour
from cour import Cours
import os
import time
from calendermaker import CalenderMaker
from ics import Calendar

from icalendar import Calendar, Event, vCalAddress, vText
import pytz
from datetime import datetime
import os
from pathlib import Path

calender = CalenderMaker()
url="https://intranet.polytech.universite-paris-saclay.fr/planning.html#"
url_app5_info="https://ade-planning.polytech.universite-paris-saclay.fr/direct/?data=5e3670a1af648401000482f65ebb1c4e51e7ab85056895b4cf55c89501c3748af5fe262b0b0938f81c1a3c30b54b9c65a1fff1df12d753d0f40f34e833a103db3fa636948ec0c7765b03a789de2f58aad102b01eed60a8b514847b385457efed"
url_peip1='https://ade-planning.polytech.universite-paris-saclay.fr/direct/?data=5e3670a1af648401000482f65ebb1c4e51e7ab85056895b4cf55c89501c3748af5fe262b0b0938f87a9882e74a3f76e0b760d181e6772c6df15f60700e60a742b2ed5e3c27118796ba1d70a4827aadb7ef015f9604cfa310b7b0dae73ff76118'







def get_data_from_url_app5_info(url,day,week):

    dataSession=[]
    script="""
    setTimeout(function(){
        document.getElementsByClassName('x-btn-text')["""+week+"""].click();
    }, 1000);
    setTimeout(function(){
        document.getElementsByClassName('x-btn-text')["""+day+"""].click();
    }, 1500);   
    """

    
    session=HTMLSession()
    response = session.get(url)
    response.html.render(10,script,sleep=2,reload=True,keep_page=True)
     
    dateJour=response.html.find('#4')[0].text.split(' ')
    day=dateJour[1].split('/')

    dateJourIcalender=day[2]+"-"+day[1]+"-"+day[0]
    
    EmploieDuTemps=[]

    for i in range(0,100):
        string="#inner"+str(i)
        dataSession.append(response.html.find(string) ) #recuperer les informations d'un jour 


        # on traite les informations d'un jour
        

        InfoDeJour=str(dataSession[i]).split("aria-label")
        if len(InfoDeJour)>1:
            cours=InfoDeJour[1]
            cours = cours.replace("=' ", "")
            cours = cours.replace("=\" ", "")
            cours = cours.replace("'>]", "")
            cours = cours.replace("\">]", "")
            cours=cours.split("null")
           
            
            

            if(len(cours)>1):
                begin=cours[len(cours)-2].split("-")[0].split("h")[0]+":"+cours[len(cours)-2].split("-")[0].split("h")[1]+":00"
                begin=begin.replace(" ","")
                end=cours[len(cours)-2].split("-")[1].split("h")[0]+":"+cours[len(cours)-2].split("-")[1].split("h")[1]+":00"
                end=end.replace(" ","")
               

                c=Cours(cours[0],begin,end,cours[2])
                EmploieDuTemps.append(c)

    j=Jour(dateJour[0],dateJourIcalender,EmploieDuTemps)
    calender.addEvent2(j)
    calender.save("calender1.ics")

    # print (j)
    response.session.close() 

      
 

#print(video)

def get_data_from_url_week():
    for j in range(7,58):
        for i in range(0,6):
            get_data_from_url_app5_info(url_app5_info,str(i),str(j))


get_data_from_url_week()