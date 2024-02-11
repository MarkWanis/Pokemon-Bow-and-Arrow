#This defines the stats needed for a pokemon, i.e. max health, attack, etc.

import math #math.floor(number)

from game_info import *


def define_stats(stats): #This takes a list of stats and updates variables based on base stats, returning the list
  stats[max_health] = math.floor(.01 * (2 * stats[base_health] + 30 + math.floor(.25 * 250)) * stats[level]) + stats[level] + 10

  stats[attack] = math.floor(.01 * (2 * stats[base_attack] + 30 + math.floor(.25 * 250)) * stats[level]) + stats[level] + 10

  stats[defense] = math.floor(.01 * (2 * stats[base_defense] + 30 + math.floor(.25 * 250)) * stats[level]) + stats[level] + 10

  stats[sp_attack] = math.floor(.01 * (2 * stats[base_sp_attack] + 30 + math.floor(.25 * 250)) * stats[level]) + stats[level] + 10

  stats[sp_defense] = math.floor(.01 * (2 * stats[base_sp_defense] + 30 + math.floor(.25 * 250)) * stats[level]) + stats[level] + 10

  stats[speed] = math.floor(.01 * (2 * stats[base_speed] + 30 + math.floor(.25 * 250)) * stats[level]) + stats[level] + 10

  return stats