"""
Programme permettant de convertir une quantité en plusieurs unités d'énergie.

1J  =  0.738 ft-lb  =  0.239 cal  =  6.24*10^18 eV

Unités : joule, calorie, Ft-lb et eV
  Données : Une valeur et une unité
  Indications:
        Selon l'unité entrée par l'utilisateur, afficher la conversion
        dans les 3 autres unités.
  Résultats : Affichage des conversions
"""

### Déclaration et initialisation des variable

#Puissance exposant > **
#Variable de base > Joule

#Nomenclature des unités
UNIT_NAME_JLE: str = "Joule"
UNIT_NAME_FT_LB: str = "Ft lb"
UNIT_NAME_CAL: str = "Calorie"
UNIT_NAME_EV: str = "Ev"

#Valeur pour chaques unités
unit_joule: int = 1
unit_ft_lb: int = 0.738
unit_cal: int = 0.239
unit_eV: int = 6.24*10**18

var_unit: str = (input("Entrez une unité (Joule, Ft lb, Calorie, Ev : "))
var_val: int = int(input("Entrez une valeur: "))


### Séquence d'opération

if var_unit == UNIT_NAME_JOULE:
    print("", var_val * unit_ft_lb ,"ft lb")
    print(var_val * unit_cal)
    print(var_val * unit_eV)

elif var_unit == UNIT_NAME_FT_LB:
    print(var_val * unit_joule)
    print(var_val * unit_cal)
    print(var_val * unit_eV)





