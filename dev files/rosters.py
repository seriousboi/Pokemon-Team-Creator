from pokedex import *
from charts import *



class Roster():

    def __init__(self,name,pokemon_list):
        self.name= name
        self.pokemon_list= pokemon_list



def get_rosters():
    global rosters
    return rosters



def update_rosters():
    global rosters,sorted_rosters,all_mons

    rosters= []
    generation= get_generation()
    for tier in tiers:
        roster= sorted_rosters[generation][tier]
        if tier != "nd" and roster.pokemon_list != []:
            rosters += [roster]

    rosters += [all_mons]



sorted_rosters= []
tiers= ["OU","UU","RU","NU","PU","uber","nd"]
for generation in range(8):
    sorted_rosters += [{}]
    for tier in tiers:
        sorted_rosters[generation][tier]= Roster(str(generation+1)+"G "+tier,[])



pokedex= get_pokedex()
for pokemon in pokedex:
    for generation in range(8):
        sorted_rosters[generation][pokemon.tier[generation]].pokemon_list += [pokemon]



rosters= []
generation= get_generation()
for tier in tiers:
    roster= sorted_rosters[generation][tier]
    if tier != "nd" and roster.pokemon_list != []:
        rosters += [roster]

all_mons= Roster("all pokemons",pokedex)
rosters += [all_mons]
