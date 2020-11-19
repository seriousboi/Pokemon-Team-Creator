from menus import *



def main():

    pygame.init()
    window= pygame.display.set_mode((1100,600))
    Turtwig= pygame.image.load("data/icons/wig.png")
    pygame.display.set_icon(Turtwig)
    pygame.display.set_caption("Pokemon Team Creator (work in progress)")
    pygame.event.set_blocked(None)
    pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN,pygame.QUIT])

    state= "menu"

    while state != "quit":

        if state == "menu":
            state= menu(window)
        if state == "team builder":
            state= team_builder(window)
        if state == "team manager":
            state= team_manager(window,"manage",[])
        if state == "chart":
            state= chart(window)
        if state == "team generator":
            state= team_generator(window)
        if state == "pokedex info":
            state= pokedex_info(window)
        if state == "options":
            state= options(window)

    pygame.display.quit()



main()
