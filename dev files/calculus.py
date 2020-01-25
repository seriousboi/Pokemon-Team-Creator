from pokedex import *
import math



existing_types=["none","normal","fire","water","electric","grass","ice","fighting","poison","ground","flying","psychic","bug","rock","ghost","dragon","dark","steel","fairy"]

types_values= {}

for i in range(len(existing_types)):
    types_values[existing_types[i]]= i

type_chart =[
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,2,1,1,1,1,1,1,0,1,1,1,1],
[1,1,0.5,2,1,0.5,0.5,1,1,2,1,1,0.5,2,1,1,1,0.5,0.5],
[1,1,0.5,0.5,2,2,0.5,1,1,1,1,1,1,1,1,1,1,0.5,1],
[1,1,1,1,0.5,1,1,1,1,2,0.5,1,1,1,1,1,1,0.5,1],
[1,1,2,0.5,0.5,0.5,2,1,2,0.5,2,1,2,1,1,1,1,1,1],
[1,1,2,1,1,1,0.5,2,1,1,1,1,1,2,1,1,1,2,1],
[1,1,1,1,1,1,1,1,1,1,2,2,0.5,0.5,1,1,0.5,1,2],
[1,1,1,1,1,0.5,1,0.5,0.5,2,1,2,0.5,1,1,1,1,1,0.5],
[1,1,1,2,0,2,2,1,0.5,1,1,1,1,0.5,1,1,1,1,1],
[1,1,1,1,2,0.5,2,0.5,1,0,1,1,0.5,2,1,1,1,1,1],
[1,1,1,1,1,1,1,0.5,1,1,1,0.5,2,1,2,1,2,1,1],
[1,1,2,1,1,0.5,1,0.5,1,0.5,2,1,1,2,1,1,1,1,1],
[1,0.5,0.5,2,1,2,1,2,0.5,2,0.5,1,1,1,1,1,1,2,1],
[1,0,1,1,1,1,1,0,0.5,1,1,1,0.5,1,2,1,2,1,1],
[1,1,0.5,0.5,0.5,0.5,2,1,1,1,1,1,1,1,1,2,1,1,2],
[1,1,1,1,1,1,1,2,1,1,1,0,2,1,0.5,1,0.5,1,2],
[1,0.5,2,1,1,0.5,0.5,2,0,2,0.5,0.5,0.5,0.5,1,0.5,1,0.5,0.5],
[1,1,1,1,1,1,1,0.5,2,1,1,1,0.5,1,1,0,0.5,2,1],
]



def among(k,n):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))



def attack_coefficient(attacking_type,defending_type):
    global types_values , type_chart

    attacking_value= types_values[attacking_type]
    defending_value_1= types_values[defending_type[0]]
    defending_value_2= types_values[defending_type[1]]

    coef_1= type_chart[defending_value_1][attacking_value]
    coef_2= type_chart[defending_value_2][attacking_value]

    return coef_1*coef_2



def type_weaknesses(defending_type):
    global existing_types

    weaknesses_chart= []
    for attacking_type in existing_types:
        weaknesses_chart= weaknesses_chart + [attack_coefficient(attacking_type,defending_type)]

    return weaknesses_chart



def pokemon_weaknesses(pokemon):
    global pokedex, types_values

    weaknesses_chart= type_weaknesses(pokemon.type)

    if pokemon.ability.weaknesses_influent:
        weaknesses_chart= pokemon.ability.ability_function(weaknesses_chart,types_values)

    return weaknesses_chart



def team_weaknesses(team):
    global existing_types

    team_weaknesses_chart= []
    for i in range(len(existing_types)):
        team_weaknesses_chart = team_weaknesses_chart + [0]


    for pokemon in team:
        weaknesses_chart= pokemon_weaknesses(pokemon)

        for i in range(len(weaknesses_chart)):
            if weaknesses_chart[i] < 1:
                team_weaknesses_chart[i]= team_weaknesses_chart[i] +1
            elif weaknesses_chart[i] > 1:
                team_weaknesses_chart[i]= team_weaknesses_chart[i] -1

    return team_weaknesses_chart



def typing_only_weaknesses(typing):
    global types_values

    weaknesses_chart= type_weaknesses(typing)
    ability= typing[2]

    if ability.weaknesses_influent:
        weaknesses_chart= ability.ability_function(weaknesses_chart,types_values)

    return weaknesses_chart



def typings_only_weaknesses(typings):
    global existing_types

    typings_weaknesses_chart= []
    for i in range(len(existing_types)):
        typings_weaknesses_chart = typings_weaknesses_chart + [0]


    for typing in typings:
        weaknesses_chart= typing_only_weaknesses(typing)

        for i in range(len(weaknesses_chart)):
            if weaknesses_chart[i] < 1:
                typings_weaknesses_chart[i]= typings_weaknesses_chart[i] +1
            elif weaknesses_chart[i] > 1:
                typings_weaknesses_chart[i]= typings_weaknesses_chart[i] -1

    return typings_weaknesses_chart
