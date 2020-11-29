from display import text
from charts import get_generation, set_generation
from pokedex import update_pokedex
from rosters import update_rosters
from storage import clean_teams
import pygame



def options(window):
    current_generation= get_generation()

    window.fill((150,250,150))
    hitbox_back= text(window,"back",20,(0,0,0),"bottomleft",15,585)
    hitbox_generation= text(window,"change generation (current: "+str(current_generation+1)+")",20,(0,0,0),"center",550,300)
    hitbox_reset= text(window,"reset team file",20,(0,0,0),"center",550,350)

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

            if hitbox_reset.collidepoint(event.pos):
                pygame.draw.rect(window,(150,250,150),hitbox_reset,0)
                hitbox_confirm= text(window,"All team data will be lost, press Enter to confirm, press any other key to cancel.",20,(0,0,0),"center",550,350)
                pygame.display.update()

                if confirm_choice():
                    clean_teams("data/teams.txt")

                pygame.draw.rect(window,(150,250,150),hitbox_confirm,0)
                text(window,"reset team file",20,(0,0,0),"center",550,350)


            if hitbox_back.collidepoint(event.pos):
                set_generation(current_generation)
                update_pokedex()
                update_rosters()
                return "menu"



def confirm_choice():
    pygame.event.set_allowed(pygame.KEYDOWN)
    event= pygame.event.wait()
    pygame.event.set_blocked(None)
    pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN,pygame.QUIT])
    if event.type == pygame.KEYDOWN and event.key == 13:
        return True
    return False
