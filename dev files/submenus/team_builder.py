from display import text, display_page, display_team, display_team_weaknesses
from rosters import get_common_rosters
from storage import save_team
from submenus.shared import choose_roster
import pygame



def team_builder(window):
    rosters= get_common_rosters()

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
                save_team(current_team,"data/teams.txt")
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
