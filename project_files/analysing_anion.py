#installing required tables
import tables
import func_module as fm

#generating salt
fm.generate_salt()

#connection
fm.connect_mysql()

print('\na salt has been generated for analysation!')

fm.c.execute("use salts;")
prelim_anion=["dil_H2SO4","conc_H2SO4","conc_H2SO4_heating","BaCl2"]
confirm_anion=["Limewater","AgNO3","Brown_Ring_Test","LeadAcetate"]

# notepad for user to make notes regarding their inferences to help them guess the salt.
notepad='' 

sql="select {} from anions where anion = %s ;"

# menu driven loop for matching ion with test
while True:

#menu for preliminary tests of anion
    menu=int(input("\nMENU:\n\n0.Add dilute sulphuric acid to salt\n1.Add concentrated sulphuric acid to salt\n2.Add concentrated sulphuric acid to salt,heat test tube and add copper chip\n3.Add Barium Chloride to salt solution\n4.Use notepad\n5.Move on to confirmatory tests\n6.Quit\nchoose option : "))
    
#printing result from table
    if menu in range(4):
        fm.c.execute(sql.format(prelim_anion[menu],),(fm.a,))
        result=fm.c.fetchall()
        print('\nResult of the test is:\n',result[0][0])

#using notepad   
    elif menu == 4:
        print('\nopening notepad')
        print(notepad)
        notes = input('enter your notes:\n')
        notepad += notes
    
    elif menu == 5:
        while True:
#menu for confirmatory tests of anion
            menu1=int(input('\nMENU:\n\n0.pass gas from effervescence through limewater\n1.Add silver nitrate to salt solution\n2.Add freshly prepared ferrous sulphate and add concentrated sulphuric acid dropwise\n3.Add acetic acid and lead acetate to salt solution\n4.Use notepad\n5.go back to preliminary tests\n6.move on to cation\nchoose option : '))
 
 #printing result from table           
            if menu1 in range(4):
                fm.c.execute(sql.format(confirm_anion[menu1],),(fm.a,))
                result=fm.c.fetchall()
                print('\nResult of the test is:\n',result[0][0])

 #using notepad           
            elif menu1 == 4:
                print('\nopening notepad')
                print(notepad)
                notes = input('enter your notes:\n')
                notepad += notes

#exiting confirmatory         
            elif menu1 == 5: 
                break  

            elif menu1 == 6:
                exit

    else:
        break 

