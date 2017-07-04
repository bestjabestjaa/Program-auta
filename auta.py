import datetime
import linecache

class car:
    # max fuel = 6
    # max road = 12
    cena_paliwa = 0
    day = datetime.datetime.today().weekday()

    def __init__(self):
        self.car = []
        self.fuel = 6
        self.road = 1
        self.cost = 0

        print ("Witaj! Własnie stworzyłeś swój samochód \nPojemność twojego baku wynosi " + str(self.fuel) + "\n")
        print ("Twoja mapa: Warszawa: 1, 2, 3, łódź: 4, 5, 6, Kraków: 7, 8, 9, Zakopane: 10,11, 12")

    def run (self, km):
        if self.fuel < km:
            self.check_fuel()
            print ("Masz za mało paliwa w baku. \nZatankuj samochód!\nDo pełnego baku brakuje ci " + str(6-self.fuel) + " jednostek paliwa")
        elif km > (12 - self.road):
            print ("Podałeś zbyt duży dystans! Do końca trasy brakuje ci " + str(12 - self.road) + " jednostek drogi")
        elif km == 0:
            print ("Podałeś zerową liczbę jednostek drogi")
        else:
            print (self.road) #pole, z ktorego ruszamy
            for i in range(km):
                self.road += 1
                print (self.road)
                self.fuel -= 1
                if self.fuel <= 2: #swiecaca sie kontrolka
                    print ("Ostrzeżenie!\nPozostało ci tylko " + str(self.fuel) + " jednostek paliwa")

    def tankuj (self, fuel):
        if fuel > (6 - self.fuel):
            print ("Przetankujesz samochód! Do pełnego baku brakuje ci " + str(6 - self.fuel) + " jednostek paliwa")
        elif fuel == 0:
            print ("Zatankowałeś 0 jednostek paliwa")
        else:
            self.fuel = self.fuel + fuel
            print ("Zatankowałeś: " + str(fuel) + ", Twój bak: " + str(self.fuel))
            if self.day == 0:
                today = "Poniedziałek"
                cena_paliwa = 2.5
            elif self.day == 1:
                today = "Wtorek"
                cena_paliwa = 3.5
            elif self.day == 2:
                today = "Środa"
                cena_paliwa = 2.6
            elif self.day == 3:
                today = "Czwartek"
                cena_paliwa = 2
            elif self.day == 4:
                today = "Piątek"
                cena_paliwa = 1.5
            elif self.day == 5:
                today = "Sobota"
                cena_paliwa = 3
            elif self.day == 6:
                today = "Niedziela"
                cena_paliwa = 3.3

            print ("Dzisiaj jest %s, a paliwo kosztuje " % (today) + str(cena_paliwa))
            print ("Zapłaciłeś za paliwo " + str(fuel*cena_paliwa))
            self.cost += fuel * cena_paliwa

    def check_road (self):
        if self.road <= 3:
            wiersz = linecache.getline('miasta.txt', 1)
            print (" Jesteś w Warszawie - pole nr " + str(self.road) +"\n" +str(wiersz) )
        elif self.road <= 6:
            print ("Jesteś w łodzi - pole nr " + str(self.road))
        elif self.road <= 9:
            print ("Jesteś w Krakowie - pole nr " + str(self.road))
        elif self.road <= 12:
            print ("Jesteś w Zakopanem - pole nr " + str(self.road))
    def check_fuel(self):
        print ("Obecny stan baku: " + str(self.fuel) + " jednostek paliwa")
    def chech_cost(self):
        print ("Całkowity koszt za paliwo wynosi " +str (self.cost))


'''
Program bez interakcji

car1 = car()
print ("----CHECK------")
car1.check_fuel()
car1.check_road()
print ("---RUN 5-------")
car1.run(5)
car1.check_road()
print ("---RUN 5-------")
car1.run(5)
print ("---TANKUJ-------")
car1.tankuj(5)
print ("---RUN 5-------")
car1.run(5)
car1.check_road()
print ("---RUN 5-------")
car1.run(5)
print ("---TANKUJ-------")
car1.tankuj(5)
print ("---RUN 5-------")
car1.run(5)
print ("----CHECK------")
car1.chech_cost()
'''

#Interakcja

start = input ("Napisz 'start', by rozpocząć")
while start.lower() != 'start':
    start = input ("Napisz poprawnie słowo 'start', używając liter dowolnej wielkości")
else:
    print ("\n")
    car1 = car()

car1.check_road()


