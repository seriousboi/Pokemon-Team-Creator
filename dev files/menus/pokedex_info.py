from display import text, info_pokemon, display_page, display_pokemon_weaknesses, display_pokemon_roles
from rosters import get_common_rosters
from menus.shared import choose_roster
import pygame



def pokedex_info(window):
    rosters= get_common_rosters()

    current_roster= rosters[-1]
    current_page= 0
    current_pokemon= None

    window.fill((150,250,150))
    hitbox_back= text(window,"back",20,(0,0,0),"bottomleft",15,585)
    hitbox_roster= text(window,"choose roster",20,(0,0,0),"midbottom",550,585)

    while True:
        pygame.draw.rect(window,(150,250,150),(15,0,206,55),0)
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
                current_roster= choose_roster(window,rosters,current_roster)

            else:
                for i in range(2,len(hitbox_choices)):

                    if hitbox_choices[i].collidepoint(event.pos):
                        pokemon= current_roster.pokemon_list[i-2+current_page*10]
                        current_pokemon= pokemon
