"""
El funcionamiento de los radares de velocidad se basa en un
principio básico de la cinéticaque establece𝑣=𝑥𝑡, donde:
v:velocidad
x:posición –distancia
:tiempo
Dadas las dos distancias obtenidas del vehículo y el tiempo, calcular
si debe pagar una multa de acuerdo conla siguiente tabla:

En caso de tener multapor velocidad, se le practica un examen de
alcoholemia   al   conductor   que   acarrea   multas   adicionales de acuerdo conla siguiente norma:
acuerdo conla siguiente norma:
"""
# captures and stores position value as float
position = float(input("Posicion del vehiculo: "))
# captures and stores distance value as float
distance = float(input("Distancia: "))
# captures and stores time value as float
time = float(input("Tiempo transcurrido: "))

speed = (position-distance)/time # calculates speed's value
breathalyzer_test = False # aux variable for test. Default as boolean false
if speed >= 1 and speed <= 20: # checks if speed is between 1 and 20
    message = "Llamado de atención por baja velocidad." # stores action in variable message
elif speed > 20 and speed <= 60: # checks if speed is between 21 and 60
    message = "Normal"
elif speed > 60 and speed <= 80:# checks if speed is between 61 and 80
    message = "Llamado de atención por alta velocidad."
elif speed > 80 and speed <= 120: # checks if speed is between 81 and 120
    message = "Multa tipo 1"
    breathalyzer_test = True
else:
    # excecute by default if speed is greater than 120
    message = "Multa tipo II e inmovilización del vehículo."
    breathalyzer_test = True # changes aux variable test value

#checks if it is necessary to do test
if breathalyzer_test:
    # captures and stores test value as float
    test_result = float(input("Grados de alcohol: "))
    # control flow for test value and adds to message a string acording to test
    if test_result >= 20 and test_result <= 39:
        message += " y suspensión  de  la  licencia  de  conducción  entre  seis  (6)  y  doce (12) meses."
    elif test_result > 39 and test_result <= 99:
        message += " y suspensión  de  la  Licencia  de  Conducción  entre uno (1) y tres (3) años."
    elif test_result > 99 and test_result <= 149:
        message += " y uspensión de la Licencia de Conducción entre tres (3) y cinco (5) años, y la obligación de realizar curso de   sensibilización,   conocimientos   y   consecuencias   de   la alcoholemia   y   drogadicción   en   centros   de   rehabilitación debidamente  autorizados,  por  un  mínimo  de  cuarenta  (40) horas"
    else:
        message += " y uspensión entre cinco (5) y diez (10) años de la Licencia de Conducción, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente  autorizados,  por  un  mínimo  de  ochenta  (80) horas."
# shows message
print(message)