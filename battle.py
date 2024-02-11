
#This creates all of the functions needed for wild pokemon battling and trainer battling

import random
from replit import db
import time 
import math

from pokemon_stats import *
from game_info import *
from base_stats import *
from moves import *
from choice_functions import *
from catch import *
from colors import *
from evolutions import *
from exp import *


accuracy_mod = 0
attack_mod = 1
defense_mod = 2
sp_attack_mod = 3
sp_defense_mod = 4
speed_mod = 5

burned_attack_modifier = {
  "Burned": .5,
  "None": 1,
  "Poisoned": 1,
  "Asleep": 1,
  "Frozen": 1,
  "Paralyzed": 1
}

paralyzed_speed_modifier = {
  "Paralyzed": .5,
  "None": 1,
  "Poisoned": 1,
  "Burned": 1,
  "Asleep": 1,
  "Frozen": 1,
}


def move_type_status_condition(current_status_condition, opponent_move_type, pokemon_name, user_or_opposing): #This looks at the move type played against the pokemon and decides whether to apply a status condition or not
  if current_status_condition != "None" or (opponent_move_type != "Fire" and opponent_move_type != "Electric" and opponent_move_type != "Ice" and opponent_move_type != "Poison"):
    return current_status_condition 

  random_num = random.randint(1, 100)

  if random_num > 10:
    return current_status_condition

  else:
    if opponent_move_type == "Fire":
      print("\n" + user_or_opposing + pokemon_name + " is burned by the attack!")
      return "Burned"

    elif opponent_move_type == "Electric":
      print("\n" + user_or_opposing + pokemon_name + " is paralyzed by the attack!")
      return "Paralyzed"

    elif opponent_move_type == "Ice":
      print("\n" + user_or_opposing + pokemon_name + " is frozen solid!")
      return "Frozen"

    elif opponent_move_type == "Poison":
      print("\n" + user_or_opposing + pokemon_name + " is poisoned by the attack!")
      return "Poisoned"


def check_status_turn_skip(current_status_condition, status_counter, pokemon_name, user_or_opposing): #Returns if the turn is skipped and if the status condition is removed
  if current_status_condition != "Asleep" and current_status_condition != "Frozen" and current_status_condition != "Paralyzed":
    return [False, current_status_condition]

  random_num = random.randint(1, 100)

  if current_status_condition == "Asleep":
    if status_counter == 0 and random_num <= 25:
      print("\n" + user_or_opposing + pokemon_name + " wakes up!")
      return [False, "None"]

    elif status_counter == 1 and random_num <= 50:
      print("\n" + user_or_opposing + pokemon_name + " wakes up!")
      return [False, "None"]

    elif status_counter == 2:
      print("\n" + user_or_opposing + pokemon_name + " woke up!")
      return [False, "None"]

    print("\n" + user_or_opposing + pokemon_name + " is fast asleep!")

  elif current_status_condition == "Frozen":
    if random_num <= 20:
      print("\n" + user_or_opposing + pokemon_name + " is unfrozen!")
      return [False, "None"]

    print("\n" + user_or_opposing + pokemon_name + " is frozen and unable to move!")

  elif current_status_condition == "Paralyzed":
    if random_num <= 25:
      print("\n" + user_or_opposing + pokemon_name + " is paralyzed and unable to move!")

    else:
      return [False, current_status_condition]

  return [True, current_status_condition]


def change_stat_modifier(stat_modifier, stage_increase, pokemon_name, modifier_name, user_or_opposing):
  if stage_increase > 0:
    for index in range(stage_increase):
      if stat_modifier == .25:
        stat_modifier = .28

      elif stat_modifier == .28:
        stat_modifier = .33

      elif stat_modifier == .33:
        stat_modifier = .40

      elif stat_modifier == .40:
        stat_modifier = .50

      elif stat_modifier == .50:
        stat_modifier = .66

      elif stat_modifier == .66:
        stat_modifier = 1

      elif stat_modifier >= 1 and stat_modifier < 4:
        stat_modifier += .5

      else:
        print("\n" + user_or_opposing + pokemon_name + "'s " + modifier_name + " can't increase further!")
        return stat_modifier

    print("\n" + user_or_opposing + pokemon_name + "'s " + modifier_name + " has increased!")

  elif stage_increase < 0:
    for index in range(stage_increase * -1):
      if stat_modifier > 1 and stat_modifier <= 4:
        stat_modifier -= .5

      elif stat_modifier == 1:
        stat_modifier = .66

      elif stat_modifier == .66:
        stat_modifier = .50

      elif stat_modifier == .50:
        stat_modifier = .40

      elif stat_modifier == .40:
        stat_modifier = .33

      elif stat_modifier == .33:
        stat_modifier = .28

      elif stat_modifier == .28:
        stat_modifier = .25

      else:
        print("\n" + user_or_opposing + pokemon_name + "'s " + modifier_name + " can't decrease further!")
        return stat_modifier

    print("\n" + user_or_opposing + pokemon_name + "'s " + modifier_name + " has decreased!")

  return stat_modifier


def fight_choice(sel_pokemon): #This prints all of the moves of the selected pokemon and returns a valid move choice
  print("\nList of Possible Moves:\n")
  for move_index in range(4):
    if db["Team Stats"][sel_pokemon][moves][move_index] != "None":
      print(db["Team Stats"][sel_pokemon][moves][move_index])
  
  while True:
    move_choice = input("\nWhich move do you choose (Type 'cancel' to go back)? ")

    if move_choice == "cancel":
      return False
    
    elif move_choice in db["Team Stats"][sel_pokemon][moves] and move_choice != "None":
      return move_choice
      
    else:
      print("\nEither that is not a valid move or it is the incorrect format.")


def effective_check(move_type, opponent_type):
  damage_multiplier = 1

  if move_type == "Normal" and ("Rock" in opponent_type or "Steel" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Normal" and ("Ghost" in opponent_type):
    damage_multiplier *= 0

  if move_type == "Fire" and ("Grass" in opponent_type or "Ice" in opponent_type or "Bug" in opponent_type or "Steel" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Fire" and ("Fire" in opponent_type or "Water" in opponent_type or "Rock" in opponent_type or "Dragon" in opponent_type):
    damage_multiplier *= .5

  if move_type == "Water" and ("Fire" in opponent_type or "Ground" in opponent_type or "Rock" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Water" and ("Water" in opponent_type or "Grass" in opponent_type or "Dragon" in opponent_type):
    damage_multiplier *= .5

  if move_type == "Electric" and ("Water" in opponent_type or "Flying" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Electric" and ("Electric" in opponent_type or "Grass" in opponent_type or "Dragon" in opponent_type):
    damage_multiplier *= .5
  if move_type == "Electric" and ("Ground" in opponent_type):
    damage_multiplier *= 0

  if move_type == "Grass" and ("Water" in opponent_type or "Ground" in opponent_type or "Rock" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Grass" and ("Fire" in opponent_type or "Grass" in opponent_type or "Poison" in opponent_type or "Flying" in opponent_type or "Bug" in opponent_type or "Dragon" in opponent_type or "Steel" in opponent_type):
    damage_multiplier *= .5

  if move_type == "Ice" and ("Grass" in opponent_type or "Ground" in opponent_type or "Flying" in opponent_type or "Dragon" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Ice" and ("Fire" in opponent_type or "Water" in opponent_type or "Ice" in opponent_type or "Steel" in opponent_type):
    damage_multiplier *= .5
  
  if move_type == "Fighting" and ("Normal" in opponent_type or "Ice" in opponent_type or "Rock" in opponent_type or "Dark" in opponent_type or "Steel" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Fighting" and ("Poison" in opponent_type or "Flying" in opponent_type or "Psychic" in opponent_type or "Bug" in opponent_type or "Fairy" in opponent_type):
    damage_multiplier *= .5
  if move_type == "Fighting" and ("Ghost" in opponent_type):
    damage_multiplier *= 0
  
  if move_type == "Poison" and ("Grass" in opponent_type or "Fairy" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Poison" and ("Poison" in opponent_type or "Ground" in opponent_type or "Rock" in opponent_type or "Ghost" in opponent_type):
    damage_multiplier *= .5
  if move_type == "Poison" and ("Steel" in opponent_type):
    damage_multiplier *= 0
  
  if move_type == "Ground" and ("Fire" in opponent_type or "Electric" in opponent_type or "Poison" in opponent_type or "Rock" in opponent_type or "Steel" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Ground" and ("Grass" in opponent_type or "Bug" in opponent_type):
    damage_multiplier *= .5
  if move_type == "Ground" and ("Flying" in opponent_type):
    damage_multiplier *= 0
  
  if move_type == "Flying" and ("Grass" in opponent_type or "Fighting" in opponent_type or "Bug" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Flying" and ("Electric" in opponent_type or "Rock" in opponent_type or "Steel" in opponent_type):
    damage_multiplier *= .5
  
  if move_type == "Psychic" and ("Fighting" in opponent_type or "Poison" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Psychic" and ("Psychic" in opponent_type or "Steel" in opponent_type):
    damage_multiplier *= .5
  if move_type == "Psychic" and ("Dark" in opponent_type):
    damage_multiplier *= 0
  
  if move_type == "Bug" and ("Grass" in opponent_type or "Psychic" in opponent_type or "Dark" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Bug" and ("Fire" in opponent_type or "Fighting" in opponent_type or "Poison" in opponent_type or "Flying" in opponent_type or "Ghost" in opponent_type or "Steel" in opponent_type or "Fairy" in opponent_type):
    damage_multiplier *= .5
  
  if move_type == "Rock" and ("Fire" in opponent_type or "Ice" in opponent_type or "Flying" in opponent_type or "Bug" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Rock" and ("Fighting" in opponent_type or "Ground" in opponent_type or "Steel" in opponent_type):
    damage_multiplier *= .5
  
  if move_type == "Ghost" and ("Psychic" in opponent_type or "Ghost" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Ghost" and ("Dark" in opponent_type):
    damage_multiplier *= .5
  if move_type == "Ghost" and ("Normal" in opponent_type):
    damage_multiplier *= 0
  
  if move_type == "Dragon" and ("Dragon" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Dragon" and ("Steel" in opponent_type):
    damage_multiplier *= .5
  if move_type == "Dragon" and ("Fairy" in opponent_type):
    damage_multiplier *= 0
  
  if move_type == "Dark" and ("Psychic" in opponent_type or "Ghost" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Dark" and ("Fighting" in opponent_type or "Dark" in opponent_type or "Fairy" in opponent_type):
    damage_multiplier *= .5
  
  if move_type == "Steel" and ("Ice" in opponent_type or "Rock" in opponent_type or "Fairy" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Steel" and ("Fire" in opponent_type or "Water" in opponent_type or "Electric" in opponent_type or "Steel" in opponent_type):
    damage_multiplier *= .5
  
  if move_type == "Fairy" and ("Fighting" in opponent_type or "Dragon" in opponent_type or "Dark" in opponent_type):
    damage_multiplier *= 2
  if move_type == "Fairy" and ("Fire" in opponent_type or "Poison" in opponent_type or "Steel" in opponent_type):
    damage_multiplier *= .5

  if damage_multiplier == 2:
    print("\nIt's super effective!")
    
  elif damage_multiplier == .5:
    print("\nIt's not very effective...")

  return damage_multiplier


def determine_damage(attack_stat, attack_level, attack_move_type, power, attack_pokemon_type, defense_pokemon_type, defense_stat, attack_modifier, defense_modifier):
  damage = (((.4 * attack_level + 2) * power * ((attack_stat * attack_modifier) / (defense_stat * defense_modifier))) / 50) + 2 
  
  if random.randint(1, 100) <= 6: #Crit
    damage *= 1.5
    print("\nA critical hit!")

  if attack_move_type in attack_pokemon_type: #STAB
    damage *= 1.5
  
  damage *= effective_check(attack_move_type, defense_pokemon_type) #Solves for type reduction/increase (passes move type and type of pokemon being attacked) returns multiplier

  damage = math.floor(damage)

  return damage


def attack_damage(sel_attacker, sel_attacker_stats, sel_defender, sel_defender_stats, sel_move, sel_attacker_stat_mod, sel_defender_stat_mod, user_or_opposing):
  if all_moves[sel_move][category] == "Physical":
    return round(determine_damage(sel_attacker_stats[attack], sel_attacker_stats[level], all_moves[sel_move][move_type], all_moves[sel_move][power], sel_attacker_stats[type], sel_defender_stats[type], sel_defender_stats[defense], sel_attacker_stat_mod[1], sel_defender_stat_mod[2]) * burned_attack_modifier[sel_attacker_stats[status_condition]]) #Attack, level, move type, power, attacker_type, defense type, defense
    
  elif all_moves[sel_move][category] == "Special":
    return round(determine_damage(sel_attacker_stats[sp_attack], sel_attacker_stats[level], all_moves[sel_move][move_type], all_moves[sel_move][power], sel_attacker_stats[type], sel_defender_stats[type], sel_defender_stats[sp_defense], sel_attacker_stat_mod[3], sel_defender_stat_mod[4]))
    
  elif all_moves[sel_move][category] == "Status":
    sel_attacker_stats[current_health] += round((sel_attacker_stats[max_health] * all_moves[sel_move][health_inc]))
    if sel_attacker_stats[current_health] > sel_attacker_stats[max_health]:
      sel_attacker_stats[current_health] = sel_attacker_stats[max_health] 

    if all_moves[sel_move][accuracy_dec] < 0: #If accuracy is decreasing apply debuff to defender
      if user_or_opposing == "Your ":
        sel_defender_stat_mod[accuracy_mod] = change_stat_modifier(sel_defender_stat_mod[accuracy_mod], all_moves[sel_move][accuracy_dec], sel_defender, "accuracy", "The opposing ")
      elif user_or_opposing == "The opposing ":
        sel_defender_stat_mod[accuracy_mod] = change_stat_modifier(sel_defender_stat_mod[accuracy_mod], all_moves[sel_move][accuracy_dec], sel_defender, "accuracy", "Your ")

    else: #If accuracy is increasing apply debuff to attacker
      sel_attacker_stat_mod[accuracy_mod] = change_stat_modifier(sel_attacker_stat_mod[accuracy_mod], all_moves[sel_move][accuracy_dec], sel_attacker, "accuracy", user_or_opposing)
    
    sel_attacker_stat_mod[attack_mod] = change_stat_modifier(sel_attacker_stat_mod[attack_mod], all_moves[sel_move][attack_inc], sel_attacker, "attack", user_or_opposing)
    sel_attacker_stat_mod[defense_mod] = change_stat_modifier(sel_attacker_stat_mod[defense_mod], all_moves[sel_move][defense_inc], sel_attacker, "defense", user_or_opposing)
    sel_attacker_stat_mod[sp_attack_mod] = change_stat_modifier(sel_attacker_stat_mod[sp_attack_mod], all_moves[sel_move][sp_attack_inc], sel_attacker, "special attack", user_or_opposing)
    sel_attacker_stat_mod[sp_defense_mod] = change_stat_modifier(sel_attacker_stat_mod[sp_defense_mod], all_moves[sel_move][sp_defense_inc], sel_attacker, "special defense", user_or_opposing)
    sel_attacker_stat_mod[speed_mod] = change_stat_modifier(sel_attacker_stat_mod[speed_mod], all_moves[sel_move][speed_inc], sel_attacker, "speed", user_or_opposing)

    if sel_defender_stats[status_condition] == "None" and all_moves[sel_move][status_debuff] != "None":
      sel_defender_stats[status_condition] = all_moves[sel_move][status_debuff]

      if user_or_opposing == "Your ":
        if all_moves[sel_move][status_debuff] == "Poisoned":
          print("\nThe opposing " + sel_defender + " is poisoned by the attack!")
  
        elif all_moves[sel_move][status_debuff] == "Asleep":
          print("\nThe opposing " + sel_defender + " fell asleep!")
  
        elif all_moves[sel_move][status_debuff] == "Burned":
          print("\nThe opposing " + sel_defender + " is burned by the attack!")
  
        elif all_moves[sel_move][status_debuff] == "Frozen":
          print("\nThe opposing " + sel_defender + " is frozen solid by the attack!")
  
        elif all_moves[sel_move][status_debuff] == "Paralyzed":
          print("\nThe opposing " + sel_defender + " is paralyzed by the attack!")

      elif user_or_opposing == "The opposing ":
        if all_moves[sel_move][status_debuff] == "Poisoned":
          print("\nYour " + sel_defender + " is poisoned by the attack!")
  
        elif all_moves[sel_move][status_debuff] == "Asleep":
          print("\nYour " + sel_defender + " fell asleep!")
  
        elif all_moves[sel_move][status_debuff] == "Burned":
          print("\nYour " + sel_defender + " is burned by the attack!")
  
        elif all_moves[sel_move][status_debuff] == "Frozen":
          print("\nYour " + sel_defender + " is frozen solid by the attack!")
  
        elif all_moves[sel_move][status_debuff] == "Paralyzed":
          print("\nYour " + sel_defender + " is paralyzed by the attack!")

    if sel_move == "Haze":
      sel_defender_stat_mod = [1, 1, 1, 1, 1, 1]
      sel_attacker_stat_mod = [1, 1, 1, 1, 1, 1]
      print("\nAll stat changes were eliminated!")
    
    return [sel_attacker_stats[current_health], sel_defender_stat_mod, sel_attacker_stat_mod, sel_defender_stats[status_condition]]

  else:
    print("Faulty Move Category")


def wild_pokemon_encounter(min_level, max_level, possible_pokemon, chance_of_encounter):
  sel_pokemon_number = random.randint(1, 100)

  last_percent_chance = 0
  for i in range(len(possible_pokemon)): #This goes through the list of encounter chance and selects the pokemon within the range
    if sel_pokemon_number >= (1 + last_percent_chance) and sel_pokemon_number <= (chance_of_encounter[i] + last_percent_chance):
      sel_foe = possible_pokemon[i]
      break
      
    last_percent_chance += chance_of_encounter[i]

  foe_stats = {} #This sets all of the stats for the foe
  foe_stats[sel_foe] = base_stats[sel_foe]
  foe_stats[sel_foe][level] = random.randint(min_level, max_level)
  foe_stats[sel_foe] = define_stats(foe_stats[sel_foe])
  foe_stats[sel_foe][exp] = round(1.25 * (foe_stats[sel_foe][level]) ** 3)
  foe_stats[sel_foe][current_health] = foe_stats[sel_foe][max_health]

  for level_index in range(math.floor((foe_stats[sel_foe][level]/4) + 2)): #This sets all of the moves for the foe
    try:
      if "None" in foe_stats[sel_foe][moves]: #This checks if one of the foe's moves is not set
        for move_index in range(4): #This goes through each of the foe's moves and replaces 'None' with the next move
          if foe_stats[sel_foe][moves][move_index] == "None":
            foe_stats[sel_foe][moves][move_index] = move_progression[sel_foe][level_index]
            break
      else: #This randomly replaces a move with another if there no empty moves
        rand_int = random.randint(0, 4)
        if rand_int == 4:
          continue
        foe_stats[sel_foe][moves][rand_int] = move_progression[sel_foe][level_index]
    except IndexError: #This makes it so it doesn't throw an error when it runs out of moves
      break

  print("\nYou encountered a level " + str(foe_stats[sel_foe][level]) + " wild " + foe_stats[sel_foe][nickname] + "!")

  sel_pokemon = db["Team Order"][0]
  pokemon_participated = [db["Team Order"][0]]

  foe_stat_mod = {sel_foe: [1, 1, 1, 1, 1, 1]} #Acc | Att | Def | Sp. Att | Sp. Def | Speed
  team_stat_mod = {}
  for pokemon_element in db["Team Order"]:
    team_stat_mod[pokemon_element] = [1, 1, 1, 1, 1, 1]
  foe_status_counter = 0
  team_status_counter = 0

  user_not_fainted = True
  opponent_not_defeated = True

  last_user_move = "None"
  last_foe_move = "None"

  while user_not_fainted and opponent_not_defeated: #At the end of the loop, check if these statements change
    print("\nFight     Bag     Pokemon     Run Away")
    user_choice = input("\nWhat will you do next? ")

    if user_choice == "Fight": #Have function return boolian
      user_move = fight_choice(sel_pokemon) #Have this return which move user picks

      if user_move == False:
        continue
      
    elif user_choice == "Bag":
      item_choice = bag("Wild Battle") #Returns boolean or item_choice
      
      if item_choice == False: #If user says cancel bring back to top
        continue
        
      elif item_choice == "Pokeball" or item_choice == "Greatball" or item_choice == "Ultraball": #If user picks a pokeball attempt to catch the pokemon
        catch_successful = catch_pokemon(item_choice, foe_stats[sel_foe][nickname], foe_stats[sel_foe]) #Return boolean

        if catch_successful == False:
          user_move = "None"

        elif catch_successful: #Add the pokemon to the team or pc
          opponent_not_defeated = False
          break

        else:
          print("Faulty Catch")
        
      else: #If user picks a potion of some sort user pokemon doesnt attack 
        if item_choice == "Antidote" or item_choice == "Awakening" or item_choice == "Burn Heal" or item_choice == "Ice Heal" or item_choice == "Paralyze Heal":
          team_status_counter = 0
          
        user_move = "None"

    elif user_choice == "Pokemon":
      switched_pokemon = pokemon("Battle", "None")

      if switched_pokemon:
        sel_pokemon = db["Team Order"][0]
        pokemon_participated.append(db["Team Order"][0])
        team_status_counter = 0
        user_move = "None"

      elif switched_pokemon == False:
        continue

      else:
        print("Faulty Switch")

    elif user_choice == "Run Away":
      odds_of_escape = (db["Team Stats"][sel_pokemon][speed] * 32)/((foe_stats[sel_foe][speed] / 4) % 256) 
      
      if odds_of_escape > 255 or random.randint(0, 255) < odds_of_escape:
        print("\nYou ran away.") 
        time.sleep(1)
        return "Ran Away"
        
      else:
        print("\nYou couldn't escape!") #Might need to change what it says
        user_move = "None"

    else:
      print("\nThat is not a valid option.")
      continue

    while True: #This selects which move the foe will use
      foe_move = foe_stats[sel_foe][moves][random.randint(0, 3)]
      if foe_move != "None":
        break

    #At this point both sides have a selected move and it now goes into the attack phase

    if (db["Team Stats"][sel_pokemon][speed] * team_stat_mod[sel_pokemon][speed_mod] * paralyzed_speed_modifier[db["Team Stats"][sel_pokemon][status_condition]]) >= (foe_stats[sel_foe][speed] * foe_stat_mod[sel_foe][speed_mod] * paralyzed_speed_modifier[foe_stats[sel_foe][status_condition]]): 
      turn_order = ["User", "Foe"]

    elif (foe_stats[sel_foe][speed] * foe_stat_mod[sel_foe][speed_mod] * paralyzed_speed_modifier[foe_stats[sel_foe][status_condition]]) > (db["Team Stats"][sel_pokemon][speed] * team_stat_mod[sel_pokemon][speed_mod] * paralyzed_speed_modifier[db["Team Stats"][sel_pokemon][status_condition]]):
      turn_order = ["Foe", "User"]

    else:
      print("Faulty Turn Order")

    if turn_order[0] == "User": #This switches turn order if a move with higher priority is used
      if foe_move == "Quick Attack" or foe_move == "Sucker Punch":
        turn_order = ["Foe", "User"]

      if user_move == "Quick Attack" or user_move == "Sucker Punch":
        turn_order = ["User", "Foe"]

    elif turn_order[0] == "Foe":
      if user_move == "Quick Attack" or user_move == "Sucker Punch":
        turn_order = ["User", "Foe"]

      if foe_move == "Quick Attack" or foe_move == "Sucker Punch":
        turn_order = ["Foe", "User"]

    while len(turn_order) > 0:
      if turn_order[0] == "User": #User's Turn
        if db["Team Stats"][sel_pokemon][current_health] > 0: 
          team_status_turn_skip = check_status_turn_skip(db["Team Stats"][sel_pokemon][status_condition], team_status_counter, db["Team Stats"][sel_pokemon][nickname], "Your ")
    
          if team_status_turn_skip[0]:
            user_move = "None"
            
          db["Team Stats"][sel_pokemon][status_condition] = team_status_turn_skip[1]
    
          if user_move != "None":
            print("\nYour " + db["Team Stats"][sel_pokemon][nickname] + " used " + user_move + "!")
            last_user_move = user_move
            time.sleep(1)

            if user_move == "Copycat" or user_move == "Mirror Move":
              if last_foe_move == "None" or last_foe_move == "Copycat" or last_foe_move == "Mirror Move":
                print("\nIt failed!")
                del turn_order[0]
                continue

              else:
                user_move = last_foe_move
                print("\nYour " + db["Team Stats"][sel_pokemon][nickname] + " used " + user_move + "!") 
            
            if ((all_moves[user_move][accuracy] * team_stat_mod[sel_pokemon][accuracy_mod]) * 100) >= random.randint(1, 100):
              if user_move == "Teleport":
                print("\nYour " + db["Team Stats"][sel_pokemon][nickname] + " teleported away!")
                return "Ran Away"
                del turn_order[0]
                continue

              if user_move == "Splash":
                print("\nBut nothing happened!")
                del turn_order[0]
                continue
                
              attack_result = attack_damage(db["Team Stats"][sel_pokemon][nickname], db["Team Stats"][sel_pokemon], foe_stats[sel_foe][nickname], foe_stats[sel_foe], user_move, team_stat_mod[sel_pokemon], foe_stat_mod[sel_foe], "Your ")
        
              if all_moves[user_move][category] == "Status":
                db["Team Stats"][sel_pokemon][current_health] = attack_result[0]
                foe_stat_mod[sel_foe] = attack_result[1]
                team_stat_mod[sel_pokemon] = attack_result[2]
                foe_stats[sel_foe][status_condition] = attack_result[3] 
        
              else:
                foe_stats[sel_foe][current_health] -= attack_result
                db["Team Stats"][sel_pokemon][current_health] -= round(db["Team Stats"][sel_pokemon][max_health] * all_moves[user_move][recoil_damage]) #Recoil damage
  
                if user_move == "Absorb" or user_move == "Drain Punch" or user_move == "Giga Drain" or user_move == "Leech Life" or user_move == "Mega Drain": #This accounts for all of the life draining moves
                  print("\nThe opposing " + foe_stats[sel_foe][nickname] + " had its energy drained!")
                  db["Team Stats"][sel_pokemon][current_health] += round(attack_result / 2)
                  if db["Team Stats"][sel_pokemon][current_health] > db["Team Stats"][sel_pokemon][max_health]:
                    db["Team Stats"][sel_pokemon][current_health] = db["Team Stats"][sel_pokemon][max_health]
  
              foe_stats[sel_foe][status_condition] = move_type_status_condition(foe_stats[sel_foe][status_condition], all_moves[user_move][move_type], foe_stats[sel_foe][nickname], "The opposing ")
        
            else:
              print("\nIt missed!")
  
              if user_move == "Jump Kick" or user_move == "High Jump Kick":
                print("\nYour " + db["Team Stats"][sel_pokemon][nickname] + " kept going and crashed!")
                db["Team Stats"][sel_pokemon][current_health] -= round(attack_damage(db["Team Stats"][sel_pokemon][nickname], db["Team Stats"][sel_pokemon], foe_stats[sel_foe][nickname], foe_stats[sel_foe], user_move, team_stat_mod[sel_pokemon], foe_stat_mod[sel_foe], "Your ") / 2)

          del turn_order[0] #This removes "User" from turn_order

        else: #sel_pokemon has fainted
          break

      elif turn_order[0] == "Foe": #Foe's Turn
        if foe_stats[sel_foe][current_health] > 0: #Foe's Turn
          foe_status_turn_skip = check_status_turn_skip(foe_stats[sel_foe][status_condition], foe_status_counter, foe_stats[sel_foe][nickname], "The opposing ")
  
          if foe_status_turn_skip[0]:
            foe_move = "None"
            
          foe_stats[sel_foe][status_condition] = foe_status_turn_skip[1]
    
          if foe_move != "None":
            print("\nThe opposing " + foe_stats[sel_foe][nickname] + " used " + foe_move + "!")
            last_foe_move = foe_move
            time.sleep(1)

            if foe_move == "Copycat" or foe_move == "Mirror Move":
              if last_user_move == "None" or last_user_move == "Copycat" or last_user_move == "Mirror Move":
                print("\nIt failed!")
                del turn_order[0]
                continue

              else:
                foe_move = last_user_move
                print("\nThe opposing " + foe_stats[sel_foe][nickname] + " used " + foe_move + "!") 
            
            if ((all_moves[foe_move][accuracy] * foe_stat_mod[sel_foe][accuracy_mod]) * 100) >= random.randint(1, 100):
              if foe_move == "Teleport":
                print("\nThe opposing " + foe_stats[sel_foe][nickname] + " teleported away!")
                return "Ran Away"

              if foe_move == "Splash": 
                print("\nBut nothing happened!")
                del turn_order[0]
                continue
                
              attack_result = attack_damage(foe_stats[sel_foe][nickname], foe_stats[sel_foe], db["Team Stats"][sel_pokemon][nickname], db["Team Stats"][sel_pokemon], foe_move, foe_stat_mod[sel_foe], team_stat_mod[sel_pokemon], "The opposing ")
        
              if all_moves[foe_move][category] == "Status":
                foe_stats[sel_foe][current_health] = attack_result[0]
                team_stat_mod[sel_pokemon] = attack_result[1]
                foe_stat_mod[sel_foe] = attack_result[2]
                db["Team Stats"][sel_pokemon][status_condition] = attack_result[3] 
        
              else:
                db["Team Stats"][sel_pokemon][current_health] -= attack_result
                foe_stats[sel_foe][current_health] -= round(foe_stats[sel_foe][max_health] * all_moves[foe_move][recoil_damage]) #Recoil damage
  
                if foe_move == "Absorb" or foe_move == "Drain Punch" or foe_move == "Giga Drain" or foe_move == "Leech Life" or foe_move == "Mega Drain": #This accounts for all of the life draining moves
                  print("\nYour " + db["Team Stats"][sel_pokemon][nickname] + " had its energy drained!")
                  foe_stats[sel_foe][current_health] += round(attack_result / 2)
                  if foe_stats[sel_foe][current_health] > foe_stats[sel_foe][max_health]:
                    foe_stats[sel_foe][current_health] = foe_stats[sel_foe][max_health]
  
              db["Team Stats"][sel_pokemon][status_condition] = move_type_status_condition(db["Team Stats"][sel_pokemon][status_condition], all_moves[foe_move][move_type], db["Team Stats"][sel_pokemon][nickname], "Your ")
      
            else:
              print("\nIt missed!")
  
              if foe_move == "Jump Kick" or foe_move == "High Jump Kick":
                print("\nThe opposing " + foe_stats[sel_foe][nickname] + " kept going and crashed!")
                db["Team Stats"][sel_foe][current_health] -= round(attack_damage(foe_stats[sel_foe][nickname], foe_stats[sel_foe], db["Team Stats"][sel_pokemon][nickname], db["Team Stats"][sel_pokemon], foe_move, foe_stat_mod[sel_foe], team_stat_mod[sel_pokemon], "The opposing ") / 2)

          del turn_order[0] #This removes "Foe" from turn_order
          
        else: #sel_foe has fainted
          break
    
    #At this point the attacking phase has passed and now it checks for poison and burn status
    
    if foe_stats[sel_foe][status_condition] == "Poisoned":
      foe_stats[sel_foe][current_health] -= round(foe_stats[sel_foe][max_health] / 8)
      print("\nThe opposing " + foe_stats[sel_foe][nickname] + " is hurt by the poison.")

    elif foe_stats[sel_foe][status_condition] == "Burned":
      foe_stats[sel_foe][current_health] -= round(foe_stats[sel_foe][max_health] / 16)
      print("\nThe opposing " + foe_stats[sel_foe][nickname] + " is hurt by the burn.")

    if db["Team Stats"][sel_pokemon][status_condition] == "Poisoned":
      db["Team Stats"][sel_pokemon][current_health] -= round(db["Team Stats"][sel_pokemon][max_health] / 8)
      print("\nYour " + db["Team Stats"][sel_pokemon][nickname] + " is hurt by the poison.")

    elif db["Team Stats"][sel_pokemon][status_condition] == "Burned":
      db["Team Stats"][sel_pokemon][current_health] -= round(db["Team Stats"][sel_pokemon][max_health] / 16)
      print("\nYour " + db["Team Stats"][sel_pokemon][nickname] + " is hurt by the burn.")

    #This increases or resets the value on the status counter if necessary

    if foe_stats[sel_foe][status_condition] != "None":
      foe_status_counter += 1

    else:
      foe_status_counter = 0

    if db["Team Stats"][sel_pokemon][status_condition] != "None":
      team_status_counter += 1

    else:
      team_status_counter = 0
            
    #This prints out the updated health

    print_stats(sel_foe, foe_stats[sel_foe][level], foe_stats[sel_foe][current_health], foe_stats[sel_foe][max_health], foe_stats[sel_foe][status_condition], "The opposing ") 

    print_stats(db["Team Stats"][sel_pokemon][nickname], db["Team Stats"][sel_pokemon][level], db["Team Stats"][sel_pokemon][current_health], db["Team Stats"][sel_pokemon][max_health], db["Team Stats"][sel_pokemon][status_condition], "Your ")

    #This checks the status of both sides and checks if any of them have fainted

    if db["Team Stats"][sel_pokemon][current_health] <= 0:
      db["Team Stats"][sel_pokemon][current_health] = 0

      print("\nYour " + db["Team Stats"][sel_pokemon][nickname] + " fainted!") 

      team_fainted = True #This checks if the team has all fainted
      for key_element in [*db["Team Stats"]]:
        if db["Team Stats"][key_element][current_health] > 0: 
          team_fainted = False
          break

      if team_fainted == False:
        while True:
          if pokemon("Battle", "None"):
            sel_pokemon = db["Team Order"][0]
            pokemon_participated.append(sel_pokemon)
            break
            
          else:
            print("\nYou must switch to another pokemon!")

        team_status_counter = 0

      else:
        print("\nAll of your pokemon have fainted! You hurry to the Pokémon Center with your fainted pokemon...")
        user_not_fainted = False

    if foe_stats[sel_foe][current_health] <= 0:
      foe_stats[sel_foe][current_health] = 0

      print("\nThe opposing " + foe_stats[sel_foe][nickname] + " fainted!") 

      opponent_not_defeated = False

  #This looks at which boolean has changed after the battle is over and returns a statement based on the outcome

  if user_not_fainted == False:
    return "Pokemon Center"
    
  elif opponent_not_defeated == False:
    battle_rewards("Wild", foe_stats[sel_foe][level], pokemon_participated, sel_foe)
    return "Opponent Defeated"

  else:
    print("Faulty Wild End Value")


def trainer_encounter(trainer_name, reward_money, trainer_pokemon, trainer_pokemon_level, trainer_pokemon_moves):
  sel_foe = trainer_pokemon[0]
  
  foe_stats = {} #This sets all of the stats for the foe

  for index in range(len(trainer_pokemon)):
    foe_stats[trainer_pokemon[index]] = base_stats[trainer_pokemon[index]]
    foe_stats[trainer_pokemon[index]][level] = trainer_pokemon_level[index]
    foe_stats[trainer_pokemon[index]] = define_stats(foe_stats[trainer_pokemon[index]])
    foe_stats[trainer_pokemon[index]][exp] = round(1.25 * (foe_stats[trainer_pokemon[index]][level]) ** 3)
    foe_stats[trainer_pokemon[index]][current_health] = foe_stats[trainer_pokemon[index]][max_health]

    if trainer_pokemon_moves == "Random":
      for level_index in range(math.floor((foe_stats[trainer_pokemon[index]][level]/4) + 2)): #This sets all of the moves for the foe
        try:
          if "None" in foe_stats[trainer_pokemon[index]][moves]: #This checks if one of the foe's moves is not set
            for move_index in range(4): #This goes through each of the foe's moves and replaces 'None' with the next move
              if foe_stats[trainer_pokemon[index]][moves][move_index] == "None":
                foe_stats[trainer_pokemon[index]][moves][move_index] = move_progression[trainer_pokemon[index]][level_index]
                break
          else: #This randomly replaces a move with another if there no empty moves
            rand_int = random.randint(0, 4)
            if rand_int == 4:
              continue
            foe_stats[trainer_pokemon[index]][moves][rand_int] = move_progression[trainer_pokemon[index]][level_index]
        except IndexError: #This makes it so it doesn't throw an error when it runs out of moves
          break
  
    else:
      foe_stats[trainer_pokemon[index]][moves] = trainer_pokemon_moves[index]

  print("\nYou were approached by " + trainer_name + "!")
  print("\n" + pre_battle_quotes[trainer_name][random.randint(0, len(pre_battle_quotes[trainer_name]) - 1)])
  print("\n" + trainer_name + " sent out a level " + str(foe_stats[sel_foe][level]) + " " + foe_stats[sel_foe][nickname] + "!")

  sel_pokemon = db["Team Order"][0]
  pokemon_participated = [db["Team Order"][0]]

  foe_stat_mod = {} #Acc | Att | Def | Sp. Att | Sp. Def | Speed
  for pokemon_element in trainer_pokemon:
    foe_stat_mod[pokemon_element] = [1, 1, 1, 1, 1, 1]
    
  team_stat_mod = {}
  for pokemon_element in db["Team Order"]:
    team_stat_mod[pokemon_element] = [1, 1, 1, 1, 1, 1]
    
  foe_status_counter = 0
  team_status_counter = 0

  user_not_fainted = True
  opponent_not_defeated = True

  last_user_move = "None"
  last_foe_move = "None"

  while user_not_fainted and opponent_not_defeated: #At the end of the loop, check if these statements change
    print("\nFight     Bag     Pokemon     Run Away")
    user_choice = input("\nWhat will you do next? ")

    if user_choice == "Fight": #Have function return boolian
      user_move = fight_choice(sel_pokemon) #Have this return which move user picks

      if user_move == False:
        continue
      
    elif user_choice == "Bag":
      item_choice = bag("Trainer Battle") #Returns boolean or item_choice
      
      if item_choice == False: #If user says cancel bring back to top
        continue
        
      elif item_choice == "Pokeball" or item_choice == "Greatball" or item_choice == "Ultraball": #If user picks a pokeball attempt to catch the pokemon
        catch_successful = catch_pokemon(item_choice, foe_stats[sel_foe][nickname], foe_stats[sel_foe]) #Return boolean

        if catch_successful == False:
          user_move = "None"

        elif catch_successful: #Add the pokemon to the team or pc
          opponent_not_defeated = False
          break

        else:
          print("Faulty Catch")
        
      else: #If user picks a potion of some sort user pokemon doesnt attack 
        if item_choice == "Antidote" or item_choice == "Awakening" or item_choice == "Burn Heal" or item_choice == "Ice Heal" or item_choice == "Paralyze Heal":
          team_status_counter = 0
          
        user_move = "None"

    elif user_choice == "Pokemon":
      switched_pokemon = pokemon("Battle", "None")

      if switched_pokemon:
        sel_pokemon = db["Team Order"][0]
        pokemon_participated.append(db["Team Order"][0])
        team_status_counter = 0
        user_move = "None"

      elif switched_pokemon == False:
        continue

      else:
        print("Faulty Switch")

    elif user_choice == "Run Away":
      print("\nYou can't run from a trainer battle!")
      continue

    else:
      print("\nThat is not a valid option.")
      continue

    while True: #This selects which move the foe will use
      foe_move = foe_stats[sel_foe][moves][random.randint(0, 3)]
      if foe_move != "None":
        break

    #At this point both sides have a selected move and it now goes into the attack phase

    if (db["Team Stats"][sel_pokemon][speed] * team_stat_mod[sel_pokemon][speed_mod] * paralyzed_speed_modifier[db["Team Stats"][sel_pokemon][status_condition]]) >= (foe_stats[sel_foe][speed] * foe_stat_mod[sel_foe][speed_mod] * paralyzed_speed_modifier[foe_stats[sel_foe][status_condition]]): 
      turn_order = ["User", "Foe"]

    elif (foe_stats[sel_foe][speed] * foe_stat_mod[sel_foe][speed_mod] * paralyzed_speed_modifier[foe_stats[sel_foe][status_condition]]) > (db["Team Stats"][sel_pokemon][speed] * team_stat_mod[sel_pokemon][speed_mod] * paralyzed_speed_modifier[db["Team Stats"][sel_pokemon][status_condition]]):
      turn_order = ["Foe", "User"]

    else:
      print("Faulty Turn Order")

    if turn_order[0] == "User": #This switches turn order if a move with higher priority is used
      if foe_move == "Quick Attack" or foe_move == "Sucker Punch":
        turn_order = ["Foe", "User"]

      if user_move == "Quick Attack" or user_move == "Sucker Punch":
        turn_order = ["User", "Foe"]

    elif turn_order[0] == "Foe":
      if user_move == "Quick Attack" or user_move == "Sucker Punch":
        turn_order = ["User", "Foe"]

      if foe_move == "Quick Attack" or foe_move == "Sucker Punch":
        turn_order = ["Foe", "User"]

    while len(turn_order) > 0:
      if turn_order[0] == "User": #User's Turn
        if db["Team Stats"][sel_pokemon][current_health] > 0: 
          team_status_turn_skip = check_status_turn_skip(db["Team Stats"][sel_pokemon][status_condition], team_status_counter, db["Team Stats"][sel_pokemon][nickname], "Your ")
    
          if team_status_turn_skip[0]:
            user_move = "None"
            
          db["Team Stats"][sel_pokemon][status_condition] = team_status_turn_skip[1]
    
          if user_move != "None":
            print("\nYour " + db["Team Stats"][sel_pokemon][nickname] + " used " + user_move + "!")
            last_user_move = user_move
            time.sleep(1)

            if user_move == "Copycat" or user_move == "Mirror Move":
              if last_foe_move == "None" or last_foe_move == "Copycat" or last_foe_move == "Mirror Move":
                print("\nIt failed!")
                del turn_order[0]
                continue

              else:
                user_move = last_foe_move
                print("\nYour " + db["Team Stats"][sel_pokemon][nickname] + " used " + user_move + "!") 
            
            if ((all_moves[user_move][accuracy] * team_stat_mod[sel_pokemon][accuracy_mod]) * 100) >= random.randint(1, 100):
              if user_move == "Teleport":
                print("\nYour " + db["Team Stats"][sel_pokemon][nickname] + " teleported away!")
                return "Ran Away"
                del turn_order[0]
                continue

              if user_move == "Splash":
                print("\nBut nothing happened!")
                del turn_order[0]
                continue
                
              attack_result = attack_damage(db["Team Stats"][sel_pokemon][nickname], db["Team Stats"][sel_pokemon], foe_stats[sel_foe][nickname], foe_stats[sel_foe], user_move, team_stat_mod[sel_pokemon], foe_stat_mod[sel_foe], "Your ")
        
              if all_moves[user_move][category] == "Status":
                db["Team Stats"][sel_pokemon][current_health] = attack_result[0]
                foe_stat_mod[sel_foe] = attack_result[1]
                team_stat_mod[sel_pokemon] = attack_result[2]
                foe_stats[sel_foe][status_condition] = attack_result[3] 
        
              else:
                foe_stats[sel_foe][current_health] -= attack_result
                db["Team Stats"][sel_pokemon][current_health] -= round(db["Team Stats"][sel_pokemon][max_health] * all_moves[user_move][recoil_damage]) #Recoil damage
  
                if user_move == "Absorb" or user_move == "Drain Punch" or user_move == "Giga Drain" or user_move == "Leech Life" or user_move == "Mega Drain": #This accounts for all of the life draining moves
                  print("\nThe opposing " + foe_stats[sel_foe][nickname] + " had its energy drained!")
                  db["Team Stats"][sel_pokemon][current_health] += round(attack_result / 2)
                  if db["Team Stats"][sel_pokemon][current_health] > db["Team Stats"][sel_pokemon][max_health]:
                    db["Team Stats"][sel_pokemon][current_health] = db["Team Stats"][sel_pokemon][max_health]
  
              foe_stats[sel_foe][status_condition] = move_type_status_condition(foe_stats[sel_foe][status_condition], all_moves[user_move][move_type], foe_stats[sel_foe][nickname], "The opposing ")
        
            else:
              print("\nIt missed!")
  
              if user_move == "Jump Kick" or user_move == "High Jump Kick":
                print("\nYour " + db["Team Stats"][sel_pokemon][nickname] + " kept going and crashed!")
                db["Team Stats"][sel_pokemon][current_health] -= round(attack_damage(db["Team Stats"][sel_pokemon][nickname], db["Team Stats"][sel_pokemon], foe_stats[sel_foe][nickname], foe_stats[sel_foe], user_move, team_stat_mod[sel_pokemon], foe_stat_mod[sel_foe], "Your ") / 2)

          del turn_order[0] #This removes "User" from turn_order

        else: #sel_pokemon has fainted
          break

      elif turn_order[0] == "Foe": #Foe's Turn
        if foe_stats[sel_foe][current_health] > 0: #Foe's Turn
          foe_status_turn_skip = check_status_turn_skip(foe_stats[sel_foe][status_condition], foe_status_counter, foe_stats[sel_foe][nickname], "The opposing ")
  
          if foe_status_turn_skip[0]:
            foe_move = "None"
            
          foe_stats[sel_foe][status_condition] = foe_status_turn_skip[1]
    
          if foe_move != "None":
            print("\nThe opposing " + foe_stats[sel_foe][nickname] + " used " + foe_move + "!")
            last_foe_move = foe_move
            time.sleep(1)

            if foe_move == "Copycat" or foe_move == "Mirror Move":
              if last_user_move == "None" or last_user_move == "Copycat" or last_user_move == "Mirror Move":
                print("\nIt failed!")
                del turn_order[0]
                continue

              else:
                foe_move = last_user_move
                print("\nThe opposing " + foe_stats[sel_foe][nickname] + " used " + foe_move + "!") 
            
            if ((all_moves[foe_move][accuracy] * foe_stat_mod[sel_foe][accuracy_mod]) * 100) >= random.randint(1, 100):
              if foe_move == "Teleport":
                print("\nThe opposing " + foe_stats[sel_foe][nickname] + " teleported away!")
                return "Ran Away"

              if foe_move == "Splash": 
                print("\nBut nothing happened!")
                del turn_order[0]
                continue
                
              attack_result = attack_damage(foe_stats[sel_foe][nickname], foe_stats[sel_foe], db["Team Stats"][sel_pokemon][nickname], db["Team Stats"][sel_pokemon], foe_move, foe_stat_mod[sel_foe], team_stat_mod[sel_pokemon], "The opposing ")
        
              if all_moves[foe_move][category] == "Status":
                foe_stats[sel_foe][current_health] = attack_result[0]
                team_stat_mod[sel_pokemon] = attack_result[1]
                foe_stat_mod[sel_foe] = attack_result[2]
                db["Team Stats"][sel_pokemon][status_condition] = attack_result[3] 
        
              else:
                db["Team Stats"][sel_pokemon][current_health] -= attack_result
                foe_stats[sel_foe][current_health] -= round(foe_stats[sel_foe][max_health] * all_moves[foe_move][recoil_damage]) #Recoil damage
  
                if foe_move == "Absorb" or foe_move == "Drain Punch" or foe_move == "Giga Drain" or foe_move == "Leech Life" or foe_move == "Mega Drain": #This accounts for all of the life draining moves
                  print("\nYour " + db["Team Stats"][sel_pokemon][nickname] + " had its energy drained!")
                  foe_stats[sel_foe][current_health] += round(attack_result / 2)
                  if foe_stats[sel_foe][current_health] > foe_stats[sel_foe][max_health]:
                    foe_stats[sel_foe][current_health] = foe_stats[sel_foe][max_health]
  
              db["Team Stats"][sel_pokemon][status_condition] = move_type_status_condition(db["Team Stats"][sel_pokemon][status_condition], all_moves[foe_move][move_type], db["Team Stats"][sel_pokemon][nickname], "Your ")
      
            else:
              print("\nIt missed!")
  
              if foe_move == "Jump Kick" or foe_move == "High Jump Kick":
                print("\nThe opposing " + foe_stats[sel_foe][nickname] + " kept going and crashed!")
                db["Team Stats"][sel_foe][current_health] -= round(attack_damage(foe_stats[sel_foe][nickname], foe_stats[sel_foe], db["Team Stats"][sel_pokemon][nickname], db["Team Stats"][sel_pokemon], foe_move, foe_stat_mod[sel_foe], team_stat_mod[sel_pokemon], "The opposing ") / 2)

          del turn_order[0] #This removes "Foe" from turn_order
          
        else: #sel_foe has fainted
          break
    
    #At this point the attacking phase has passed and now it checks for poison and burn status
    
    if foe_stats[sel_foe][status_condition] == "Poisoned":
      foe_stats[sel_foe][current_health] -= round(foe_stats[sel_foe][max_health] / 8)
      print("\nThe opposing " + foe_stats[sel_foe][nickname] + " is hurt by the poison.")

    elif foe_stats[sel_foe][status_condition] == "Burned":
      foe_stats[sel_foe][current_health] -= round(foe_stats[sel_foe][max_health] / 16)
      print("\nThe opposing " + foe_stats[sel_foe][nickname] + " is hurt by the burn.")

    if db["Team Stats"][sel_pokemon][status_condition] == "Poisoned":
      db["Team Stats"][sel_pokemon][current_health] -= round(db["Team Stats"][sel_pokemon][max_health] / 8)
      print("\nYour " + db["Team Stats"][sel_pokemon][nickname] + " is hurt by the poison.")

    elif db["Team Stats"][sel_pokemon][status_condition] == "Burned":
      db["Team Stats"][sel_pokemon][current_health] -= round(db["Team Stats"][sel_pokemon][max_health] / 16)
      print("\nYour " + db["Team Stats"][sel_pokemon][nickname] + " is hurt by the burn.")

    #This increases or resets the value on the status counter if necessary

    if foe_stats[sel_foe][status_condition] != "None":
      foe_status_counter += 1

    else:
      foe_status_counter = 0

    if db["Team Stats"][sel_pokemon][status_condition] != "None":
      team_status_counter += 1

    else:
      team_status_counter = 0
            
    #This prints out the updated health

    print_stats(foe_stats[sel_foe][nickname], foe_stats[sel_foe][level], foe_stats[sel_foe][current_health], foe_stats[sel_foe][max_health], foe_stats[sel_foe][status_condition], "The opposing ") 

    print_stats(db["Team Stats"][sel_pokemon][nickname], db["Team Stats"][sel_pokemon][level], db["Team Stats"][sel_pokemon][current_health], db["Team Stats"][sel_pokemon][max_health], db["Team Stats"][sel_pokemon][status_condition], "Your ")

    #This checks the status of both sides and checks if any of them have fainted

    if db["Team Stats"][sel_pokemon][current_health] <= 0:
      db["Team Stats"][sel_pokemon][current_health] = 0

      print("\nYour " + db["Team Stats"][sel_pokemon][nickname] + " fainted!") 

      team_fainted = True #This checks if the team has all fainted
      for key_element in [*db["Team Stats"]]:
        if db["Team Stats"][key_element][current_health] > 0: 
          team_fainted = False
          break

      if team_fainted == False:
        while True:
          if pokemon("Battle", "None"):
            sel_pokemon = db["Team Order"][0]
            pokemon_participated.append(sel_pokemon)
            break
            
          else:
            print("\nYou must switch to another pokemon!")

        team_status_counter = 0

      else:
        print("\nAll of your pokemon have fainted! You hurry to the Pokémon Center with your fainted pokemon...")
        user_not_fainted = False

    if foe_stats[sel_foe][current_health] <= 0:
      foe_stats[sel_foe][current_health] = 0

      print("\nThe opposing " + foe_stats[sel_foe][nickname] + " fainted!") 

      battle_rewards("Trainer", foe_stats[sel_foe][level], pokemon_participated, sel_foe)

      if db["Team Order"][0] != sel_pokemon:
        team_stat_mod[db["Team Order"][0]] = team_stat_mod[sel_pokemon]
        del team_stat_mod[sel_pokemon]
        sel_pokemon = db["Team Order"][0]
      
      pokemon_participated = [db["Team Order"][0]] #This resets who has participated

      trainer_fainted = True #This checks if the trainer has fainted
      for key_element in trainer_pokemon:
        if foe_stats[key_element][current_health] > 0: 
          trainer_fainted = False 
          break

      if trainer_fainted == False: #If the trainer still has a living pokemon, find it and switch to it
        for key_element in trainer_pokemon:
          if foe_stats[key_element][current_health] > 0: 
            sel_foe = key_element
            print("\n" + trainer_name + " sent out a level " + str(foe_stats[sel_foe][level]) + " " + foe_stats[sel_foe][nickname] + "!")
            break

      else:
        opponent_not_defeated = False

  #This looks at which boolean has changed after the battle is over and returns a statement based on the outcome

  if user_not_fainted == False:
    return "Pokemon Center"
    
  elif opponent_not_defeated == False:
    print("\n" + db["User Name"] + " defeated " + trainer_name + "!")
    #Here we could print a random generic quote of defeat
    print("\nYou received " + str(reward_money) + " Poke Dollars!")
    return "Opponent Defeated"

  else:
    print("Faulty Trainer End Value")


        
    