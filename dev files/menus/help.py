from display import text
from menus.shared import display_text_file
import pygame



def help_menu(window):
    help_list=["general infos","team builder","team generator","type sensitivity","report a bug"]
    help_hitboxes=[]
    help_length= len(help_list)
    for index in range(help_length):
        help_hitboxes += [text(window,help_list[index],20,(0,0,0),"center",550,150+50*index)]
    hitbox_back= text(window,"back",20,(0,0,0),"bottomleft",15,585)

    while True:
        window.fill((150,250,150))
        text(window,"back",20,(0,0,0),"bottomleft",15,585)
        for index in range(help_length):
            text(window,help_list[index],20,(0,0,0),"center",550,150+50*index)
        pygame.display.update()

        event= pygame.event.wait()

        if event.type == pygame.QUIT:
                return "quit"

        if event.type == pygame.MOUSEBUTTONDOWN:

            if hitbox_back.collidepoint(event.pos):
                    return "menu"

            for index in range(help_length):
                if help_hitboxes[index].collidepoint(event.pos):
                    if display_text_file(window,"data/help/"+help_list[index]+".txt") == "quit":
                        return "quit"
