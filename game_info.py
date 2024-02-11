user_route_options = ["Route 1", "Route 2", "Route 3", "Route 4", "Route 5", "Route 6", "Route 7", "Route 8", "Route 9", "Route 11", "Route 12", "Route 13", "Route 14", "Route 15", "Route 16", "Route 18", "Route 19", "Route 20", "Route 21", "Route 22", "Route 23", "Route 24", "Route 25", "Viridian Forest", "Power Plant", "Rock Tunnel", "Cycling Road", "Safari Zone", "Seafoam Islands", "Victory Road"]

user_city_options = ["Pallet Town", "Viridian City", "Pewter City", "Mt. Moon", "Cerulean City", "Route 10", "Saffron City", "Lavender Town", "Celadon City", "Vermilion City", "Fuchsia City", "Cinnabar Island", "Indigo Plateau"] #Sorted this way to show which places are alright to spawn at after all pokemon faint

user_gui_options = ["Bag", "Pokemon", "Pokemart", "Pokemon Center", "Save", "Save and Quit"] #For obtaining items in a place, we could ask user if they wanted to explore or leave. If they pick explore, we can set a randomizer to get an item or encounter a pokemon. We should set a limit on the items if we do this.

#Name: [Level, EXP, Base Health, Base Attack, Base Defense, Base Sp. Attack, Base Sp. Defense, Base Speed, Max Health, Current Health, Attack, Defense, Sp. Attack, Sp. Defense, Speed, Type, Moves, Status Conditions, ID Number, Nickname]
level = 0
exp = 1
base_health = 2
base_attack = 3
base_defense = 4
base_sp_attack = 5
base_sp_defense = 6
base_speed = 7
max_health = 8
current_health = 9
attack = 10
defense = 11
sp_attack = 12
sp_defense = 13
speed = 14
type = 15
moves = 16
status_condition = 17
id_number = 18
nickname = 19

trainer_stats = {
  "Route 1": {},
  "Route 2": {},
  "Route 3": {
    "Lass 1": [135, ["Pidgey", "Pidgey"], [9, 9]],
    "Lass 2": [150, ["Rattata", "Nidoran Male"], [9, 9]],
    "Lass 3": [210, ["Jigglypuff"], [14]],
    "Bug Catcher 1": [100, ["Caterpie", "Weedle", "Caterpie"], [10, 10, 10]],
    "Bug Catcher 2": [90, ["Weedle", "Kakuna", "Caterpie", "Metapod"], [9, 9, 9, 9]],
    "Bug Catcher 3": [110, ["Caterpie", "Metapod"], [11, 11]],
    "Youngster 1": [165, ["Rattata", "Nidoran Male"], [11, 9]],
    "Youngster 2": [210, ["Spearow"], [14]],
  },
  "Route 4": {},
  "Route 5": {},
  "Route 6": {
    "Bug Catcher 1": [160, ["Weedle", "Caterpie", "Weedle"], [16, 16, 16]],
    "Bug Catcher 2": [200, ["Butterfree"], [20]],
    "Jr. Trainer 1": [400, ["Squirtle"], [20]],
    "Jr. Trainer 2": [320, ["Rattata", "Pikachu"], [16, 16]],
    "Jr. Trainer 3": [320, ["Pidgey", "Pidgey", "Pidgey"], [16, 16, 16]],
    "Jr. Trainer 4": [320, ["Spearow", "Raticate"], [16, 16]]
  },
  "Route 7": {},
  "Route 8": {
    "Lass 1": [330, ["Clefairy", "Clefairy"], [22, 22]],
    "Lass 2": [345, ["Nidoran Female", "Nidorina"], [23, 23]],
    "Lass 3": [360, ["Meowth", "Meowth", "Meowth"], [24, 24, 24]],
    "Lass 4": [285, ["Pidgey", "Rattata", "Nidoran Male", "Meowth", "Pikachu"], [19, 19, 19, 19, 19]],
    "Gambler 1": [1680, ["Growlithe", "Vulpix"], [24, 24]],
    "Gambler 2": [1540, ["Poliwag", "Poliwag", "Poliwhirl"], [22, 22, 22]],
    "Super Nerd 1": [550, ["Grimer", "Muk", "Grimer"], [22, 22, 22]],
    "Super Nerd 2": [650, ["Koffing"], [26]],
    "Super Nerd 3": [500, ["Voltorb", "Koffing", "Voltorb", "Magnemite"], [20, 20, 20, 20]],
  },
  "Route 9": {
    "Jr. Trainer 1": [360, ["Oddish", "Bellsprout", "Oddish", "Bellsprout"], [18, 18, 18, 18]],
    "Jr. Trainer 2": [420, ["Growlithe", "Charmander"], [21, 21]],
    "Jr. Trainer 3": [380, ["Rattata", "Diglett", "Ekans", "Sandshrew"], [19, 19, 19, 19]],
    "Jr. Trainer 4": [460, ["Meowth"], [23]],
    "Hiker 1": [700, ["Machop", "Onix"], [20, 20]],
    "Hiker 2": [735, ["Geodude", "Onix"], [21, 21]],
    "Hiker 3": [700, ["Geodude", "Machop", "Geodude"], [20, 20, 20]],
    "Bug Catcher 1": [190, ["Beedrill", "Beedrill"], [19, 19]],
    "Bug Catcher 2": [200, ["Caterpie", "Weedle", "Venonat"], [20, 20, 20]],
  },
  "Route 10": {
    "Jr. Trainer 1": [400, ["Pikachu", "Clefairy"], [20, 20]],
    "Jr. Trainer 2": [420, ["Pidgey", "Pidgeotto"], [21, 21]],
    "PokeManiac 1": [1500, ["Rhyhorn", "Lickitung"], [20, 20]],
    "PokeManiac 2": [1000, ["Cubone", "Slowpoke"], [20, 20]],
    "Hiker 1": [735, ["Geodude", "Onix"], [21, 21]],
    "Hiker 2": [665, ["Onix", "Graveler"], [19, 19]],
  },
  "Route 11": {
    "Gambler 1": [1260, ["Poliwag", "Horsea"], [18, 18]],
    "Gambler 2": [1260, ["Bellsprout", "Oddish"], [18, 18]],
    "Gambler 3": [1260, ["Growlithe", "Vulpix"], [18, 18]],
    "Gambler 4": [1260, ["Voltorb", "Magnemite"], [18, 18]],
    "Youngster 1": [315, ["Ekans"], [21]],
    "Youngster 2": [285, ["Sandshrew", "Zubat"], [19, 19]],
    "Youngster 3": [270, ["Nidoran Male", "Nidorino"], [18, 18]],
    "Youngster 4": [255, ["Rattata", "Rattata", "Raticate"], [17, 17, 17]],
    "Engineer 1": [1050, ["Magnemite"], [21]],
    "Engineer 2": [900, ["Magnemite", "Magnemite", "Magneton"], [18, 18, 18]],
  },
  "Route 12": {
    "Fisherman 1": [770, ["Goldeen", "Poliwag", "Goldeen"], [22, 22, 22]],
    "Fisherman 2": [840, ["Tentacool", "Goldeen"], [24, 24]],
    "Fisherman 3": [945, ["Goldeen"], [27]],
    "Fisherman 4": [735, ["Poliwag", "Shellder", "Goldeen", "Horsea"], [21, 21, 21, 21]],
    "Fisherman 5": [840, ["Magikarp", "Magikarp"], [24, 24]],
    "Rocker 1": [725, ["Voltorb", "Electrode"], [29, 29]],
    "Jr. Trainer 1": [840, ["Nidoran Male", "Nidorino"], [29, 29]],
  },
  "Route 13": {
    "Jr. Trainer 1": [560, ["Goldeen", "Poliwag", "Horsea"], [28, 28, 28]],
    "Jr. Trainer 2": [480, ["Pidgey", "Meowth", "Rattata", "Pikachu", "Meowth"], [24, 24, 24, 24, 24]],
    "Jr. Trainer 3": [600, ["Poliwag", "Poliwag"], [30, 30]],
    "Jr. Trainer 4": [540, ["Pidgey", "Meowth", "Pidgey", "Pidgeotto"], [27, 27, 27, 27]],
    "Bird Keeper 1": [725, ["Pidgey", "Pidgeotto"], [29, 29]],
    "Bird Keeper 2": [625, ["Spearow", "Pidgey", "Pidgey", "Spearow", "Spearow"], [25, 25, 25, 25, 25]],
    "Bird Keeper 3": [650, ["Pidgey", "Pidgeotto", "Spearow", "Fearow"], [26, 26, 26, 26]],
    "Beauty 1": [1890, ["Rattata", "Pikachu", "Rattata"], [27, 27, 27]],
    "Beauty 2": [2030, ["Clefairy", "Meowth"], [29, 29]],
    "Biker 1": [560, ["Koffing", "Koffing", "Koffing"], [28, 28, 28]],
  },
  "Route 14": {
    "Bird Keeper 1": [650, ["Pidgey", "Spearow", "Pidgey", "Fearow"], [26, 26, 26, 26]],
    "Bird Keeper 2": [700, ["Pidgey", "Doduo", "Pidgeotto"], [28, 28, 28]],
    "Bird Keeper 3": [725, ["Pidgeotto", "Fearow"], [29, 29]],
    "Bird Keeper 4": [700, ["Spearow", "Doduo", "Fearow"], [28, 28, 28]],
    "Bird Keeper 5": [825, ["Farfetch'd"], [33]],
    "Bird Keeper 6": [725, ["Spearow", "Fearow"], [29, 29]],
    "Biker 1": [580, ["Koffing", "Muk"], [29, 29]],
    "Biker 2": [580, ["Koffing", "Grimer"], [29, 29]],
    "Biker 3": [560, ["Grimer", "Grimer", "Koffing"], [28, 28, 28]],
    "Biker 4": [520, ["Koffing", "Koffing", "Grimer", "Koffing"], [26, 26, 26, 26]],
  },
  "Route 15": {
    "Jr. Trainer 1": [660, ["Clefairy"], [33]],
    "Jr. Trainer 2": [580, ["Pikachu", "Raichu"], [29, 29]],
    "Jr. Trainer 3": [560, ["Gloom", "Oddish", "Oddish"], [28, 28, 28]],
    "Jr. Trainer 4": [580, ["Bellsprout", "Oddish", "Tangela"], [29, 29, 29]],
    "Beauty 1": [2030, ["Pidgeotto", "Wigglytuff"], [29, 29]],
    "Beauty 2": [2030, ["Bulbasaur", "Ivysaur"], [29, 29]],
    "Biker 1": [500, ["Koffing", "Koffing", "Weezing", "Koffing", "Grimer"], [25, 25, 25, 25, 25]],
    "Biker 2": [560, ["Koffing", "Grimer", "Weezing"], [28, 28, 28]],
    "Bird Keeper 1": [700, ["Dodrio", "Doduo", "Doduo"], [28, 28, 28]],
    "Bird Keeper 2": [650, ["Pidgeotto", "Farfetch'd", "Doduo", "Pidgey"], [26, 26, 26, 26]],
  },
  "Route 16": {
    "Biker 1": [580, ["Grimer", "Koffing"], [29, 29]],
    "Biker 2": [660, ["Weezing"], [33]],
    "Biker 3": [520, ["Grimer", "Grimer", "Grimer", "Grimer"], [26, 26, 26, 26]],
    "Cue Ball 1": [700, ["Machop", "Mankey", "Machop"], [28, 28, 28]],
    "Cue Ball 2": [725, ["Mankey", "Machop"], [29, 29]],
    "Cue Ball 3": [825, ["Machop"], [33]],
  },
  "Route 18": {
    "Bird Keeper 1": [725, ["Spearow", "Fearow"], [29, 29]],
    "Bird Keeper 2": [650, ["Spearow", "Spearow", "Fearow", "Spearow"], [26, 26, 26, 26]],
    "Bird Keeper 3": [850, ["Dodrio"], [34]],
  },
  "Route 19": {
    "Swimmer 1": [150, ["Tentacool", "Shellder"], [30, 30]],
    "Swimmer 2": [145, ["Goldeen", "Horsea", "Staryu"], [29, 29, 29]],
    "Swimmer 3": [150, ["Horsea", "Horsea"], [30, 30]],
    "Swimmer 4": [150, ["Poliwag", "Poliwhirl"], [30, 30]],
    "Swimmer 5": [135, ["Horsea", "Tentacool", "Tentacool", "Goldeen"], [27, 27, 27, 27]],
    "Swimmer 6": [145, ["Goldeen", "Shellder", "Seaking"], [29, 29, 29]],
    "Swimmer 7": [135, ["Tentacool", "Tentacool", "Staryu", "Horsea", "Tentacruel"], [27, 27, 27, 27, 27]],
    "Beauty 1": [2100, ["Goldeen", "Seaking"], [30, 30]],
    "Beauty 2": [1890, ["Poliwag", "Goldeen", "Seaking", "Goldeen", "Poliwag"], [27, 27, 27, 27, 27]],
    "Beauty 3": [2030, ["Staryu", "Staryu", "Staryu"], [29, 29, 29]],
  },
  "Route 20": {
    "Swimmer 1": [155, ["Shellder", "Cloyster"], [31, 31]],
    "Swimmer 2": [140, ["Horsea", "Horsea", "Seadra", "Horsea"], [28, 28, 28, 28]],
    "Swimmer 3": [175, ["Staryu"], [35]],
    "Beauty 1": [2100, ["Seadra", "Horsea", "Seadra"], [30, 30, 30]],
    "Beauty 2": [2450, ["Seaking"], [35]],
    "Beauty 3": [2100, ["Shellder", "Shellder", "Cloyster"], [30, 30, 30]],
    "Beauty 4": [2170, ["Poliwag", "Seaking"], [31, 31]],
    "Jr. Trainer 1": [600, ["Tentacool", "Horsea", "Seel"], [30, 30, 30]],
    "Jr. Trainer 2": [620, ["Goldeen", "Seaking"], [31, 31]],
    "Bird Keeper 1": [750, ["Fearow", "Fearow", "Fearow"], [30, 30, 30]],
  },
  "Route 21": {
    "Fisherman 1": [945, ["Magikarp", "Magikarp", "Magikarp", "Magikarp", "Magikarp", "Magikarp"], [27, 27, 27, 27, 27, 27]],
    "Fisherman 2": [980, ["Seaking", "Goldeen", "Seaking", "Seaking"], [28, 28, 28, 28]],
    "Fisherman 3": [1085, ["Shellder", "Cloyster"], [31, 31]],
    "Fisherman 4": [1155, ["Seaking", "Goldeen"], [33, 33]],
    "Swimmer 1": [165, ["Seadra", "Tentacruel"], [33, 33]],
    "Swimmer 2": [185, ["Starmie"], [37]],
    "Swimmer 3": [165, ["Staryu", "Wartortle"], [33, 33]],
    "Swimmer 4": [160, ["Poliwhirl", "Tentacool", "Seadra"], [32, 32, 32]],
    "Cue Ball 1": [775, ["Tentacool", "Tentacool", "Tentacruel"], [31, 31, 31]],
  },
  "Route 22": {},
  "Route 23": {},
  "Route 24": {
    "Bug Catcher 1": [140, ["Caterpie", "Weedle"], [14, 14]],
    "Lass 1": [210, ["Pidgey", "Nidoran Female"], [14, 14]],
    "Lass 2": [240, ["Pidgey", "Nidoran Female"], [16, 16]],
    "Youngster 1": [210, ["Rattata", "Ekans", "Zubat"], [14, 14, 14]],
    "Jr. Trainer 1": [360, ["Mankey"], [18]],
    "Jr. Trainer 2": [280, ["Rattata", "Ekans"], [14, 14]],
    "Rocket 1": [450, ["Ekans", "Zubat"], [15, 15]],
  },
  "Route 25": {
    "Hiker 1": [525, ["Machop", "Geodude"], [15, 15]],
    "Hiker 2": [595, ["Onix"], [17]],
    "Hiker 3": [455, ["Geodude", "Geodude", "Machop", "Geodude"], [13, 13, 13, 13]],
    "Youngster 1": [225, ["Rattata", "Spearow"], [15, 15]],
    "Youngster 2": [255, ["Slowpoke"], [17]],
    "Youngster 3": [210, ["Ekans", "Sandshrew"], [14, 14]],
    "Lass 1": [225, ["Nidoran Male", "Nidoran Female"], [15, 15]],
    "Lass 2": [195, ["Oddish", "Pidgey", "Oddish"], [13, 13, 13]],
    "Jr. Trainer 1": [280, ["Rattata", "Ekans"], [14, 14]],
  },
  "Viridian Forest": {
    "Bug Catcher 1": [60, ["Weedle", "Caterpie"], [6, 6]],
    "Bug Catcher 2": [70, ["Weedle", "Kakuna", "Weedle"], [7, 7, 7]],
    "Bug Catcher 3": [90, ["Weedle"], [9]],
  },
  "Power Plant": {},
  "Rock Tunnel": {
    "PokeManiac 1": [1150, ["Cubone", "Slowpoke"], [23, 23]],
    "PokeManiac 2": [1250, ["Slowpoke"], [25]],
    "PokeManiac 3": [1100, ["Charmander", "Cubone"], [22, 22]],
    "PokeManiac 4": [1000, ["Slowpoke", "Slowpoke", "Slowpoke"], [20, 20, 20]],
    "Jr. Trainer 1": [440, ["Oddish", "Bulbasaur"], [22, 22]],
    "Jr. Trainer 2": [420, ["Jigglypuff", "Pidgey", "Meowth"], [21, 21, 21]],
    "Jr. Trainer 3": [440, ["Bellsprout", "Clefairy"], [22, 22]],
    "Jr. Trainer 4": [380, ["Pidgey", "Rattata", "Rattata", "Bellsprout"], [19, 19, 19, 19]],
    "Jr. Trainer 5": [420, ["Meowth", "Oddish", "Pidgey"], [20, 20, 20]],
    "Hiker 1": [875, ["Geodude"], [25]],
    "Hiker 2": [700, ["Machop", "Onix"], [20, 20]],
    "Hiker 3": [665, ["Geodude", "Machop", "Geodude", "Geodude"], [19, 19, 19, 19]],
    "Hiker 4": [700, ["Onix", "Onix", "Geodude"], [20, 20, 20]],
    "Hiker 5": [735, ["Geodude", "Graveler"], [21, 21]],
    "Hiker 6": [735, ["Geodude", "Geodude", "Graveler"], [21, 21, 21]],
  },
  "Cycling Road": {
    "Cue Ball 1": [725, ["Machop", "Machoke"], [29, 29]],
    "Cue Ball 2": [725, ["Mankey", "Primeape"], [29, 29]],
    "Cue Ball 3": [825, ["Machoke"], [33]],
    "Cue Ball 4": [725, ["Primeape", "Machoke"], [29, 29]],
    "Cue Ball 5": [650, ["Mankey", "Mankey", "Machoke", "Machop"], [26, 26, 26, 26]],
    "Biker 1": [560, ["Weezing", "Koffing", "Weezing"], [28, 28, 28]],
    "Biker 2": [660, ["Muk"], [33]],
    "Biker 3": [580, ["Voltorb", "Voltorb"], [29, 29]],
    "Biker 4": [580, ["Weezing", "Muk"], [29, 29]],
    "Biker 5": [500, ["Koffing", "Weezing", "Koffing", "Koffing", "Weezing"], [25, 25, 25, 25, 25]],
  },
  "Safari Zone": {},
  "Seafoam Islands": {},
  "Victory Road": {
    "Cooltrainer 1": [1540, ["Persian", "Ninetales"], [44, 44]],
    "Cooltrainer 2": [1470, ["Ivysaur", "Wartortle", "Charmeleon", "Charizard"], [42, 42, 42, 42]],
    "Cooltrainer 3": [1505, ["Exeggutor", "Cloyster", "Arcanine"], [43, 43, 43]],
    "Cooltrainer 4": [1505, ["Parasect", "Dewgong", "Chansey"], [43, 43, 43]],
    "Cooltrainer 5": [1505, ["Kingler", "Tentacruel", "Blastoise"], [43, 43, 43]],
    "Cooltrainer 6": [1505, ["Bellsprout", "Weepinbell", "Victreebel"], [43, 43, 43]],
    "Blackbelt 1": [1075, ["Machoke", "Machop", "Machoke"], [43, 43, 43]],
    "Juggler 1": [1435, ["Drowzee", "Hypno", "Kadabra", "Kadabra"], [41, 41, 41, 41]],
    "Juggler 2": [1680, ["Mr. Mime"], [48]],
    "Tamer 1": [1760, ["Persian", "Golduck"], [44, 44]],
    "PokeManiac 1": [2000, ["Charmeleon", "Lapras", "Lickitung"], [40, 40, 40]],
  },
  "Pewter Gym": {
    "Jr. Trainer 1": [220, ["Diglett", "Sandshrew"], [11, 11]],
  },
  "Cerulean Gym": {
    "Swimmer 1": [80, ["Horsea", "Shellder"], [16, 16]],
    "Jr. Trainer 1": [380, ["Goldeen"], [19]],
  },
  "Vermilion Gym": {
    "Sailor 1": [630, ["Pikachu", "Pikachu"], [21, 21]],
    "Rocker 1": [500, ["Voltorb", "Magnemite", "Voltorb"], [20, 20, 20]],
    "Gentleman 1": [1610, ["Pikachu"], [23]],
  },
  "Celadon Gym": {
    "Lass 1": [345, ["Bellsprout", "Weepinbell"], [23, 23]],
    "Beauty 1": [1470, ["Oddish", "Bellsprout", "Oddish", "Bellsprout"], [21, 21, 21, 21]],
    "Beauty 2": [1680, ["Bellsprout", "Bellsprout"], [23, 23]],
    "Jr. Trainer 1": [480, ["Bulbasaur", "Ivysaur"], [24, 24]],
    "Beauty 3": [1820, ["Exeggcute"], [26]],
    "Cooltrainer 1": [840, ["Weepinbell", "Gloom", "Ivysaur"], [24, 24, 24]],
    "Lass 2": [345, ["Oddish", "Gloom"], [23, 23]],
  },
  "Fuchsia Gym": {
    "Juggler 1": [1190, ["Drowzee", "Kadabra"], [34, 34]],
    "Juggler 2": [1330, ["Hypno"], [38]],
    "Juggler 3": [1470, ["Drowzee", "Drowzee", "Kadabra", "Drowzee"], [31, 31, 31, 31]],
    "Tamer 1": [1320, ["Arbok", "Sandslash", "Arbok"], [33, 33, 33]],
    "Tamer 2": [1360, ["Sandslash", "Arbok"], [34, 34]],
    "Juggler 4": [1190, ["Drowzee", "Hypno"], [34, 34]],
  },
  "Saffron Gym": {
    "Psychic 1": [330, ["Slowpoke", "Slowpoke", "Slowbro"], [33, 33, 33]],
    "Psychic 2": [340, ["Mr. Mime", "Kadabra"], [34, 34]],
    "Channeler 1": [1140, ["Haunter"], [38]],
    "Psychic 3": [380, ["Slowbro"], [38]],
    "Channeler 2": [1020, ["Gastly", "Haunter"], [34, 34]],
    "Channeler 3": [990, ["Gastly", "Gastly", "Haunter"], [33, 33, 33]],
    "Psychic 4": [310, ["Kadabra", "Slowpoke", "Mr. Mime", "Kadabra"], [31, 31, 31, 31]],
  },
  "Cinnabar Gym": {
    "Burglar 1": [3240, ["Growlithe", "Vulpix", "Ninetales"], [36, 36, 36]],
    "Super Nerd 1": [900, ["Vulpix", "Vulpix", "Ninetales"], [36, 36, 36]],
    "Super Nerd 2": [850, ["Ponyta", "Charmander", "Vulpix", "Growlithe"], [34, 34, 34, 34]],
    "Burglar 2": [3690, ["Ponyta"], [41]],
    "Super Nerd 3": [1025, ["Rapidash"], [41]],
    "Burglar 3": [3330, ["Vulpix", "Growlithe"], [37, 37]],
    "Super Nerd 4": [925, ["Growlithe", "Vulpix"], [37, 37]],
  },
  "Viridian Gym": {
    "Tamer 1": [1560, ["Arbok", "Tauros"], [39, 39]],
    "Blackbelt 1": [1075, ["Machoke"], [43]],
    "Cooltrainer 1": [1365, ["Nidorino", "Nidoking"], [39, 39]],
    "Tamer 2": [1720, ["Rhyhorn"], [43]],
    "Blackbelt 2": [1000, ["Machop", "Machoke"], [40, 40]],
    "Cooltrainer 2": [1365, ["Sandslash", "Dugtrio"], [39, 39]],
    "Cooltrainer 3": [1505, ["Rhyhorn"], [43]],
    "Blackbelt 3": [950, ["Machoke", "Machop", "Machoke"], [38, 38, 38]],
  },
  "Elite 4": {
    "Lorelei": [5544, ["Dewgong", "Cloyster", "Slowbro", "Jynx", "Lapras"], [54, 53, 54, 56, 56], [["Growl", "Aurora Beam", "Take Down", "None"], ["Shell Smash", "Aurora Beam", "Water Gun", "None"], ["Growl", "Water Gun", "Withdraw", "Amnesia"], ["Double Slap", "Ice Punch", "Body Slam", "None"], ["Body Slam", "Blizzard", "Hydro Pump", "None"]]],
    "Bruno": [5742, ["Onix", "Hitmonchan", "Hitmonlee", "Onix", "Machamp"], [53, 55, 55, 56, 58], [["Rock Throw", "Rage", "Slam", "Harden"], ["Ice Punch", "Thunder Punch", "Mega Punch", "None"], ["Jump Kick", "Hi Jump Kick", "Mega Kick", "None"], ["Rock Throw", "Rage", "Slam", "Harden"], ["Leer", "Submission", "None", "None"]]],
    "Agatha": [5940, ["Gengar", "Golbat", "Haunter", "Arbok", "Gengar"], [56, 56, 55, 58, 60], [["Hynosis", "Shadow Ball", "Dark Pulse", "None"], ["Screech", "Wing Attack", "Haze", "None"], ["Hynosis", "Shadow Ball", "Dark Pulse", "None"], ["Bite", "Glare", "Screech", "Acid"], ["Toxic", "Shadow Ball", "Dark Pulse", "None"]]],
    "Lance": [6138, ["Gyarados", "Dragonair", "Dragonair", "Aerodactyl", "Dragonite"], [58, 56, 56, 60, 62], [["Hydro Pump", "Leer", "Aqua Tail", "None"], ["Agility", "Slam", "Dragon Rush", "None"], ["Agility", "Slam", "Dragon Rush", "None"], ["Scary Face", "Bite", "Take Down", "None"], ["Agility", "Slam", "Fire Punch", "Thunder Punch"]]],
  }
}

gym_leader_stats = {
  "Pewter Gym": ["Gym Leader Brock", 1386, ["Geodude", "Onix"], [12, 14], [["Tackle", "Defense Curl", "None", "None"], ["Tackle", "Screech", "None", "None"]]],
  "Cerulean Gym": ["Gym Leader Misty", 2079, ["Staryu", "Starmie"], [18, 21], [["Tackle", "Water Gun", "None", "None"], ["Tackle", "Water Gun", "Bubble Beam", "None"]]],
  "Vermilion Gym": ["Gym Leader Lt. Surge", 2376, ["Voltorb", "Pikachu", "Raichu"], [21, 18, 24], [["Tackle", "Screech", "None", "None"], ["Thunder Shock", "Growl", "Thunder Wave", "Quick Attack"], ["Thunder Shock", "Growl", "Thunderbolt", "None"]]],
  "Celadon Gym": ["Gym Leader Erika", 2871, ["Victreebel", "Tangela", "Vileplume"], [29, 24, 29], [["Razor Leaf", "Poison Powder", "Sleep Powder", "None"], ["Growth", "Mega Drain", "None", "None"], ["Petal Dance", "Poison Powder", "Mega Drain", "Sleep Powder"]]],
  "Fuchsia Gym": ["Gym Leader Koga", 4257, ["Koffing", "Muk", "Koffing", "Weezing"], [37, 39, 37, 43], [["Tackle", "Smog", "Sludge", "Smokescreen"], ["Poison Gas", "Minimize", "Sludge", "None"], ["Tackle", "Smog", "Sludge", "Smokescreen"], ["Smog", "Sludge", "Toxic", "Self-destruct"]]],
  "Saffron Gym": ["Gym Leader Sabrina", 4257, ["Kadabra", "Mr. Mime", "Venomoth", "Alakazam"], [38, 37, 38, 43], [["Psybeam", "Recover", "Psychic", "None"], ["Confusion", "Double Slap", "None", "None"], ["Poison Powder", "Leech Life", "Stun Spore", "Psybeam"], ["Psybeam", "Recover", "None", "None"]]],
  "Cinnabar Gym": ["Gym Leader Blaine", 4653, ["Growlithe", "Ponyta", "Rapidash", "Arcanine"], [42, 40, 42, 47], [["Ember", "Leer", "Take Down", "Agility"], ["Tail Whip", "Stomp", "Growl", "None"], ["Tail Whip", "Stomp", "Growl", "None"], ["Ember", "Fire Blast", "Take Down", "None"]]],
  "Viridian Gym": ["Gym Leader Giovanni", 4950, ["Rhyhorn", "Dugtrio", "Nidoqueen", "Nidoking", "Rhydon"], [45, 42, 44, 45, 50], [["Stomp", "Tail Whip", "Fury Attack", "Horn Drill"], ["Growl", "Sand Attack", "Slash", "None"], ["Scratch", "Tail Whip", "Body Slam", "Poison Sting"], ["Tackle", "Horn Attack", "Poison Sting", "None"], ["Stomp", "Tail Whip", "Horn Drill", "None"]]],
}

pre_battle_quotes = {
  "Lass": ["Come battle me! My Pokemon pack a punch!", "Let’s have a fun Pokemon battle!"],
  "Bug Catcher": ["I came here with some friends to catch us some Bug Pokemon!", "If you take Bug Pokemon to school, you get to be instantly popular!"],
  "Youngster": ["Hi! I like shorts! They're comfy and easy to wear!", "I might be little, but I won't like it if you go easy on me!"],
  "Jr. Trainer": ["Have a battle with me!", "Get ready to lose!"],
  "Gambler": ["Time to throw the dice and see who wins!", "You're taking a mighty gamble fighting me!"],
  "Super Nerd": ["I'm married to science!", "I've calculated the chances of beating and have determined them to be 0!"],
  "Hiker": ["I inherited this big-boned body from my parents... I’m like a living mountain range...", "Ho there! You are a mountain standing in my way, aren’t ya?"],
  "PokeManiac": ["I normally only ever listen to classical music, but if I lose, I think I shall try a bit of new age!", "Here, come check out my pokemon!"],
  "Engineer": ["After this battle, I gotta go back and fix a broken generator.", "I'm in for a long night of fixing things."],
  "Fisherman": ["Fishing is such a calm experience. You should try it some time.", "Take a look at my fish!"],
  "Rocker": ["Time to rock your world!", "Get ready for an electrifying showdown!"],
  "Bird Keeper": ["I take injured birds in release them when they are recovered. Except for ones that want to stay with me.", "Do you ever wanna just be a bird and fly all over the place?"],
  "Beauty": ["Isn’t that nice... You’re still a kid... I wish I could go back...", "I’ve always wanted to be a Beauty, so I’ve made a fresh start, focusing on my appearance."],
  "Biker": ["Feeling the wind in your hair is the best about biking!", "You think you can beat me kid? Think again!"],
  "Cue Ball": ["Time to make you cry for your ma!", "Let's see who's really the best!"],
  "Swimmer": ["Swimming is really good for your body!", "I love swimming out into the ocean and seeing all of the interesting Pokemon!"],
  "Rocket": ["Team Rocket blasts off at the speed of light! Surrender now, or prepare to fight!", "Get ready for an explosive battle!"],
  "Cooltrainer": ["The main character of this story... I’ll tell you who it is!", "You seem quite confident. I’ll sink you straightaway."],
  "Blackbelt": ["Oh, I see. Would you like to be cut to pieces? Or do you prefer the role of punching bag?", "The sweat that drips before a battle... Don’t you love how cool it is?"],
  "Juggler": ["Learning to juggle is a wonderful challenge!", "Watch me juggle while we battle!"],
  "Tamer": ["Taming is a skill that requires patience and discipline.", "My Pokemon are the most disciplined Pokemon that you'll ever find!"],
  "Gym Leader Brock": ["I'm Brock! I'm Pewter's Gym Leader! I believe in rock hard defense and determination! That's why my Pokemon are all the Rock-type! Do you still want to challenge me? Fine then! Show me your best!"],
  "Gym Leader Misty": ["Hi, you're a new face! Trainers who want to turn pro have to have a policy about Pokemon! What is your approach when you catch Pokemon? My policy is an all-out offensive with Water-type Pokemon!"],
  "Gym Leader Lt. Surge": ["Hey, kid! What do you think you're doing here? You won't live long in combat! That's for sure! I tell you kid, electric Pokemon saved me during the war! They zapped my enemies into paralysis! The same as I'll do to you!"],
  "Gym Leader Erika": ["Hello. Lovely weather isn't it? It's so pleasant. ...Oh dear... I must have dozed off. Welcome. My name is Erika. I am the Leader of Celadon Gym. I teach the art of flower arranging. My Pokemon are of the grass-type. Oh, I'm sorry, I had no idea that you wished to challenge me. Very well, but I shall not lose."],
  "Gym Leader Koga": ["Fwahahaha! A mere child like you dares to challenge me? Very well, I shall show you true terror as a ninja master! You shall feel the despair of poison and sleep techniques!"],
  "Gym Leader Sabrina": ["I had a vision of your arrival! I have had psychic powers since I was a child. I first learned to bend spoons with my mind. I dislike fighting, but if you wish, I will show you my powers!"],
  "Gym Leader Blaine": ["Hah! I'm Blaine! I am the Leader of Cinnabar Gym! My fiery Pokemon will incinerate all challengers! Hah! You better have Burn Heal!"],
  "Gym Leader Giovanni": ["Fwahahaha! This is my hideout! I planned to resurrect Team Rocket here! But, you have caught me again! So be it! This time, I'm not holding back! Once more, you shall face Giovanni, the greatest trainer!"],
  "Lorelei": ["Welcome to Pokemon League! I am Lorelei of the Elite Four! No one can best me when it comes to icy Pokemon! Freezing moves are powerful! Your Pokemon will be at my mercy when they are frozen solid! Hahaha! Are you ready?"],
  "Bruno": ["I am Bruno of the Elite Four! Through rigorous training, people and Pokemon can become stronger! I've weight trained with my Pokemon! And that will never change! We will grind you down with our superior power! Hoo hah!"],
  "Agatha": ["I am Agatha of the Elite Four! Oak's taken a lot of interest in you, child! That old duff was once tough and handsome! That was decades ago! Now he just wants to fiddle with his Pokedex! He's wrong! Pokemon are for fighting! I'll show you how a real trainer fights!"],
  "Lance": ["Ah! I heard about you! I lead the Elite Four! You can call me Lance the dragon trainer! You know that dragons are mythical Pokemon! They're hard to catch and raise, but their powers are superior! They're virtually indestructible! Well, are you ready to lose? Your League challenge ends with me!"]
}

win_battle_quotes = {
  "Lass": ["Hehe! Mehehehehe! See? It’s fun to win!", "Seriously, winning a serious battle is seriously the best!"],
  "Bug Catcher": ["You amazed? You surprised? By the power of my Bug Pokemon?!", "Yay! My Bug Pokemon finally won me a battle!"],
  "Youngster": ["Yahoo! Ya-hoooooo! I did it! I won again!", "What do you think?! Hawesome, huh? My Pokémon and I are the strongest!"],
  "Jr. Trainer": ["What a match! I’m quite satisfied with the result.", "You amazed? You surprised? By the power of my Pokémon?!"],
  "Gambler": ["I guess the odds were in my favor this battle!", "That's the luck of a professional gambler for you!"],
  "Super Nerd": ["Ha! All according to my calculations!", "Of course I won! By comparing the statistics of both sides it was obvious that I had the advantage!"],
  "Hiker": ["Bwahaha! You’ll win, too, if you just up your calorie intake a bit!", "You’re no good at all, I tell ya! Wanna hide away in the mountains with me?"],
  "PokeManiac": ["This victory proves my true love for Pokémon.", "What do you think about my dear Pokémon? Great, right?"],
  "Engineer": ["How were my Pokémon? Powerful, weren’t they?", "My body and mind aren’t necessarily always in sync."],
  "Fisherman": ["You should not get angry at your Pokémon, even if you lose a battle.", "Pokémon...are nice... They may be selfish, but they won’t betray you."],
  "Rocker": ["I won! What an electrifying experience!", "My Pokemon really gave you a shock!"],
  "Bird Keeper": ["This proves my Pokémon have accepted my love.", "The most fun part of this job is getting close to Pokémon."],
  "Beauty": ["If you want to make your dreams reality, then you have to be completely dedicated!", "Uh-oh! You’re OK, aren’t you? Sorry I flew into a rage!"],
  "Biker": ["All right! I’m on my way now! My battle begins here!", "Winning bells are ringing, winning bells are ringing. Ding ding dong! Ding ding dong!"],
  "Cue Ball": ["When my hairstyle is looking really sharp, it gets me really fired up!", "Victory is what makes battling worth it. What what?! I just dropped knowledge!"],
  "Swimmer": ["No one can stop me now that I’m as fast as the wind itself!", "That speed! It’s electrastic!"],
  "Rocket": ["Ha! No one can outmatch Team Rocket", "Nice battle kid! I could feel the explosive power from here!"],
  "Cooltrainer": ["I am devoting my body and soul to Pokémon battles!", "All within my expectations... Nothing to be surprised about..."],
  "Blackbelt": ["Haha... I probably did not have to use my strongest kick on you.", "Being tired from battle with disheveled clothing... It’s cool! Isn’t it actually the coolest?"],
  "Juggler": ["Learning to juggle is a wonderful challenge!", "Watch me juggle while we battle!"],
  "Tamer": ["Taming is a skill that requires patience and discipline.", "My Pokemon are the most disciplined Pokemon that you'll ever find!"],
  "Gym Leader Brock": ["I'm Brock! I'm Pewter's Gym Leader! I believe in rock hard defense and determination! That's why my Pokemon are all the Rock-type! Do you still want to challenge me? Fine then! Show me your best!"],
  "Gym Leader Misty": ["Hi, you're a new face! Trainers who want to turn pro have to have a policy about Pokemon! What is your approach when you catch Pokemon? My policy is an all-out offensive with Water-type Pokemon!"],
  "Gym Leader Lt. Surge": ["Hey, kid! What do you think you're doing here? You won't live long in combat! That's for sure! I tell you kid, electric Pokemon saved me during the war! They zapped my enemies into paralysis! The same as I'll do to you!"],
  "Gym Leader Erika": ["Hello. Lovely weather isn't it? It's so pleasant. ...Oh dear... I must have dozed off. Welcome. My name is Erika. I am the Leader of Celadon Gym. I teach the art of flower arranging. My Pokemon are of the grass-type. Oh, I'm sorry, I had no idea that you wished to challenge me. Very well, but I shall not lose."],
  "Gym Leader Koga": ["Fwahahaha! A mere child like you dares to challenge me? Very well, I shall show you true terror as a ninja master! You shall feel the despair of poison and sleep techniques!"],
  "Gym Leader Sabrina": ["I had a vision of your arrival! I have had psychic powers since I was a child. I first learned to bend spoons with my mind. I dislike fighting, but if you wish, I will show you my powers!"],
  "Gym Leader Blaine": ["Hah! I'm Blaine! I am the Leader of Cinnabar Gym! My fiery Pokemon will incinerate all challengers! Hah! You better have Burn Heal!"],
  "Gym Leader Giovanni": ["Fwahahaha! This is my hideout! I planned to resurrect Team Rocket here! But, you have caught me again! So be it! This time, I'm not holding back! Once more, you shall face Giovanni, the greatest trainer!"],
  "Lorelei": ["Welcome to Pokemon League! I am Lorelei of the Elite Four! No one can best me when it comes to icy Pokemon! Freezing moves are powerful! Your Pokemon will be at my mercy when they are frozen solid! Hahaha! Are you ready?"],
  "Bruno": ["I am Bruno of the Elite Four! Through rigorous training, people and Pokemon can become stronger! I've weight trained with my Pokemon! And that will never change! We will grind you down with our superior power! Hoo hah!"],
  "Agatha": ["I am Agatha of the Elite Four! Oak's taken a lot of interest in you, child! That old duff was once tough and handsome! That was decades ago! Now he just wants to fiddle with his Pokedex! He's wrong! Pokemon are for fighting! I'll show you how a real trainer fights!"],
  "Lance": ["Ah! I heard about you! I lead the Elite Four! You can call me Lance the dragon trainer! You know that dragons are mythical Pokemon! They're hard to catch and raise, but their powers are superior! They're virtually indestructible! Well, are you ready to lose? Your League challenge ends with me!"]
}

stat_names = { 
  "Level": level,
  "EXP": exp,
  "Max Health": max_health,
  "Current Health": current_health,
  "Attack": attack,
  "Defense": defense,
  "Special Attack": sp_attack,
  "Special Defense": sp_defense,
  "Speed": speed,
  "Type": type,
  "Status Condition": status_condition
}

status_healing = {
  "Antidote": "Poisoned",
  "Awakening": "Asleep",
  "Burn Heal": "Burned",
  "Ice Heal": "Frozen",
  "Paralyze Heal": "Paralyzed"
}

item_cost = {
  "Pokeball": 200,
  "Greatball": 600,
  "Ultraball": 1200,
  "Potion": 300,
  "Super Potion": 700,
  "Hyper Potion": 1200,
  "Max Potion": 2500, 
  "Antidote": 100,
  "Awakening": 250,
  "Burn Heal": 250,
  "Ice Heal": 250,
  "Paralyze Heal": 200,
  "Revive": 1500,
  "Max Revive": 3000
}

battle_items = ["Pokeball", "Greatball", "Ultraball", "Potion", "Super Potion", "Hyper Potion", "Hyper Potion", "Max Potion", "Antidote", "Awakening", "Burn Heal", "Ice Heal", "Paralyze Heal", "Revive", "Max Revive"]

gym_list = ["Pewter Gym", "Cerulean Gym", "Vermilion Gym", "Celadon Gym", "Fuchsia Gym", "Saffron Gym", "Cinnabar Gym", "Viridian Gym"]

badge_list = ["Boulder Badge", "Cascade Badge", "Thunder Badge", "Rainbow Badge", "Soul Badge", "Marsh Badge", "Volcano Badge", "Earth Badge"]

tm_list = ["TM01", "TM02", "TM03", "TM05", "TM06", "TM07", "TM08", "TM09", "TM10", "TM11", "TM12", "TM13", "TM14", "TM15", "TM16", "TM17", "TM20", "TM21", "TM22", "TM24", "TM25", "TM26", "TM29", "TM30", "TM32", "TM36", "TM37", "TM38", "TM39", "TM40", "TM41", "TM43", "TM45", "TM47", "TM48", "TM49"]

gym_locations = { 
  "Pewter City": "Pewter Gym",
  "Cerulean City": "Cerulean Gym",
  "Vermilion City": "Vermilion Gym",
  "Celadon City": "Celadon Gym",
  "Fuchsia City": "Fuchsia Gym",
  "Saffron City": "Saffron Gym",
  "Cinnabar Island": "Cinnabar Gym",
  "Viridian City": "Viridian Gym"
}

badge_locations = {
  "Pewter Gym": "Boulder Badge",
  "Cerulean Gym": "Cascade Badge",
  "Vermilion Gym": "Thunder Badge",
  "Celadon Gym": "Rainbow Badge",
  "Fuchsia Gym": "Soul Badge",
  "Saffron Gym": "Marsh Badge",
  "Cinnabar Gym": "Volcano Badge",
  "Viridian Gym": "Earth Badge"
}

tm_rewards = {
  "Pewter Gym": "TM34",
  "Cerulean Gym": "TM11",
  "Vermilion Gym": "TM24",
  "Celadon Gym": "TM21",
  "Fuchsia Gym": "TM06",
  "Saffron Gym": "TM46",
  "Cinnabar Gym": "TM38",
  "Viridian Gym": "TM27"
}

elite_four_members = ["Lorelei", "Bruno", "Agatha", "Lance"]