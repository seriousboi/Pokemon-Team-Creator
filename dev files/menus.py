from pokedex import *
from storage import *
from display import *
from generator import *
from rosters import *
from charts import *
import pygame



def menu(window):

    window.fill((150,250,150))
    title= text(window,"Pokemon Team Creator (work in progress)",30,(0,0,0),"center",550,50)
    Turtwig= pygame.image.load("data/icons/wig.png")
    window.blit(Turtwig,(title.x + title.width,title.y + title.height - 30))
    hitbox_builder= text(window,"team builder",20,(0,0,0),"center",550,200)
    hitbox_generator= text(window,"team generator",20,(0,0,0),"center",550,250)
    hitbox_manager= text(window,"team manager",20,(0,0,0),"center",550,300)
    hitbox_chart= text(window,"type chart",20,(0,0,0),"center",550,350)
    hitbox_pokedex= text(window,"pokedex",20,(0,0,0),"center",550,400)
    hitbox_options= text(window,"options",20,(0,0,0),"center",550,450)

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

            elif hitbox_options.collidepoint(event.pos):
                return "options"



def team_builder(window):
    rosters= get_rosters()

    already_saved= False
    current_roster= rosters[0]
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
                current_page= (current_page-1)%(((len(current_roster.pokemon_list)-1)//10)+1)

            elif hitbox_choices[1].collidepoint(event.pos):
                current_page= (current_page+1)%(((len(current_roster.pokemon_list)-1)//10)+1)

            elif hitbox_undo.collidepoint(event.pos) and len(current_team) > 0:
                current_team.pop()

            elif hitbox_roster.collidepoint(event.pos):
                current_roster= choose_roster(window,rosters,current_roster)

            elif len(current_team) < 6:

                for i in range(2,len(hitbox_choices)):

                    if hitbox_choices[i].collidepoint(event.pos):
                        current_team= current_team + [current_roster.pokemon_list[i-2+current_page*10]]
                        already_saved= False



def choose_roster(window,rosters,current_roster):
    rosters_amount= len(rosters)
    pages_amount= 1+(rosters_amount-1)//18
    choosing_roster= True
    page= 0
    while choosing_roster:
        hitboxes= display_rosters(window,rosters,page)
        hitboxes_amount= len(hitboxes)-2
        pygame.display.update()

        event= pygame.event.wait()

        if event.type == pygame.QUIT:
            return "quit"

        elif hitboxes[0].collidepoint(event.pos):
            page= (page-1)%pages_amount

        elif hitboxes[1].collidepoint(event.pos):
            page= (page +1)%pages_amount

        else:
            for index in range(hitboxes_amount):
                if hitboxes[index+2].collidepoint(event.pos):
                    return rosters[index+page*18]

            return current_roster



def team_manager(window,mode,teams):

    if mode == "select" or mode == "manage":
        team_file= open("data/teams.txt","r")
        number= get_team_ammount(team_file.read())
        team_file.close()
        for i in range(number):
            teams= teams + [get_team(i)]

    current_team= -1
    current_page= 0

    window.fill((150,250,150))
    hitbox_back= text(window,"back",20,(0,0,0),"bottomleft",15,585)
    hitbox_prev= text(window,"<<",20,(0,0,0),"topleft",15,340)
    hitbox_nex= text(window,">>",20,(0,0,0),"topright",215,340)
    hitbox_page= (75,340,80,30)

    if mode == "select":
        hitbox_select= text(window,"select team",20,(0,0,0),"bottomright",1085,585)
    elif mode == "manage":
        hitbox_delete= text(window,"delete team",20,(0,0,0),"bottomright",1085,585)
    elif mode == "save":
        hitbox_save= text(window,"save team",20,(0,0,0),"bottomright",1085,585)
        hitbox_sort= text(window,"sort",20,(0,0,0),"midbottom",550,585)

    while True:
        type_chart= get_type_chart()

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
                if mode == "select":
                    return []
                elif mode == "manage":
                    return "menu"
                elif mode == "save":
                    return "team generator"

            elif hitbox_prev.collidepoint(event.pos) and len(teams)!=0:
                current_page= (current_page-1)%(((len(teams)-1)//5)+1)
                current_team= -1

            elif hitbox_nex.collidepoint(event.pos) and len(teams)!=0:
                current_page= (current_page+1)%(((len(teams)-1)//5)+1)
                current_team= -1

            elif mode == "save" and hitbox_sort.collidepoint(event.pos):
                teams= sort_teams(window,teams,True)
                pygame.draw.rect(window,(150,250,150),(550-300/2,585-100/2,300,100),0)
                hitbox_sort= text(window,"sort",20,(0,0,0),"midbottom",550,585)

            elif mode == "select" and hitbox_select.collidepoint(event.pos) and current_team != -1 and len(teams[current_team+current_page*5]) < 6:
                return teams[current_team+current_page*5]

            elif mode == "manage" and hitbox_delete.collidepoint(event.pos) and current_team != -1:
                delete_team(current_team+current_page*5)
                del teams[current_team+current_page*5]
                current_team= -1

            elif mode == "save" and hitbox_save.collidepoint(event.pos) and current_team != -1:
                save_team(teams[current_team+current_page*5])
                del teams[current_team+current_page*5]
                current_team= -1

            else:
                for i in range(len(hitboxes)):

                    if hitboxes[i].collidepoint(event.pos):
                        current_team= i



def team_generator(window):
    rosters= get_rosters()
    types_amount= len(get_existing_types())-1

    window.fill((150,250,150))
    hitbox_back= text(window,"back",20,(0,0,0),"bottomleft",15,585)
    hitbox_add_team= text(window,"add starting team",20,(0,0,0),"topleft",15,345)
    hitbox_roster= text(window,"choose roster",20,(0,0,0),"topleft",15,375)
    hitbox_generate= text(window,"generate",20,(0,0,0),"midbottom",550,585)
    text(window,"requirements",20,(0,0,0),"midtop",550,10)

    hitboxes= [[],[]]
    for index in range(types_amount):
        pygame.draw.rect(window,(200,200,200),(225+9+36*index,70-30,18,100),0)
        pygame.draw.rect(window,(100,100,100),(225+9+36*index,70-30,18,100),1)
        text(window,"+",20,(100,100,100),"midbottom",225+18+36*index,70)
        text(window,"-",20,(100,100,100),"midtop",225+18+36*index,70+40)
        hitboxes[0]= hitboxes[0] + [pygame.Rect(225+9+36*index,70-30,18,30)]
        hitboxes[1]= hitboxes[1] + [pygame.Rect(225+9+36*index,110,18,30)]

    current_requirements= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    current_roster= rosters[0]
    hitbox_mega= (15,405,200,30)
    stealth_rock_state= [False,"off"]
    anti_hazard_state= [False,"off"]
    priority_state= [False,"off"]
    mega_state= [False,"off"]
    roles= [[0,"physical attacker"],[0,"special attacker"],[0,"physical wall"],[0,"special wall"],[0,'rock setter'],[0,"defoger"],[0,"spiner"],[0,"priority user"]]
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
                current_team= team_manager(window,"select",[])
                window.fill((150,250,150))
                text(window,"back",20,(0,0,0),"bottomleft",15,585)
                text(window,"add starting team",20,(0,0,0),"topleft",15,345)
                text(window,"choose roster",20,(0,0,0),"topleft",15,375)
                text(window,"generate",20,(0,0,0),"midbottom",550,585)
                text(window,"requirements",20,(0,0,0),"midtop",550,10)
                for i in range(types_amount):
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
                teams= generating(window,generating_params)
                return team_manager(window,"save",teams)

            elif hitbox_roster.collidepoint(event.pos):
                current_roster= choose_roster(window,rosters,current_roster)

            else:
                for i in range(len(hitboxes_roles)):
                    if hitboxes_roles[i].collidepoint(event.pos):
                        roles[i][0]= (roles[i][0] + 1)%7

                for i in range(types_amount):
                    if hitboxes[0][i].collidepoint(event.pos) and current_requirements[i+1] < 6:
                        current_requirements[i+1]= current_requirements[i+1] + 1
                    elif hitboxes[1][i].collidepoint(event.pos) and current_requirements[i+1] > -6:
                        current_requirements[i+1]= current_requirements[i+1] - 1



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



def pokedex_info(window):
    rosters= get_rosters()

    current_roster= rosters[-1]
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
                current_page= (current_page-1)%(((len(current_roster.pokemon_list)-1)//10)+1)

            elif hitbox_choices[1].collidepoint(event.pos):
                current_page= (current_page+1)%(((len(current_roster.pokemon_list)-1)//10)+1)

            elif hitbox_roster.collidepoint(event.pos):
                pygame.draw.rect(window,(150,250,150),(880,10,210,580),0)

                hitbox_rosters= {}
                i=0
                for roster in rosters:
                    hitbox_rosters[roster]= text(window,roster.name,20,(0,0,0),"topright",1085,15+i*30)
                    i= i+1

                pygame.display.update()

                event= pygame.event.wait()

                if event.type == pygame.QUIT:
                    return "quit"

                for roster in rosters:

                    if hitbox_rosters[roster].collidepoint(event.pos):

                        current_roster= roster

            else:
                for i in range(2,len(hitbox_choices)):

                    if hitbox_choices[i].collidepoint(event.pos):
                        current_pokemon= current_roster.pokemon_list[i-2+current_page*10]



def options(window):
    current_generation= get_generation()

    window.fill((150,250,150))
    hitbox_back= text(window,"back",20,(0,0,0),"bottomleft",15,585)
    hitbox_generation= text(window,"change generation (current: "+str(current_generation+1)+")",20,(0,0,0),"center",550,300)

    while True:
        pygame.draw.rect(window,(150,250,150),(350,280,400,40),0)
        text(window,"change generation (current: "+str(current_generation+1)+")",20,(0,0,0),"center",550,300)
        pygame.display.update()

        event= pygame.event.wait()

        if event.type == pygame.QUIT:
            return "quit"

        if event.type == pygame.MOUSEBUTTONDOWN:

            if hitbox_generation.collidepoint(event.pos):
                current_generation= (current_generation + 1)%8

            if hitbox_back.collidepoint(event.pos):
                set_generation(current_generation)
                update_rosters()
                return "menu"
