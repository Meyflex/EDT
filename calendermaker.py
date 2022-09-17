from ics import Calendar, Event
from datetime import datetime, timedelta
class CalenderMaker:
    def __init__(self):
        self.cal = Calendar()
        self.event = Event()
        self.cal.events.add(self.event)
        self.cal.events
        self.cal.events
    def addEvent(self, name, start, end, data):
        self.event = Event()
        self.event.name = name
        self.event.begin = start
        self.event.end = end

        self.event.description = data
        print(self.event)
        self.cal.events.add(self.event)

    def addEvent2(self,jour):
        for i in range(len(jour.cours)):
            debut=jour.date+" "+jour.cours[i].begin
            fin=jour.date+" "+jour.cours[i].end
            dt = datetime.strptime(debut, '%Y-%m-%d %H:%M:%S').isoformat()
            
            dt2 = datetime.strptime(fin, '%Y-%m-%d %H:%M:%S').isoformat()

            self.addEvent(jour.cours[i].nom,dt,dt2,jour.cours[i].data)
        
        
        

        

    def save(self, filename):
        with open(filename, 'w') as my_file:
            my_file.writelines(self.cal)
    def __str__(self):
        return self.cal.events
