# I think we should make a list of cations and anions in python and use random to generate them. We should have tables for each anion and cation in mysql and that table should have what tests it gives. Also a salt may not give only its preliminary test the user should do it in order but we give them the options to do whatever.
import random 
anions=["Carbonate","Chloride","Bromide","Iodide","Nitrate","Sulphate"]
cations=["Ammonium","Aluminium","Zinc","Strontium","Magnesium","Manganese","Calcium","Barium","Cadmium"]
a=random.choice(anions)
c=random.choice(cations)
salt=c+a #concating both the strings to form the variable which stores salt name
