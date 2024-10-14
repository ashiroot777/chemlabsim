#main program
while True:
    choice = int(input('MAIN MENU :\n\n1.begin analysing salt\n2.review chart'))

    if choice == 1:
        import analysing_anion 

    elif choice == 2:
        import analysing_cation
