#this code must be run once by user to create all the required tables in their local storage. 

#connection
import func_module as fm
fm.connect_mysql()

#checking whether database exists
fm.c.execute('show databases;')
data=(fm.c.fetchall())
if ('salts',) in data:
    overwrite = input('do you want to replace this table with a new one?\n enter Y for yes and N for no\nyour choice :')
    if overwrite == 'Y':
        fm.c.execute('drop database salts;')
    else:
        print('try again!')

# anion table creation code
fm.c.execute("create database salts;")
fm.c.execute("use salts;")

fm.c.execute("""create table carbonate(dil_H2SO4 varchar(30),conc_H2SO4 varchar(30),conc_H2SO4_heating varchar(30),BaCl2 varchar(30),Limewater varchar(30),AgNO3 varchar(30),Brown_Ring_Test varchar(30),LeadAcetate varchar(30));""")
fm.c.execute("""insert into carbonate values("brisk effervesence","No Fumes","No Fumes","No precipitate","Lime Water turns milky","No precipitate","Not given by this anion","Not given by this anion");""")
fm.mydb.commit()

fm.c.execute("""create table chloride(dil_H2SO4 varchar(30),conc_H2SO4 varchar(30),conc_H2SO4h_eating varchar(30),BaCl2 varchar(30),Limewater varchar(30),AgNO3 varchar(30),Brown_Ring_Test varchar(30),LeadAcetate varchar(30));""")
fm.mydb.commit()

fm.c.execute("""insert into chloride values("No effervesence","White Fumes","White Fumes","No precipitate","Lime Water does not turn milky","White precipitate","Not given by this anion","Not given by this anion");""")
fm.mydb.commit()

fm.c.execute("""create table bromide(dil_H2SO4 varchar(30),conc_H2SO4 varchar(30),conc_H2SO4_heating varchar(30),BaCl2 varchar(30),Limewater varchar(30),AgNO3 varchar(30),Brown_Ring_Test varchar(30),LeadAcetate varchar(30));""")
fm.c.execute("""insert into bromide values("No effervesence","Light Brown Fumes","Light Brown Fumes","No precipitate","Lime Water does not turn milky","Pale yellow precipitate ","Not given by this anion","Not given by this anion");""")
fm.mydb.commit()

fm.c.execute("""create table iodide(dil_H2SO4 varchar(30),conc_H2SO4 varchar(30),conc_H2SO4_heating varchar(30),BaCl2 varchar(30),Limewater varchar(30),AgNO3 varchar(30),Brown_Ring_Test varchar(30),LeadAcetate varchar(30));""")
fm.c.execute("""insert into iodide values("No effervesence","Violet Fumes","Violet Fumes","No precipitate","Lime Water does not turn milky","Pale yellow precipitate","Not given by this anion","Not given by this anion");""")
fm.mydb.commit()

fm.c.execute("""create table nitrate(dil_H2SO4 varchar(30),conc_H2SO4 varchar(30),conc_H2SO4_heating varchar(30),BaCl2 varchar(30),Limewater varchar(30),AgNO3 varchar(30),Brown_Ring_Test varchar(30),LeadAcetate varchar(30));""")
fm.c.execute("""insert into nitrate values("No effervesence","No Fumes","Light Brown Fumes","No precipitate","Lime Water does not turn milky","No precipitate","A dark brown ring is formed","Not given by this anion");""")
fm.mydb.commit()

fm.c.execute("""create table Sulphate(dil_H2SO4 varchar(30),conc_H2SO4 varchar(30),conc_H2SO4_heating varchar(30),BaCl2 varchar(30),Limewater varchar(30),AgNO3 varchar(30),Brown_Ring_Test varchar(30),LeadAcetate varchar(30));""")
fm.c.execute("""insert into Sulphate values("No effervesence","No Fumes","No Fumes","White precipitate","Lime Water does not turn milky","No precipitate","Not given by this anion","White precipitate");""")
fm.mydb.commit()
#ANIONS CREATED

#cation table creation code
fm.c.execute("""create table ammonium(conc_NaOH_heating varchar(30),dil_HCl varchar(30),dil_HCl_H2S varchar(30),solid_NH4Cl_excess_NH4OH varchar(30),solid_NH4Cl_excess_NH4OH_H2S varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumCarbonate varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumPhosphate varchar(30),Nesslers_reagent varchar(30),potassium_hexacyanoferrate varchar(30),blue_lake_test varchar(30),sodium_hydroxide_test varchar(30),potassium_chromate_test varchar(30),ammonium_sulphate_test varchar(30),ammonium_oxalate_test varchar(30),magneton_reagent varchar(30));""")
fm.c.execute("""insert into ammonium values("ammonical smell","No precipitate","No precipitate","No precipitate","no precipitate","No precipitate","No precipitate","brown precipitate","not given by this ion","not given by this ion","not given by this ion","not given by this ion","not given by this ion","not given by this ion","not given by this ion");""")
fm.mydb.commit()

fm.c.execute("""create table cadmium(conc_NaOH_heating varchar(30),dil_HCl varchar(30),dil_HCl_H2S varchar(30),solid_NH4Cl_excess_NH4OH varchar(30),solid_NH4Cl_excess_NH4OH_H2S varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumCarbonate varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumPhosphate varchar(30),Nesslers_reagent varchar(30),potassium_hexacyanoferrate varchar(30),blue_lake_test varchar(30),sodium_hydroxide_test varchar(30),potassium_chromate_test varchar(30),ammonium_sulphate_test varchar(30),ammonium_oxalate_test varchar(30),magneton_reagent varchar(30));""")
fm.c.execute("""insert into cadmium values("no ammonical smell","No precipitate","yellow precipitate","No precipitate","no precipitate","No precipitate","No precipitate","no precipitate","white precipitate","not given by this ion","not given by this ion","not given by this ion","not given by this ion","not given by this ion","not given by this ion");""")
fm.mydb.commit()

fm.c.execute("""create table aluminium(conc_NaOH_heating varchar(30),dil_HCl varchar(30),dil_HCl_H2S varchar(30),solid_NH4Cl_excess_NH4OH varchar(30),solid_NH4Cl_excess_NH4OH_H2S varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumCarbonate varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumPhosphate varchar(30),Nesslers_reagent varchar(30),potassium_hexacyanoferrate varchar(30),blue_lake_test varchar(30),sodium_hydroxide_test varchar(30),potassium_chromate_test varchar(30),ammonium_sulphate_test varchar(30),ammonium_oxalate_test varchar(30),magneton_reagent varchar(30));""")
fm.c.execute("""insert into aluminium values("no ammonical smell","No precipitate","No precipitate","gelatinous precipitate","no precipitate","No precipitate","No precipitate","no precipitate","not given by this ion","blue precipitate","not given by this ion","not given by this ion","not given by this ion","not given by this ion","not given by this ion");""")
fm.mydb.commit()

fm.c.execute("""create table zinc(conc_NaOH_heating varchar(30),dil_HCl varchar(30),dil_HCl_H2S varchar(30),solid_NH4Cl_excess_NH4OH varchar(30),solid_NH4Cl_excess_NH4OH_H2S varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumCarbonate varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumPhosphate varchar(30),Nesslers_reagent varchar(30),potassium_hexacyanoferrate varchar(30),blue_lake_test varchar(30),sodium_hydroxide_test varchar(60),potassium_chromate_test varchar(30),ammonium_sulphate_test varchar(30),ammonium_oxalate_test varchar(30),magneton_reagent varchar(30));""")
fm.c.execute("""insert into zinc values("no ammonical smell","No precipitate","No precipitate","No precipitate","white precipitate","No precipitate","No precipitate","no precipitate","not given by this ion","not given by this ion","white ppt that dissolves in excess NaOH","not given by this ion","not given by this ion","not given by this ion","not given by this ion");""")
fm.mydb.commit()

fm.c.execute("""create table manganese(conc_NaOH_heating varchar(30),dil_HCl varchar(30),dil_HCl_H2S varchar(30),solid_NH4Cl_excess_NH4OH varchar(30),solid_NH4Cl_excess_NH4OH_H2S varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumCarbonate varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumPhosphate varchar(30),Nesslers_reagent varchar(30),potassium_hexacyanoferrate varchar(30),blue_lake_test varchar(30),sodium_hydroxide_test varchar(60),potassium_chromate_test varchar(30),ammonium_sulphate_test varchar(30),ammonium_oxalate_test varchar(30),magneton_reagent varchar(30));""")
fm.c.execute("""insert into manganese values("no ammonical smell","No precipitate","No precipitate","No precipitate","buff precipitate","No precipitate","No precipitate","no precipitate","not given by this ion","not given by this ion","white ppt that does not dissolve in excess NaOH","not given by this ion","not given by this ion","not given by this ion","not given by this ion");""")
fm.mydb.commit()

fm.c.execute("""create table barium(conc_NaOH_heating varchar(30),dil_HCl varchar(30),dil_HCl_H2S varchar(30),solid_NH4Cl_excess_NH4OH varchar(30),solid_NH4Cl_excess_NH4OH_H2S varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumCarbonate varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumPhosphate varchar(30),Nesslers_reagent varchar(30),potassium_hexacyanoferrate varchar(30),blue_lake_test varchar(30),sodium_hydroxide_test varchar(30),potassium_chromate_test varchar(30),ammonium_sulphate_test varchar(30),ammonium_oxalate_test varchar(30),magneton_reagent varchar(30));""")
fm.c.execute("""insert into barium values("no ammonical smell","No precipitate","No precipitate","No precipitate","no precipitate","white precipitate","No precipitate","no precipitate","not given by this ion","not given by this ion","not given by this ion","yellow precipitate","not given by this ion","not given by this ion","not given by this ion");""")
fm.mydb.commit()

fm.c.execute("""create table strontium(conc_NaOH_heating varchar(30),dil_HCl varchar(30),dil_HCl_H2S varchar(30),solid_NH4Cl_excess_NH4OH varchar(30),solid_NH4Cl_excess_NH4OH_H2S varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumCarbonate varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumPhosphate varchar(30),Nesslers_reagent varchar(30),potassium_hexacyanoferrate varchar(30),blue_lake_test varchar(30),sodium_hydroxide_test varchar(30),potassium_chromate_test varchar(30),ammonium_sulphate_test varchar(30),ammonium_oxalate_test varchar(30),magneton_reagent varchar(30));""")
fm.c.execute("""insert into strontium values("no ammonical smell","No precipitate","No precipitate","No precipitate","no precipitate","white precipitate","No precipitate","no precipitate","not given by this ion","not given by this ion","not given by this ion","no precipitate","white precipitate","not given by this ion","not given by this ion");""")
fm.mydb.commit()

fm.c.execute("""create table calcium(conc_NaOH_heating varchar(30),dil_HCl varchar(30),dil_HCl_H2S varchar(30),solid_NH4Cl_excess_NH4OH varchar(30),solid_NH4Cl_excess_NH4OH_H2S varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumCarbonate varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumPhosphate varchar(30),Nesslers_reagent varchar(30),potassium_hexacyanoferrate varchar(30),blue_lake_test varchar(30),sodium_hydroxide_test varchar(30),potassium_chromate_test varchar(30),ammonium_sulphate_test varchar(30),ammonium_oxalate_test varchar(30),magneton_reagent varchar(30));""")
fm.c.execute("""insert into calcium values("no ammonical smell","No precipitate","No precipitate","No precipitate","no precipitate","white precipitate","No precipitate","no precipitate","not given by this ion","not given by this ion","not given by this ion","no precipitate","not given by this ion","white precipitate","not given by this ion");""")
fm.mydb.commit()

fm.c.execute("""create table magnesium(conc_NaOH_heating varchar(30),dil_HCl varchar(30),dil_HCl_H2S varchar(30),solid_NH4Cl_excess_NH4OH varchar(30),solid_NH4Cl_excess_NH4OH_H2S varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumCarbonate varchar(30),solid_NH4Cl_excess_NH4OH_ammoniumPhosphate varchar(30),Nesslers_reagent varchar(30),potassium_hexacyanoferrate varchar(30),blue_lake_test varchar(30),sodium_hydroxide_test varchar(30),potassium_chromate_test varchar(30),ammonium_sulphate_test varchar(30),ammonium_oxalate_test varchar(30),magneton_reagent varchar(30));""")
fm.c.execute("""insert into magnesium values("no ammonical smell","No precipitate","No precipitate","No precipitate","no precipitate","white precipitate","No precipitate","no precipitate","not given by this ion","not given by this ion","not given by this ion","no precipitate","not given by this ion","no precipitate","blue precipitate");""")
fm.mydb.commit()

print('installed files!')
