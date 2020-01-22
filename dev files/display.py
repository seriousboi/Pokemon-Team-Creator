from pokedex import *
from calculus import *
import sys, pygame



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



def info_pokemon(window,pokemon,anchor,x,y):
    global pokedex

    if pokemon == None:
        return

    pokemon= pokedex[pokemon]


    if anchor == "topleft":

        name_area= text(window,pokemon["name"],17,(0,0,0),"topleft",x,y+13)

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
                text(window,"["+pokemon["ability"][3]+"]",12,(0,0,0),"topleft",x+70,y)
        else:
            if pokemon["ability"][0]:
                text(window,"["+pokemon["ability"][3]+"]",12,(0,0,0),"topleft",x+35,y)

    info_area= name_area
    info_area.height= info_area.height+ 15
    info_area.y= info_area.y -15

    return info_area



def info_pokemon(window,pokemon,anchor,x,y):
    global pokedex

    if pokemon == None:
        return

    pokemon= pokedex[pokemon]


    if anchor == "topleft":

        name_area= text(window,pokemon["name"],17,(0,0,0),"topleft",x,y+13)

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
                text(window,"["+pokemon["ability"][3]+"]",12,(0,0,0),"topleft",x+70,y)
        else:
            if pokemon["ability"][0]:
                text(window,"["+pokemon["ability"][3]+"]",12,(0,0,0),"topleft",x+35,y)

    info_area= name_area
    info_area.height= info_area.height+ 15
    info_area.y= info_area.y -15

    return info_area



def display_team(window,team,color,x,y):

    hitboxes= []

    for i in range(6):
        hitboxes= hitboxes + [pygame.draw.rect(window,color,(x,y+i*55,200,40),0)]
        pygame.draw.rect(window,(100,100,100),(x,y+i*55,200,40),1)

    for i in range(len(team)):
        [info_pokemon(window,team[i],"topleft",x+4,y+4+i*55)]

    return hitboxes



def display_page(window,roster,page):

    hitboxes= []
    pygame.draw.rect(window,(150,250,150),(880,10,210,580),0)
    text(window,"page "+str(page+1),20,(0,0,0),"midbottom",985,585)
    hitboxes= hitboxes + [text(window,"<<",20,(0,0,0),"bottomleft",885,585)]
    hitboxes= hitboxes + [text(window,">>",20,(0,0,0),"bottomright",1085,585)]

    for i in range(10):
        hitbox= pygame.draw.rect(window,(200,200,200),(885,15+i*55,200,40),0)
        pygame.draw.rect(window,(100,100,100),(885,15+i*55,200,40),1)

        if i+10*(page) < len(roster):
            hitboxes= hitboxes + [hitbox]

    for i in range((page)*10,min(10+(page)*10,len(roster))):
        info_pokemon(window,roster[i],"topleft",889,19+(i%10)*55)

    return hitboxes



def display_team_weaknesses(window,team,x,y):
    global existing_types, types_values

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

            text(window,str(weaknesses_chart[types_values[type_name]]),20,color,"center",x+20+i*36,y+28)
            i= i+1

    pygame.draw.rect(window,(100,100,100),(x,y,i*36,40),1)



def display_pokemon_weaknesses(window,pokemon,x,y):
    global existing_types, types_values

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
            text(window,coef,17,color_2,"center",x+20+i*36,y+28)
            i= i+1

    pygame.draw.rect(window,(100,100,100),(x,y,i*36,40),1)
    pygame.draw.line(window,(100,100,100),(x,y+19),(x-1+i*36,y+19))



def display_pokemon_roles(window,pokemon,x,y):
    global pokedex

    pygame.draw.rect(window,(150,250,150),(x,y,200,250),0)

    if pokemon == None:
        return

    pokemon= pokedex[pokemon]

    potential_roles= [['physical attacker','physical attacker'],['special attacker','special attacker'],['physical wall','physical wall'],['special wall','special wall'],['stealth rock','rock setter'],['defog','defoger'],['rapid spin','spiner'],['priority','priority user']]

    i= 0
    for potential_role in potential_roles:

        if pokemon[potential_role[0]]:
            text(window,potential_role[1],20,(0,0,0),"topleft",x,y+i*30)
            i= i + 1








def display_requirements(window,requirements,x,y):
    global existing_types, types_values


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

            text(window,str(coef),20,color,"center",x+20+i*36,y+28)
            i= i+1

    pygame.draw.rect(window,(100,100,100),(x,y,i*36,40),1)



def display_chart(window,mode):
    global existing_types, types_values, type_chart

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
                    text(window,str(coef),20,color_txt,"center",218+36*c2,30+30*c1)

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
                    text(window,str(coef),20,color_txt,"center",218+36*c1,30+30*c2)



def display_teams(window,teams,page,team):

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
            display_team(window,teams[i+5*(page)],color_1,15+i*215,15)
            hitboxes= hitboxes + [hitbox]

        else:
            pygame.draw.rect(window,(150,150,150),(10+i*215,10,210,325),0)
            pygame.draw.rect(window,(100,100,100),(10+i*215,10,210,325),1)
            display_team(window,[],(200,200,200),15+i*215,15)

    return hitboxes
