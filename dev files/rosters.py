from pokedex import *
from charts import *



class Roster():

    def __init__(self,name,pokemon_list):
        self.name= name
        self.pokemon_list= pokemon_list



def init_rosters():
    init_pokedex_roster()
    init_tiers_rosters()
    init_maximum_evolution_stage_pokemons_roster()

def init_pokedex_roster():
    global pokedex_roster

    pokedex= get_pokedex()
    pokedex_roster= Roster("all pokemons",pokedex)

def init_tiers_rosters():
    global all_tiers_rosters

    tiers= ["OU","UU","RU","NU","PU","uber","nd"]
    for generation in range(8):
        all_tiers_rosters += [{}]
        for tier in tiers:
            all_tiers_rosters[generation][tier]= Roster(str(generation+1)+"G "+tier,[])

    pokedex= get_pokedex()
    for pokemon in pokedex:
        for generation in range(8):
            all_tiers_rosters[generation][pokemon.tier[generation]].pokemon_list += [pokemon]

def init_maximum_evolution_stage_pokemons_roster():
    global MES_roster

    MES_roster= Roster("final evolutions",[])



def update_rosters():
    update_tiers_rosters()
    update_MES_roster()

def update_tiers_rosters():
    global generation_tiers_rosters, all_tiers_rosters


    generation= get_generation()
    generation_tiers_rosters= []
    tiers= ["OU","UU","RU","NU","PU","uber","nd"]
    for tier in tiers:
        roster= all_tiers_rosters[generation][tier]
        if tier != "nd" and roster.pokemon_list != []:
            generation_tiers_rosters += [roster]

def update_MES_roster():
    global MES_roster

    MES_list= []
    pokedex= get_pokedex()
    for pokemon in pokedex:
        if 'MES' in pokemon.properties:
            MES_list += [pokemon]
    
    MES_roster.pokemon_list= MES_list



def get_pokedex_roster():
    global pokedex_roster
    return pokedex_roster

def get_generation_tiers_rosters():
    global generation_tiers_rosters
    return generation_tiers_rosters

def get_MES_roster():
    global MES_roster
    return MES_roster

def get_common_rosters():
    common_rosters_list=[]
    common_rosters_list += get_generation_tiers_rosters()
    common_rosters_list += [get_pokedex_roster()]
    common_rosters_list += [get_MES_roster()]
    return common_rosters_list


pokedex_roster= []
all_tiers_rosters= []
generation_tiers_rosters= []
MES_roster= []
init_rosters()
update_rosters()
