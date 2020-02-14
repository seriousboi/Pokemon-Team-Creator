from pokedex import *



class Roster():

    def __init__(self,name,pokemon_list):
        self.name= name
        self.pokemon_list= pokemon_list



rosters= []
sorted_rosters= []
tiers= ["OU","UU","RU","NU","PU","uber","nd"]



for generation in range(8):
    sorted_rosters += [{}]
    for tier in tiers:
        sorted_rosters[generation][tier]= Roster(str(generation+1)+"G "+tier,[])


all_mons= Roster("all pokemons",[])
for pokemon in pokedex:
    all_mons.pokemon_list += [pokemon]
    for generation in range(8):
        sorted_rosters[generation][pokemon.tier[generation]].pokemon_list += [pokemon]



for generation in range(8):
    for tier in tiers:
        roster= sorted_rosters[generation][tier]
        if tier != "nd" and roster.pokemon_list != []:
            rosters += [roster]
rosters += [all_mons]
