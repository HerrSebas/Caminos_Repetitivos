"""
Dadas dos listas, se debe crear un programaquegenere una tercera
lista  con  los  elementos  que  se  repiten  en  las  dos  anteriores  listas sin 
repetirse ningún elemento en lanueva lista.
"""

# given lists
List_1 = ['h', 'e', 'l', 'l', 'o', ' ', 't', 'e','a', 'm']
List_2 = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o','r', 'l', 'd']

# empty list to store values form list_1 and list_2
new_list = []
#for loop to iterate over list_1
for i in List_1:
    # checks if ith element of list_1 is in list_2 but not in new_list
    if i in List_2 and i not in new_list:
        #adds an element to new_list
        new_list.append(i)
    else:
        # if below condition is false, continues to next i
        continue
# shows new_list values
print(new_list)