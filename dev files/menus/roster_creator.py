from menus.shared import choose_roster
from display import text, display_team, display_page
from rosters import get_common_rosters
from storage import save_custom_roster
import pygame


def roster_creator(window):
    rosters= get_common_rosters()
    already_saved= False
    current_roster= rosters[0]
    current_page= 0
    current_custom_roster= []

    window.fill((150,250,150))
    hitbox_back= text(window,"back",20,(0,0,0),"bottomleft",15,585)
    hitbox_roster= text(window,"choose roster",20,(0,0,0),"topleft",15,345)
    hitbox_add= text(window,"add whole roster",20,(0,0,0),"topleft",15,375)
    hitbox_undo= text(window,"undo",20,(0,0,0),"topleft",15,405)
    hitbox_save= text(window,"save custom roster",20,(0,0,0),"midbottom",550,585)
    pygame.display.update()

    while True:
        hitbox_choices= display_page(window,current_roster,current_page)
        pygame.draw.rect(window,(150,150,200),(10,10,855,325),0)
        pygame.draw.rect(window,(100,100,100),(10,10,855,325),1)
        for index in range(4):
            segment_start= max(0,len(current_custom_roster)-(6+index*6))
            segment_end= max(0,len(current_custom_roster)-index*6)
            roster_segment= current_custom_roster[segment_start:segment_end]
            display_team(window,roster_segment,(200,200,250),15+index*215,15)
        pygame.display.update()

        event= pygame.event.wait()

        if event.type == pygame.QUIT:
            return "quit"

        if event.type == pygame.MOUSEBUTTONDOWN:

            if hitbox_back.collidepoint(event.pos):
                return "menu"

            elif hitbox_save.collidepoint(event.pos) and len(current_custom_roster) != 0 and already_saved == False:
                save_custom_roster(current_custom_roster)
                already_saved= True

            elif hitbox_choices[0].collidepoint(event.pos):
                current_page= (current_page-1)%(((len(current_roster.pokemon_list)-1)//10)+1)

            elif hitbox_choices[1].collidepoint(event.pos):
                current_page= (current_page+1)%(((len(current_roster.pokemon_list)-1)//10)+1)

            elif hitbox_undo.collidepoint(event.pos) and len(current_custom_roster) > 0:
                current_custom_roster.pop()
                already_saved= False

            elif hitbox_roster.collidepoint(event.pos):
                current_roster= choose_roster(window,rosters,current_roster)

            elif hitbox_add.collidepoint(event.pos):
                current_custom_roster += current_roster.pokemon_list
                already_saved= False

            for i in range(2,len(hitbox_choices)):

                if hitbox_choices[i].collidepoint(event.pos):
                    current_custom_roster= current_custom_roster + [current_roster.pokemon_list[i-2+current_page*10]]
                    already_saved= False
