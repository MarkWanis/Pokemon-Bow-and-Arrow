from replit import db
from tkinter import *
import yaml
import sys

from base_stats import *
from colors import *
from menu import *  #This gives dictionary needed to set global variables
from pokemon_stats import *
from game_info import *
from place_functions import *


if db["First Time"]:
  db["First Time"] = False

  #screen_print("You wake up early in the morning and realize what time it is - your 10th birthday! You are finally old enough to become a pokemon trainer. All you need to do is go to Professor Oak to get your starter pokemon.")

  print("You wake up early in the morning and realize what time it is - your 10th birthday! You are finally old enough to become a pokemon trainer. All you need to do is go to Professor Oak to get your starter pokemon.")
  while True:
    db["User Choice"] = input("\nDo you go to Professor Oak's workplace? (Yes or No) ").lower()
    
    if db["User Choice"] == "yes":
      print("\nYou walk to Professor Oak's workplace.")
      
    elif db["User Choice"] == "no":
      while True:
        db["User Choice"] = input("\nAre you sure? (Yes or No) ").lower()
      
        if db["User Choice"] == "yes":
          print("\n-_-")
          print("You somehow will yourself to get back into your bed and go to sleep. You finish school, get a job at the nearby PokeMart, and get paid minimum wage selling items to travelling adventurues. Sometimes you wonder if you made the right choice not going to Professor Oak's. You wonder if there was so much more in store for you. But you ignore this silly notion and continue on with your mundane job.")
          sys.exit()
          
        elif db["User Choice"] == "no":
          print("\nYou walk to Professor Oak's workplace.")
          break
          
        else:
          print("\nThat is not a valid option.")
              
    else:
      print("\nThat is not a valid option.")
      continue
      
    break

  while True:
    print("\nHi " + db["User Name"] + ". I see you are very excited to get your first pokemon, so let's get right to it. I currently have a charmander, bulbasaur, and squirtle ready to go. ", end="")
    starter_pokemon = input("Which one would you like? ").lower()

    if starter_pokemon == "charmander":
      print("\nYou selected Charmander.")
      db["Team Stats"]["Charmander #1"] = [5, 0, 39, 52, 43, 60, 50, 65, 0, 0, 0, 0, 0, 0, 0, "Fire", ["Growl", "Scratch", "Ember", "None"], "None", 1, "Charmander"]
      db["Team Stats"]["Charmander #1"] = define_stats(db["Team Stats"]["Charmander #1"])
      db["Team Stats"]["Charmander #1"][exp] = round(1.25 * (db["Team Stats"]["Charmander #1"][level])**3)
      db["Team Stats"]["Charmander #1"][current_health] = db["Team Stats"]["Charmander #1"][max_health]
      db["Team Order"].append("Charmander #1")

    elif starter_pokemon == "bulbasaur":
      print("\nYou selected Bulbasaur.")
      db["Team Stats"]["Bulbasaur #1"] = [5, 0, 45, 49, 49, 65, 65, 45, 0, 0, 0, 0, 0, 0, 0, "Grass & Poison", ["Growl", "Tackle", "Vine Whip", "None"], "None", 1, "Bulbasaur"]
      db["Team Stats"]["Bulbasaur #1"] = define_stats(db["Team Stats"]["Bulbasaur #1"])
      db["Team Stats"]["Bulbasaur #1"][exp] = round(1.25 * (db["Team Stats"]["Bulbasaur #1"][level])**3)
      db["Team Stats"]["Bulbasaur #1"][current_health] = db["Team Stats"]["Bulbasaur #1"][max_health]
      db["Team Order"].append("Bulbasaur #1")

    elif starter_pokemon == "squirtle":
      print("\nYou selected Squirtle.")
      db["Team Stats"]["Squirtle #1"] = [5, 0, 44, 48, 65, 50, 64, 43, 0, 0, 0, 0, 0, 0, 0, "Water", ["Tackle", "Tail Whip", "Water Gun", "None"], "None", 1, "Squirtle"]
      db["Team Stats"]["Squirtle #1"] = define_stats(db["Team Stats"]["Squirtle #1"])
      db["Team Stats"]["Squirtle #1"][exp] = round(1.25 * (db["Team Stats"]["Squirtle #1"][level])**3)
      db["Team Stats"]["Squirtle #1"][current_health] = db["Team Stats"]["Squirtle #1"][max_health]
      db["Team Order"].append("Squirtle #1")

    else:
      print("\nThat is not a valid option.")
      continue

    db["Collected Pokemon"] += 1

    break

  print("\nVery nice choice! That " + starter_pokemon + " has a lot of potential for growth as you go along your arduous journey. I wish you the best of luck.")

  db["User Choice"] = pallet_town()
  
else:
  if "Gym" in db["User Location"]:
    gym_encounter()

  elif db["User Location"] == "Elite 4":
    elite_four()
  
  db["User Choice"] = db["User Location"]

while True:
    if db["User Choice"] in user_route_options:
        if db["User Choice"] == "Route 1":
            db["User Location"] = "Route 1"
            db["User Choice"] = route_one()
        elif db["User Choice"] == "Route 2":
            db["User Location"] = "Route 2"
            db["User Choice"] = route_two()
        elif db["User Choice"] == "Route 3":
            db["User Location"] = "Route 3"
            db["User Choice"] = route_three()
        elif db["User Choice"] == "Route 4":
            db["User Location"] = "Route 4"
            db["User Choice"] = route_four()
        elif db["User Choice"] == "Route 5":
            db["User Location"] = "Route 5"
            db["User Choice"] = route_five()
        elif db["User Choice"] == "Route 6":
            db["User Location"] = "Route 6"
            db["User Choice"] = route_six()
        elif db["User Choice"] == "Route 7":
            db["User Location"] = "Route 7"
            db["User Choice"] = route_seven()
        elif db["User Choice"] == "Route 8":
            db["User Location"] = "Route 8"
            db["User Choice"] = route_eight()
        elif db["User Choice"] == "Route 9":
            db["User Location"] = "Route 9"
            db["User Choice"] = route_nine()
        elif db["User Choice"] == "Route 11":
            db["User Location"] = "Route 11"
            db["User Choice"] = route_eleven()
        elif db["User Choice"] == "Route 12":
            db["User Location"] = "Route 12"
            db["User Choice"] = route_twelve()
        elif db["User Choice"] == "Route 13":
            db["User Location"] = "Route 13"
            db["User Choice"] = route_thirteen()
        elif db["User Choice"] == "Route 14":
            db["User Location"] = "Route 14"
            db["User Choice"] = route_fourteen()
        elif db["User Choice"] == "Route 15":
            db["User Location"] = "Route 15"
            db["User Choice"] = route_fifteen()
        elif db["User Choice"] == "Route 16":
            db["User Location"] = "Route 16"
            db["User Choice"] = route_sixteen()
        elif db["User Choice"] == "Route 18":
            db["User Location"] = "Route 18"
            db["User Choice"] = route_eighteen()
        elif db["User Choice"] == "Route 19":
            db["User Location"] = "Route 19"
            db["User Choice"] = route_nineteen()
        elif db["User Choice"] == "Route 20":
            db["User Location"] = "Route 20"
            db["User Choice"] = route_twenty()
        elif db["User Choice"] == "Route 21":
            db["User Location"] = "Route 21"
            db["User Choice"] = route_twenty_one()
        elif db["User Choice"] == "Route 22":
            db["User Location"] = "Route 22"
            db["User Choice"] = route_twenty_two()
        elif db["User Choice"] == "Route 23":
            db["User Location"] = "Route 23"
            db["User Choice"] = route_twenty_three()
        elif db["User Choice"] == "Route 24":
            db["User Location"] = "Route 24"
            db["User Choice"] = route_twenty_four()
        elif db["User Choice"] == "Route 25":
            db["User Location"] = "Route 25"
            db["User Choice"] = route_twenty_five()
        elif db["User Choice"] == "Viridian Forest":
            db["User Location"] = "Viridian Forest"
            db["User Choice"] = viridian_forest()
        elif db["User Choice"] == "Power Plant":
            db["User Location"] = "Power Plant"
            db["User Choice"] = power_plant()
        elif db["User Choice"] == "Rock Tunnel":
            db["User Location"] = "Rock Tunnel"
            db["User Choice"] = rock_tunnel()
        elif db["User Choice"] == "Safari Zone":
            db["User Location"] = "Safari Zone"
            db["User Choice"] = safari_zone()
        elif db["User Choice"] == "Cycling Road":
            db["User Location"] = "Cycling Road"
            db["User Choice"] = cycling_road()
        elif db["User Choice"] == "Seafoam Islands":
            db["User Location"] = "Seafoam Islands"
            db["User Choice"] = seafoam_islands()
        elif db["User Choice"] == "Victory Road":
            db["User Location"] = "Victory Road"
            db["User Choice"] = victory_road()

    elif db["User Choice"] in user_city_options:
        if db["User Choice"] == "Pallet Town":
            db["User Location"] = "Pallet Town"
            db["Last User City"] = "Pallet Town"
            db["User Choice"] = pallet_town()
        elif db["User Choice"] == "Viridian City":
            db["User Location"] = "Viridian City"
            db["Last User City"] = "Viridian City"
            db["User Choice"] = viridian_city()
        elif db["User Choice"] == "Pewter City":
            db["User Location"] = "Pewter City"
            db["Last User City"] = "Pewter City"
            db["User Choice"] = pewter_city()
        elif db["User Choice"] == "Mt. Moon":
            db["User Location"] = "Mt. Moon"
            db["User Choice"] = mt_moon()
        elif db["User Choice"] == "Cerulean City":
            db["User Location"] = "Cerulean City"
            db["Last User City"] = "Cerulean City"
            db["User Choice"] = cerulean_city()
        elif db["User Choice"] == "Saffron City":
            db["User Location"] = "Saffron City"
            db["Last User City"] = "Saffron City"
            db["User Choice"] = saffron_city()
        elif db["User Choice"] == "Lavender City":
            db["User Location"] = "Lavender City"
            db["Last User City"] = "Lavender City"
            db["User Choice"] = lavender_city()
        elif db["User Choice"] == "Celadon City":
            db["User Location"] = "Celadon City"
            db["Last User City"] = "Celadon City"
            db["User Choice"] = celadon_city()
        elif db["User Choice"] == "Vermilion City":
            db["User Location"] = "Vermilion City"
            db["Last User City"] = "Vermilion City"
            db["User Choice"] = vermilion_city()
        elif db["User Choice"] == "Fuchsia City":
            db["User Location"] = "Fuchsia City"
            db["Last User City"] = "Fuchsia City"
            db["User Choice"] = fuchsia_city()
        elif db["User Choice"] == "Cinnabar Island":
            db["User Location"] = "Cinnabar Island"
            db["Last User City"] = "Cinnabar Island"
            db["User Choice"] = cinnabar_island()
        elif db["User Choice"] == "Indigo Plateau":
            db["User Location"] = "Indigo Plateau"
            db["Last User City"] = "Indigo Plateau"
            db["User Choice"] = indigo_plateau()
    else:
        print("Faulty Location")
        break

root.mainloop()  # Actually draws what was coded
