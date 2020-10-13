from abilities import *



class Pokemon():
    def __init__(self,pid,name,type,ability,picid,properties,tier,generations_changes):
        self.pid= pid
        self.name= name
        self.type= type
        self.ability= ability
        self.picid= picid
        self.properties= properties
        self.tier= tier
        self.generations_changes= generations_changes



class Change():
    def __init__(self,affected_generations,attribute,change):
        self.affected_generations= affected_generations
        self.attribute= attribute
        self.change= change



def get_pokedex():
    global pokedex
    return pokedex



def get_pokemon_from_name(name):
    pokedex= get_pokedex()
    for pokemon in pokedex:
        if pokemon.name == name:
            return pokemon
    return None



def print_dex(dex):
    print("    original_pokedex= []")
    for pokemon in dex:
        line= "    original_pokedex += [Pokemon("+str(pokemon.pid)+',"'+pokemon.name+'",'+str(pokemon.type)+","
        if pokemon.ability.weaknesses_influent:
            line= line + get_ability_variable_name(pokemon.ability.ability_name)
        else:
            line= line + "no_ability"
        line= line + ',"'+pokemon.picid+'",'+str(pokemon.properties)+','+str(pokemon.tier)+",["
        for change in pokemon.generations_changes:
            line= line + "Change("+str(change.affected_generations)+",'"+change.attribute+"',"+str(change.change)+"),"
        line= line +"])]"
        print(line)


def get_original_pokedex():
    original_pokedex= []
    original_pokedex += [Pokemon(3,"Venusaur",['grass', 'poison'],no_ability,"3",['special wall'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(3,"Venusaur-Mega",['grass', 'poison'],Thick_Fat,"3-1",['mega', 'special wall', 'physical wall'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(6,"Charizard",['fire', 'flying'],no_ability,"6",['special attacker', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(6,"Charizard-Mega-X",['fire', 'dragon'],no_ability,"6-1",['mega', 'physical attacker', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(6,"Charizard-Mega-Y",['fire', 'flying'],no_ability,"6-2",['mega', 'special attacker', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(9,"Blastoise",['water', 'none'],no_ability,"9",['special wall', 'physical wall', 'spiner', 'priority user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(9,"Blastoise-Mega",['water', 'none'],no_ability,"9-1",['mega', 'special attacker', 'spiner', 'priority user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(12,"Butterfree",['bug', 'flying'],no_ability,"12",['special attacker', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(15,"Beedrill",['bug', 'poison'],no_ability,"15",['defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(15,"Beedrill",['bug', 'poison'],no_ability,"15-1",['mega', 'physical attacker', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(20,"Raticate",['normal', 'none'],no_ability,"20",['physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(22,"Fearow",['normal', 'flying'],no_ability,"22",['physical attacker', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(24,"Arbok",['poison', 'none'],no_ability,"24",['physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(26,"Raichu",['electric', 'none'],Lightning_Rod,"26",['special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(28,"Sandslash",['ground', 'none'],no_ability,"28",['physical wall', 'physical attacker', 'rock setter', 'spiner'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(31,"Nidoqueen",['ground', 'poison'],no_ability,"31",['rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(34,"Nidoking",['ground', 'poison'],no_ability,"34",['physical attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(36,"Clefable",['fairy', 'none'],no_ability,"36",['special wall', 'special attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[Change([0, 1, 2, 3, 4],'type',['normal', 'none']),])]
    original_pokedex += [Pokemon(38,"Ninetales",['fire', 'none'],no_ability,"38",['special wall', 'special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(40,"Wigglytuff",['normal', 'fairy'],no_ability,"40",['rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(45,"Vileplume",['grass', 'poison'],no_ability,"45",['special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(47,"Parasect",['bug', 'grass'],Dry_Skin,"47",['physical attacker', 'very cool'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(49,"Venomoth",['bug', 'poison'],no_ability,"49",['special attacker', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(51,"Dugtrio",['ground', 'none'],no_ability,"51",['physical attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(53,"Persian",['normal', 'none'],no_ability,"53",[],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(55,"Golduck",['water', 'none'],no_ability,"55",['special attacker', 'priority user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(57,"Primeape",['fighting', 'none'],no_ability,"57",['physical attacker', 'priority user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(59,"Arcanine",['fire', 'none'],Flash_Fire,"59",['physical attacker', 'priority user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(62,"Poliwrath",['water', 'fighting'],Water_Absorb,"62",['physical attacker', 'priority user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(65,"Alakazam",['psychic', 'none'],no_ability,"65",['special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(65,"Alakazam-Mega",['psychic', 'none'],no_ability,"65-1",['mega', 'special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(68,"Machamp",['fighting', 'none'],no_ability,"68",['physical attacker', 'priority user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(71,"Victreebel",['grass', 'poison'],no_ability,"71",['special attacker', 'physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(73,"Tentacruel",['water', 'poison'],no_ability,"73",['special wall', 'spiner'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(76,"Golem",['rock', 'ground'],no_ability,"76",['physical wall', 'physical attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(78,"Rapidash",['fire', 'none'],Flash_Fire,"78",['physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(80,"Slowbro",['water', 'psychic'],no_ability,"80",['physical wall'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(83,"Farfetch’d",['normal', 'flying'],no_ability,"83",['physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(85,"Dodrio",['normal', 'flying'],no_ability,"85",['physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(87,"Dewgong",['water', 'ice'],Thick_Fat,"87",['special wall'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(89,"Muk",['poison', 'none'],no_ability,"89",['physical wall', 'physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(91,"Cloyster",['water', 'ice'],no_ability,"91",['physical wall', 'physical attacker', 'spiner'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(94,"Gengar",['ghost', 'poison'],Levitate,"94",['special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(94,"Gengar-Mega",['ghost', 'poison'],no_ability,"94-1",['special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(97,"Hypno",['psychic', 'none'],no_ability,"97",['mega', 'special wall'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(99,"Kingler",['water', 'none'],no_ability,"99",['physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(101,"Electrode",['electric', 'none'],no_ability,"101",['special attacker', 'priority user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(103,"Exeggutor",['grass', 'psychic'],no_ability,"103",['special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(105,"Marowak",['ground', 'none'],no_ability,"105",['physical attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(106,"Hitmonlee",['fighting', 'none'],no_ability,"106",['physical attacker', 'spiner'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(107,"Hitmonchan",['fighting', 'none'],no_ability,"107",['physical attacker', 'spiner'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(110,"Weezing",['poison', 'none'],Levitate,"110",['physical wall'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(113,"Chansey",['normal', 'none'],no_ability,"113",['special wall', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(115,"Kangaskhan",['normal', 'none'],no_ability,"115",['physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(115,"Kangaskhan-Mega",['normal', 'none'],no_ability,"115-1",['mega', 'physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(119,"Seaking",['water', 'none'],Lightning_Rod,"119",['physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(121,"Starmie",['water', 'psychic'],no_ability,"121",['special attacker', 'spiner'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(122,"Mr. Mime",['psychic', 'fairy'],Filter,"122",['special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(124,"Jynx",['ice', 'fairy'],Dry_Skin,"124",['special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(127,"Pinsir",['bug', 'none'],no_ability,"127",['physical attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(127,"Pinsir-Mega",['bug', 'flying'],no_ability,"127-1",['mega', 'physical attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(128,"Tauros",['normal', 'none'],no_ability,"128",['physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(130,"Gyarados",['water', 'flying'],no_ability,"130",['physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(130,"Gyarados-Mega",['water', 'dark'],no_ability,"130-1",['mega', 'physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(131,"Lapras",['water', 'ice'],Water_Absorb,"131",['physical wall', 'special wall', 'priority user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(132,"Ditto",['normal', 'none'],no_ability,"132",[],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(134,"Vaporeon",['water', 'none'],Water_Absorb,"134",['special wall', 'special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(135,"Jolteon",['electric', 'none'],Volt_Absorb,"135",['special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(136,"Flareon",['fire', 'none'],Flash_Fire,"136",['physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(139,"Omastar",['rock', 'water'],no_ability,"139",['physical wall', 'special attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(141,"Kabutops",['rock', 'water'],no_ability,"141",['physical attacker', 'rock setter', 'spiner'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(142,"Aerodactyl",['rock', 'flying'],no_ability,"142",['physical attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(142,"Aerodactyl-Mega",['rock', 'flying'],no_ability,"142-1",['mega', 'physical attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(143,"Snorlax",['normal', 'none'],Thick_Fat,"143",['special wall', 'physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(144,"Articuno",['ice', 'flying'],no_ability,"144",['special wall', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(145,"Zapdos",['electric', 'flying'],no_ability,"145",['special attacker', 'physical wall', 'special wall', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(146,"Moltres",['fire', 'flying'],no_ability,"146",['special attacker', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(149,"Dragonite",['dragon', 'flying'],no_ability,"149",['physical attacker', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(150,"Mewtwo",['psychic', 'none'],no_ability,"150",['special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(150,"Mewtwo-Mega-X",['psychic', 'fighting'],no_ability,"150-1",['mega', 'physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(150,"Mewtwo-Mega-Y",['psychic', 'none'],no_ability,"150-2",['mega', 'special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(151,"Mew",['psychic', 'none'],no_ability,"151",['physical wall', 'special wall', 'rock setter', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(387,"Turtwig",['grass', 'none'],no_ability,"387",['rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(390,"Chimchar",['fire', 'none'],no_ability,"390",['rock setter', 'priority user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(393,"Piplup",['water', 'none'],no_ability,"393",['rock setter', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(417,"Pachirisu",['electric', 'none'],Volt_Absorb,"417",['priority user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'nd'],[])]
    original_pokedex += [Pokemon(184,"Azumarill",['water', 'fairy'],no_ability,"184",['physical attacker', 'priority user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(806,"Blacephalon",['fire', 'ghost'],no_ability,"806",['special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(797,"Celesteela",['steel', 'flying'],no_ability,"797",['physical wall', 'special wall'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(719,"Diancie-Mega",['rock', 'fairy'],no_ability,"719-1",['mega', 'special attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(530,"Excadrill",['ground', 'steel'],no_ability,"530",['physical attacker', 'rock setter', 'spiner'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(598,"Ferrothorn",['grass', 'steel'],no_ability,"598",['physical wall', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(445,"Garchomp",['dragon', 'ground'],no_ability,"445",['physical attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(472,"Gliscor",['ground', 'flying'],no_ability,"472",['physical attacker', 'physical wall', 'rock setter', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(658,"Greninja",['water', 'dark'],no_ability,"658",['special attacker', 'priority user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(701,"Hawlucha",['fighting', 'flying'],no_ability,"701",['physical attacker', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(485,"Heatran",['fire', 'steel'],Flash_Fire,"485",['special attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(385,"Jirachi",['steel', 'psychic'],no_ability,"385",['physical attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(798,"Kartana",['grass', 'steel'],no_ability,"798",['physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(647,"Keldeo",['water', 'fighting'],no_ability,"647",['special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(784,"Kommo-o",['dragon', 'fighting'],no_ability,"784",['physical attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(644,"Kyurem-Black",['dragon', 'ice'],no_ability,"646-2",['physical attacker', 'special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(644,"Landorus-Therian",['ground', 'flying'],no_ability,"645-1",['physical attacker', 'rock setter', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(428,"Lopunny-Mega",['normal', 'fighting'],no_ability,"428-1",['mega', 'physical attacker', 'priority user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(801,"Magearna",['steel', 'fairy'],no_ability,"801",['special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(462,"Magnezone",['electric', 'steel'],no_ability,"462",['special attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(303,"Mawile-Mega",['steel', 'fairy'],no_ability,"303-1",['mega', 'physical attacker', 'rock setter', 'priority user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(308,"Medicham-Mega",['fighting', 'psychic'],no_ability,"308-1",['mega', 'physical attacker', 'priority user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(279,"Pelipper",['water', 'flying'],no_ability,"279",['physical wall', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(477,"Rotom-Wash",['electric', 'water'],Levitate,"479-2",['physical wall', 'special wall', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(212,"Scizor-Mega",['bug', 'steel'],no_ability,"212-1",['mega', 'physical attacker', 'physical wall', 'defoger', 'prioriOU user'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(497,"Serperior",['grass', 'none'],no_ability,"497",['special attacker', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(227,"Skarmory",['steel', 'flying'],no_ability,"227",['physical wall', 'rock setter', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(260,"Swampert-Mega",['water', 'ground'],no_ability,"260-1",['mega', 'physical attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(465,"Tangrowth",['grass', 'none'],no_ability,"465",['physical wall', 'special wall'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(787,"Tapu Bulu",['grass', 'fairy'],no_ability,"787",['physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(788,"Tapu Fini",['water', 'fairy'],no_ability,"788",['physical wall', 'special wall', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(785,"Tapu Koko",['electric', 'fairy'],no_ability,"785",['special attacker', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(786,"Tapu Lele",['psychic', 'fairy'],no_ability,"786",['special attacker', 'special wall'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(640,"Tornadus-Therian",['flying', 'none'],no_ability,"641-1",['special attacker', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(748,"Toxapex",['poison', 'water'],no_ability,"748",['physical wall', 'special wall'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(248,"Tyranitar",['rock', 'dark'],no_ability,"248",['physical attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(248,"Tyranitar-Mega",['rock', 'dark'],no_ability,"248-1",['mega', 'physical attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(494,"Victini",['psychic', 'fire'],no_ability,"494",['physical attacker'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(637,"Volcarona",['bug', 'fire'],no_ability,"637",['special attacker', 'defoger'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    original_pokedex += [Pokemon(445,"Garchomp-Mega",['dragon', 'ground'],no_ability,"445-1",['mega', 'physical attacker', 'rock setter'],['nd', 'nd', 'nd', 'nd', 'nd', 'nd', 'OU', 'nd'],[])]
    return original_pokedex



def update_pokedex():
    global pokedex
    generation= get_generation()
    pokedex= get_original_pokedex()
    for pokemon in pokedex:
        for change in pokemon.generations_changes:
            if generation in change.affected_generations:
                setattr(pokemon,change.attribute,change.change)
    return



pokedex= get_original_pokedex()
