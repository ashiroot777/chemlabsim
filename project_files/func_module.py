#functionmodule

import random 

#creating function for generating salt

def generate_salt():
# making a list of anions and cations
    anions=["Carbonate","Chloride","Bromide","Iodide","Nitrate","Sulphate"]
    cations=["Ammonium","Aluminium","Zinc","Strontium","Magnesium","Manganese","Calcium","Barium","Cadmium"]

#using random to generate them
    a=random.choice(anions)
    c=random.choice(cations)

#concatenating both the strings to form the variable which stores salt name
    salt = c + ' ' + a 

    return salt

#creating function for establishing connection

def connect_mysql():
#taking password from user
    pass_word = str(input('Enter your MySQL password : '))
    import mysql.connector as m
#connecting
    global mydb
    mydb=m.connect(host='localhost',user='root',password=pass_word)
#creating cursor
    global c
    c=mydb.cursor()

    print('connection established!')