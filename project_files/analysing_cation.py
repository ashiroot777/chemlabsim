#analysing cation
import tables
import func_module as fm
import analysing_anion

#generating salt
 

#connection
fm.connect_mysql()

fm.c.execute("use salts;")

prelim_cation=["conc_NaOH_heating","dil_HCl","dil_HCl_H2S","solid_NH4Cl_excess_NH4OH","solid_NH4Cl_excess_NH4OH_H2S","solid_NH4Cl_excess_NH4OH_ammoniumCarbonate","solid_NH4Cl_excess_NH4OH_ammoniumPhosphate"]
confirm_cation=["Nesslers_reagent","potassium_hexacyanoferrate","blue_lake_test","sodium_hydroxide_test","potassium_chromate_test","ammonium_sulphate_test","ammonium_oxalate_test","magneton_reagent"]

# notepad for user to make notes regarding their inferences to help them guess the salt.
notepad='' 


sql="select {} from anions where anion = %s ;"

while True:
     menu2=int(input("\nMENU:\n\n0.Add dilute sodium hydroxide to salt and heat\n1.Add diluted hydrochloric acid to salt solution\n2.Add diluted hydrochloric acid to salt solution and pass through H2S gas\n3.Add solid ammonium chloride and excess ammonium hydroxide solution to salt solution\n4.Add solid ammonium chloride and excess ammonium hydroxide solution to salt solution and pass H2S gas\n5.Add solid ammonium chloride, excess ammonium hydroxide solution and ammonium carbonate solution to salt solution\n6.Add solid ammonium chloride, excess ammonium hydroxide solution and ammonium phosphate solution to salt solution\n7.Use notepad\n8.Move onto confirmatory tests\n9.Quit\nchoose option : "))
     if menu2 in range(7):
        fm.c.execute(sql.format(prelim_cation[menu2],),(fm.cation,))
        result=fm.c.fetchall()
        print('\nResult of the test is:\n',result[0][0])

     elif menu2 == 7:
        print('\nopening notepad')
        print(notepad)
        notes = input('enter your notes:\n')
        notepad += notes

#moving onto confirmatory tests
     elif menu2 == 8:
        while True:
            menu3=int(input("\nMENU:\n\n0.Add Nesslers reagent to salt solution\n1.Add potassium hexacyanoferrate to salt solution\n2.blue lake test\n3.Add sodium hydroxide solution to salt solution\n4.Add potassium chromate to salt solution\n5.Add ammonium sulphate to salt solution\n6.Add ammonium oxalate to salt solution\n7.Add magneton reagent to salt solution\n8.Use notepad\n9.go back to preliminary tests\n10.guess cation\nchoose option : "))
            
            if menu3 in range(8):
                fm.c.execute(sql.format(confirm_cation[menu3],),(fm.cation,))
                result=fm.c.fetchall()
                print('\nResult of the test is:\n',result[0][0])

#opening notepad
            elif menu3 == 8:
                print('\nopening notepad')
                print(notepad)
                notes = input('enter your notes:\n')
                notepad += notes

#go back to preliminary tests
            elif menu3 == 9:
                break #exits confirmatory loop

#guess cation
            elif menu3 == 10:
                cation_guess=int(input('\nchoose anion name:\n\n1.ammonium\n2.aluminium\n3.zinc\n4.strontium\n5.magnesium\n6.manganese\n7.calcium\n8.barium\n9.cadmium\n\nyour option : '))
                if fm.cations[cation_guess - 1] == fm.cation: 
                    print('congratulations! you have identified the', analysing_anion.salt_gen, 'correctly!')

                    exit 
                else:
                    print('oops, try again!')
                

#quit option
     elif menu2 == 9:
         exit 

#invalid option
     else:
         print('invalid option!')
