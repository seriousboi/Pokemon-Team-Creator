from pokedex import pokedex, rosters
import sys, pygame, math

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



def text(message,size,color,anchor,x,y):
    global window

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

    weaknesses_chart= type_weaknesses(pokedex[pokemon]["type"])


    if pokedex[pokemon]["ability"][0]:
        value= types_values[pokedex[pokemon]["ability"][1]]
        coef= pokedex[pokemon]["ability"][2]
        weaknesses_chart[value]= weaknesses_chart[value]*coef

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


    if typing[2][0]:
        value= types_values[typing[2][1]]
        coef= typing[2][2]
        weaknesses_chart[value]= weaknesses_chart[value]*coef

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



def find(txt,char,start):
    for i in range(start,len(txt)):
        if txt[i] == char:
            return i



def get_team_ammount(txt):

    index= find(txt,"]",2)

    return int(txt[1:index])



def clean_teams():
    teams= open("data/teams.txt","w")
    teams.write("[0].")
    teams.close()



def save_team(team):
    teams= open("data/teams.txt","r")
    txt= teams.read()
    teams.close()

    total= get_team_ammount(txt)

    new_txt= "[" + str(total+1) + "]"

    i_1= find(txt,"]",2)
    i_2= find(txt,".",3)

    new_txt= new_txt + txt[i_1+1:i_2] + "[" + str(len(team))

    for pokemon in team:

        new_txt= new_txt + "," + pokemon

    new_txt= new_txt + "]" + "."

    teams= open("data/teams.txt","w")
    teams.write(new_txt)
    teams.close()

    return total + 1



def delete_team(number):
    teams= open("data/teams.txt","r")
    txt= teams.read()
    teams.close()

    total= get_team_ammount(txt)

    new_txt= "[" + str(total-1) + "]"

    i_1= find(txt,"]",2)
    i_2= find(txt,"[",3)

    for i in range(number):

        i_2= find(txt,"[",i_2+1)

    new_txt= new_txt + txt[i_1+1:i_2]

    if number != total-1:

        i_1= find(txt,"[",i_2+1)

        i_2= find(txt,".",i_2+1)

        new_txt= new_txt + txt[i_1:i_2]

    new_txt= new_txt + "."

    teams= open("data/teams.txt","w")
    teams.write(new_txt)
    teams.close()



def get_team(number):
    teams= open("data/teams.txt","r")
    txt= teams.read()
    teams.close()
    team=[]

    total= get_team_ammount(txt)

    if number >= total:
        return team

    i_1= find(txt,"[",3)

    for i in range(number):

        i_1= find(txt,"[",i_1+1)

    i_2= find(txt,",",i_1+2)

    size= int(txt[i_1+1:i_2])

    for i in range(size):

              i_1= i_2

              if i != size-1:
                  i_2= find(txt,",",i_2+1)
              else:
                  i_2= find(txt,"]",i_2+1)

              team= team + [txt[i_1+1:i_2]]

    return team



def find(txt,char,start):
    for i in range(start,len(txt)):
        if txt[i] == char:
            return i



def str_op(string,op):
    return str(int(string)+op)



def generate_team(team,roster,requirements):
    global pokedex

    index= []
    for pokemon in team + roster:

        type_ = pokedex[pokemon]["type"] + [pokedex[pokemon]["ability"]]

        if not type_ in index:

            index= index + [type_]

    types= []
    for pokemon in team:

        i=0

        while pokedex[pokemon]["type"] + [pokedex[pokemon]["ability"]] != index[i]:

            i= i+1

        types= types + [i]

    num_teams= generate_team_rec(types,index,requirements)

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



def generate_team_rec(types,index,requirements):
    global progression

    if len(types) >= 6:

        typings= []
        for i in range(6):
            typings= typings + [index[types[i]]]

        typings_weaknesses_chart= typings_only_weaknesses(typings)

        display_progression()

        for i in range(len(requirements)):

            if typings_weaknesses_chart[i] < requirements[i]:
                return []

        return [types]

    valid_types=[]

    for i in range(len(index)):

        if len(types)==0 or i > types[-1]:

            next_types= types + [i]

            valid_types= valid_types + generate_team_rec(next_types,index,requirements)

    return valid_types



def generate_team_advanced(team,roster,requirements,mega):
    global progression_goal

    if len(team) + len(roster) < 6:
        return []

    already_mega= False
    for pokemon in team:
        if pokedex[pokemon]["mega"] == True:
            already_mega= True


    non_mega_index=[]
    mega_index=[]
    non_mega_roster= []
    mega_roster= []
    for pokemon in roster:
        if pokedex[pokemon]["mega"] == False:
            non_mega_roster= non_mega_roster + [pokemon]
            type_ = pokedex[pokemon]["type"] + [pokedex[pokemon]["ability"]]
            if not type_ in non_mega_index:
                non_mega_index= non_mega_index + [type_]
        else:
            mega_roster= mega_roster + [pokemon]
            type_ = pokedex[pokemon]["type"] + [pokedex[pokemon]["ability"]]
            if not type_ in mega_index:
                mega_index= mega_index + [type_]

    if already_mega == True:

        progression_goal= among(6-len(team),len(non_mega_index))
        progression_goal= 100 + progression_goal - progression_goal%100

        return generate_team(team,non_mega_roster,requirements)

    teams= []

    progression_goal= among(5-len(team),len(non_mega_index))*len(mega_index)
    if mega == False:
        progression_goal= progression_goal + among(6-len(team),len(non_mega_index))
    progression_goal= 100 + progression_goal - progression_goal%100

    for pokemon in mega_roster:

        team_with_mega= team + [pokemon]

        teams= teams + generate_team(team_with_mega,non_mega_roster,requirements)

    if mega == False:
        teams= teams + generate_team(team,non_mega_roster,requirements)

    return teams



def display_progression():
    global window, progression, progression_goal

    pygame.event.pump()

    progression= progression + 1

    if progression%(progression_goal/100) == 0:

        window.fill((150,250,150))

        advancement= int(100*progression/progression_goal)

        text(str(advancement)+"%",40,(0,0,0),"center",550,300)

        pygame.display.update()



def find_pokemons_with_typing(typing,roster):
    global pokedex

    pokemons= []
    for pokemon in roster:

        if pokedex[pokemon]["type"] + [pokedex[pokemon]["ability"]] == typing:

            pokemons= pokemons + [pokemon]

    return pokemons



def filter_teams(teams,roles):

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
                    display_progression()

    teams_1= teams_2
    teams_2= []

    for team in teams_1:

        if main_roles_fullfiled(team,roles):
            teams_2= teams_2 + [team]

        else:
            display_progression()


    return teams_2



def main_roles_fullfiled(team,roles):
    global pokedex

    main_roles= {"physical attacker":None,"special attacker":None,"physical wall":None,"special wall":None}

    A_team= 0
    D_team= 0

    for role in roles:

        if role[1] in main_roles:

            main_roles[role[1]]= role[0]


    for pokemon in team:

        if pokedex[pokemon]["physical attacker"]:
            if pokedex[pokemon]["special attacker"]:
                A_team= A_team + 1
            else:
                main_roles["physical attacker"]= main_roles["physical attacker"] - 1

        elif pokedex[pokemon]["special attacker"]:
            main_roles["special attacker"]= main_roles["special attacker"] - 1


        if pokedex[pokemon]["physical wall"]:
            if pokedex[pokemon]["special wall"]:
                D_team= D_team + 1
            else:
                main_roles["physical wall"]= main_roles["physical wall"] - 1

        elif pokedex[pokemon]["special wall"]:
            main_roles["special wall"]= main_roles["special wall"] - 1

    for role in main_roles:
        if main_roles[role] < 0:
            main_roles[role]=0

    if A_team >= main_roles["physical attacker"] + main_roles["special attacker"]:
        if D_team >= main_roles["physical wall"] + main_roles["special wall"]:
            return True

    return False



def role_fullfiled(team,role):
    global pokedex

    i= 0

    for pokemon in team:
        for key in role[2]:
            if pokedex[pokemon][key]:
                i= i + 1
                break
        if i >= role[0]:
            return True

    return False


def info_pokemon(pokemon,anchor,x,y):
    global window, pokedex

    if pokemon == None:
        return

    pokemon= pokedex[pokemon]


    if anchor == "topleft":

        name_area= text(pokemon["name"],17,(0,0,0),"topleft",x,y+13)

        try:
            icon_name= "data/pokemons/" + pokemon["ID"] + ".png"
            icon_image= pygame.image.load(icon_name)
        except:
            icon_image= pygame.image.load("data/pokemons/unknown.png")
        window.blit(icon_image,(x+155,y+4))

        type_name= "data/types/" + pokemon["type"][0] + "IC.GIF"
        type_image= pygame.image.load(type_name)
        window.blit(type_image,(x,y))

        if pokemon["type"][1] != "none":

            type_name= "data/types/" + pokemon["type"][1] + "IC.GIF"
            type_image= pygame.image.load(type_name)
            window.blit(type_image,(x+35,y))

            if pokemon["ability"][0]:
                text("["+pokemon["ability"][3]+"]",12,(0,0,0),"topleft",x+70,y)
        else:
            if pokemon["ability"][0]:
                text("["+pokemon["ability"][3]+"]",12,(0,0,0),"topleft",x+35,y)

    info_area= name_area
    info_area.height= info_area.height+ 15
    info_area.y= info_area.y -15

    return info_area



def display_team(team,color,x,y):
    global window

    hitboxes= []

    for i in range(6):
        hitboxes= hitboxes + [pygame.draw.rect(window,color,(x,y+i*55,200,40),0)]
        pygame.draw.rect(window,(100,100,100),(x,y+i*55,200,40),1)

    for i in range(len(team)):
        [info_pokemon(team[i],"topleft",x+4,y+4+i*55)]

    return hitboxes



def display_page(roster,page):
    global window

    hitboxes= []
    pygame.draw.rect(window,(150,250,150),(880,10,210,580),0)
    text("page "+str(page+1),20,(0,0,0),"midbottom",985,585)
    hitboxes= hitboxes + [text("<<",20,(0,0,0),"bottomleft",885,585)]
    hitboxes= hitboxes + [text(">>",20,(0,0,0),"bottomright",1085,585)]

    for i in range(10):
        hitbox= pygame.draw.rect(window,(200,200,200),(885,15+i*55,200,40),0)
        pygame.draw.rect(window,(100,100,100),(885,15+i*55,200,40),1)

        if i+10*(page) < len(roster):
            hitboxes= hitboxes + [hitbox]

    for i in range((page)*10,min(10+(page)*10,len(roster))):
        info_pokemon(roster[i],"topleft",889,19+(i%10)*55)

    return hitboxes



def display_team_weaknesses(team,x,y):
    global window, existing_types, types_values

    weaknesses_chart= team_weaknesses(team)
    i= 0

    for type_name in existing_types:

        if type_name != "none":

            pygame.draw.rect(window,(200,200,200),(x+i*36,y,36,40),0)

            type_image= pygame.image.load("data/types/" + type_name + "IC.GIF")
            window.blit(type_image,(x+2+i*36,y+4))
            if weaknesses_chart[types_values[type_name]] >= 2:
                color= [50,150,50]
            elif weaknesses_chart[types_values[type_name]] == 1:
                color= [100,200,100]
            elif weaknesses_chart[types_values[type_name]] == 0:
                color= [250,255,250]
            elif weaknesses_chart[types_values[type_name]] == -1:
                color= [250,150,100]
            elif weaknesses_chart[types_values[type_name]] <= -2:
                color= [200,50,50]

            text(str(weaknesses_chart[types_values[type_name]]),20,color,"center",x+20+i*36,y+28)
            i= i+1

    pygame.draw.rect(window,(100,100,100),(x,y,i*36,40),1)



def display_pokemon_weaknesses(pokemon,x,y):
    global window, existing_types, types_values

    if pokemon == None:
        weaknesses_chart= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    else:
        weaknesses_chart= pokemon_weaknesses(pokemon)

    i= 0

    for type_name in existing_types:

        if type_name != "none":

            if weaknesses_chart[types_values[type_name]] == 0:
                color_1= [80,80,80]
                color_2= [230,230,230]
                coef= "0"
            elif weaknesses_chart[types_values[type_name]] == 0.25:
                color_1= [50,220,120]
                color_2= [0,0,0]
                coef= "1/4"
            elif weaknesses_chart[types_values[type_name]] == 0.5:
                color_1= [120,250,120]
                color_2= [0,0,0]
                coef= "1/2"
            elif weaknesses_chart[types_values[type_name]] == 1:
                color_1= [200,200,200]
                color_2= [0,0,0]
                coef= "1"
            elif weaknesses_chart[types_values[type_name]] == 2:
                color_1= [250,120,120]
                color_2= [0,0,0]
                coef= "2"
            elif weaknesses_chart[types_values[type_name]] == 4:
                color_1= [200,50,50]
                color_2= [0,0,0]
                coef= "4"

            pygame.draw.rect(window,(200,200,200),(x+i*36,y,36,20),0)
            pygame.draw.rect(window,color_1,(x+i*36,y+20,36,20),0)
            pygame.draw.line(window,(100,100,100),(x+35+i*36,y),(x+35+i*36,y+39))
            type_image= pygame.image.load("data/types/" + type_name + "IC.GIF")
            window.blit(type_image,(x+2+i*36,y+2))
            text(coef,17,color_2,"center",x+20+i*36,y+28)
            i= i+1

    pygame.draw.rect(window,(100,100,100),(x,y,i*36,40),1)
    pygame.draw.line(window,(100,100,100),(x,y+19),(x-1+i*36,y+19))



def display_pokemon_roles(pokemon,x,y):
    global pokedex

    pygame.draw.rect(window,(150,250,150),(x,y,200,250),0)

    if pokemon == None:
        return

    pokemon= pokedex[pokemon]

    potential_roles= [['physical attacker','physical attacker'],['special attacker','special attacker'],['physical wall','physical wall'],['special wall','special wall'],['stealth rock','rock setter'],['defog','defoger'],['rapid spin','spiner'],['priority','priority user']]

    i= 0
    for potential_role in potential_roles:

        if pokemon[potential_role[0]]:
            text(potential_role[1],20,(0,0,0),"topleft",x,y+i*30)
            i= i + 1








def display_requirements(requirements,x,y):
    global window, existing_types, types_values


    i= 0

    for type_name in existing_types:

        if type_name != "none":

            pygame.draw.rect(window,(200,200,200),(x+i*36,y,36,40),0)

            type_image= pygame.image.load("data/types/" + type_name + "IC.GIF")
            window.blit(type_image,(x+2+i*36,y+4))

            coef= requirements[i+1]

            if coef >= 2:
                color= [50,150,50]
            elif coef == 1:
                color= [100,200,100]
            elif coef == 0:
                color= [250,255,250]
            elif coef == -1:
                color= [250,150,100]
            elif coef <= -2:
                color= [200,50,50]

            text(str(coef),20,color,"center",x+20+i*36,y+28)
            i= i+1

    pygame.draw.rect(window,(100,100,100),(x,y,i*36,40),1)



def display_chart(mode):
    global window, existing_types, types_values, type_chart

    pygame.draw.rect(window,(200,200,200),(200,15,684,570),0)
    i=0

    for type_name in existing_types:
        if type_name != "none":
            type_image= pygame.image.load("data/types/" + type_name + "ic.gif")
            window.blit(type_image,(202+(i+1)*36,23))
            window.blit(type_image,(202,23+(i+1)*30))
            i=i+1

    for i in range(20):
        pygame.draw.line(window,(100,100,100),(200,15+i*30),(884,15+i*30))
        pygame.draw.line(window,(100,100,100),(200+i*36,15),(200+i*36,585))

    for type_1 in existing_types:
        for type_2 in existing_types:
            c1= types_values[type_1]
            c2= types_values[type_2]

            coef= type_chart[c1][c2]

            if coef != 1:
                if mode == "defending":
                    if coef == 2:
                        color_cell= (250,120,120)
                        color_txt= (0,0,0)
                    elif coef == 0.5:
                        color_cell= (120,250,120)
                        color_txt= (0,0,0)
                    elif coef == 0:
                        color_cell= (80,80,80)
                        color_txt= (230,230,230)
                    pygame.draw.rect(window,color_cell,(201+36*c2,16+30*c1,35,29),0)
                    text(str(coef),20,color_txt,"center",218+36*c2,30+30*c1)

                if mode == "attacking":
                    if coef == 2:
                        color_cell= (120,250,120)
                        color_txt= (0,0,0)
                    elif coef == 0.5:
                        color_cell= (250,120,120)
                        color_txt= (0,0,0)
                    elif coef == 0:
                        color_cell= (80,80,80)
                        color_txt= (230,230,230)
                    pygame.draw.rect(window,color_cell,(201+36*c1,16+30*c2,35,29),0)
                    text(str(coef),20,color_txt,"center",218+36*c1,30+30*c2)



def display_teams(teams,page,team):
    global window

    hitboxes= []

    for i in range(5):

        if i+5*page < len(teams):

            if i == team:
                color_1= (200,200,250)
                color_2= (150,150,200)
            else:
                color_1= (200,200,200)
                color_2= (150,150,150)

            hitbox= pygame.draw.rect(window,color_2,(10+i*215,10,210,325),0)
            pygame.draw.rect(window,(100,100,100),(10+i*215,10,210,325),1)
            display_team(teams[i+5*(page)],color_1,15+i*215,15)
            hitboxes= hitboxes + [hitbox]

        else:
            pygame.draw.rect(window,(150,150,150),(10+i*215,10,210,325),0)
            pygame.draw.rect(window,(100,100,100),(10+i*215,10,210,325),1)
            display_team([],(200,200,200),15+i*215,15)

    return hitboxes



def choose_team():
    global window
    teams= open("data/teams.txt","r")
    number= get_team_ammount(teams.read())
    teams.close()
    teams= []
    current_team= -1
    current_page= 0

    for i in range(number):
        teams= teams + [get_team(i)]

    window.fill((150,250,150))
    hitbox_back= text("back",20,(0,0,0),"bottomleft",15,585)
    hitbox_prev= text("<<",20,(0,0,0),"topleft",15,340)
    hitbox_nex= text(">>",20,(0,0,0),"topright",215,340)
    hitbox_select= text("select team",20,(0,0,0),"bottomright",1085,585)
    hitbox_page= (75,340,80,30)

    while True:
        hitboxes= display_teams(teams,current_page,current_team)
        pygame.draw.rect(window,(150,250,150),hitbox_page,0)
        hitbox_page= text("page "+str(current_page+1),20,(0,0,0),"midtop",115,340)

        if current_team != -1:
            display_team_weaknesses(teams[current_team+current_page*5],330,340)
        else:
            display_team_weaknesses([],330,340)

        pygame.display.update()

        event= pygame.event.wait()

        if event.type == pygame.QUIT:
                return "quit"

        if event.type == pygame.MOUSEBUTTONDOWN:

            if hitbox_back.collidepoint(event.pos):
                    return []

            elif hitbox_prev.collidepoint(event.pos) and len(teams)!=0:
                current_page= (current_page-1)%(((len(teams)-1)//5)+1)
                current_team= -1

            elif hitbox_nex.collidepoint(event.pos) and len(teams)!=0:
                current_page= (current_page+1)%(((len(teams)-1)//5)+1)
                current_team= -1

            elif hitbox_select.collidepoint(event.pos) and current_team != -1 and len(teams[current_team+current_page*5]) < 6:
                return teams[current_team+current_page*5]

            else:
                for i in range(len(hitboxes)):

                    if hitboxes[i].collidepoint(event.pos):
                        current_team= i



def menu():
    global window

    window.fill((150,250,150))
    title= text("Pokemon Team Creator (work in progress)",30,(0,0,0),"center",550,50)
    Turtwig= pygame.image.load("data/icons/wig.png")
    window.blit(Turtwig,(title.x + title.width,title.y + title.height - 30))
    hitbox_builder= text("team builder",20,(0,0,0),"center",550,250)
    hitbox_generator= text("team generator",20,(0,0,0),"center",550,300)
    hitbox_manager= text("team manager",20,(0,0,0),"center",550,350)
    hitbox_chart= text("type chart",20,(0,0,0),"center",550,400)
    hitbox_pokedex= text("pokedex",20,(0,0,0),"center",550,450)

    pygame.display.update()

    while True:
        event= pygame.event.wait()

        if event.type == pygame.QUIT:
            return "quit"

        if event.type == pygame.MOUSEBUTTONDOWN:

            if hitbox_builder.collidepoint(event.pos):
                return "team builder"

            elif hitbox_manager.collidepoint(event.pos):
                return "team manager"

            elif hitbox_generator.collidepoint(event.pos):
                return "team generator"

            elif hitbox_chart.collidepoint(event.pos):
                return "chart"

            elif hitbox_pokedex.collidepoint(event.pos):
                return "pokedex info"



def team_builder():
    global window, rosters


    already_saved= False
    current_roster= rosters["OU"]
    current_team= []
    current_page= 0

    window.fill((150,250,150))
    hitbox_back= text("back",20,(0,0,0),"bottomleft",15,585)
    hitbox_roster= text("choose roster",20,(0,0,0),"topleft",15,345)
    hitbox_save= text("save team",20,(0,0,0),"topleft",15,375)
    hitbox_undo= text("undo",20,(0,0,0),"topleft",15,405)

    while True:
        hitbox_choices= display_page(current_roster,current_page)
        pygame.draw.rect(window,(150,150,200),(10,10,210,325),0)
        pygame.draw.rect(window,(100,100,100),(10,10,210,325),1)
        display_team(current_team,(200,200,250),15,15)
        display_team_weaknesses(current_team,225,15)

        pygame.display.update()

        event= pygame.event.wait()

        if event.type == pygame.QUIT:
            return "quit"

        if event.type == pygame.MOUSEBUTTONDOWN:

            if hitbox_back.collidepoint(event.pos):
                return "menu"

            elif hitbox_save.collidepoint(event.pos) and len(current_team) != 0 and already_saved == False:
                save_team(current_team)
                already_saved= True

            elif hitbox_choices[0].collidepoint(event.pos):
                current_page= (current_page-1)%(((len(current_roster)-1)//10)+1)

            elif hitbox_choices[1].collidepoint(event.pos):
                current_page= (current_page+1)%(((len(current_roster)-1)//10)+1)

            elif hitbox_undo.collidepoint(event.pos) and len(current_team) > 0:
                current_team.pop()

            elif hitbox_roster.collidepoint(event.pos):
                pygame.draw.rect(window,(150,250,150),(880,10,210,580),0)

                hitbox_rosters= {}
                i=0
                for roster in rosters:
                    hitbox_rosters[roster]= text(roster,20,(0,0,0),"topright",1085,15+i*30)
                    i= i+1

                pygame.display.update()

                event= pygame.event.wait()

                if event.type == pygame.QUIT:
                    return "quit"

                for roster in rosters:

                    if hitbox_rosters[roster].collidepoint(event.pos):

                        current_roster= rosters[roster]

            elif len(current_team) < 6:

                for i in range(2,len(hitbox_choices)):

                    if hitbox_choices[i].collidepoint(event.pos):
                        current_team= current_team + [current_roster[i-2+current_page*10]]
                        already_saved= False



def chart():
    global window

    window.fill((150,250,150))
    hitbox_back= text("back",20,(0,0,0),"bottomleft",15,585)
    hitbox_change_mode= text("change mode",20,(0,0,0),"topleft",15,15)
    current_mode= "defending"

    while True:
        display_chart(current_mode)
        pygame.draw.rect(window,(150,250,150),(15,290,100,25),0)
        hitbox_mode= text(current_mode,20,(0,0,0),"midleft",15,300)

        pygame.display.update()

        event= pygame.event.wait()

        if event.type == pygame.QUIT:
                return "quit"

        if event.type == pygame.MOUSEBUTTONDOWN:

            if hitbox_back.collidepoint(event.pos):
                    return "menu"
            elif hitbox_change_mode.collidepoint(event.pos):
                if current_mode == "defending":
                    current_mode= "attacking"
                else:
                    current_mode= "defending"



def team_manager():
    global window
    teams= open("data/teams.txt","r")
    number= get_team_ammount(teams.read())
    teams.close()
    teams= []
    current_team= -1
    current_page= 0

    for i in range(number):
        teams= teams + [get_team(i)]

    window.fill((150,250,150))
    hitbox_back= text("back",20,(0,0,0),"bottomleft",15,585)
    hitbox_prev= text("<<",20,(0,0,0),"topleft",15,340)
    hitbox_nex= text(">>",20,(0,0,0),"topright",215,340)
    hitbox_delete= text("delete team",20,(0,0,0),"bottomright",1085,585)
    hitbox_page= (75,340,80,30)

    while True:
        hitboxes= display_teams(teams,current_page,current_team)
        pygame.draw.rect(window,(150,250,150),hitbox_page,0)
        hitbox_page= text("page "+str(current_page+1),20,(0,0,0),"midtop",115,340)

        if current_team != -1:
            display_team_weaknesses(teams[current_team+current_page*5],330,340)
        else:
            display_team_weaknesses([],330,340)

        pygame.display.update()

        event= pygame.event.wait()

        if event.type == pygame.QUIT:
                return "quit"

        if event.type == pygame.MOUSEBUTTONDOWN:

            if hitbox_back.collidepoint(event.pos):
                    return "menu"

            elif hitbox_prev.collidepoint(event.pos) and len(teams)!=0:
                current_page= (current_page-1)%(((len(teams)-1)//5)+1)
                current_team= -1

            elif hitbox_nex.collidepoint(event.pos) and len(teams)!=0:
                current_page= (current_page+1)%(((len(teams)-1)//5)+1)
                current_team= -1

            elif hitbox_delete.collidepoint(event.pos) and current_team != -1:
                delete_team(current_team+current_page*5)
                del teams[current_team+current_page*5]
                current_team= -1

            else:
                for i in range(len(hitboxes)):

                    if hitboxes[i].collidepoint(event.pos):
                        current_team= i



def team_generator():
    global window, rosters, generating_params

    window.fill((150,250,150))
    hitbox_back= text("back",20,(0,0,0),"bottomleft",15,585)
    hitbox_add_team= text("add starting team",20,(0,0,0),"topleft",15,345)
    hitbox_roster= text("choose roster",20,(0,0,0),"topleft",15,375)
    hitbox_generate= text("generate",20,(0,0,0),"midbottom",550,585)
    text("requirements",20,(0,0,0),"midtop",550,10)

    hitboxes= [[],[]]
    for i in range(18):
        pygame.draw.rect(window,(200,200,200),(225+9+36*i,70-30,18,100),0)
        pygame.draw.rect(window,(100,100,100),(225+9+36*i,70-30,18,100),1)
        text("+",20,(100,100,100),"midbottom",225+18+36*i,70)
        text("-",20,(100,100,100),"midtop",225+18+36*i,70+40)
        hitboxes[0]= hitboxes[0] + [pygame.Rect(225+9+36*i,70-30,18,30)]
        hitboxes[1]= hitboxes[1] + [pygame.Rect(225+9+36*i,110,18,30)]

    current_requirements= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    current_roster= rosters["OU"]
    hitbox_mega= (15,405,200,30)
    stealth_rock_state= [False,"off"]
    anti_hazard_state= [False,"off"]
    priority_state= [False,"off"]
    mega_state= [False,"off"]
    roles= [[0,"physical attacker",["physical attacker"]],[0,"special attacker",["special attacker"]],[0,"physical wall",["physical wall"]],[0,"special wall",["special wall"]],[0,'rock setter',["stealth rock"]],[0,"hazard remover",["defog","rapid spin"]],[0,"priority user",["priority"]]]
    current_team= []




    while True:

        pygame.draw.rect(window,(150,150,200),(10,10,210,325),0)
        pygame.draw.rect(window,(100,100,100),(10,10,210,325),1)
        pygame.draw.rect(window,(150,250,150),(880,10,210,580),0)
        pygame.draw.rect(window,(150,250,150),hitbox_mega,0)
        pygame.draw.rect(window,(150,250,150),(880,0,220,600))
        hitbox_mega= text("have a mega: "+mega_state[1],20,(0,0,0),"topleft",15,405)

        hitboxes_roles= []
        for i in range(len(roles)):
            hitboxes_roles= hitboxes_roles + [text(roles[i][1]+": "+str(roles[i][0]),20,(0,0,0),"topright",1085,15+30*i)]

        display_team(current_team,(200,200,250),15,15)
        display_requirements(current_requirements,225,70)

        pygame.display.update()

        event= pygame.event.wait()

        if event.type == pygame.QUIT:
                return "quit"

        if event.type == pygame.MOUSEBUTTONDOWN:

            if hitbox_add_team.collidepoint(event.pos):
                current_team= choose_team()
                window.fill((150,250,150))
                text("back",20,(0,0,0),"bottomleft",15,585)
                text("add starting team",20,(0,0,0),"topleft",15,345)
                text("choose roster",20,(0,0,0),"topleft",15,375)
                text("generate",20,(0,0,0),"midbottom",550,585)
                text("requirements",20,(0,0,0),"midtop",550,10)
                for i in range(18):
                    pygame.draw.rect(window,(200,200,200),(225+9+36*i,70-30,18,100),0)
                    pygame.draw.rect(window,(100,100,100),(225+9+36*i,70-30,18,100),1)
                    text("+",20,(100,100,100),"midbottom",225+18+36*i,70)
                    text("-",20,(100,100,100),"midtop",225+18+36*i,70+40)

            elif hitbox_mega.collidepoint(event.pos):
                if mega_state[0]:
                    mega_state= [False,"off"]
                else:
                    mega_state= [True,"on"]

            elif hitbox_back.collidepoint(event.pos):
                    return "menu"

            elif hitbox_generate.collidepoint(event.pos):
                generating_params= [current_team,current_roster,current_requirements,mega_state[0],roles]
                return "generating"

            elif hitbox_roster.collidepoint(event.pos):

                pygame.draw.rect(window,(150,250,150),(880,0,220,600))

                hitbox_rosters= {}
                i=0
                for roster in rosters:
                    hitbox_rosters[roster]= text(roster,20,(0,0,0),"topright",1085,15+i*30)
                    i= i+1

                pygame.display.update()

                event= pygame.event.wait()

                if event.type == pygame.QUIT:
                    return "quit"

                for roster in rosters:

                    if hitbox_rosters[roster].collidepoint(event.pos):

                        current_roster= rosters[roster]

            else:
                for i in range(len(hitboxes_roles)):
                    if hitboxes_roles[i].collidepoint(event.pos):
                        roles[i][0]= (roles[i][0] + 1)%7

                for i in range(18):
                    if hitboxes[0][i].collidepoint(event.pos) and current_requirements[i+1] < 6:
                        current_requirements[i+1]= current_requirements[i+1] + 1
                    elif hitboxes[1][i].collidepoint(event.pos) and current_requirements[i+1] > -6:
                        current_requirements[i+1]= current_requirements[i+1] - 1



def generating():
    global generating_params, progression, progression_goal

    window.fill((150,250,150))
    text("starting",40,(0,0,0),"center",550,300)
    pygame.display.update()

    progression= 0

    team= generating_params[0]
    roster= generating_params[1]
    requirements= generating_params[2]
    mega= generating_params[3]
    roles= generating_params[4]
    teams= generate_team_advanced(team,roster,requirements,mega)

    teams= filter_teams(teams,roles)

    window.fill((150,250,150))
    hitbox_back= text("back",20,(0,0,0),"bottomleft",15,585)
    hitbox_prev= text("<<",20,(0,0,0),"topleft",15,340)
    hitbox_nex= text(">>",20,(0,0,0),"topright",215,340)
    hitbox_save= text("save team",20,(0,0,0),"bottomright",1085,585)
    hitbox_page= (75,340,80,30)

    current_team= -1
    current_page= 0


    while True:
        hitboxes= display_teams(teams,current_page,current_team)
        pygame.draw.rect(window,(150,250,150),hitbox_page,0)
        hitbox_page= text("page "+str(current_page+1),20,(0,0,0),"midtop",115,340)

        if current_team != -1:
            display_team_weaknesses(teams[current_team+current_page*5],330,340)
        else:
            display_team_weaknesses([],330,340)

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



def pokedex_info():
    global rosters

    current_roster= rosters["all_pokemons"]
    current_page= 0
    current_pokemon= None

    window.fill((150,250,150))
    hitbox_back= text("back",20,(0,0,0),"bottomleft",15,585)
    hitbox_roster= text("choose roster",20,(0,0,0),"midbottom",550,585)

    while True:
        pygame.draw.rect(window,(200,200,250),(15,15,200,40),0)
        pygame.draw.rect(window,(100,100,100),(15,15,200,40),1)
        info_pokemon(current_pokemon,"topleft",19,19)
        hitbox_choices= display_page(current_roster,current_page)
        display_pokemon_weaknesses(current_pokemon,225,15)
        display_pokemon_roles(current_pokemon,15,70)




        pygame.display.update()

        event= pygame.event.wait()

        if event.type == pygame.QUIT:
                return "quit"

        if event.type == pygame.MOUSEBUTTONDOWN:

            if hitbox_back.collidepoint(event.pos):
                    return "menu"

            elif hitbox_choices[0].collidepoint(event.pos):
                current_page= (current_page-1)%(((len(current_roster)-1)//10)+1)

            elif hitbox_choices[1].collidepoint(event.pos):
                current_page= (current_page+1)%(((len(current_roster)-1)//10)+1)

            elif hitbox_roster.collidepoint(event.pos):
                pygame.draw.rect(window,(150,250,150),(880,10,210,580),0)

                hitbox_rosters= {}
                i=0
                for roster in rosters:
                    hitbox_rosters[roster]= text(roster,20,(0,0,0),"topright",1085,15+i*30)
                    i= i+1

                pygame.display.update()

                event= pygame.event.wait()

                if event.type == pygame.QUIT:
                    return "quit"

                for roster in rosters:

                    if hitbox_rosters[roster].collidepoint(event.pos):

                        current_roster= rosters[roster]

            else:
                for i in range(2,len(hitbox_choices)):

                    if hitbox_choices[i].collidepoint(event.pos):
                        current_pokemon= current_roster[i-2+current_page*10]




def main():
    global window
    pygame.init()
    window = pygame.display.set_mode((1100,600))
    Turtwig= pygame.image.load("data/icons/wig.png")
    pygame.display.set_icon(Turtwig)
    pygame.display.set_caption("Pokemon Team Creator (work in progress)")
    pygame.event.set_blocked(None)
    pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN,pygame.QUIT])

    state= "menu"

    while state != "quit":

        if state == "menu":
            state= menu()
        if state == "team builder":
            state= team_builder()
        if state == "team manager":
            state= team_manager()
        if state == "chart":
            state= chart()
        if state == "team generator":
            state= team_generator()
        if state == "generating":
            state= generating()
        if state == "pokedex info":
            state= pokedex_info()

    pygame.display.quit()



main()
