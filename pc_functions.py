#This is in charge accessing the pc

from replit import db

from choice_functions import print_stats
from game_info import *


def open_box(pc_boxes, sel_box):
  print("\n" + sel_box + ":")
  
  if len([*pc_boxes[sel_box]]) != 0:
    for pokemon_element in [*pc_boxes[sel_box]]:
      print_stats(db["PC"][pokemon_element][nickname] + " (" + pokemon_element + ")", db["PC"][pokemon_element][level], db["PC"][pokemon_element][current_health], db["PC"][pokemon_element][max_health], db["PC"][pokemon_element][status_condition], "Your ")

  else:
    print("Empty")


def define_pc_boxes():
  pc_boxes = {
    "Box 1": {},
    "Box 2": {},
    "Box 3": {},
    "Box 4": {},
    "Box 5": {},
    "Box 6": {},
    "Box 7": {},
    "Box 8": {},
    "Box 9": {},
    "Box 10": {}
  }

  pc_index = 0
  for box_element in [*pc_boxes]: #This temporarily stores pc pokemon into the boxes
    for index in range(10):
      try:
        pc_boxes[box_element][[*db["PC"]][pc_index]] = db["PC"][[*db["PC"]][pc_index]]
        pc_index += 1

      except IndexError:
        break

  return pc_boxes


def access_pc():
  sel_box = "Box 1"

  while True:
    pc_boxes = define_pc_boxes()
    open_box(pc_boxes, sel_box)
    
    print("\nPrevious Box     Next Box     Switch Pokemon")
    user_choice = input("\nWhat will you do next (type 'cancel' to leave the pc)? ").lower()

    if "cancel" in user_choice:
      print("\nYou left the pc.")
      break

    elif "previous" in user_choice:
      if "1" in sel_box:
        print("\nYou are already at the first box!")
        continue

      sel_box = sel_box.split(" ")[0] + " " + str(int(sel_box.split(" ")[1]) - 1)

    elif "next" in user_choice:
      if "10" in sel_box:
        print("\nYou are already at the last box!")
        continue

      sel_box = sel_box.split(" ")[0] + " " + str(int(sel_box.split(" ")[1]) + 1)

    elif "switch" in user_choice or "pokemon" in user_choice:
      if len([*pc_boxes[sel_box]]) == 0:
        print("\nThere are no pokemon in that box!")
        continue
      
      while True: #This selects valid pokemon
        pokemon_choice = input("\nWhich pokemon would you like to select (Type 'cancel' to go back)? ")
    
        if pokemon_choice == "cancel":
          break
        
        elif pokemon_choice in [*pc_boxes[sel_box]]:
          pokemon_switched = False
          
          print("\nList of Pokemon:\n")
          for pokemon_element in db["Team Order"]: #This prints names
            print_stats(db["Team Stats"][pokemon_element][nickname] + " (" + pokemon_element + ")", db["Team Stats"][pokemon_element][level], db["Team Stats"][pokemon_element][current_health], db["Team Stats"][pokemon_element][max_health], db["Team Stats"][pokemon_element][status_condition], "Your ")
          
          while True: #This selects valid pokemon
            second_pokemon_choice = input("\nWhich pokemon would you want " + pokemon_choice + " to replace (Type 'cancel' to go back)? ")

            if "cancel" in second_pokemon_choice:
              break
        
            elif second_pokemon_choice in db["Team Order"] and (db["PC"][pokemon_choice][current_health] > 0 or db["Team Order"][0] != second_pokemon_choice):
              print("\nYou replaced " + second_pokemon_choice + " with " + pokemon_choice + ".")
              pokemon_switched = True

              db["PC"][second_pokemon_choice] = db["Team Stats"][second_pokemon_choice]
              db["Team Stats"][pokemon_choice] = db["PC"][pokemon_choice]
              del db["PC"][pokemon_choice]
              del db["Team Stats"][second_pokemon_choice]
              db["Team Order"][db["Team Order"].index(second_pokemon_choice)] = pokemon_choice

              break
      
            else:
              print("\nEither that is not a valid pokemon or the format is wrong.")

          if pokemon_switched:
            break

        else:
          print("\nEither that is not a valid pokemon or the format is wrong.")

    else:
      print("\nEither that is not a valid choice or the format is wrong.")
      