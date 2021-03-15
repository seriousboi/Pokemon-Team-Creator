from display import text
import pygame



def main_menu(window):
    window.fill((150,250,150))
    title= text(window,"Pokemon Team Creator",30,(0,0,0),"center",550,50)
    Turtwig= pygame.image.load("data/icons/wig.png")
    window.blit(Turtwig,(title.x + title.width,title.y + title.height - 30))
    hitbox_builder= text(window,"team builder",20,(0,0,0),"center",550,150)
    hitbox_roster= text(window,"roster creator",20,(0,0,0),"center",550,200)
    hitbox_generator= text(window,"team generator",20,(0,0,0),"center",550,250)
    hitbox_manager= text(window,"team manager",20,(0,0,0),"center",550,300)
    hitbox_chart= text(window,"type chart",20,(0,0,0),"center",550,350)
    hitbox_pokedex= text(window,"pokedex",20,(0,0,0),"center",550,400)
    hitbox_options= text(window,"options",20,(0,0,0),"center",550,450)
    hitbox_help= text(window,"help",20,(0,0,0),"center",550,500)

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

            elif hitbox_roster.collidepoint(event.pos):
                return "roster creator"

            elif hitbox_help.collidepoint(event.pos):
                return "help"
