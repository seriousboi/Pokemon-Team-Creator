from display import text, display_rosters
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



def confirm_choice():
    pygame.event.set_allowed(pygame.KEYDOWN)
    event= pygame.event.wait()
    pygame.event.set_blocked(None)
    pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN,pygame.QUIT])
    if event.type == pygame.KEYDOWN and event.key == 13:
        return True
    return False



def display_text_file(window,filename):
    file= open(filename,"r")
    lines= file.readlines()
    file.close()

    window.fill((150,250,150))
    hitbox_back= text(window,"back",20,(0,0,0),"bottomleft",15,585)
    index= 0
    for line in lines:
        index += 1
        text(window,line[0:len(line)-1],15,(0,0,0),"topleft",10,10+20*index)
    pygame.display.update()

    while True:
        event= pygame.event.wait()
        if event.type == pygame.QUIT:
                return "quit"
        if event.type == pygame.MOUSEBUTTONDOWN and hitbox_back.collidepoint(event.pos):
                return
