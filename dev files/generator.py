from pokedex import *
from storage import *
from calculus import *
from display import *
import pygame



def generating(window,generating_params):

    window.fill((150,250,150))
    text(window,"starting",40,(0,0,0),"center",550,300)
    pygame.display.update()

    team= generating_params[0]
    roster= generating_params[1]
    requirements= generating_params[2]
    mega= generating_params[3]
    roles= generating_params[4]
    [teams,progression,progression_goal]= generate_team_advanced(window,team,roster,requirements,mega)

    teams= filter_teams(window,teams,roles,progression,progression_goal)

    window.fill((150,250,150))
    hitbox_back= text(window,"back",20,(0,0,0),"bottomleft",15,585)
    hitbox_prev= text(window,"<<",20,(0,0,0),"topleft",15,340)
    hitbox_nex= text(window,">>",20,(0,0,0),"topright",215,340)
    hitbox_save= text(window,"save team",20,(0,0,0),"bottomright",1085,585)
    hitbox_page= (75,340,80,30)

    current_team= -1
    current_page= 0


    while True:
        hitboxes= display_teams(window,teams,current_page,current_team)
        pygame.draw.rect(window,(150,250,150),hitbox_page,0)
        hitbox_page= text(window,"page "+str(current_page+1),20,(0,0,0),"midtop",115,340)

        if current_team != -1:
            display_team_weaknesses(window,teams[current_team+current_page*5],330,340)
        else:
            display_team_weaknesses(window,[],330,340)

        pygame.display.update()

        event= pygame.event.wait()

        if event.type == pygame.QUIT:
                return "quit"

        if event.type == pygame.MOUSEBUTTONDOWN:

            if hitbox_back.collidepoint(event.pos):
                    return "team generator"

            elif hitbox_prev.collidepoint(event.pos) and len(teams)!=0:
                current_page= (current_page-1)%(((len(teams)-1)//5)+1)
                current_team= -1

            elif hitbox_nex.collidepoint(event.pos) and len(teams)!=0:
                current_page= (current_page+1)%(((len(teams)-1)//5)+1)
                current_team= -1

            elif hitbox_save.collidepoint(event.pos) and current_team != -1:
                save_team(teams[current_team+current_page*5])
                del teams[current_team+current_page*5]
                current_team= -1

            else:
                for i in range(len(hitboxes)):

                    if hitboxes[i].collidepoint(event.pos):
                        current_team= i



def display_progression(window,progression,progression_goal):

    pygame.event.pump()

    progression[0]= progression[0] + 1

    if progression[0]%(progression_goal/100) == 0:

        window.fill((150,250,150))

        advancement= int(100*progression[0]/progression_goal)

        text(window,str(advancement)+"%",40,(0,0,0),"center",550,300)

        pygame.display.update()



def generate_team_advanced(window,team,roster,requirements,mega):

    progression= [0]

    if len(team) + len(roster.pokemon_list) < 6:
        return []

    already_mega= False
    for pokemon in team:
        if "mega" in pokemon.properties:
            already_mega= True


    non_mega_index=[]
    mega_index=[]
    non_mega_roster= []
    mega_roster= []
    for pokemon in roster.pokemon_list:
        if not "mega" in pokemon.properties:
            non_mega_roster= non_mega_roster + [pokemon]
            type_ = pokemon.type + [pokemon.ability]
            if not type_ in non_mega_index:
                non_mega_index= non_mega_index + [type_]
        else:
            mega_roster= mega_roster + [pokemon]
            type_ = pokemon.type + [pokemon.ability]
            if not type_ in mega_index:
                mega_index= mega_index + [type_]

    if already_mega == True:

        progression_goal= among(6-len(team),len(non_mega_index))
        progression_goal= 100 + progression_goal - progression_goal%100

        return generate_team(window,team,non_mega_roster,requirements,progression,progression_goal)

    teams= []

    progression_goal= among(5-len(team),len(non_mega_index))*len(mega_index)
    if mega == False:
        progression_goal= progression_goal + among(6-len(team),len(non_mega_index))
    progression_goal= 100 + progression_goal - progression_goal%100

    for pokemon in mega_roster:

        team_with_mega= team + [pokemon]

        teams= teams + generate_team(window,team_with_mega,non_mega_roster,requirements,progression,progression_goal)

    if mega == False:
        teams= teams + generate_team(window,team,non_mega_roster,requirements,progression,progression_goal)

    return [teams,progression,progression_goal]



def generate_team(window,team,roster,requirements,progression,progression_goal):
    global pokedex

    index= []
    for pokemon in team + roster:

        type_ = pokemon.type + [pokemon.ability]

        if not type_ in index:

            index= index + [type_]

    types= []
    for pokemon in team:

        i=0

        while pokemon.type + [pokemon.ability] != index[i]:

            i= i+1

        types= types + [i]

    num_teams= generate_team_rec(window,types,index,requirements,progression,progression_goal)

    teams= []
    for num_team in num_teams:

        pokemons= []
        for i in range(6):

            if i < len(team):
                pokemons= pokemons  + [[team[i]]]
            else:
                pokemons= pokemons  + [find_pokemons_with_typing(index[num_team[i]],roster)]

        for pokemon_0 in pokemons[0]:
            for pokemon_1 in pokemons[1]:
                for pokemon_2 in pokemons[2]:
                    for pokemon_3 in pokemons[3]:
                        for pokemon_4 in pokemons[4]:
                            for pokemon_5 in pokemons[5]:

                                teams= teams + [[pokemon_0,pokemon_1,pokemon_2,pokemon_3,pokemon_4,pokemon_5]]

    return teams



def generate_team_rec(window,types,index,requirements,progression,progression_goal):
    
    if len(types) >= 6:

        typings= []
        for i in range(6):
            typings= typings + [index[types[i]]]

        typings_weaknesses_chart= typings_only_weaknesses(typings)

        display_progression(window,progression,progression_goal)

        for i in range(len(requirements)):

            if typings_weaknesses_chart[i] < requirements[i]:
                return []

        return [types]

    valid_types=[]

    for i in range(len(index)):

        if len(types)==0 or i > types[-1]:

            next_types= types + [i]

            valid_types= valid_types + generate_team_rec(window,next_types,index,requirements,progression,progression_goal)

    return valid_types



def find_pokemons_with_typing(typing,roster):
    global pokedex

    pokemons= []
    for pokemon in roster:

        if pokemon.type + [pokemon.ability] == typing:

            pokemons= pokemons + [pokemon]

    return pokemons



def filter_teams(window,teams,roles,progression,progression_goal):

    teams_1=[]
    teams_2= teams

    for role in roles:

        if not (role[1] in ["physical attacker","special attacker","physical wall","special wall"]):

            teams_1= teams_2
            teams_2= []

            for team in teams_1:

                if role_fullfiled(team,role):
                    teams_2= teams_2 + [team]

                else:
                    display_progression(window,progression,progression_goal)

    teams_1= teams_2
    teams_2= []

    for team in teams_1:

        if main_roles_fullfiled(team,roles):
            teams_2= teams_2 + [team]

        else:
            display_progression(window,progression,progression_goal)


    return teams_2



def main_roles_fullfiled(team,roles):

    main_roles= {"physical attacker":None,"special attacker":None,"physical wall":None,"special wall":None}

    A_team= 0
    D_team= 0

    for role in roles:

        if role[1] in main_roles:

            main_roles[role[1]]= role[0]


    for pokemon in team:

        if "physical attacker" in pokemon.properties:
            if "special attacker" in pokemon.properties:
                A_team= A_team + 1
            else:
                main_roles["physical attacker"]= main_roles["physical attacker"] - 1

        elif "special attacker" in pokemon.properties:
            main_roles["special attacker"]= main_roles["special attacker"] - 1


        if "physical wall" in pokemon.properties:
            if "special wall" in pokemon.properties:
                D_team= D_team + 1
            else:
                main_roles["physical wall"]= main_roles["physical wall"] - 1

        elif "special wall" in pokemon.properties:
            main_roles["special wall"]= main_roles["special wall"] - 1

    for role in main_roles:
        if main_roles[role] < 0:
            main_roles[role]=0

    if A_team >= main_roles["physical attacker"] + main_roles["special attacker"]:
        if D_team >= main_roles["physical wall"] + main_roles["special wall"]:
            return True

    return False



def role_fullfiled(team,role):

    candidates_amount= 0
    for pokemon in team:
        if role[1] in pokemon.properties:
            candidates_amount= candidates_amount + 1

    if candidates_amount >= role[0]:
        return True
    else:
        return False
