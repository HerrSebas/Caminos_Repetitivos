"""
Debe crear un programaque dada una generación (mayor o igual a cero):
Le indique al usuario el número total de personas de la familia (de
todas las generaciones hasta la generación dada).
Muestre  el  número  de  personas  de  cada  generación  mientras 
hace el cálculo.
"""
# captures and stores number of generations as string
num = int(input("Ingrese el número de generaciones: "))
# family members counter (set default to 0)
family = 0
# loop to iterate over each generation
for generation in range( num+1 ):
    # calculates family members in generation_i as an exponetial function
    people = 2**generation
    # prints the number of people in the generation_i
    print(f"la generación {generation} tiene {people} miembros")
    # adds people to total family members counter
    family += people
# prints total family members
print(f"La familia tiene {family} miembros")