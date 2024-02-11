#This creates functions for every place in Kanto

import random
import sys
import time
from replit import db

from choice_functions import *
from pc_functions import * 
from battle import *
from game_info import *


def remove_end_number(name):
  name_list = name.split(" ") 

  if len(name_list) <= 2:
    shortened_name = name_list[0]

  elif len(name_list) == 3:
    shortened_name = name_list[0] + " " + name_list[1]

  return shortened_name


def user_has_all_badges():
  if db["User Bag"]["Boulder Badge"] == 0:
    print("\nYou do not have the Boulder Badge! Go defeat the Gym Leader in Pewter City to obtain the Boulder Badge!")
    return False
    
  if db["User Bag"]["Cascade Badge"] == 0:
    print("\nYou do not have the Cascade Badge! Go defeat the Gym Leader in Cerulean City to obtain the Cascade Badge!")
    return False
    
  if db["User Bag"]["Thunder Badge"] == 0:
    print("\nYou do not have the Thunder Badge! Go defeat the Gym Leader in Vermilion City to obtain the Thunder Badge!")
    return False
    
  if db["User Bag"]["Rainbow Badge"] == 0:
    print("\nYou do not have the Rainbow Badge! Go defeat the Gym Leader in Celadon City to obtain the Rainbow Badge!")
    return False
    
  if db["User Bag"]["Soul Badge"] == 0:
    print("\nYou do not have the Soul Badge! Go defeat the Gym Leader in Fuchsia City to obtain the Soul Badge!")
    return False
    
  if db["User Bag"]["Marsh Badge"] == 0:
    print("\nYou do not have the Marsh Badge! Go defeat the Gym Leader in Saffron City to obtain the Marsh Badge!")
    return False
    
  if db["User Bag"]["Volcano Badge"] == 0:
    print("\nYou do not have the Volcano Badge! Go defeat the Gym Leader in Cinnabar Island to obtain the Volcano Badge!")
    return False
    
  if db["User Bag"]["Earth Badge"] == 0:
    print("\nYou do not have the Earth Badge! Go defeat the Gym Leader in Viridian City to obtain the Earth Badge!")
    return False

  return True


def route_one():
  while True:  
    print("\nPallet Town     Viridian City     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Pallet Town":
      print("\nYou walked to Pallet Town.")
      return db["User Choice"]

    elif db["User Choice"] == "Viridian City":
      print("\nYou walked to Viridian City.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      encounter_outcome = wild_pokemon_encounter(2, 5, ["Pidgey", "Rattata"], [50, 50]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_two():
  while True:  
    print("\nViridian City     Viridian Forest     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Viridian City":
      print("\nYou walked to Viridian City.")
      return db["User Choice"]

    elif db["User Choice"] == "Viridian Forest":
      print("\nYou walked to Viridian Forest.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      encounter_outcome = wild_pokemon_encounter(2, 5, ["Pidgey", "Rattata", "Caterpie"], [45, 40, 15]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_three():
  while True:  
    print("\nPewter City     Mt. Moon     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Pewter City":
      print("\nYou walked to Pewter City.")
      return db["User Choice"]

    elif db["User Choice"] == "Mt. Moon":
      print("\nYou walked to Mt. Moon.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore":
      rand_num = random.randint(1, 4)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num == 2 and len(db["Item Locations"][db["User Location"]]) > 0:
        time.sleep(3)
        rand_item = db["Item Locations"][db["User Location"]][random.randint(0, len(db["Item Locations"][db["User Location"]]) - 1)]

        db["User Bag"][remove_end_number(rand_item)] += int(rand_item.split(" ")[-1]) #This adds the item to the user bag

        if int(rand_item.split(" ")[-1]) == 1: #This tells the user what they found
          print("\nYou found a " + remove_end_number(rand_item) + "!")

        else:
          print("\nYou found " + rand_item.split(" ")[-1] + " " + remove_end_number(rand_item) + "!")

      elif rand_num <= 4:  
        encounter_outcome = wild_pokemon_encounter(3, 8, ["Pidgey", "Spearow", "Jigglypuff"], [45, 45, 10]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_four():
  while True:  
    print("\nMt. Moon     Cerulean City     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Mt. Moon":
      print("\nYou walked to Mt. Moon.")
      return db["User Choice"]

    elif db["User Choice"] == "Cerulean City":
      print("\nYou walked to Cerulean City.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      encounter_outcome = wild_pokemon_encounter(6, 15, ["Rattata", "Spearow", "Sandshrew", "Magikarp", "Poliwag", "Goldeen", "Psyduck", "Krabby"], [20, 17, 13, 10, 10, 10, 10, 10]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_five():
  while True:  
    print("\nCerulean City     Saffron City     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Cerulean City":
      print("\nYou walked to Cerulean City.")
      return db["User Choice"]

    elif db["User Choice"] == "Saffron City":
      print("\nYou walked to Saffron City.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      encounter_outcome = wild_pokemon_encounter(10, 16, ["Pidgey", "Meowth", "Bellsprout"], [40, 25, 35]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_six():
  while True:  
    print("\nSaffron City     Vermilion City     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Saffron City":
      print("\nYou walked to Saffron City.")
      return db["User Choice"]

    elif db["User Choice"] == "Vermilion City":
      print("\nYou walked to Vermilion City.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore":
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(10, 16, ["Pidgey", "Meowth", "Bellsprout", "Magikarp", "Poliwag", "Goldeen", "Shellder", "Krabby"], [20, 12, 18, 10, 10, 10, 10, 10]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_seven():
  while True:  
    print("\nSaffron City     Lavender Town     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Saffron City":
      print("\nYou walked to Saffron City.")
      return db["User Choice"]

    elif db["User Choice"] == "Lavender Town":
      print("\nYou walked to Lavender Town.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      encounter_outcome = wild_pokemon_encounter(17, 22, ["Pidgey", "Vulpix", "Meowth", "Bellsprout"], [30, 10, 30, 30]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_eight():
  while True:  
    print("\nSaffron City     Celadon City     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Saffron City":
      print("\nYou walked to Saffron City.")
      return db["User Choice"]

    elif db["User Choice"] == "Celadon City":
      print("\nYou walked to Celadon City.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore":
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(15, 20, ["Pidgey", "Sandshrew", "Vulpix", "Meowth"], [35, 20, 20, 25]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_nine():
  while True:  
    print("\nCerulean City     Route 10     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Cerulean City":
      print("\nYou walked to Cerulean City.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 10":
      print("\nYou walked to Route 10.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore":
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(11, 17, ["Rattata", "Spearow", "Sandshrew"], [40, 35, 25])
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_eleven():
  while True:  
    print("\nVermilion City     Route 12     Route 13     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Vermilion City":
      print("\nYou walked to Vermilion City.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 12":
      print("\nYou walked to Route 12.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 13":
      print("\nYou walked to Route 13.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore":
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(9, 17, ["Spearow", "Sandshrew", "Drowzee", "Magikarp", "Poliwag", "Goldeen", "Shellder", "Krabby"], [17, 20, 13, 10, 10, 10, 10, 10]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_twelve():
  while True:  
    print("\nRoute 11     Route 13     Lavender Town     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 11":
      print("\nYou walked to Route 11.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 13":
      print("\nYou walked to Route 13.")
      return db["User Choice"]

    elif db["User Choice"] == "Lavender Town":
      print("\nYou walked to Lavender Town.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore":
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(22, 30, ["Pidgey", "Venonat", "Bellsprout", "Weepinbell", "Snorlax", "Magikarp", "Poliwag", "Goldeen", "Tentacool", "Krabby"], [17, 10, 15, 5, 3, 10, 10, 10, 10, 10]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_thirteen():
  while True:  
    print("\nRoute 11     Route 12     Route 14     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 11":
      print("\nYou walked to Route 11.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 12":
      print("\nYou walked to Route 12.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 14":
      print("\nYou walked to Route 14.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": 
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(22, 30, ["Pidgey", "Venonat", "Bellsprout", "Weepinbell", "Ditto", "Magikarp", "Poliwag", "Goldeen", "Tentacool", "Krabby"], [15, 10, 15, 5, 5, 10, 10, 10, 10, 10]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_fourteen():
  while True:  
    print("\nRoute 13     Route 15     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 13":
      print("\nYou walked to Route 13.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 15":
      print("\nYou walked to Route 15.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore":
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(22, 30, ["Pidgey", "Pidgeotto", "Venonat", "Bellsprout", "Weepinbell", "Ditto"], [15, 5, 20, 40, 5, 15]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_fifteen():
  while True:  
    print("\nRoute 14     Fuchsia City     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 14":
      print("\nYou walked to Route 14.")
      return db["User Choice"]

    elif db["User Choice"] == "Fuchsia City":
      print("\nYou walked to Fuchsia City.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore":
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(22, 30, ["Pidgey", "Pidgeotto", "Venonat", "Bellsprout", "Weepinbell", "Ditto"], [15, 5, 20, 40, 5, 15]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_sixteen():
  while True:  
    print("\nCeladon City     Cycling Road     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Celadon City":
      print("\nYou walked to Celadon City.")
      return db["User Choice"]

    elif db["User Choice"] == "Cycling Road":
      print("\nYou walked to Cycling Road.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": 
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(18, 25, ["Rattata", "Raticate", "Spearow", "Doduo"], [30, 5, 40, 25]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_eighteen():
  while True:  
    print("\nCycling Road     Fuchsia City     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Cycling Road":
      print("\nYou walked to Cycling Road.")
      return db["User Choice"]

    elif db["User Choice"] == "Fuchsia City":
      print("\nYou walked to Fuchsia City.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": 
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(20, 29, ["Raticate", "Spearow", "Fearow", "Doduo"], [20, 40, 15, 25]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_nineteen():
  while True:  
    print("\nFuchsia City     Seafoam Islands     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Fuchsia City":
      print("\nYou swam to Fuchsia City.")
      return db["User Choice"]

    elif db["User Choice"] == "Seafoam Islands":
      print("\nYou swam to Seafoam Islands.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": 
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(10, 15, ["Magikarp", "Poliwag", "Goldeen", "Shellder", "Horsea", "Staryu"], [15, 20, 20, 15, 15, 15]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_twenty():
  while True:  
    print("\nSeafoam Islands     Cinnabar Island     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Seafoam Islands":
      print("\nYou swam to Seafoam Islands.")
      return db["User Choice"]

    elif db["User Choice"] == "Cinnabar Island":
      print("\nYou swam to Cinnabar Island.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": 
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(10, 15, ["Magikarp", "Poliwag", "Goldeen", "Shellder", "Horsea", "Staryu"], [15, 20, 20, 15, 15, 15]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_twenty_one():
  while True:  
    print("\nSeafoam Islands     Cinnabar Island     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Seafoam Islands":
      print("\nYou walked to Seafoam Islands.")
      return db["User Choice"]

    elif db["User Choice"] == "Cinnabar Island":
      print("\nYou walked to Cinnabar Island.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": 
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(21, 32, ["Pidgey", "Pidgeotto", "Rattata", "Raticate", "Tangela", "Magikarp", "Poliwag", "Goldeen", "Shellder", "Horsea", "Staryu"], [12, 8, 17, 8, 5, 7, 10, 10, 8, 7, 8]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_twenty_two():
  while True:  
    print("\nViridian City     Route 23     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Viridian City":
      print("\nYou walked to Viridian City.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 23":
      if user_has_all_badges():
        print("\nYou walked to Route 23.")
        return db["User Choice"]
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      encounter_outcome = wild_pokemon_encounter(2, 10, ["Rattata", "Spearow", "Nidoran Female", "Nidoran Male", "Magikarp", "Poliwag", "Goldeen"], [25, 5, 20, 5, 15, 15, 15]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_twenty_three():
  while True:  
    print("\nRoute 22     Victory Road     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 22":
      print("\nYou walked to Route 22.")
      return db["User Choice"]

    elif db["User Choice"] == "Victory Road":
      print("\nYou walked to Victory Road.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      encounter_outcome = wild_pokemon_encounter(26, 43, ["Spearow", "Fearow", "Sandshrew", "Sandslash", "Ditto", "Magikarp", "Poliwag", "Goldeen", "Slowbro", "Kingler", "Seadra", "Seaking"], [8, 12, 12, 3, 15, 5, 5, 5, 10, 10, 10, 5]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_twenty_four():
  while True:  
    print("\nCerulean City     Route 25     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Cerulean City":
      print("\nYou walked to Cerulean City.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 25":
      print("\nYou walked to Route 25.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": 
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(7, 14, ["Caterpie", "Metapod", "Pidgey", "Abra", "Bellsprout", "Magikarp", "Poliwag", "Goldeen", "Psyduck", "Krabby"], [10, 10, 10, 8, 12, 10, 10, 10, 10, 10]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_twenty_five():
  while True:  
    print("\nRoute 24     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 24":
      print("\nYou walked to Route 24.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": 
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(7, 14, ["Caterpie", "Metapod", "Pidgey", "Abra", "Bellsprout", "Magikarp", "Poliwag", "Goldeen", "Psyduck", "Krabby"], [10, 10, 10, 8, 12, 10, 10, 10, 10, 10]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def viridian_forest():
  while True:  
    print("\nRoute 2     Pewter City     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 2":
      print("\nYou walked to Route 2.")
      return db["User Choice"]

    elif db["User Choice"] == "Pewter City":
      print("\nYou walked to Pewter City.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore":
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(3, 6, ["Caterpie", "Metapod", "Weedle", "Kakuna", "Pikachu"], [45, 40, 5, 5, 5]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def power_plant():
  while True:  
    print("\nRoute 10     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 10":
      print("\nYou walked to Route 10.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      encounter_outcome = wild_pokemon_encounter(20, 36, ["Pikachu", "Raichu", "Magnemite", "Magneton", "Voltorb"], [25, 5, 25, 10, 35])
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def rock_tunnel():
  while True:  
    print("\nRoute 10     Lavender Town     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 10":
      print("\nYou walked to Route 10.")
      return db["User Choice"]

    elif db["User Choice"] == "Lavender Town":
      print("\nYou walked to Lavender Town.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore":
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(13, 18, ["Zubat", "Geodude", "Machop", "Onix"], [50, 25, 15, 10])
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def cycling_road():
  while True:  
    print("\nRoute 16     Route 18     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 16":
      print("\nYou walked to Route 16.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 18":
      print("\nYou walked to Route 18.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore":
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(20, 29, ["Raticate", "Spearow", "Fearow", "Doduo", "Magikarp", "Poliwag", "Goldeen", "Tentacool", "Krabby"], [15, 18, 5, 12, 10, 10, 10, 10, 10])
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def safari_zone():
  while True:  
    print("\nFuchsia City     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Fuchsia City":
      print("\nYou walked to Fuchsia City.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      encounter_outcome = wild_pokemon_encounter(22, 33, ["Nidoran Female", "Nidorina", "Nidoran Male", "Nidorino", "Paras", "Parasect", "Venonat", "Venomoth", "Exeggcute", "Rhyhorn", "Chansey", "Doduo", "Pinsir", "Scyther", "Tauros", "Kangaskhan", "Dratini"], [8, 4, 8, 4, 10, 5, 8, 4, 8, 4, 4, 8, 6, 4, 6, 5, 4])
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def seafoam_islands():
  while True:  
    print("\nRoute 19     Route 20     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 19":
      print("\nYou swam to Route 19.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 20":
      print("\nYou swam to Route 20.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      encounter_outcome = wild_pokemon_encounter(21, 38, ["Zubat", "Golbat", "Psyduck", "Golduck", "Slowpoke", "Slobro", "Seel", "Dewgong", "Shellder", "Krabby", "Kingler", "Horsea", "Staryu", "Magikarp", "Poliwag", "Goldeen"], [10, 5, 8, 4, 10, 5, 8, 4, 5, 10, 5, 8, 6, 4, 4, 4])
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def victory_road():
  while True:  
    print("\nRoute 23     Indigo Plateau     Explore     Bag     Pokemon     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 23":
      print("\nYou walked to Route 23.")
      return db["User Choice"]

    elif db["User Choice"] == "Indigo Plateau":
      print("\nYou walked to Indigo Plateau.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore":
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(22, 45, ["Zubat", "Golbat", "Venomoth", "Machop", "Machoke", "Geodude", "Graveler", "Onix", "Marowak"], [15, 5, 10, 20, 5, 15, 5, 20, 5])
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")
      
#######################################################################

def pallet_town():
  while True:
    print("\nRoute 1     Explore     Bag     Pokemon     Pokemon Center     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 1":
      print("\nYou walked to Route 1.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      print("\nSearching...")
      time.sleep(3)
      print("\nYou didn't find anything!")
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
      
    elif db["User Choice"] == "Pokemon Center":
      while True:
        db["User Choice"] = input("\nWould you like to heal your pokemon or access your pc? ").lower()

        if "heal" in db["User Choice"]:
          pokemon_center()
          break
          
        elif "pc" in db["User Choice"]:
          access_pc()
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def viridian_city():
  while True:
    print("\nRoute 1     Route 2     Viridian Gym     Explore     Bag     Pokemon     Poke Mart     Pokemon Center     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 1":
      print("\nYou walked to Route 1.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 2":
      print("\nYou walked to Route 2.")
      return db["User Choice"]

    elif db["User Choice"] == "Viridian Gym":
      print("\nYou entered Viridian Gym.")
      gym_encounter()
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      print("\nSearching...")
      time.sleep(3)
      print("\nYou didn't find anything!")
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")

    elif db["User Choice"] == "Poke Mart":
      poke_mart() #Pass in extra items like tms
      
    elif db["User Choice"] == "Pokemon Center":
      while True:
        db["User Choice"] = input("\nWould you like to heal your pokemon or access your pc? ").lower()

        if "heal" in db["User Choice"]:
          pokemon_center()
          break
          
        elif "pc" in db["User Choice"]:
          access_pc()
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def pewter_city():
  while True:
    print("\nViridian Forest     Route 3     Pewter Gym     Explore     Bag     Pokemon     Poke Mart     Pokemon Center     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Viridian Forest":
      print("\nYou walked to Viridian Forest.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 3":
      print("\nYou walked to Route 3.")
      return db["User Choice"]

    elif db["User Choice"] == "Pewter Gym":
      print("\nYou entered Pewter Gym.")
      gym_encounter()
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      print("\nSearching...")
      time.sleep(3)
      print("\nYou didn't find anything!")
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")

    elif db["User Choice"] == "Poke Mart":
      poke_mart() #Pass in extra items like tms
      
    elif db["User Choice"] == "Pokemon Center":
      while True:
        db["User Choice"] = input("\nWould you like to heal your pokemon or access your pc? ").lower()

        if "heal" in db["User Choice"]:
          pokemon_center()
          break
          
        elif "pc" in db["User Choice"]:
          access_pc()
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def mt_moon():
  while True:
    print("\nRoute 3     Route 4     Explore     Bag     Pokemon     Pokemon Center     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 3":
      print("\nYou walked to Route 3.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 4":
      print("\nYou walked to Route 4.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      encounter_outcome = wild_pokemon_encounter(9, 12, ["Clefairy", "Zubat", "Paras", "Geodude"], [6, 49, 15, 30]) 
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
      
    elif db["User Choice"] == "Pokemon Center":
      while True:
        db["User Choice"] = input("\nWould you like to heal your pokemon or access your pc? ").lower()

        if "heal" in db["User Choice"]:
          pokemon_center()
          break
          
        elif "pc" in db["User Choice"]:
          access_pc()
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def cerulean_city():
  while True:
    print("\nRoute 4     Route 5     Route 9     Route 24     Cerulean Gym     Explore     Bag     Pokemon     Poke Mart     Pokemon Center     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 4":
      print("\nYou walked to Route 4.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 5":
      print("\nYou walked to Route 5.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 9":
      print("\nYou walked to Route 9.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 24":
      print("\nYou walked to Route 24.")
      return db["User Choice"]

    elif db["User Choice"] == "Cerulean Gym":
      print("\nYou entered Cerulean Gym.")
      gym_encounter()
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      print("\nSearching...")
      time.sleep(3)
      print("\nYou didn't find anything!")
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")

    elif db["User Choice"] == "Poke Mart":
      poke_mart() #Pass in extra items like tms
      
    elif db["User Choice"] == "Pokemon Center":
      while True:
        db["User Choice"] = input("\nWould you like to heal your pokemon or access your pc? ").lower()

        if "heal" in db["User Choice"]:
          pokemon_center()
          break
          
        elif "pc" in db["User Choice"]:
          access_pc()
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def route_ten():
  while True:
    print("\nRoute 9     Power Plant     Rock Tunnel     Explore     Bag     Pokemon     Pokemon Center     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 9":
      print("\nYou walked to Route 9.")
      return db["User Choice"]

    elif db["User Choice"] == "Power Plant":
      print("\nYou walked to Power Plant.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Rock Tunnel":
      print("\nYou walked to Rock Tunnel.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": 
      rand_num = random.randint(1, 3)

      if rand_num == 1 and len(db["Trainer Locations"][db["User Location"]]) > 0:
        rand_trainer = db["Trainer Locations"][db["User Location"]][random.randint(0, len(db["Trainer Locations"][db["User Location"]]) - 1)]

        encounter_outcome = trainer_encounter(remove_end_number(rand_trainer), trainer_stats[db["User Location"]][rand_trainer][0], trainer_stats[db["User Location"]][rand_trainer][1], trainer_stats[db["User Location"]][rand_trainer][2], "Random")

        if encounter_outcome == "Opponent Defeated":
          del db["Trainer Locations"][db["User Location"]][db["Trainer Locations"][db["User Location"]].index(rand_trainer)] #This removes the trainer from the list so they can't be beat twice

      elif rand_num <= 3:  
        encounter_outcome = wild_pokemon_encounter(11, 17, ["Spearow", "Sandshrew", "Voltorb", "Magikarp", "Poliwag", "Goldeen", "Slowpoke"], [15, 13, 22, 15, 10, 15, 10])
  
      if encounter_outcome == "Pokemon Center":
        pokemon_center()
        return db["Last User City"]
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")
      
    elif db["User Choice"] == "Pokemon Center":
      while True:
        db["User Choice"] = input("\nWould you like to heal your pokemon or access your pc? ").lower()

        if "heal" in db["User Choice"]:
          pokemon_center()
          break
          
        elif "pc" in db["User Choice"]:
          access_pc()
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def saffron_city():
  while True:
    print("\nRoute 5     Route 6     Route 7     Route 8     Saffron Gym     Explore     Bag     Pokemon     Poke Mart     Pokemon Center     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 5":
      print("\nYou walked to Route 5.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 6":
      print("\nYou walked to Route 6.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 7":
      print("\nYou walked to Route 7.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 8":
      print("\nYou walked to Route 8.")
      return db["User Choice"]

    elif db["User Choice"] == "Saffron Gym":
      print("\nYou entered Saffron Gym.")
      gym_encounter()
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      print("\nSearching...")
      time.sleep(3)
      print("\nYou didn't find anything!")
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")

    elif db["User Choice"] == "Poke Mart":
      poke_mart() #Pass in extra items like tms
      
    elif db["User Choice"] == "Pokemon Center":
      while True:
        db["User Choice"] = input("\nWould you like to heal your pokemon or access your pc? ").lower()

        if "heal" in db["User Choice"]:
          pokemon_center()
          break
          
        elif "pc" in db["User Choice"]:
          access_pc()
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def lavender_town():
  while True:
    print("\nRoute 7     Route 12     Rock Tunnel     Explore     Bag     Pokemon     Poke Mart     Pokemon Center     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 7":
      print("\nYou walked to Route 7.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 12":
      print("\nYou walked to Route 12.")
      return db["User Choice"]

    elif db["User Choice"] == "Rock Tunnel":
      print("\nYou walked to Rock Tunnel.")
      return db["User Choice"]
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      print("\nSearching...")
      time.sleep(3)
      print("\nYou didn't find anything!")
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")

    elif db["User Choice"] == "Poke Mart":
      poke_mart() #Pass in extra items like tms
      
    elif db["User Choice"] == "Pokemon Center":
      while True:
        db["User Choice"] = input("\nWould you like to heal your pokemon or access your pc? ").lower()

        if "heal" in db["User Choice"]:
          pokemon_center()
          break
          
        elif "pc" in db["User Choice"]:
          access_pc()
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def celadon_city():
  while True:
    print("\nRoute 8     Route 16     Celadon Gym     Explore     Bag     Pokemon     Poke Mart     Pokemon Center     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 8":
      print("\nYou walked to Route 8.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 16":
      print("\nYou walked to Route 16.")
      return db["User Choice"]

    elif db["User Choice"] == "Celadon Gym":
      print("\nYou entered Celadon Gym.")
      gym_encounter()
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      print("\nSearching...")
      time.sleep(3)
      print("\nYou didn't find anything!")
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")

    elif db["User Choice"] == "Poke Mart":
      poke_mart() #Pass in extra items like tms
      
    elif db["User Choice"] == "Pokemon Center":
      while True:
        db["User Choice"] = input("\nWould you like to heal your pokemon or access your pc? ").lower()

        if "heal" in db["User Choice"]:
          pokemon_center()
          break
          
        elif "pc" in db["User Choice"]:
          access_pc()
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def vermilion_city():
  while True:
    print("\nRoute 6     Route 11     Vermilion Gym     Explore     Bag     Pokemon     Poke Mart     Pokemon Center     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 6":
      print("\nYou walked to Route 6.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 11":
      print("\nYou walked to Route 11.")
      return db["User Choice"]

    elif db["User Choice"] == "Vermilion Gym":
      print("\nYou entered Vermilion Gym.")
      gym_encounter()
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      print("\nSearching...")
      time.sleep(3)
      print("\nYou didn't find anything!")
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")

    elif db["User Choice"] == "Poke Mart":
      poke_mart() #Pass in extra items like tms
      
    elif db["User Choice"] == "Pokemon Center":
      while True:
        db["User Choice"] = input("\nWould you like to heal your pokemon or access your pc? ").lower()

        if "heal" in db["User Choice"]:
          pokemon_center()
          break
          
        elif "pc" in db["User Choice"]:
          access_pc()
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def fuchsia_city():
  while True:
    print("\nRoute 15     Route 18     Route 19     Safari Zone     Fuchsia Gym     Explore     Bag     Pokemon     Poke Mart     Pokemon Center     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 15":
      print("\nYou walked to Route 15.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 18":
      print("\nYou walked to Route 18.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 19":
      print("\nYou swam to Route 19.")
      return db["User Choice"]

    elif db["User Choice"] == "Safari Zone":
      print("\nYou walked to Safari Zone.")
      return db["User Choice"]

    elif db["User Choice"] == "Fuchsia Gym":
      print("\nYou entered Fuchsia Gym.")
      gym_encounter()
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      print("\nSearching...")
      time.sleep(3)
      print("\nYou didn't find anything!")
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")

    elif db["User Choice"] == "Poke Mart":
      poke_mart() #Pass in extra items like tms
      
    elif db["User Choice"] == "Pokemon Center":
      while True:
        db["User Choice"] = input("\nWould you like to heal your pokemon or access your pc? ").lower()

        if "heal" in db["User Choice"]:
          pokemon_center()
          break
          
        elif "pc" in db["User Choice"]:
          access_pc()
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def cinnabar_island():
  while True:
    print("\nRoute 20     Route 21     Cinnabar Gym     Explore     Bag     Pokemon     Poke Mart     Pokemon Center     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Route 20":
      print("\nYou swam to Route 20.")
      return db["User Choice"]

    elif db["User Choice"] == "Route 21":
      print("\nYou swam to Route 21.")
      return db["User Choice"]

    elif db["User Choice"] == "Cinnabar Gym":
      print("\nYou entered Cinnabar Gym.")
      gym_encounter()
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      print("\nSearching...")
      time.sleep(3)
      print("\nYou didn't find anything!")
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")

    elif db["User Choice"] == "Poke Mart":
      poke_mart() #Pass in extra items like tms
      
    elif db["User Choice"] == "Pokemon Center":
      while True:
        db["User Choice"] = input("\nWould you like to heal your pokemon or access your pc? ").lower()

        if "heal" in db["User Choice"]:
          pokemon_center()
          break
          
        elif "pc" in db["User Choice"]:
          access_pc()
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def indigo_plateau():
  while True:
    print("\nVictory Road     Elite 4     Explore     Bag     Pokemon     Poke Mart     Pokemon Center     Save     Save and Quit")
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Victory Road":
      print("\nYou walked to Victory Road.")
      return db["User Choice"]

    elif db["User Choice"] == "Elite 4":
      print("\nYou challenged the Elite 4.")
      elite_four()
      
    elif db["User Choice"] == "Explore": #Maybe set a timer to search?
      print("\nSearching...")
      time.sleep(3)
      print("\nYou didn't find anything!")
      
    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")

    elif db["User Choice"] == "Poke Mart":
      poke_mart() #Pass in extra items like tms
      
    elif db["User Choice"] == "Pokemon Center":
      while True:
        db["User Choice"] = input("\nWould you like to heal your pokemon or access your pc? ").lower()

        if "heal" in db["User Choice"]:
          pokemon_center()
          break
          
        elif "pc" in db["User Choice"]:
          access_pc()
          break
          
        else:
          print("\nThat is not a valid choice.")
          
    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")

#######################################################################

def gym_encounter():
  db["User Location"] = gym_locations[db["Last User City"]]

  for badge_index in range(badge_list.index(badge_locations[db["User Location"]])):
    if db["User Bag"][badge_list[badge_index]] == 0:
      print("\nThis is the ", end="") #This tells the user that they need to defeat the previous gyms to enter this gym
      if (gym_list.index(db["User Location"]) + 1) == 2:
        print("2nd Gym in the Kanto Region! You must defeat the previous Gym Leaders to challenge this Gym Leader!")
      elif (gym_list.index(db["User Location"]) + 1) == 3:
        print("3rd Gym in the Kanto Region! You must defeat the previous Gym Leaders to challenge this Gym Leader!")
      else:
        print(str(gym_list.index(db["User Location"]) + 1) + "th Gym in the Kanto Region! You must defeat the previous Gym Leaders to challenge this Gym Leader!")

      db["User Location"] = db["Last User City"]
      return db["User Location"]
  
  if len(db["Trainer Locations"][db["User Location"]]) == 0 and db["User Bag"][badge_locations[db["User Location"]]] == 1:
    print("\nYou have already defeated this gym. Move on to the next challenge!")
    db["User Location"] = db["Last User City"]
    return db["User Location"]
    
  while True:
    print("\n" + db["Last User City"] + "     ", end="") #This prints all of the options the user can perform
    if len(db["Trainer Locations"][db["User Location"]]) > 0:
      print("Fight Trainer     ", end="")
    elif db["User Bag"][badge_locations[db["User Location"]]] == 0:
      print("Challenge Gym Leader     ", end="")
    print("Bag     Pokemon     Save     Save and Quit")

    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == db["Last User City"]:
      print("\nYou exited the gym.")
      db["User Location"] = db["Last User City"]
      return db["User Choice"]

    elif db["User Choice"] == "Fight Trainer" and len(db["Trainer Locations"][db["User Location"]]) > 0:
      sel_trainer = db["Trainer Locations"][db["User Location"]][0]
      
      encounter_outcome = trainer_encounter(remove_end_number(sel_trainer), trainer_stats[db["User Location"]][sel_trainer][0], trainer_stats[db["User Location"]][sel_trainer][1], trainer_stats[db["User Location"]][sel_trainer][2], "Random")

      if encounter_outcome == "Opponent Defeated":
        del db["Trainer Locations"][db["User Location"]][0] #This removes the trainer from the list so they can't be beat twice

      elif encounter_outcome == "Pokemon Center":
        pokemon_center()
        db["User Location"] = db["Last User City"]
        return db["Last User City"]

    elif db["User Choice"] == "Challenge Gym Leader" and len(db["Trainer Locations"][db["User Location"]]) == 0 and db["User Bag"][badge_locations[db["User Location"]]] == 0:
      encounter_outcome = trainer_encounter(gym_leader_stats[db["User Location"]][0], gym_leader_stats[db["User Location"]][1], gym_leader_stats[db["User Location"]][2], gym_leader_stats[db["User Location"]][3], gym_leader_stats[db["User Location"]][4])

      if encounter_outcome == "Opponent Defeated":
        print("\nCongratulations on defeating me! Here is your reward: ")

        db["User Bag"][badge_locations[db["User Location"]]] = 1
        print("\nYou received the " + badge_locations[db["User Location"]] + "!")

        if db["User Location"] != "Pewter Gym" and db["User Location"] != "Saffron Gym" and db["User Location"] != "Viridian Gym": 
          db["User Bag"][tm_rewards[db["User Location"]]] = 1
          print("\nYou received " + tm_rewards[db["User Location"]] + "!")

      elif encounter_outcome == "Pokemon Center":
        pokemon_center()
        db["User Location"] = db["Last User City"]
        return db["Last User City"]

    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")

    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")


def elite_four():
  db["User Location"] = "Elite 4"
  
  while True:
    current_elite_four_member = db["Trainer Locations"]["Elite 4"][0]
    print("\nIndigo Plateau     Challenge " + current_elite_four_member + "     Bag     Pokemon     Save     Save and Quit") #Prints options for user
    db["User Choice"] = input("\nWhat will you do next? ")

    if db["User Choice"] == "Indigo Plateau":
      db["Trainer Locations"]["Elite 4"] = ["Lorelei", "Bruno", "Agatha", "Lance"]
      print("\nYou walked back to the Indigo Plateau.")
      db["User Location"] = "Indigo Plateau"
      return db["User Choice"]

    elif db["User Choice"] == ("Challenge " + current_elite_four_member): #Start battle, delete from list, for Lance maybe add post-quote that says something like 'you can choose to challenge us again if you wish'
      encounter_outcome = trainer_encounter(current_elite_four_member, trainer_stats["Elite 4"][current_elite_four_member][0], trainer_stats["Elite 4"][current_elite_four_member][1], trainer_stats["Elite 4"][current_elite_four_member][2], trainer_stats["Elite 4"][current_elite_four_member][3])
      
      if encounter_outcome == "Opponent Defeated":
        del db["Trainer Locations"]["Elite 4"][0] #This removes the trainer from the list so they can't be beat twice

        if len(db["Trainer Locations"]["Elite 4"]) == 0:
          db["Trainer Locations"]["Elite 4"] = ["Lorelei", "Bruno", "Agatha", "Lance"]
          db["User Location"] = "Indigo Plateau"
          return db["User Choice"]

      elif encounter_outcome == "Pokemon Center":
        pokemon_center()
        db["Trainer Locations"]["Elite 4"] = ["Lorelei", "Bruno", "Agatha", "Lance"]
        db["User Location"] = "Indigo Plateau"
        return "Indigo Plateau"

    elif db["User Choice"] == "Bag":
      bag("None")
      
    elif db["User Choice"] == "Pokemon":
      while True:
        print("\nWould you like to switch your team order, get info on your pokemon, or rename your pokemon?", end="")
        db["User Choice"] = input(" ").lower()

        if "switch" in db["User Choice"] or "team" in db["User Choice"] or "order" in db["User Choice"]:
          pokemon("Switch", "None")
          break
          
        elif "info" in db["User Choice"]:
          pokemon("Info", "None")
          break

        elif "rename" in db["User Choice"]:
          pokemon("Rename", "None")
          break
          
        else:
          print("\nThat is not a valid choice.")

    elif db["User Choice"] == "Save":
      save_file()
      
    elif db["User Choice"] == "Save and Quit":
      save_file()
      sys.exit()
      
    else:
      print("\nThat is not a valid choice.")