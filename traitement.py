import asyncio
from requests_html import HTMLSession
from requests_html import AsyncHTMLSession

from jour import Jour
from cour import Cours
import os
from calendermaker import CalenderMaker
from ics import Calendar

from datetime import datetime
import os
from pathlib import Path


url_og="https://intranet.polytech.universite-paris-saclay.fr/planning.html#"
url_peip1='https://ade-planning.polytech.universite-paris-saclay.fr/direct/?data=5e3670a1af648401000482f65ebb1c4e51e7ab85056895b4cf55c89501c3748af5fe262b0b0938f87a9882e74a3f76e0b760d181e6772c6df15f60700e60a742b2ed5e3c27118796ba1d70a4827aadb7ef015f9604cfa310b7b0dae73ff76118'
url_peip2='https://ade-planning.polytech.universite-paris-saclay.fr/direct/?data=5e3670a1af648401000482f65ebb1c4e51e7ab85056895b4cf55c89501c3748af5fe262b0b0938f8e7485d9bee2c84dbb760d181e6772c6df15f60700e60a742b2ed5e3c27118796ba1d70a4827aadb7ef015f9604cfa310b7b0dae73ff76118'
url_peipc='https://ade-planning.polytech.universite-paris-saclay.fr/direct/?data=5e3670a1af648401000482f65ebb1c4e51e7ab85056895b4cf55c89501c3748af5fe262b0b0938f87b035ebf272a6adfb760d181e6772c6df15f60700e60a742b2ed5e3c27118796ba1d70a4827aadb7ef015f9604cfa310b7b0dae73ff76118'
url_ET3="https://ade-planning.polytech.universite-paris-saclay.fr/direct/?data=5e3670a1af648401000482f65ebb1c4e51e7ab85056895b4cf55c89501c3748af5fe262b0b0938f8a296a2ffb0037d5bb760d181e6772c6df15f60700e60a742b2ed5e3c27118796ba1d70a4827aadb7ef015f9604cfa310b7b0dae73ff76118"
url_ET4="https://ade-planning.polytech.universite-paris-saclay.fr/direct/?data=5e3670a1af648401000482f65ebb1c4e51e7ab85056895b4cf55c89501c3748af5fe262b0b0938f8f04f4a6b90e17f71b760d181e6772c6df15f60700e60a742b2ed5e3c27118796ba1d70a4827aadb7ef015f9604cfa310b7b0dae73ff76118"
url_ET5="https://ade-planning.polytech.universite-paris-saclay.fr/direct/?data=5e3670a1af648401000482f65ebb1c4e51e7ab85056895b4cf55c89501c3748af5fe262b0b0938f8c8df41a0a7ef48f7b760d181e6772c6df15f60700e60a742b2ed5e3c27118796ba1d70a4827aadb7ef015f9604cfa310b7b0dae73ff76118"
url_app3="https://ade-planning.polytech.universite-paris-saclay.fr/direct/?data=5e3670a1af648401000482f65ebb1c4e51e7ab85056895b4cf55c89501c3748af5fe262b0b0938f8b0da01d9866c6b06b760d181e6772c6df15f60700e60a742b2ed5e3c27118796ba1d70a4827aadb7ef015f9604cfa310b7b0dae73ff76118"
url_app4="https://ade-planning.polytech.universite-paris-saclay.fr/direct/?data=5e3670a1af648401000482f65ebb1c4e51e7ab85056895b4cf55c89501c3748af5fe262b0b0938f824f1ecce698039f3b760d181e6772c6df15f60700e60a742b2ed5e3c27118796ba1d70a4827aadb7ef015f9604cfa310b7b0dae73ff76118"
url_app5="https://ade-planning.polytech.universite-paris-saclay.fr/direct/?data=5e3670a1af648401000482f65ebb1c4e51e7ab85056895b4cf55c89501c3748af5fe262b0b0938f83efacf3364b3523fb760d181e6772c6df15f60700e60a742b2ed5e3c27118796ba1d70a4827aadb7ef015f9604cfa310b7b0dae73ff76118"



async def get_data_from_url(url,day,week,Promo,calender):

    dataSession=[]
    script="""
    setTimeout(function(){
        document.getElementsByClassName('x-btn-text')["""+week+"""].click();
    }, 1000);
    setTimeout(function(){
        document.getElementsByClassName('x-btn-text')["""+day+"""].click();
    }, 1500);   
    """

    
    session=AsyncHTMLSession()
    response =await session.get(url)
    await response.html.arender(10,script,sleep=2,reload=True,keep_page=True)
     
    if response.html.find('#4')!=[]:
        
        dateJour=response.html.find('#4')[0].text.split(' ')
        day=dateJour[1].split('/')
        dateJourIcalender=day[2]+"-"+day[1]+"-"+day[0]
    
    EmploieDuTemps=[]
    i=0
    string="#inner"+str(i)
    while response.html.find(string) !=[]:
        
        dataSession.append(response.html.find(string) ) #recuperer les informations d'un jour 
        

        # on traite les informations d'un jour
        

        InfoDeJour=str(dataSession[i]).split("aria-label")
        if len(InfoDeJour)>1:
            cours=InfoDeJour[1]
            cours = cours.replace("=' ", "")
            cours = cours.replace("=\" ", "")
            cours = cours.replace("'>]", "")
            cours = cours.replace("\">]", "")
            cours = cours.replace("\"", "")
            cours = cours.replace("=''", "")
            cours=cours.split("null")
            

           
            
            

            if(len(cours)>1):
                begin=cours[len(cours)-2].split("-")[0].split("h")[0]+":"+cours[len(cours)-2].split("-")[0].split("h")[1]+":00"
                begin=begin.replace(" ","")

                end=cours[len(cours)-2].split("-")[1].split("h")[0]+":"+cours[len(cours)-2].split("-")[1].split("h")[1]+":00"
                end=end.replace(" ","")

                #on recupere toutes les autres informations du cours
                info=""
                for acc in range (1,len(cours)-2):
                    
                    info=info+"\n"+cours[acc]
                if info.__contains__("ET4 MATE") or info.__contains__("ET4 PHOT") or info.__contains__("ET4 ELEC"):
                    print("ET4")
                else:
                    c=Cours(cours[0],begin,end,info)
                    EmploieDuTemps.append(c)
                
        i=i+1
        string="#inner"+str(i)
    if len(EmploieDuTemps)>0:
        j=Jour(dateJour[0],dateJourIcalender,EmploieDuTemps)
    else:
        j=Jour(dateJour[0],dateJourIcalender,[])
    print(j)
    calender.addEvent2(j)
    await response.session.close() 

      
 



async def get_data_from_url_week():
    calenderPEIP1 = CalenderMaker()
    calenderPEIP2 = CalenderMaker()
    calenderPEIPC = CalenderMaker()
    calenderET3 = CalenderMaker()
    calenderET4 = CalenderMaker()
    calenderET5 = CalenderMaker()
    calenderAPP3 = CalenderMaker()
    calenderAPP4 = CalenderMaker()
    calenderAPP5 = CalenderMaker()

    for j in range(7,58):
        for i in range(0,6):
            # get_data_from_url(url_peip1,str(i),str(j),"Peip1",calenderPEIP1)
            # get_data_from_url(url_peip2,str(i),str(j),"Peip2",calenderPEIP2)
            # get_data_from_url(url_peipc,str(i),str(j),"Peipc",calenderPEIPC)
            # get_data_from_url(url_ET3,str(i),str(j),"Et3",calenderET3)
            await get_data_from_url(url_ET4,str(i),str(j),"Et4",calenderET4)
            # get_data_from_url(url_ET5,str(i),str(j),"Et5",calenderET5)
            # get_data_from_url(url_app3,str(i),str(j),"App3",calenderAPP3)
            # get_data_from_url(url_app4,str(i),str(j),"App4",calenderAPP4)
            # get_data_from_url(url_app5,str(i),str(j),"App5",calenderAPP5)

    # calenderPEIP1.save("Peip1.ics")
    # calenderPEIP2.save("Peip2.ics")
    # calenderPEIPC.save("Peipc.ics")
    # calenderET3.save("Et3.ics")
    calenderET4.save("Et4.ics")
    # calenderET5.save("Et5.ics")
    # calenderAPP3.save("App3.ics")
    # calenderAPP4.save("App4.ics")
    # calenderAPP5.save("App5.ics")

    

asyncio.run(get_data_from_url_week())
print("done")