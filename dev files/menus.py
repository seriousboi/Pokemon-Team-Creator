from pokedex import *
from storage import *
from display import *
from generator import *
import pygame



def choose_team(window):

    teams= open("data/teams.txt","r")
    number= get_team_ammount(teams.read())
    teams.close()
    teams= []
    current_team= -1
    current_page= 0

    for i in range(number):
        teams= teams + [get_team(i)]

    window.fill((150,250,150))
    hitbox_back= text(window,"back",20,(0,0,0),"bottomleft",15,585)
    hitbox_prev= text(window,"<<",20,(0,0,0),"topleft",15,340)
    hitbox_nex= text(window,">>",20,(0,0,0),"topright",215,340)
    hitbox_select= text(window,"select team",20,(0,0,0),"bottomright",1085,585)
    hitbox_page= (75,340,80,30)

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



def menu(window):

    window.fill((150,250,150))
    title= text(window,"Pokemon Team Creator (work in progress)",30,(0,0,0),"center",550,50)
    Turtwig= pygame.image.load("data/icons/wig.png")
    window.blit(Turtwig,(title.x + title.width,title.y + title.height - 30))
    hitbox_builder= text(window,"team builder",20,(0,0,0),"center",550,250)
    hitbox_generator= text(window,"team generator",20,(0,0,0),"center",550,300)
    hitbox_manager= text(window,"team manager",20,(0,0,0),"center",550,350)
    hitbox_chart= text(window,"type chart",20,(0,0,0),"center",550,400)
    hitbox_pokedex= text(window,"pokedex",20,(0,0,0),"center",550,450)

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



def team_builder(window):
    global rosters

    already_saved= False
    current_roster= rosters["OU"]
    current_team= []
    current_page= 0

    window.fill((150,250,150))
    hitbox_back= text(window,"back",20,(0,0,0),"bottomleft",15,585)
    hitbox_roster= text(window,"choose roster",20,(0,0,0),"topleft",15,345)
    hitbox_save= text(window,"save team",20,(0,0,0),"topleft",15,375)
    hitbox_undo= text(window,"undo",20,(0,0,0),"topleft",15,405)

    while True:
        hitbox_choices= display_page(window,current_roster,current_page)
        pygame.draw.rect(window,(150,150,200),(10,10,210,325),0)
        pygame.draw.rect(window,(100,100,100),(10,10,210,325),1)
        display_team(window,current_team,(200,200,250),15,15)
        display_team_weaknesses(window,current_team,225,15)

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
                    hitbox_rosters[roster]= text(window,roster,20,(0,0,0),"topright",1085,15+i*30)
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



def chart(window):

    window.fill((150,250,150))
    hitbox_back= text(window,"back",20,(0,0,0),"bottomleft",15,585)
    hitbox_change_mode= text(window,"change mode",20,(0,0,0),"topleft",15,15)
    current_mode= "defending"

    while True:
        display_chart(window,current_mode)
        pygame.draw.rect(window,(150,250,150),(15,290,100,25),0)
        hitbox_mode= text(window,current_mode,20,(0,0,0),"midleft",15,300)

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



def team_manager(window):
    teams= open("data/teams.txt","r")
    number= get_team_ammount(teams.read())
    teams.close()
    teams= []
    current_team= -1
    current_page= 0

    for i in range(number):
        teams= teams + [get_team(i)]

    window.fill((150,250,150))
    hitbox_back= text(window,"back",20,(0,0,0),"bottomleft",15,585)
    hitbox_prev= text(window,"<<",20,(0,0,0),"topleft",15,340)
    hitbox_nex= text(window,">>",20,(0,0,0),"topright",215,340)
    hitbox_delete= text(window,"delete team",20,(0,0,0),"bottomright",1085,585)
    hitbox_page= (75,340,80,30)

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



def team_generator(window):
    global rosters

    window.fill((150,250,150))
    hitbox_back= text(window,"back",20,(0,0,0),"bottomleft",15,585)
    hitbox_add_team= text(window,"add starting team",20,(0,0,0),"topleft",15,345)
    hitbox_roster= text(window,"choose roster",20,(0,0,0),"topleft",15,375)
    hitbox_generate= text(window,"generate",20,(0,0,0),"midbottom",550,585)
    text(window,"requirements",20,(0,0,0),"midtop",550,10)

    hitboxes= [[],[]]
    for i in range(18):
        pygame.draw.rect(window,(200,200,200),(225+9+36*i,70-30,18,100),0)
        pygame.draw.rect(window,(100,100,100),(225+9+36*i,70-30,18,100),1)
        text(window,"+",20,(100,100,100),"midbottom",225+18+36*i,70)
        text(window,"-",20,(100,100,100),"midtop",225+18+36*i,70+40)
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
        hitbox_mega= text(window,"have a mega: "+mega_state[1],20,(0,0,0),"topleft",15,405)

        hitboxes_roles= []
        for i in range(len(roles)):
            hitboxes_roles= hitboxes_roles + [text(window,roles[i][1]+": "+str(roles[i][0]),20,(0,0,0),"topright",1085,15+30*i)]

        display_team(window,current_team,(200,200,250),15,15)
        display_requirements(window,current_requirements,225,70)

        pygame.display.update()

        event= pygame.event.wait()

        if event.type == pygame.QUIT:
                return "quit"

        if event.type == pygame.MOUSEBUTTONDOWN:

            if hitbox_add_team.collidepoint(event.pos):
                current_team= choose_team(window)
                window.fill((150,250,150))
                text(window,"back",20,(0,0,0),"bottomleft",15,585)
                text(window,"add starting team",20,(0,0,0),"topleft",15,345)
                text(window,"choose roster",20,(0,0,0),"topleft",15,375)
                text(window,"generate",20,(0,0,0),"midbottom",550,585)
                text(window,"requirements",20,(0,0,0),"midtop",550,10)
                for i in range(18):
                    pygame.draw.rect(window,(200,200,200),(225+9+36*i,70-30,18,100),0)
                    pygame.draw.rect(window,(100,100,100),(225+9+36*i,70-30,18,100),1)
                    text(window,"+",20,(100,100,100),"midbottom",225+18+36*i,70)
                    text(window,"-",20,(100,100,100),"midtop",225+18+36*i,70+40)

            elif hitbox_mega.collidepoint(event.pos):
                if mega_state[0]:
                    mega_state= [False,"off"]
                else:
                    mega_state= [True,"on"]

            elif hitbox_back.collidepoint(event.pos):
                    return "menu"

            elif hitbox_generate.collidepoint(event.pos):
                generating_params= [current_team,current_roster,current_requirements,mega_state[0],roles]
                return generating(window,generating_params)

            elif hitbox_roster.collidepoint(event.pos):

                pygame.draw.rect(window,(150,250,150),(880,0,220,600))

                hitbox_rosters= {}
                i=0
                for roster in rosters:
                    hitbox_rosters[roster]= text(window,roster,20,(0,0,0),"topright",1085,15+i*30)
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



def pokedex_info(window):
    global rosters

    current_roster= rosters["all_pokemons"]
    current_page= 0
    current_pokemon= None

    window.fill((150,250,150))
    hitbox_back= text(window,"back",20,(0,0,0),"bottomleft",15,585)
    hitbox_roster= text(window,"choose roster",20,(0,0,0),"midbottom",550,585)

    while True:
        pygame.draw.rect(window,(200,200,250),(15,15,200,40),0)
        pygame.draw.rect(window,(100,100,100),(15,15,200,40),1)
        info_pokemon(window,current_pokemon,"topleft",19,19)
        hitbox_choices= display_page(window,current_roster,current_page)
        display_pokemon_weaknesses(window,current_pokemon,225,15)
        display_pokemon_roles(window,current_pokemon,15,70)




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
                    hitbox_rosters[roster]= text(window,roster,20,(0,0,0),"topright",1085,15+i*30)
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



def main_menu():

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
            state= menu(window)
        if state == "team builder":
            state= team_builder(window)
        if state == "team manager":
            state= team_manager(window)
        if state == "chart":
            state= chart(window)
        if state == "team generator":
            state= team_generator(window)
        if state == "pokedex info":
            state= pokedex_info(window)

    pygame.display.quit()
