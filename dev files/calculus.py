from pokedex import *
import pygame, math



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



def get_team_weaknesses(team):
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



def get_team_weakness_value(team,type_chart):
    team_weakness_value= 0
    team_weaknesses= get_team_weaknesses(team)
    for weakness_value in team_weaknesses:
        team_weakness_value += weakness_value
    return team_weakness_value



def sort_teams(window,teams,type_chart,display_progression):
    teams_amount= len(teams)
    if teams_amount == 0:
        return []
    progression_goal= int(teams_amount*(1+(teams_amount+1)/2))
    progression= [0]

    teams_weaknesses_values= []
    for team in teams:
        teams_weaknesses_values += [get_team_weakness_value(team,type_chart)]

        pygame.event.pump()
        if display_progression == True:
            display_sort_progression(window,progression,progression_goal)

    sorted_teams= []
    for amount_sorted in range(teams_amount):
        max_weakness_value= -6*19
        max_index= None
        for index in range(teams_amount-amount_sorted):
            weakness_value= teams_weaknesses_values[index]
            if weakness_value > max_weakness_value:
                max_weakness_value= weakness_value
                max_index= index

            pygame.event.pump()
            if display_progression == True:
                display_sort_progression(window,progression,progression_goal)

        sorted_teams += [teams[max_index]]
        del teams[max_index]
        del teams_weaknesses_values[max_index]

    return sorted_teams



def display_sort_progression(window,progression,progression_goal):
    progression[0] += 1
    if progression[0]%(progression_goal/100) == 0:
        advancement= int(100*progression[0]/progression_goal)
        pygame.draw.rect(window,(150,250,150),(550-300/2,585-100/2,300,100),0)
        text(window,"sorting "+str(advancement)+"%",20,(0,0,0),"midbottom",550,585)
        pygame.display.update()



def text(window,message,size,color,anchor,x,y):

    font = pygame.font.SysFont("verdana", size)
    text = font.render(message,True,color)
    area = text.get_rect()
    width= area.width
    height= area.height

    vect= {"topleft":[0,0],
           "bottomleft":[0,-2],
           "topright":[-2,0],
           "bottomright":[-2,-2],
           "midtop":[-1,0],
           "midleft":[0,-1],
           "midbottom":[-1,-2],
           "midright":[-2,-1],
           "center":[-1,-1]}

    x= x + vect[anchor][0]*width/2
    y= y + vect[anchor][1]*height/2

    return window.blit(text,(x,y))
