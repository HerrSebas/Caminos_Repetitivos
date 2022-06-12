"""
Se  debe  crear  un  programaque  dada  luna  longitud  en  cuadros
mayor a cero), genere untablero,como en la siguiente imagen(Es
un tablero con una longitud de 8x8):
"""
# captures and stores the layout width as integer
width = int(input("ingrese el ancho del cuadro: "))
# captures and stores the layout lenght as integer
length = int(input("ingrese el largo del cuadro: "))
# aux string to add according to layout
star_string = "***"
# aux string to add according to layout 
empty_string = "   "

# empty string to write every rows      
rows = ""
# set a counter with default value 1
cont = 1
# while loop to add star_string or empty_string over the rows
while cont <= length:
    # for loop to write 3 lines of stars for every row
    for i in range(1,4):
        # checks if row number is odd
        if cont%2 != 0:
            # for loop over to write over the columns
            for column in range(1,width+1):
                # control flow to add text according to column value
                # (empty for even columns,stars for odd columns )
                if column%2 != 0:
                    rows += empty_string
                else:
                    rows += star_string
        else:
            for column in range(1,width+1):
                 # control flow to add text according to column value
                # (string for even columns,empty for odd columns )
                if column%2 != 0:
                    rows += star_string
                else:
                    rows += empty_string
        # adds a new line after every row
        rows += "\n"
    # adds 1 to cont
    cont += 1
# prints the layout.
print(rows)