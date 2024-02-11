#This calculates the catch chance given the pokemon's stats and the pokeball used

from replit import db
import time
import random

from game_info import *


catch_rate = {
  "Bulbasaur": 45,
  "Ivysaur": 45,
  "Venusaur": 45, 
  "Charmander": 45,
  "Charmeleon": 45,
  "Charizard": 45,
  "Squirtle": 45,
  "Wartortle": 45,
  "Blastoise": 45,
  "Caterpie": 255,
  "Metapod": 120,
  "Butterfree": 45,
  "Weedle": 255,
  "Kakuna": 120,
  "Beedrill": 45,
  "Pidgey": 255,
  "Pidgeotto": 120,
  "Pidgeot": 45,
  "Rattata": 255,
  "Raticate": 127,
  "Spearow": 255,
  "Fearow": 90,
  "Ekans": 255,
  "Arbok": 90,
  "Pikachu": 190,
  "Raichu": 75,
  "Sandshrew": 255,
  "Sandslash": 90,
  "Nidoran Female": 235,
  "Nidorina": 120,
  "Nidoqueen": 45,
  "Nidoran Male": 235,
  "Nidorino": 120,
  "Nidoking": 45,
  "Clefairy": 150,
  "Clefable": 25,
  "Vulpix": 190,
  "Ninetales": 75,
  "Jigglypuff": 170,
  "Wigglytuff": 50,
  "Zubat": 255,
  "Golbat": 90,
  "Oddish": 255,
  "Gloom": 120,
  "Vileplume": 45,
  "Paras": 190,
  "Parasect": 75,
  "Venonat": 190,
  "Venomoth": 75,
  "Diglett": 255,
  "Dugtrio": 50,
  "Meowth": 255,
  "Persian": 90,
  "Psyduck": 190,
  "Golduck": 75,
  "Mankey": 190,
  "Primeape": 75,
  "Growlithe": 190,
  "Arcanine": 75,
  "Poliwag": 255,
  "Poliwhirl": 120,
  "Poliwrath": 45,
  "Abra": 200,
  "Kadabra": 100,
  "Alakazam": 50,
  "Machop": 180,
  "Machoke": 90,
  "Machamp": 45,
  "Bellsprout": 255,
  "Weepinbell": 120,
  "Victreebel": 45,
  "Tentacool": 190,
  "Tentacruel": 60,
  "Geodude": 255,
  "Graveler": 120,
  "Golem": 45,
  "Ponyta": 190,
  "Rapidash": 60,
  "Slowpoke": 190,
  "Slowbro": 75,
  "Magnemite": 190,
  "Magneton": 60,
  "Farfetch'd": 45,
  "Doduo": 190,
  "Dodrio": 45,
  "Seel": 190,
  "Dewgong": 75,
  "Grimer": 190,
  "Muk": 75,
  "Shellder": 190,
  "Cloyster": 60,
  "Gastly": 190,
  "Haunter": 90,
  "Gengar": 45,
  "Onix": 45,
  "Drowzee": 190,
  "Hypno": 75,
  "Krabby": 225,
  "Kingler": 60,
  "Voltorb": 190,
  "Electrode": 60,
  "Exeggcute": 90,
  "Exeggutor": 45,
  "Cubone": 190,
  "Marowak": 75,
  "Hitmonlee": 45,
  "Hitmonchan": 45,
  "Lickitung": 45,
  "Koffing": 190,
  "Weezing": 60,
  "Rhyhorn": 120,
  "Rhydon": 60,
  "Chansey": 30,
  "Tangela": 45,
  "Kangaskhan": 45, 
  "Horsea": 225,
  "Seadra": 75,
  "Goldeen": 225,
  "Seaking": 60,
  "Staryu": 225,
  "Starmie": 60,
  "Mr. Mime": 45,
  "Scyther": 45,
  "Jynx": 45,
  "Electabuzz": 45,
  "Magmar": 45,
  "Pinsir": 45,
  "Tauros": 45,
  "Magikarp": 255,
  "Gyarados": 45,
  "Lapras": 45,
  "Ditto": 35,
  "Eevee": 45,
  "Vaporeon": 45,
  "Jolteon": 45,
  "Flareon": 45,
  "Porygon": 45,
  "Omanyte": 45,
  "Omastar": 45,
  "Kabuto": 45,
  "Kabutops": 45,
  "Aerodactyl": 45,
  "Snorlax": 25,
  "Articuno": 3,
  "Zapdos": 3,
  "Moltres": 3,
  "Dratini": 45,
  "Dragonair": 27,
  "Dragonite": 9,
  "Mewtwo": 3,
  "Mew": 45  
}

ball_bonus = {
  "Pokeball": 1,
  "Greatball": 1.5,
  "Ultraball": 2
}

status_bonus = {
  "Poisoned": 1.5,
  "Asleep": 2,
  "Burned": 1.5,
  "Frozen": 2,
  "Paralyzed": 1.5,
  "None": 1
}


def catch_chance(pokeball_type, foe_name, sel_foe_stats):
  a = ((3 * sel_foe_stats[max_health] - 2 * sel_foe_stats[current_health]) * catch_rate[foe_name] * ball_bonus[pokeball_type] * status_bonus[sel_foe_stats[status_condition]]) / (3 * sel_foe_stats[max_health])

  if a >= 255:
    return 1000

  b = (2 ** 16 - 1) * (a / (2 ** 8 -1)) ** 0.25

  p = ((b + 1) / (2 ** 16)) ** 4

  return round(p * 1000)
  

def catch_pokemon(pokeball_type, foe_name, sel_foe_stats): #Print if catch failed or not in this function
  print("\nYou used a " + pokeball_type + ".")

  time.sleep(3)
  
  rand_int = random.randint(1, 1000)

  if rand_int <= catch_chance(pokeball_type, foe_name, sel_foe_stats):
    print("\n" + foe_name + " was caught!")

    db["Collected Pokemon"] += 1
    foe_name = foe_name + " #" + str(db["Collected Pokemon"])
    sel_foe_stats[id_number] = db["Collected Pokemon"]

    if len(db["Team Order"]) < 6:
      db["Team Stats"][foe_name] = sel_foe_stats
      db["Team Order"].append(foe_name)
      print("\n" + foe_name + " was added to your party.")

    else:
      db["PC"][foe_name] = sel_foe_stats 
      print("\n" + foe_name + " was sent to the pc.")

    return True
  
  else:
    print("\nDarn! The pokemon broke free!")
    
    return False