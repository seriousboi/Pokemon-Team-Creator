


class Ability:
    def __init__(self,weaknesses_influent,ability_function,ability_name):
        self.weaknesses_influent= weaknesses_influent
        self.ability_function= ability_function
        self.ability_name= ability_name


def get_ability_variable_name(ability_name):
    ability_variable_name= ""
    for letter in ability_name:
        if letter == " ":
            ability_variable_name += "_"
        else:
            ability_variable_name += letter
    return ability_variable_name



def no_ability_function(weaknesses_chart,types_values):
    return weaknesses_chart



def Dry_Skin_function(weaknesses_chart,types_values):
    weaknesses_chart[types_values["fire"]]= weaknesses_chart[types_values["fire"]]*2
    weaknesses_chart[types_values["water"]]= 0
    return weaknesses_chart



def Thick_Fat_function(weaknesses_chart,types_values):
    weaknesses_chart[types_values["fire"]]= weaknesses_chart[types_values["fire"]]/2
    weaknesses_chart[types_values["ice"]]= weaknesses_chart[types_values["ice"]]/2
    return weaknesses_chart



def Volt_Absorb_function(weaknesses_chart,types_values):
    weaknesses_chart[types_values["electric"]]= 0
    return weaknesses_chart



def Flash_Fire_function(weaknesses_chart,types_values):
    weaknesses_chart[types_values["fire"]]= 0
    return weaknesses_chart



def Water_Absorb_function(weaknesses_chart,types_values):
    weaknesses_chart[types_values["water"]]= 0
    return weaknesses_chart



def Levitate_function(weaknesses_chart,types_values):
    weaknesses_chart[types_values["ground"]]= 0
    return weaknesses_chart



def Filter_function(weaknesses_chart,types_values):
    weaknesses_amount= len(weaknesses_chart)
    for weakness_index in range(weaknesses_amount):
        if weaknesses_chart[weakness_index] == 2:
            weaknesses_chart[weakness_index]= 3/2
        elif weaknesses_chart[weakness_index] == 4:
            weaknesses_chart[weakness_index]= 3
    return weaknesses_chart



no_ability= Ability(False,no_ability_function,"no ability")
Dry_Skin= Ability(True,Dry_Skin_function,"Dry Skin")
Thick_Fat= Ability(True,Thick_Fat_function,"Thick Fat")
Volt_Absorb= Ability(True,Volt_Absorb_function,"Volt Absorb")
Lightning_Rod= Ability(True,Volt_Absorb_function,"Lightning Rod")
Flash_Fire= Ability(True,Flash_Fire_function,"Flash Fire")
Water_Absorb= Ability(True,Water_Absorb_function,"Water Absorb")
Levitate= Ability(True,Levitate_function,"Levitate")
Filter= Ability(True,Filter_function,"Filter")
