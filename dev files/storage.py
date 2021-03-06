from pokedex import *
import glob



def get_txt_list(filename):
    file= open(filename,"r")
    lines= file.readlines()
    txt_list= []
    for line_index in range(len(lines)):
        txt_list += [lines[line_index].split()]
    file.close()
    return txt_list



def get_team_ammount(filename):
    txt_list= get_txt_list(filename)
    return int(txt_list[0][0])



def get_custom_rosters_ammount():
    return len(glob.glob('./data/custom_rosters/*.txt'))



def get_team(number,filename):
    txt_list= get_txt_list(filename)

    total= get_team_ammount(filename)
    if number >= total:
        return team

    size= int(txt_list[number+1][0])

    team=[]
    for pokemon_index in range(size):
              pokemon_picid= txt_list[number+1][pokemon_index+1]
              team= team + [get_pokemon_from_picid(pokemon_picid)]

    return team



def save_team(team,filename):
    file= open(filename,"r")
    lines= file.readlines()
    file.close()

    lines[0]= str(1+int(lines[0]))+'\n'
    size= len(team)
    line= str(size)
    for pokemon in team:
        line += ' '+pokemon.picid
    lines += [line+'\n']

    file= open(filename,"w")
    file.writelines(lines)
    file.close()



def save_custom_roster(custom_roster):
    custom_rosters_amount= get_custom_rosters_ammount()
    filename= "data/custom_rosters/custom roster "+str(custom_rosters_amount+1)+".txt"
    file= open(filename,"w")
    size= len(custom_roster)
    line= str(size)
    for pokemon in custom_roster:
        line += ' '+pokemon.picid
    line += '\n'
    file.writelines([line])
    file.close()




def delete_team(number,filename):
    file= open(filename,"r")
    lines= file.readlines()
    file.close()

    lines[0]= str(int(lines[0])-1)+'\n'
    lines.pop(number+1)

    file= open(filename,"w")
    file.writelines(lines)
    file.close()



def clean_teams(filename):
    file= open(filename,"w")
    file.write("0")
    file.close()
