#installing required tables
import anion_cation_table

#analysing anion
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

# menu driven loop for matching anion with test
while True:
    menu=int(input("\nMENU:\n\n0.Add dilute sulphuric acid to salt\n1.Add concentrated sulphuric acid to salt\n2.Add concentrated sulphuric acid to salt,heat test tube and add copper chip\n3.Add Barium Chloride to salt solution\n4.Use notepad\n5.Move on to confirmatory tests\nchoose option : "))
    sql="select {} from {}"

    if menu in range(4):
        fm.c.execute(sql.format(prelim_anion[menu],fm.a))
        result=fm.c.fetchall()
        print('\nResult of the test is:\n',result[0][0])
     
    elif menu == 4:
        print(notepad)
        notes = input('enter your notes:\n')
        notepad += notes
    
    elif menu == 5:
        menu1=int(input('\nMENU:\n\n0.pass gas from effervescence through limewater\n1.Add silver nitrate to salt solution\n2.Add freshly prepared ferrous sulphate and add concentrated sulphuric acid dropwise\n3.Add acetic acid and lead acetate to salt solution\n4.Use notepad\n5.Go back to preliminary tests\nchoose option : '))
        if menu1 in range(4):
            fm.c.execute(sql.format(confirm_anion[menu],fm.a))
            result=fm.c.fetchall()
            print('\nResult of the test is:\n',result[0][0])
        elif menu1 == 4:
            print(notepad)
            notes = input('enter your notes:\n')
            notepad += notes
        elif menu1 == 5:
            continue 
