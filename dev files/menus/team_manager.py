from display import text, display_rosters, display_teams, display_team_weaknesses
from charts import get_type_chart
from calculus import sort_teams
from storage import *
import pygame



def team_manager(window,mode,teams):

    if mode == "select" or mode == "manage":
        team_ammount= get_team_ammount("data/teams.txt")
        for team_index in range(team_ammount):
            teams += [get_team(team_index,"data/teams.txt")]

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
                delete_team(current_team+current_page*5,"data/teams.txt")
                del teams[current_team+current_page*5]
                current_team= -1

            elif mode == "save" and hitbox_save.collidepoint(event.pos) and current_team != -1:
                save_team(teams[current_team+current_page*5],"data/teams.txt")
                del teams[current_team+current_page*5]
                current_team= -1

            else:
                for i in range(len(hitboxes)):

                    if hitboxes[i].collidepoint(event.pos):
                        current_team= i
