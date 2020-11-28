from display import text, display_chart
import pygame



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
