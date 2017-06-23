import time

class car:
    #fuel = 6 # max
    road = 1 # max = 12

    def __init__(self):
        self.car = []
        self.fuel = 6
        print ("Witaj! Własnie stworzyłeś swój samochód \nPojemność twojego baku wynosi " + str(self.fuel) + "\n")

    def run (self, km):
        if self.fuel < km:
            self.check_fuel()
            print ("Masz za mało paliwa w baku. \nZatankuj samochód!\nDo pełnego baku brakuje ci " + str(6-self.fuel) + " jednostek paliwa")
        elif km > (12 - self.road):
            print ("Podałeś zbyt duży dystans! Do końca trasy brakuje ci " + str(12 - self.road) + " jednostek drogi")
        elif km == 0:
            print ("Podałeś zerową liczbę jednostek drogi")
        else:
            print (self.road)
            for i in range(km):
                self.road += 1
                print (self.road)
                self.fuel -= 1
                if self.fuel <= 2: #swiecaca sie kontrolka
                    print ("Ostrzeżenie!\nPozostało ci tylko " + str(self.fuel) + " jednostek paliwa")
            #self.road = self.road + km
            #self.fuel = self.fuel - km
            #self.check_road()

    def tankuj (self, fuel):
        if fuel > (6 - self.fuel):
            print ("Przetankujesz samochód! Do pełnego baku brakuje ci " + str(6 - self.fuel) + " jednostek paliwa")
        elif fuel == 0:
            print ("Zatankowałeś 0 jednostek paliwa")
        else:
            self.fuel = self.fuel + fuel
            print ("Zatankowałeś: " + str(fuel) + ", Twój bak: " + str(self.fuel))

    def check_road (self):
        if self.road <= 3:
            print (" Jesteś w Warszawie - pole nr " + str(self.road))
        elif self.road <= 6:
            print ("Jesteś w łodzi - pole nr " + str(self.road))
        elif self.road <= 9:
            print ("Jesteś w Krakowie - pole nr " + str(self.road))
        elif self.road <= 12:
            print ("Jesteś w Zakopanem - pole nr " + str(self.road))
    def check_fuel(self):
        print ("Obecny stan baku: " + str(self.fuel) + " jednostek paliwa")


#WYKONANIE PROGRAMU

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
