from menus.team_builder import team_builder
from menus.team_manager import team_manager
from menus.team_generator import team_generator
from menus.chart import chart
from menus.pokedex_info import pokedex_info
from menus.options import options
from menus.roster_creator import roster_creator
from menus.main_menu import main_menu
from menus.help import help_menu
import pygame


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
            state= main_menu(window)
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
        if state == "roster creator":
            state= roster_creator(window)
        if state == "help":
            state= help_menu(window)

    pygame.display.quit()

main()
