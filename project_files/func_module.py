#function module

import random 

#creating function for generating salt

def generate_salt():
# making a list of anions and cations
    global anions
    global cations
    anions=["carbonate","chloride","bromide","iodide","nitrate","sulphate"]
    cations=["ammonium","aluminium","zinc","strontium","magnesium","manganese","calcium","barium","cadmium"]
#using random to generate them
    global anion
    global cation
    anion =random.choice(anions)
    cation =random.choice(cations)

#concatenating both the strings to form the variable which stores salt name
    global salt
    salt = cation + ' ' + anion
#returning generated salt
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