#This calculates the exp given after the battle

from replit import db
import math

from game_info import *
from pokemon_stats import * 
from evolutions import *
from moves import *


trainer_or_wild_multiplier = {
  "Trainer": 1.5,
  "Wild": 1
}

base_experience_yield = {
  "Bulbasaur": 64,
  "Ivysaur": 142,
  "Venusaur": 263, 
  "Charmander": 62,
  "Charmeleon": 142,
  "Charizard": 267,
  "Squirtle": 63,
  "Wartortle": 142,
  "Blastoise": 265,
  "Caterpie": 39,
  "Metapod": 72,
  "Butterfree": 198,
  "Weedle": 39,
  "Kakuna": 72,
  "Beedrill": 198,
  "Pidgey": 50,
  "Pidgeotto": 122,
  "Pidgeot": 240,
  "Rattata": 51,
  "Raticate": 145,
  "Spearow": 52,
  "Fearow": 155,
  "Ekans": 58,
  "Arbok": 157,
  "Pikachu": 112,
  "Raichu": 243,
  "Sandshrew": 60,
  "Sandslash": 158,
  "Nidoran Female": 55,
  "Nidorina": 128,
  "Nidoqueen": 253,
  "Nidoran Male": 55,
  "Nidorino": 128,
  "Nidoking": 253,
  "Clefairy": 113,
  "Clefable": 242,
  "Vulpix": 60,
  "Ninetales": 177,
  "Jigglypuff": 95,
  "Wigglytuff": 218,
  "Zubat": 49,
  "Golbat": 159,
  "Oddish": 64,
  "Gloom": 138,
  "Vileplume": 245,
  "Paras": 57,
  "Parasect": 142,
  "Venonat": 61,
  "Venomoth": 158,
  "Diglett": 53,
  "Dugtrio": 149,
  "Meowth": 58,
  "Persian": 154,
  "Psyduck": 64,
  "Golduck": 175,
  "Mankey": 61,
  "Primeape": 159,
  "Growlithe": 70,
  "Arcanine": 194,
  "Poliwag": 60,
  "Poliwhirl": 135,
  "Poliwrath": 255,
  "Abra": 62,
  "Kadabra": 140,
  "Alakazam": 250,
  "Machop": 61,
  "Machoke": 142,
  "Machamp": 253,
  "Bellsprout": 60,
  "Weepinbell": 137,
  "Victreebel": 245,
  "Tentacool": 67,
  "Tentacruel": 180,
  "Geodude": 60,
  "Graveler": 137,
  "Golem": 248,
  "Ponyta": 82,
  "Rapidash": 175,
  "Slowpoke": 63,
  "Slowbro": 172,
  "Magnemite": 65,
  "Magneton": 163,
  "Farfetch'd": 132,
  "Doduo": 62,
  "Dodrio": 165,
  "Seel": 65,
  "Dewgong": 166,
  "Grimer": 65,
  "Muk": 175,
  "Shellder": 61,
  "Cloyster": 184,
  "Gastly": 62,
  "Haunter": 142,
  "Gengar": 250,
  "Onix": 77,
  "Drowzee": 66,
  "Hypno": 169,
  "Krabby": 65,
  "Kingler": 166,
  "Voltorb": 66,
  "Electrode": 172,
  "Exeggcute": 65,
  "Exeggutor": 186,
  "Cubone": 64,
  "Marowak": 149,
  "Hitmonlee": 159,
  "Hitmonchan": 159,
  "Lickitung": 77,
  "Koffing": 68,
  "Weezing": 172,
  "Rhyhorn": 69,
  "Rhydon": 170,
  "Chansey": 395,
  "Tangela": 87,
  "Kangaskhan": 172, 
  "Horsea": 59,
  "Seadra": 154,
  "Goldeen": 64,
  "Seaking": 158,
  "Staryu": 68,
  "Starmie": 182,
  "Mr. Mime": 161,
  "Scyther": 100,
  "Jynx": 159,
  "Electabuzz": 172,
  "Magmar": 173,
  "Pinsir": 175,
  "Tauros": 172,
  "Magikarp": 40,
  "Gyarados": 189,
  "Lapras": 187,
  "Ditto": 101,
  "Eevee": 65,
  "Vaporeon": 184,
  "Jolteon": 184,
  "Flareon": 184,
  "Porygon": 79,
  "Omanyte": 71,
  "Omastar": 173,
  "Kabuto": 71,
  "Kabutops": 173,
  "Aerodactyl": 180,
  "Snorlax": 189,
  "Articuno": 290,
  "Zapdos": 290,
  "Moltres": 290,
  "Dratini": 60,
  "Dragonair": 147,
  "Dragonite": 300,
  "Mewtwo": 340,
  "Mew": 300  
}

def battle_rewards(trainer_or_wild, foe_level, pokemon_participated, foe_name):
  if trainer_or_wild == "Wild":
    money_received = round(base_experience_yield[foe_name] * (foe_level / 2))
    db["User Money"] += money_received
    print("\nYou received " + str(money_received) + " Poke Dollars!")
  
  for pokemon_element in pokemon_participated: 
    if db["Team Stats"][pokemon_element][current_health] <= 0:
      continue
      
    pokemon_name = pokemon_element.split(" ")[0]
    
    exp_received = round((trainer_or_wild_multiplier[trainer_or_wild] * base_experience_yield[foe_name] * foe_level) / (3 * len(pokemon_participated)))
    db["Team Stats"][pokemon_element][exp] += exp_received #This gives the exp to all of the necessary pokemon
    print("\n" + db["Team Stats"][pokemon_element][nickname] + " received " + str(exp_received) + " EXP!")
    
    if math.floor((db["Team Stats"][pokemon_element][exp]/1.25)**(1/3)) > db["Team Stats"][pokemon_element][level]: #This checks if the pokemon leveled up
      old_level = db["Team Stats"][pokemon_element][level] 
      
      db["Team Stats"][pokemon_element][level] = math.floor((db["Team Stats"][pokemon_element][exp]/1.25)**(1/3))
      print("\n" + db["Team Stats"][pokemon_element][nickname] + " leveled up!")

      for key_element in [*all_evolutions]: #This grabs the first evolution of the tree
        if pokemon_name in all_evolutions[key_element]:
          root_pokemon = key_element

      if db["Team Stats"][pokemon_element][level] >= 16 and len(all_evolutions[root_pokemon]) > 1: #This evolves the pokemon to second evolution
        if pokemon_name == all_evolutions[root_pokemon][0]: 
          print("\nWhat?\n" + db["Team Stats"][pokemon_element][nickname] + " is evolving!")
          
          while True:
            evolution_choice = input("\nWill you let your pokemon evolve (Yes or No)? ").lower()
            if evolution_choice == "yes" or evolution_choice == "no":
              break
            else:
              print("\nThat is not a valid choice.")

          if evolution_choice == "no":
            print("\nYou canceled the evolution.")
            continue
              
          new_pokemon_name = all_evolutions[root_pokemon][1] + " " + pokemon_element.split(" ")[1]
          db["Team Stats"][new_pokemon_name] = db["Team Stats"][pokemon_element]
          print("\n" + db["Team Stats"][pokemon_element][nickname] + " evolved into " + new_pokemon_name.split(" ")[0] + "!")
          del db["Team Stats"][pokemon_element]
          db["Team Order"][db["Team Order"].index(pokemon_element)] = new_pokemon_name
          if db["Team Stats"][new_pokemon_name][nickname] == pokemon_element.split(" ")[0]: #Changes nickname to same evolution stage if the user hasn't changed it
            db["Team Stats"][new_pokemon_name][nickname] = new_pokemon_name.split(" ")[0]

      try:
        if db["Team Stats"][pokemon_element][level] >= 32 and len(all_evolutions[root_pokemon]) > 2:
          if pokemon_name == all_evolutions[root_pokemon][1]: 
            print("\nWhat?\n" + db["Team Stats"][pokemon_element][nickname] + " is evolving!")
            
            while True:
              evolution_choice = input("\nWill you let your pokemon evolve (Yes or No)? ").lower()
              if evolution_choice == "yes" or evolution_choice == "no":
                break
              else:
                print("\nThat is not a valid choice.")
  
            if evolution_choice == "no":
              print("\nYou canceled the evolution.")
              continue
                
            new_pokemon_name = all_evolutions[root_pokemon][2] + " " + pokemon_element.split(" ")[1]
            db["Team Stats"][new_pokemon_name] = db["Team Stats"][pokemon_element]
            print("\n" + db["Team Stats"][pokemon_element][nickname] + " evolved into " + new_pokemon_name.split(" ")[0] + "!")
            del db["Team Stats"][pokemon_element]
            db["Team Order"][db["Team Order"].index(pokemon_element)] = new_pokemon_name
            if db["Team Stats"][new_pokemon_name][nickname] == pokemon_element.split(" ")[0]: #Changes nickname to same evolution stage if the user hasn't changed it
              db["Team Stats"][new_pokemon_name][nickname] = new_pokemon_name.split(" ")[0]
            
      except KeyError:
        placeholder = "Already evolved"

      try:
        new_pokemon_name = new_pokemon_name
        
      except NameError:
        new_pokemon_name = pokemon_element
        
      for index in range(math.floor(db["Team Stats"][new_pokemon_name][level]/4) - math.floor(old_level/4)):
        new_move = move_progression[new_pokemon_name.split(" ")[0]][math.floor((db["Team Stats"][new_pokemon_name][level]/4) + 1)]
        
        if "None" in db["Team Stats"][new_pokemon_name][moves]: 
          db["Team Stats"][new_pokemon_name][moves][db["Team Stats"][new_pokemon_name][moves].index("None")] = new_move
          print("\n" + db["Team Stats"][new_pokemon_name][nickname] + " learned " + new_move + "!") 
          
        else:
          print("\n" + db["Team Stats"][new_pokemon_name][nickname] + " wants to learn " + new_move + " but has already learned 4 moves.\n")

          for move_index in range(4): #This prints all four of the pokemon's moves plus the new move
            print(db["Team Stats"][new_pokemon_name][moves][move_index])
          print("\n" + new_move)

          while True:
            sel_move = input("\nWhich move would you like to remove? ")

            if sel_move in db["Team Stats"][new_pokemon_name][moves]: #This replaces sel_move with new_move
              db["Team Stats"][new_pokemon_name][moves][db["Team Stats"][new_pokemon_name][moves].index(sel_move)] = new_move
              print("\n" + db["Team Stats"][new_pokemon_name][nickname] + " forgot " + sel_move + ".\nAnd...\n" + db["Team Stats"][new_pokemon_name][nickname] + " learned " + new_move + "!") 
              break

            elif sel_move == new_move:
              print("\n" + db["Team Stats"][new_pokemon_name][nickname] + " chose not to learn " + new_move + ".")
              break

            else:
              print("\nEither that is not a valid move or it is the incorrect format.")

      db["Team Stats"][new_pokemon_name] = define_stats(db["Team Stats"][new_pokemon_name])
      print("\nThe stats of " + db["Team Stats"][new_pokemon_name][nickname] + " have increased.") 
