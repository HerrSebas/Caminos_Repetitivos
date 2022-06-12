"""Sin   resistencia   los   cuerpos   caen   a   la   misma   velocidad
independientemente   de   su   masa,   forma   y   composición.
Cuando   se   lanza   un   objeto   la   distancia   que   recorre   es
proporcional al tiempo d=v∗t±(12)∗g∗𝑡2, donde:
d es la distancia recorrida.
g  es  la  aceleración  originada  por  la  gravedad  es  decir 
t es el tiempo transcurrido.
En   honor   al   gran   científicoGalilei, se   debeimplementar   una 
aplicación que dada una altura en metros de un edificiodel que se 
va a lanzar una esfera, vaya mostrando la distancia recorrida segund
a segundo hasta tocar el suelo.
"""
# captures and stores height value as integer
height = int(input("ingrese la altura: "))
# set time counter to start at 0
time = 0
# loop to calculate distance until the object reaches the ground
while height >= 0:
    # calculates and stores distance value with 10 as constant speed
    distance = 10*time + (1/2)*(9.8)*(time**2)
    # shows the distance at every second
    print (f"""La distancia recorrida en el\n
           segundo #{time} es #{distance}""")
    # substract distance to height
    height -= distance
    # adds a second to time
    time += 1
# shows a message when the object reaches the ground
print("su objeto ha llegado al suelo")