from display import display_rosters
import pygame



def choose_roster(window,rosters,current_roster):
    rosters_amount= len(rosters)
    pages_amount= 1+(rosters_amount-1)//18
    choosing_roster= True
    page= 0
    while choosing_roster:
        hitboxes= display_rosters(window,rosters,page)
        hitboxes_amount= len(hitboxes)-2
        pygame.display.update()

        event= pygame.event.wait()

        if event.type == pygame.QUIT:
            return "quit"

        elif hitboxes[0].collidepoint(event.pos):
            page= (page-1)%pages_amount

        elif hitboxes[1].collidepoint(event.pos):
            page= (page +1)%pages_amount

        else:
            for index in range(hitboxes_amount):
                if hitboxes[index+2].collidepoint(event.pos):
                    return rosters[index+page*18]

            return current_roster
