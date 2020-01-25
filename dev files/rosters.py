from pokedex import *



class Roster():

    def __init__(self,name,pokemon_list):
        self.name= name
        self.pokemon_list= pokemon_list


OU_7G=[]
for pokemon in pokedex:
    if pokemon.tier == "OU":
        OU_7G += [pokemon]



all_pokemons= Roster("all pokemons",pokedex)
OU_7G= Roster("OU 7G",OU_7G)
rosters= [OU_7G,all_pokemons]
