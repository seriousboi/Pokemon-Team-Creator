from pokedex import *
from charts import *
from storage import get_txt_list
import glob


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
    global tiers_rosters

    tiers= ["OU","UU","RU","NU","PU","uber"]

    for tier in tiers:
        tiers_rosters[tier]= Roster(tier,[])

def init_maximum_evolution_stage_pokemons_roster():
    global MES_roster

    MES_roster= Roster("final evolutions",[])



def update_rosters():
    update_pokedex_roster()
    update_tiers_rosters_list()
    update_MES_roster()

def update_pokedex_roster():
    global pokedex_roster

    pokedex= get_pokedex()
    pokedex_roster.pokemon_list= pokedex

def update_tiers_rosters_list():
    global tiers_rosters, tiers_rosters_list

    tiers= ["OU","UU","RU","NU","PU","uber"]
    generation= get_generation()

    for tier in tiers:
        tiers_rosters[tier].pokemon_list= []

    pokedex= get_pokedex()
    for pokemon in pokedex:
        pokemon_tier= pokemon.tier[generation]
        if pokemon_tier != 'nd':
            tiers_rosters[pokemon_tier].pokemon_list += [pokemon]

    tiers_rosters_list= []
    for tier in tiers:
        tiers_rosters_list += [tiers_rosters[tier]]

def update_MES_roster():
    global MES_roster

    MES_list= []
    pokedex= get_pokedex()
    for pokemon in pokedex:
        if 'MES' in pokemon.properties:
            MES_list += [pokemon]

    MES_roster.pokemon_list= MES_list



def get_common_rosters():
    common_rosters_list=[]
    common_rosters_list += get_tiers_rosters_list()
    common_rosters_list += get_custom_rosters_list()
    common_rosters_list += [get_pokedex_roster()]
    common_rosters_list += [get_MES_roster()]
    return common_rosters_list

def get_pokedex_roster():
    global pokedex_roster
    return pokedex_roster

def get_tiers_rosters_list():
    global tiers_rosters_list
    return tiers_rosters_list

def get_MES_roster():
    global MES_roster
    return MES_roster

def get_custom_rosters_list():
    filenames= glob.glob('./data/custom_rosters/*.txt')
    custom_rosters=[]
    for filename in filenames:
        custom_rosters += [get_custom_roster(filename)]
    return custom_rosters

def get_custom_roster(filename):
    txt_list= get_txt_list(filename)

    pokemon_list= []
    size= int(txt_list[0][0])
    for pokemon_index in range(size):
              pokemon_picid= txt_list[0][pokemon_index+1]
              pokemon_list= pokemon_list + [get_pokemon_from_picid(pokemon_picid)]

    roster= Roster(filename[22:len(filename)-4],pokemon_list)
    return roster



pokedex_roster= []
tiers_rosters= {}
tiers_rosters_list= []
MES_roster= []
init_rosters()
update_rosters()
