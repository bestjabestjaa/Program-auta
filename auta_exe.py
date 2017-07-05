from auta import car

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
start = input ("Napisz 'start', by rozpocząć")
while start.lower() != 'start':
    start = input ("Napisz poprawnie słowo 'start', używając liter dowolnej wielkości")
else:
    print ("\n")
    car1 = car()
    '''
