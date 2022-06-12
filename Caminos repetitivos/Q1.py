
"""
El capitán del barco pirata Thousand Sunny,el famoso Monkey D. Luffy
te hadesignado para que sirva de vigía en el mástil principal. Esto es
lo que te hadichoel capitán:
Tu   misión   es   simple   marinero,   pero   importante   para   la
tripulación,   cuando   veas   alguna   de   estas   criaturas   debes
decirlo de esta manera:
¡Ahoy! capitán, un Krake
¡Ahoy! capitán, unas Sirenas
¡Ahoy! capitán, una Ballena
¡Ahoy! capitán, un Hipocampo
¡Ahoy! capitán, una Macaraprono
¡Ahoy! capitán, un Pulpo
¡Ahoy! capitán, unos Leviatanes
¡Ahoy! capitán, Unas Hidras

Tu vida va en ello marinero, debes pronunciarlos con el articulo 
correcto de acuerdo consu especie (uno, una, unos, unas).
Además, debes decirla dirección del barco por la que aparece 
A babor
A estribor
Por la proa
Por la popa
Para cumplir la misión debes crear un programa que,dada la criatura
y  la  ubicación,  construya  la  cadena  correcta.El  programa  se  debe 
ejecutar  las  veces  que  sea  necesario  hasta  que  el capitalte  diga "stop"
"""
insight = "" # empty string to save sailor´s views later
while insight != "stop": # starts cicle to see landscape until captain says stop
    creature = input("Qué ves?!") #Saves the creature´s name
    location = input("Dónde?!") #Saves the creature´s location
    # control flow for kraken, hipocampo and pulpo
    if creature == "Kraken" or creature == "Hipocampo" or creature == "Pulpo":
        #control flow for creature´s location
        if location == "proa" or location == "popa":
            #shows message with creature and location
            print(f"¡Ahoy! capitán, un {creature} por la {location}")
        else:
            #shows message with creature and location
            print(f"¡Ahoy! capitán, un {creature} a {location}")
    # control flow for sirenas and Hidras
    elif creature == "Sirenas" or creature == "Hidras":
        #control flow for creature´s location
        if location == "proa" or location == "popa":
            #shows message with creature and location
            print(f"¡Ahoy! capitán, unas {creature} por la {location}")
        else:
            #shows message with creature and location
            print(f"¡Ahoy! capitán, unas {creature} a {location}")
    # control flow for ballena and macaraprono
    elif creature == "Ballena" or creature == "Macaraprono":
        #control flow for creature´s location
        if location == "proa" or location == "popa":
            #shows message with creature and location
            print(f"¡Ahoy! capitán, una {creature} por la {location}")
        else:
            #shows message with creature and location
            print(f"¡Ahoy! capitán, una {creature} a {location}")
    # default flow
    else:
        #control flow for creature´s location
        if location == "proa" or location == "popa":
            #shows message with creature and location
            print(f"¡Ahoy! capitán, unos {creature} por la {location}")
        else:
            #shows message with creature and location
            print(f"¡Ahoy! capitán, unos {creature} a {location}")
    # variable to capture captain's order
    insight = input("Capitan! sigo viendo? ")