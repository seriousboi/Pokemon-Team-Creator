from abilities import *



class Pokemon():
    def __init__(self,pid,name,type,ability,picid,tier,properties):
        self.pid =pid
        self.name= name
        self.type= type
        self.ability= ability
        self.picid= picid
        self.properties= properties
        self.tier= tier



def get_pokemon_from_name(name,pokedex):
    for pokemon in pokedex:
        if pokemon.name == name:
            return pokemon
    return None



def print_dex(dex):
    print("pokedex= []")
    for pokemon in dex:
        line= "pokedex += [Pokemon("+str(pokemon.pid)+',"'+pokemon.name+'",'+str(pokemon.type)+","
        if pokemon.ability[0]:
            line= line + get_ability_variable_name(pokemon.ability[3])
        else:
            line= line + "no_ability"
        line= line + ',"'+pokemon.picid+'","'+pokemon.tier+'",'+str(pokemon.properties)+")]"
        print(line)



pokedex= []
pokedex += [Pokemon(3,"Venusaur",['grass', 'poison'],no_ability,"3","nd",['special wall'])]
pokedex += [Pokemon(3,"Venusaur-Mega",['grass', 'poison'],Thick_Fat,"3-1","nd",['mega', 'special wall', 'physical wall'])]
pokedex += [Pokemon(6,"Charizard",['fire', 'flying'],no_ability,"6","nd",['special attacker', 'defoger'])]
pokedex += [Pokemon(6,"Charizard-Mega-X",['fire', 'dragon'],no_ability,"6-1","OU",['mega', 'physical attacker', 'defoger'])]
pokedex += [Pokemon(6,"Charizard-Mega-Y",['fire', 'flying'],no_ability,"6-2","OU",['mega', 'special attacker', 'defoger'])]
pokedex += [Pokemon(9,"Blastoise",['water', 'none'],no_ability,"9","nd",['special wall', 'physical wall', 'spiner', 'priority user'])]
pokedex += [Pokemon(9,"Blastoise-Mega",['water', 'none'],no_ability,"9-1","nd",['mega', 'special attacker', 'spiner', 'priority user'])]
pokedex += [Pokemon(12,"Butterfree",['bug', 'flying'],no_ability,"12","nd",['special attacker', 'defoger'])]
pokedex += [Pokemon(15,"Beedrill",['bug', 'poison'],no_ability,"15","nd",['defoger'])]
pokedex += [Pokemon(15,"Beedrill",['bug', 'poison'],no_ability,"15-1","nd",['mega', 'physical attacker', 'defoger'])]
pokedex += [Pokemon(20,"Raticate",['normal', 'none'],no_ability,"20","nd",['physical attacker'])]
pokedex += [Pokemon(22,"Fearow",['normal', 'flying'],no_ability,"22","nd",['physical attacker', 'defoger'])]
pokedex += [Pokemon(24,"Arbok",['poison', 'none'],no_ability,"24","nd",['physical attacker'])]
pokedex += [Pokemon(26,"Raichu",['electric', 'none'],Lightning_Rod,"26","nd",['special attacker'])]
pokedex += [Pokemon(28,"Sandslash",['ground', 'none'],no_ability,"28","nd",['physical wall', 'physical attacker', 'rock setter', 'spiner'])]
pokedex += [Pokemon(31,"Nidoqueen",['ground', 'poison'],no_ability,"31","nd",['rock setter'])]
pokedex += [Pokemon(34,"Nidoking",['ground', 'poison'],no_ability,"34","nd",['physical attacker', 'rock setter'])]
pokedex += [Pokemon(36,"Clefable",['fairy', 'none'],no_ability,"36","OU",['special wall', 'special attacker', 'rock setter'])]
pokedex += [Pokemon(38,"Ninetales",['fire', 'none'],no_ability,"38","nd",['special wall', 'special attacker'])]
pokedex += [Pokemon(40,"Wigglytuff",['normal', 'fairy'],no_ability,"40","nd",['rock setter'])]
pokedex += [Pokemon(45,"Vileplume",['grass', 'poison'],no_ability,"45","nd",['special attacker'])]
pokedex += [Pokemon(47,"Parasect",['bug', 'grass'],Dry_Skin,"47","nd",['physical attacker', 'best pokemon'])]
pokedex += [Pokemon(49,"Venomoth",['bug', 'poison'],no_ability,"49","nd",['special attacker', 'defoger'])]
pokedex += [Pokemon(51,"Dugtrio",['ground', 'none'],no_ability,"51","nd",['physical attacker', 'rock setter'])]
pokedex += [Pokemon(53,"Persian",['normal', 'none'],no_ability,"53","nd",[])]
pokedex += [Pokemon(55,"Golduck",['water', 'none'],no_ability,"55","nd",['special attacker', 'priority user'])]
pokedex += [Pokemon(57,"Primeape",['fighting', 'none'],no_ability,"57","nd",['physical attacker', 'priority user'])]
pokedex += [Pokemon(59,"Arcanine",['fire', 'none'],Flash_Fire,"59","nd",['physical attacker', 'priority user'])]
pokedex += [Pokemon(62,"Poliwrath",['water', 'fighting'],Water_Absorb,"62","nd",['physical attacker', 'priority user'])]
pokedex += [Pokemon(65,"Alakazam",['psychic', 'none'],no_ability,"65","nd",['special attacker'])]
pokedex += [Pokemon(65,"Alakazam-Mega",['psychic', 'none'],no_ability,"65-1","OU",['mega', 'special attacker'])]
pokedex += [Pokemon(68,"Machamp",['fighting', 'none'],no_ability,"68","nd",['physical attacker', 'priority user'])]
pokedex += [Pokemon(71,"Victreebel",['grass', 'poison'],no_ability,"71","nd",['special attacker', 'physical attacker'])]
pokedex += [Pokemon(73,"Tentacruel",['water', 'poison'],no_ability,"73","nd",['special wall', 'spiner'])]
pokedex += [Pokemon(76,"Golem",['rock', 'ground'],no_ability,"76","nd",['physical wall', 'physical attacker', 'rock setter'])]
pokedex += [Pokemon(78,"Rapidash",['fire', 'none'],Flash_Fire,"78","nd",['physical attacker'])]
pokedex += [Pokemon(80,"Slowbro",['water', 'psychic'],no_ability,"80","nd",['physical wall'])]
pokedex += [Pokemon(83,"Farfetch’d",['normal', 'flying'],no_ability,"83","nd",['physical attacker'])]
pokedex += [Pokemon(85,"Dodrio",['normal', 'flying'],no_ability,"85","nd",['physical attacker'])]
pokedex += [Pokemon(87,"Dewgong",['water', 'ice'],Thick_Fat,"87","nd",['special wall'])]
pokedex += [Pokemon(89,"Muk",['poison', 'none'],no_ability,"89","nd",['physical wall', 'physical attacker'])]
pokedex += [Pokemon(91,"Cloyster",['water', 'ice'],no_ability,"91","nd",['physical wall', 'physical attacker', 'spiner'])]
pokedex += [Pokemon(94,"Gengar",['ghost', 'poison'],Levitate,"94","nd",['special attacker'])]
pokedex += [Pokemon(94,"Gengar-Mega",['ghost', 'poison'],no_ability,"94-1","nd",['special attacker'])]
pokedex += [Pokemon(97,"Hypno",['psychic', 'none'],no_ability,"97","nd",['mega', 'special wall'])]
pokedex += [Pokemon(99,"Kingler",['water', 'none'],no_ability,"99","nd",['physical attacker'])]
pokedex += [Pokemon(101,"Electrode",['electric', 'none'],no_ability,"101","nd",['special attacker', 'priority user'])]
pokedex += [Pokemon(103,"Exeggutor",['grass', 'psychic'],no_ability,"103","nd",['special attacker'])]
pokedex += [Pokemon(105,"Marowak",['ground', 'none'],no_ability,"105","nd",['physical attacker', 'rock setter'])]
pokedex += [Pokemon(106,"Hitmonlee",['fighting', 'none'],no_ability,"106","nd",['physical attacker', 'spiner'])]
pokedex += [Pokemon(107,"Hitmonchan",['fighting', 'none'],no_ability,"107","nd",['physical attacker', 'spiner'])]
pokedex += [Pokemon(110,"Weezing",['poison', 'none'],Levitate,"110","nd",['physical wall'])]
pokedex += [Pokemon(113,"Chansey",['normal', 'none'],no_ability,"113","OU",['special wall', 'rock setter'])]
pokedex += [Pokemon(115,"Kangaskhan",['normal', 'none'],no_ability,"115","nd",['physical attacker'])]
pokedex += [Pokemon(115,"Kangaskhan-Mega",['normal', 'none'],no_ability,"115-1","nd",['mega', 'physical attacker'])]
pokedex += [Pokemon(119,"Seaking",['water', 'none'],Lightning_Rod,"119","nd",['physical attacker'])]
pokedex += [Pokemon(121,"Starmie",['water', 'psychic'],no_ability,"121","nd",['special attacker', 'spiner'])]
pokedex += [Pokemon(122,"Mr. Mime",['psychic', 'fairy'],Filter,"122","nd",['special attacker'])]
pokedex += [Pokemon(124,"Jynx",['ice', 'fairy'],Dry_Skin,"124","nd",['special attacker'])]
pokedex += [Pokemon(127,"Pinsir",['bug', 'none'],no_ability,"127","nd",['physical attacker', 'rock setter'])]
pokedex += [Pokemon(127,"Pinsir-Mega",['bug', 'flying'],no_ability,"127-1","nd",['mega', 'physical attacker', 'rock setter'])]
pokedex += [Pokemon(128,"Tauros",['normal', 'none'],no_ability,"128","nd",['physical attacker'])]
pokedex += [Pokemon(130,"Gyarados",['water', 'flying'],no_ability,"130","nd",['physical attacker'])]
pokedex += [Pokemon(130,"Gyarados-Mega",['water', 'dark'],no_ability,"130-1","OU",['mega', 'physical attacker'])]
pokedex += [Pokemon(131,"Lapras",['water', 'ice'],Water_Absorb,"131","nd",['physical wall', 'special wall', 'priority user'])]
pokedex += [Pokemon(132,"Ditto",['normal', 'none'],no_ability,"132","nd",[])]
pokedex += [Pokemon(134,"Vaporeon",['water', 'none'],Water_Absorb,"134","nd",['special wall', 'special attacker'])]
pokedex += [Pokemon(135,"Jolteon",['electric', 'none'],Volt_Absorb,"135","nd",['special attacker'])]
pokedex += [Pokemon(136,"Flareon",['fire', 'none'],Flash_Fire,"136","nd",['physical attacker'])]
pokedex += [Pokemon(139,"Omastar",['rock', 'water'],no_ability,"139","nd",['physical wall', 'special attacker', 'rock setter'])]
pokedex += [Pokemon(141,"Kabutops",['rock', 'water'],no_ability,"141","nd",['physical attacker', 'rock setter', 'spiner'])]
pokedex += [Pokemon(142,"Aerodactyl",['rock', 'flying'],no_ability,"142","nd",['physical attacker', 'rock setter'])]
pokedex += [Pokemon(142,"Aerodactyl-Mega",['rock', 'flying'],no_ability,"142-1","nd",['mega', 'physical attacker', 'rock setter'])]
pokedex += [Pokemon(143,"Snorlax",['normal', 'none'],Thick_Fat,"143","nd",['special wall', 'physical attacker'])]
pokedex += [Pokemon(144,"Articuno",['ice', 'flying'],no_ability,"144","nd",['special wall', 'defoger'])]
pokedex += [Pokemon(145,"Zapdos",['electric', 'flying'],no_ability,"145","OU",['special attacker', 'physical wall', 'special wall', 'defoger'])]
pokedex += [Pokemon(146,"Moltres",['fire', 'flying'],no_ability,"146","nd",['special attacker', 'defoger'])]
pokedex += [Pokemon(149,"Dragonite",['dragon', 'flying'],no_ability,"149","nd",['physical attacker', 'defoger'])]
pokedex += [Pokemon(150,"Mewtwo",['psychic', 'none'],no_ability,"150","nd",['special attacker'])]
pokedex += [Pokemon(150,"Mewtwo-Mega-X",['psychic', 'fighting'],no_ability,"150-1","nd",['mega', 'physical attacker'])]
pokedex += [Pokemon(150,"Mewtwo-Mega-Y",['psychic', 'none'],no_ability,"150-2","nd",['mega', 'special attacker'])]
pokedex += [Pokemon(151,"Mew",['psychic', 'none'],no_ability,"151","OU",['physical wall', 'special wall', 'rock setter', 'defoger'])]
pokedex += [Pokemon(387,"Turtwig",['grass', 'none'],no_ability,"387","nd",['rock setter'])]
pokedex += [Pokemon(390,"Chimchar",['fire', 'none'],no_ability,"390","nd",['rock setter', 'priority user'])]
pokedex += [Pokemon(393,"Piplup",['water', 'none'],no_ability,"393","nd",['rock setter', 'defoger'])]
pokedex += [Pokemon(417,"Pachirisu",['electric', 'none'],Volt_Absorb,"417","nd",['priority user'])]
pokedex += [Pokemon(184,"Azumarill",['water', 'fairy'],no_ability,"184","OU",['physical attacker', 'priority user'])]
pokedex += [Pokemon(806,"Blacephalon",['fire', 'ghost'],no_ability,"806","OU",['special attacker'])]
pokedex += [Pokemon(797,"Celesteela",['steel', 'flying'],no_ability,"797","OU",['physical wall', 'special wall'])]
pokedex += [Pokemon(719,"Diancie-Mega",['rock', 'fairy'],no_ability,"719-1","OU",['mega', 'special attacker', 'rock setter'])]
pokedex += [Pokemon(530,"Excadrill",['ground', 'steel'],no_ability,"530","OU",['physical attacker', 'rock setter', 'spiner'])]
pokedex += [Pokemon(598,"Ferrothorn",['grass', 'steel'],no_ability,"598","OU",['physical wall', 'rock setter'])]
pokedex += [Pokemon(445,"Garchomp",['dragon', 'ground'],no_ability,"445","OU",['physical attacker', 'rock setter'])]
pokedex += [Pokemon(472,"Gliscor",['ground', 'flying'],no_ability,"472","OU",['physical attacker', 'physical wall', 'rock setter', 'defoger'])]
pokedex += [Pokemon(658,"Greninja",['water', 'dark'],no_ability,"658","OU",['special attacker', 'priority user'])]
pokedex += [Pokemon(701,"Hawlucha",['fighting', 'flying'],no_ability,"701","OU",['physical attacker', 'defoger'])]
pokedex += [Pokemon(485,"Heatran",['fire', 'steel'],Flash_Fire,"485","OU",['special attacker', 'rock setter'])]
pokedex += [Pokemon(385,"Jirachi",['steel', 'psychic'],no_ability,"385","OU",['physical attacker', 'rock setter'])]
pokedex += [Pokemon(798,"Kartana",['grass', 'steel'],no_ability,"798","OU",['physical attacker'])]
pokedex += [Pokemon(647,"Keldeo",['water', 'fighting'],no_ability,"647","OU",['special attacker'])]
pokedex += [Pokemon(784,"Kommo-o",['dragon', 'fighting'],no_ability,"784","OU",['physical attacker', 'rock setter'])]
pokedex += [Pokemon(644,"Kyurem-Black",['dragon', 'ice'],no_ability,"646-2","OU",['physical attacker', 'special attacker'])]
pokedex += [Pokemon(644,"Landorus-Therian",['ground', 'flying'],no_ability,"645-1","OU",['physical attacker', 'rock setter', 'defoger'])]
pokedex += [Pokemon(428,"Lopunny-Mega",['normal', 'fighting'],no_ability,"428-1","OU",['mega', 'physical attacker', 'priority user'])]
pokedex += [Pokemon(801,"Magearna",['steel', 'fairy'],no_ability,"801","OU",['special attacker'])]
pokedex += [Pokemon(462,"Magnezone",['electric', 'steel'],no_ability,"462","OU",['special attacker'])]
pokedex += [Pokemon(303,"Mawile-Mega",['steel', 'fairy'],no_ability,"303-1","OU",['mega', 'physical attacker', 'rock setter', 'priority user'])]
pokedex += [Pokemon(308,"Medicham-Mega",['fighting', 'psychic'],no_ability,"308-1","OU",['mega', 'physical attacker', 'priority user'])]
pokedex += [Pokemon(279,"Pelipper",['water', 'flying'],no_ability,"279","OU",['physical wall', 'defoger'])]
pokedex += [Pokemon(477,"Rotom-Wash",['electric', 'water'],Levitate,"479-2","OU",['physical wall', 'special wall', 'defoger'])]
pokedex += [Pokemon(212,"Scizor-Mega",['bug', 'steel'],no_ability,"212-1","OU",['mega', 'physical attacker', 'physical wall', 'defoger', 'priority user'])]
pokedex += [Pokemon(497,"Serperior",['grass', 'none'],no_ability,"497","OU",['special attacker', 'defoger'])]
pokedex += [Pokemon(227,"Skarmory",['steel', 'flying'],no_ability,"227","OU",['physical wall', 'rock setter', 'defoger'])]
pokedex += [Pokemon(260,"Swampert-Mega",['water', 'ground'],no_ability,"260-1","OU",['mega', 'physical attacker', 'rock setter'])]
pokedex += [Pokemon(465,"Tangrowth",['grass', 'none'],no_ability,"465","OU",['physical wall', 'special wall'])]
pokedex += [Pokemon(787,"Tapu Bulu",['grass', 'fairy'],no_ability,"787","OU",['physical attacker'])]
pokedex += [Pokemon(788,"Tapu Fini",['water', 'fairy'],no_ability,"788","OU",['physical wall', 'special wall', 'defoger'])]
pokedex += [Pokemon(785,"Tapu Koko",['electric', 'fairy'],no_ability,"785","OU",['special attacker', 'defoger'])]
pokedex += [Pokemon(786,"Tapu Lele",['psychic', 'fairy'],no_ability,"786","OU",['special attacker', 'special wall'])]
pokedex += [Pokemon(640,"Tornadus-Therian",['flying', 'none'],no_ability,"641-1","OU",['special attacker', 'defoger'])]
pokedex += [Pokemon(748,"Toxapex",['poison', 'water'],no_ability,"748","OU",['physical wall', 'special wall'])]
pokedex += [Pokemon(248,"Tyranitar",['rock', 'dark'],no_ability,"248","OU",['physical attacker', 'rock setter'])]
pokedex += [Pokemon(248,"Tyranitar-Mega",['rock', 'dark'],no_ability,"248-1","OU",['mega', 'physical attacker', 'rock setter'])]
pokedex += [Pokemon(494,"Victini",['psychic', 'fire'],no_ability,"494","OU",['physical attacker'])]
pokedex += [Pokemon(637,"Volcarona",['bug', 'fire'],no_ability,"637","OU",['special attacker', 'defoger'])]
pokedex += [Pokemon(445,"Garchomp-Mega",['dragon', 'ground'],no_ability,"445-1","OU",['mega', 'physical attacker', 'rock setter'])]
