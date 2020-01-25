from pokedex import *



def find(txt,char,start):
    for i in range(start,len(txt)):
        if txt[i] == char:
            return i



def get_team_ammount(txt):

    index= find(txt,"]",2)

    return int(txt[1:index])



def clean_teams():
    teams= open("data/teams.txt","w")
    teams.write("[0].")
    teams.close()



def save_team(team):
    teams= open("data/teams.txt","r")
    txt= teams.read()
    teams.close()

    total= get_team_ammount(txt)

    new_txt= "[" + str(total+1) + "]"

    i_1= find(txt,"]",2)
    i_2= find(txt,".",3)

    new_txt= new_txt + txt[i_1+1:i_2] + "[" + str(len(team))

    for pokemon in team:

        new_txt= new_txt + "," + pokemon.name

    new_txt= new_txt + "]" + "."

    teams= open("data/teams.txt","w")
    teams.write(new_txt)
    teams.close()

    return total + 1



def delete_team(number):
    teams= open("data/teams.txt","r")
    txt= teams.read()
    teams.close()

    total= get_team_ammount(txt)

    new_txt= "[" + str(total-1) + "]"

    i_1= find(txt,"]",2)
    i_2= find(txt,"[",3)

    for i in range(number):

        i_2= find(txt,"[",i_2+1)

    new_txt= new_txt + txt[i_1+1:i_2]

    if number != total-1:

        i_1= find(txt,"[",i_2+1)

        i_2= find(txt,".",i_2+1)

        new_txt= new_txt + txt[i_1:i_2]

    new_txt= new_txt + "."

    teams= open("data/teams.txt","w")
    teams.write(new_txt)
    teams.close()



def get_team(number):
    global pokedex
    teams= open("data/teams.txt","r")
    txt= teams.read()
    teams.close()
    team=[]

    total= get_team_ammount(txt)

    if number >= total:
        return team

    i_1= find(txt,"[",3)

    for i in range(number):

        i_1= find(txt,"[",i_1+1)

    i_2= find(txt,",",i_1+2)

    size= int(txt[i_1+1:i_2])

    for i in range(size):

              i_1= i_2

              if i != size-1:
                  i_2= find(txt,",",i_2+1)
              else:
                  i_2= find(txt,"]",i_2+1)

              team= team + [get_pokemon_from_name(txt[i_1+1:i_2],pokedex)]

    return team



def str_op(string,op):
    return str(int(string)+op)
