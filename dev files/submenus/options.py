from display import text
from charts import get_generation, set_generation
from pokedex import update_pokedex
from rosters import update_rosters
import pygame



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
                update_pokedex()
                update_rosters()
                return "menu"
