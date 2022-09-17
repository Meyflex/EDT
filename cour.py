class Cours:
    def __init__(self, nom,begin,end,data):
        self.nom = nom
        self.begin = begin
        self.end = end
        self.data = data

    def __str__(self):
        return "Nom: "+self.nom+"\n Heure: "+self.begin +"-"+self.end+"\n"


