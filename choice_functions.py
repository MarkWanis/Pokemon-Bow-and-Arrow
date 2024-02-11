#This creates the functions for the choices the user makes, i.e. bag, pokemon, etc.

from replit import db
import yaml
import math
import time

from game_info import *
from colors import *


def print_stats(pokemon_name, pokemon_level, remaining_health, full_health, pokemon_status, user_or_opposing):
  print("\n" + user_or_opposing + pokemon_name + ":")

  print("Level: " + str(pokemon_level))
  
  if (remaining_health / full_health) >= (2 / 3):
    print("HP: " + Green + str(remaining_health) + reset + " / " + str(full_health))

  elif (remaining_health / full_health) >= (1 / 3):
    print("HP: " + bright_yellow + str(remaining_health) + reset + " / " + str(full_health))

  elif (remaining_health / full_health) < (1 / 3):
    print("HP: " + Red + str(remaining_health) + reset + " / " + str(full_health))

  print("Status: " + pokemon_status)


def bag(situation): #This prints the bag and asks which item to use
  print()
  for key_element in battle_items: #This prints every battle-related item in the bag
    if db["User Bag"][key_element] > 0:
      print(key_element + ": " + str(db["User Bag"][key_element]))
  if situation == "None":
    for key_element in badge_list:
      if db["User Bag"][key_element] > 0:
        print(key_element)
    for key_element in tm_list:
      if db["User Bag"][key_element] > 0:
        print(key_element) #Maybe we can print the pokemon move the tm goes with here or when they select it

  while True:
    item_choice = input("\nWhich item would you like to select (Type 'cancel' to go back)? ")
    
    if item_choice == "cancel":
      return False
      
    elif item_choice in [*db["User Bag"]] and item_choice not in badge_list and (item_choice in battle_items or situation == "None"): #This allows battle-related items, doesn't allow badge items, and only allows everything else if the situation is out of battle
      if db["User Bag"][item_choice] <= 0:
        print("\nYou have run out of that item.")
        continue
        
      elif (item_choice == "Pokeball" or item_choice == "Greatball" or item_choice == "Ultraball") and situation != "Wild Battle":
        print("\nYou can't use that here! ")
        continue
        
      elif item_choice == "Revive" or item_choice == "Max Revive":
        can_use_item = False
        for key_element in [*db["Team Stats"]]:
          if db["Team Stats"][key_element][current_health] <= 0: 
            can_use_item = True
            break 
        if can_use_item == False:
          print("\nYou can't use that here! ")
          continue

      break

    else:
      print("\nEither that is not a valid item or the format is wrong.")

  #At this point we have a valid item that can be used in the situation

  if item_choice == "Pokeball":
    db["User Bag"][item_choice] -= 1
    
  elif item_choice == "Greatball":
    db["User Bag"][item_choice] -= 1
    
  elif item_choice == "Ultraball":
    db["User Bag"][item_choice] -= 1
    
  elif item_choice == "Potion": #Have pokemon function go first and if it returns valid string (maybe pokemon name) then remove item
    sel_pokemon = pokemon("Bag", item_choice)
    if sel_pokemon == False:
      return False
    db["User Bag"][item_choice] -= 1
    db["Team Stats"][sel_pokemon][current_health] += 20
    if db["Team Stats"][sel_pokemon][current_health] > db["Team Stats"][sel_pokemon][max_health]:
      db["Team Stats"][sel_pokemon][current_health] = db["Team Stats"][sel_pokemon][max_health]
    
  elif item_choice == "Super Potion":
    sel_pokemon = pokemon("Bag", item_choice)
    if sel_pokemon == False:
      return False
    db["User Bag"][item_choice] -= 1
    db["Team Stats"][sel_pokemon][current_health] += 50
    if db["Team Stats"][sel_pokemon][current_health] > db["Team Stats"][sel_pokemon][max_health]:
      db["Team Stats"][sel_pokemon][current_health] = db["Team Stats"][sel_pokemon][max_health]
    
  elif item_choice == "Hyper Potion":
    sel_pokemon = pokemon("Bag", item_choice)
    if sel_pokemon == False:
      return False
    db["User Bag"][item_choice] -= 1
    db["Team Stats"][sel_pokemon][current_health] += 200
    if db["Team Stats"][sel_pokemon][current_health] > db["Team Stats"][sel_pokemon][max_health]:
      db["Team Stats"][sel_pokemon][current_health] = db["Team Stats"][sel_pokemon][max_health]
    
  elif item_choice == "Max Potion":
    sel_pokemon = pokemon("Bag", item_choice)
    if sel_pokemon == False:
      return False
    db["User Bag"][item_choice] -= 1
    db["Team Stats"][sel_pokemon][current_health] = db["Team Stats"][sel_pokemon][max_health]
    
  elif item_choice == "Antidote":
    sel_pokemon = pokemon("Bag", item_choice)
    if sel_pokemon == False:
      return False
    db["User Bag"][item_choice] -= 1
    db["Team Stats"][sel_pokemon][status_condition] = "None"
    
  elif item_choice == "Awakening":
    sel_pokemon = pokemon("Bag", item_choice)
    if sel_pokemon == False:
      return False
    db["User Bag"][item_choice] -= 1
    db["Team Stats"][sel_pokemon][status_condition] = "None"
    
  elif item_choice == "Burn Heal":
    sel_pokemon = pokemon("Bag", item_choice)
    if sel_pokemon == False:
      return False
    db["User Bag"][item_choice] -= 1
    db["Team Stats"][sel_pokemon][status_condition] = "None"
    
  elif item_choice == "Ice Heal":
    sel_pokemon = pokemon("Bag", item_choice)
    if sel_pokemon == False:
      return False
    db["User Bag"][item_choice] -= 1
    db["Team Stats"][sel_pokemon][status_condition] = "None"
    
  elif item_choice == "Paralyze Heal":
    sel_pokemon = pokemon("Bag", item_choice)
    if sel_pokemon == False:
      return False
    db["User Bag"][item_choice] -= 1
    db["Team Stats"][sel_pokemon][status_condition] = "None"

  elif item_choice == "Revive":
    sel_pokemon = pokemon("Bag", item_choice)
    if sel_pokemon == False:
      return False
    db["User Bag"][item_choice] -= 1
    db["Team Stats"][sel_pokemon][current_health] = math.floor(db["Team Stats"][sel_pokemon][max_health] / 2)

  elif item_choice == "Max Revive":
    sel_pokemon = pokemon("Bag", item_choice)
    if sel_pokemon == False:
      return False
    db["User Bag"][item_choice] -= 1
    db["Team Stats"][sel_pokemon][current_health] = db["Team Stats"][sel_pokemon][max_health]

  return item_choice


def pokemon(situation, item_choice): #This prints every pokemon on the team and returns a variable based on the situation
  print("\nList of Pokemon:")
  for key_element in db["Team Order"]: #This prints names
    print_stats(db["Team Stats"][key_element][nickname] + " (" + key_element + ")", db["Team Stats"][key_element][level], db["Team Stats"][key_element][current_health], db["Team Stats"][key_element][max_health], db["Team Stats"][key_element][status_condition], "")
    
  while True: #This selects valid pokemon
    pokemon_choice = input("\nWhich pokemon would you like to select (Type 'cancel' to go back)? ")

    if pokemon_choice == "cancel":
      return False
    
    elif pokemon_choice in db["Team Order"]: #If pokemon is valid (potion when health empty/full or status condition doesn't match medicine or revive when health is empty) is false
      if db["Team Stats"][pokemon_choice][current_health] <= 0 and situation == "Battle":
        print("\nYou cannot switch to a fainted pokemon!")
        continue

      if (db["Team Stats"][pokemon_choice][current_health] == db["Team Stats"][pokemon_choice][max_health] or db["Team Stats"][pokemon_choice][current_health] == 0) and (item_choice == "Potion" or item_choice == "Super Potion" or item_choice == "Hyper Potion" or item_choice == "Max Potion"):
        print("\nYour selected pokemon has either fainted or is already at full health!")
        continue
        
      elif (item_choice == "Antidote" or item_choice == "Awakening" or item_choice == "Burn Heal" or item_choice == "Ice Heal" or item_choice == "Paralyze Heal"):
        if db["Team Stats"][pokemon_choice][status_condition] != status_healing[item_choice]:
          print("\nThat pokemon does not have the status condition the item heals!")
          continue

      elif (db["Team Stats"][pokemon_choice][current_health] > 0) and (item_choice == "Revive" or item_choice == "Max Revive"):
        print("\nThat pokemon has not fainted!")
        continue
      
      print("\nYou selected " + db["Team Stats"][pokemon_choice][nickname] + ".")
      break

    else:
      print("\nEither that is not a valid pokemon or the format is wrong.")

  #At this point pokemon_choice is valid, and now will find what to do next using situation
  
  if situation == "Bag":
    return pokemon_choice

  elif situation == "Info": #This prints necessary pokemon info
    print()
    for key_element in [*stat_names]:
      print(key_element + ": " + str(db["Team Stats"][pokemon_choice][stat_names[key_element]]))
    move_list = []
    for element in db["Team Stats"][pokemon_choice][16]: #This deconstructs move list in each list in Team Stats
      move_list.append(element)
    print("Move List: " + str(move_list))

    return False #Might need to change this later

  elif situation == "Switch":
    while True: #This selects valid pokemon
      second_pokemon_choice = input("\nWhich pokemon would you want " + db["Team Stats"][pokemon_choice][nickname] + " to switch with? ")
  
      if second_pokemon_choice in db["Team Order"] and db["Team Stats"][pokemon_choice][current_health] > 0:
        print("\nYou switched " + db["Team Stats"][pokemon_choice][nickname] + " with " + db["Team Stats"][second_pokemon_choice][nickname] + ".")

        db["Team Order"][db["Team Order"].index(pokemon_choice)] = "Placeholder"
        if pokemon_choice != second_pokemon_choice:
          db["Team Order"][db["Team Order"].index(second_pokemon_choice)] = pokemon_choice 
        db["Team Order"][db["Team Order"].index("Placeholder")] = second_pokemon_choice

        return False #Might need to change this later

      else:
        print("\nEither that is not a valid pokemon or the format is wrong.")

  elif situation == "Battle":
    print("\nYou replaced " + db["Team Stats"][db["Team Order"][0]][nickname] + " with " + db["Team Stats"][pokemon_choice][nickname] + ".")

    db["Team Order"][db["Team Order"].index(pokemon_choice)] = db["Team Order"][0]
    db["Team Order"][0] = pokemon_choice 

    return True

  elif situation == "Rename":
    new_nickname = input("\nPlease rename " + db["Team Stats"][pokemon_choice][nickname] + ": ")

    print("\nYou renamed " + db["Team Stats"][pokemon_choice][nickname] + " to " + new_nickname + ".")

    db["Team Stats"][pokemon_choice][nickname] = new_nickname

  else:
    print("Faulty Pokemon")


def poke_mart():
  print("\nHello! Welcome to our Poke Mart.")
    
  while True:
    for bag_element in [*item_cost]: #This prints the items and their costs
      print("\n" + bag_element + "\nCost: ₽" + str(item_cost[bag_element]))
      
    print("\nYour Remaining Money: ₽" + str(db["User Money"]))

    item_choice = input("\nWhat item would you like to purchase (Type 'cancel' to exit)? ")

    if item_choice == "cancel":
      break

    elif item_choice in [*item_cost]:
      while True:
        item_quantity = input("\nHow many " + item_choice + "s would you like (Type 'cancel' to go back)? ")

        if item_quantity == "cancel":
          break

        elif item_quantity.isdigit() == False:
          print("\nThat is not a valid number.")

        elif int(item_quantity) < 1:
          print("\nThat is not a valid number.")

        elif item_cost[item_choice] * int(item_quantity) > db["User Money"]:
          print("\nYou do not have enough money to purchase that many " + item_choice + "s!")

        else:
          print("\nYou purchased " + item_quantity + " " + item_choice + "(s).")
          db["User Bag"][item_choice] += int(item_quantity)
          db["User Money"] -= (item_cost[item_choice] * int(item_quantity))
          break

    #This is where we would insert extra items like tms

    else:
      print("\nEither that is not a valid item or the format is wrong.")

  print("\nThanks for stopping by the Poke Mart! We hope to see you soon.")


def pokemon_center():
  print("\nHello, and Welcome to the Pokémon Center. We restore your tired Pokémon to full health. Here, let me take your pokemon for you.")

  for pokemon_element in [*db["Team Stats"]]: #This heals and removes status condition
    db["Team Stats"][pokemon_element][current_health] = db["Team Stats"][pokemon_element][max_health]
    db["Team Stats"][pokemon_element][status_condition] = "None"

  time.sleep(2)

  print("\nWe've restored your Pokemon to full health! We hope to see you again!")


def save_file():
  #This first part disassembles the dictionaries and lists in db and then reconstructs them in a different variable
  user_bag = {}
  for key_element in [*db["User Bag"]]: #This deconstructs User Bag
    user_bag[key_element] = db["User Bag"][key_element]
  team_stats = {}
  for key_element in [*db["Team Stats"]]: #This deconstructs Team Stats
    team_stats[key_element] = []
    move_list = []
    for index in range(len(db["Team Stats"][key_element])): #This deconstructs each list in Team Stats
      if index != 16:
        team_stats[key_element].append(db["Team Stats"][key_element][index])
      else:
        for element in db["Team Stats"][key_element][index]: #This deconstructs move list in each list in Team Stats
          move_list.append(element)
        team_stats[key_element].append(move_list.copy())
  team_order = [] 
  for element in db["Team Order"]: #This deconstructs Team Order
    team_order.append(element)
  pc = {}
  for key_element in [*db["PC"]]: #This deconstructs PC
    pc[key_element] = []
    move_list = []
    for index in range(len(db["PC"][key_element])): #This deconstructs each list in PC
      if index != 16:
        pc[key_element].append(db["PC"][key_element][index])
      else:
        for element in db["PC"][key_element][index]: #This deconstructs move list in each list in Team Stats
          move_list.append(element)
        pc[key_element].append(move_list.copy())
  trainer_locations = {}
  for key_element in [*db["Trainer Locations"]]: #This deconstructs Trainer Locations
    trainer_locations[key_element] = []
    for index in range(len(db["Trainer Locations"][key_element])): #This deconstructs each list in Trainer Locations
      trainer_locations[key_element].append(db["Trainer Locations"][key_element][index])
  item_locations = {}
  for key_element in [*db["Item Locations"]]: #This deconstructs Item Locations
    item_locations[key_element] = []
    for index in range(len(db["Item Locations"][key_element])): #This deconstructs each list in Item Locations
      item_locations[key_element].append(db["Item Locations"][key_element][index])
  
  data = {
    "Last User City": db["Last User City"],
    "User Location": db["User Location"],
    "User Name": db["User Name"],
    "First Time": db["First Time"],
    "User Bag": user_bag,
    "User Money": db["User Money"],
    "Team Stats": team_stats,
    "Team Order": team_order,
    "Collected Pokemon": db["Collected Pokemon"],
    "PC": pc,
    "Trainer Locations": trainer_locations,
    "Item Locations": item_locations
  }
  
  with open(r'Data/' + db["User Name"] + '.yaml', 'w') as file:
    yaml.dump(data, file)

  print("\nGame Successfully Saved.")

