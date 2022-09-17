from cour import Cours

class Jour:
    def __init__(self, jour,date,cours):
        self.Nomjour = jour
        self.date = date
        self.cours = cours
    
    def __str__(self):
        return "Jour: "+self.Nomjour+"\n Date: "+self.date+"\n Cours: "+self.cours.__str__()+"\n"
  
    def __str__(self):
        s="Jour: "+self.Nomjour+"\n Date: "+self.date
        for i in range(len(self.cours)):
            s+= "\n Cours: "+self.cours[i].__str__()+"\n"
        return s