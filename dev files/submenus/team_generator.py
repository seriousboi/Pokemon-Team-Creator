from display import text, display_team, display_requirements
from rosters import get_common_rosters
from charts import get_existing_types
from generator import generating
from submenus.team_manager import team_manager
from submenus.shared import choose_roster
import pygame



def team_generator(window):
    rosters= get_common_rosters()
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

    current_requirements= [0]*(types_amount+1)
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
