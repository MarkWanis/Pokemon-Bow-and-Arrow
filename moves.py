#This creates a dictionary of each pokemon move

#"Move": [Type, Category, Power Points, Power, Accuracy, (For status moves only) Health Increase, Attack Increase, Defense Increase, Sp. Attack Increase, Sp. Defense Increase, Speed Increase, Accuracy Decrease, Status Debuff]
move_type = 0
category = 1
power_points = 2
power = 3
accuracy = 4
recoil_damage = 5 
health_inc = 5 #Only for status
attack_inc = 6
defense_inc = 7
sp_attack_inc = 8
sp_defense_inc = 9
speed_inc = 10
accuracy_dec = 11
status_debuff = 12

all_moves = {
  "Pound": ["Normal", "Physical", 35, 40, 1, 0],
  "Karate Chop": ["Fighting", "Physical", 25, 50, 1, 0],
  "Double Slap": ["Normal", "Physical", 10, 45, 1, 0],
  "Comet Punch": ["Normal", "Physical", 15, 18, .85, 0],
  "Mega Punch": ["Normal", "Physical", 20, 80, .85, 0],
  "Pay Day": ["Normal", "Physical", 20, 40, 1, 0], #
  "Fire Punch": ["Fire", "Physical", 15, 75, 1, 0],
  "Ice Punch": ["Ice", "Physical", 15, 75, 1, 0],
  "Thunder Punch": ["Electric", "Physical", 15, 75, 1, 0],
  "Scratch": ["Normal", "Physical", 35, 40, 1, 0],
  "Vise Grip": ["Normal", "Physical", 30, 55, 1, 0],
  "Guillotine": ["Normal", "Physical", 5, 0, .3, 0],
  "Razor Wind": ["Normal", "Special", 10, 80, 1, 0],
  "Swords Dance": ["Normal", "Status", 20, 0, 10, 0, 2, 0, 0, 0, 0, 0, "None"], 
  "Cut": ["Normal", "Physical", 30, 50, 1, 0], 
  "Gust": ["Flying", "Special", 35, 40, 1, 0],
  "Wing Attack": ["Flying", "Physical", 35, 60, 1, 0],
  #"Bind": ["Normal", "Physical", 20, 15, 1, 0],
  "Slam": ["Normal", "Physical", 20, 80, .75, 0],
  "Vine Whip": ["Grass", "Physical", 25, 45, 1, 0],
  "Stomp": ["Normal", "Physical", 20, 65, 1, 0],
  "Double Kick": ["Fighting", "Physical", 30, 60, 1, 0],
  "Mega Kick": ["Normal", "Physical", 5, 120, .75, 0], 
  "Jump Kick": ["Fighting", "Physical", 10, 100, .95, 0],
  "Rolling Kick": ["Fighting", "Physical", 15, 60, .85, 0],
  "Sand Attack": ["Ground", "Status", 15, 0, 1, 0, 0, 0, 0, 0, 0, -1, "None"], 
  "Headbutt": ["Normal", "Physical", 15, 70, 1, 0],
  "Horn Attack": ["Normal", "Physical", 25, 65, 1, 0],
  "Fury Attack": ["Normal", "Physical", 20, 45, 1, 0],
  "Horn Drill": ["Normal", "Physical", 5, 0, .3, 0],
  "Tackle": ["Normal", "Physical", 35, 40, 1, 0],
  "Body Slam": ["Normal", "Physical", 15, 85, 1, 0],
  #"Wrap": ["Normal", "Physical", 20, 15, .9, 0],
  "Take Down": ["Normal", "Physical", 20, 90, .85, .25],
  "Double-Edge": ["Normal", "Physical", 15, 120, 1, .33],
  "Tail Whip": ["Normal", "Status", 30, 0, 1, 0, 1, 0, 0, 0, 0, 0, "None"],
  "Poison Sting": ["Poison", "Physical", 35, 15, 1, 0],
  "Twineedle": ["Bug", "Physical", 20, 25, 1, 0],
  "Pin Missile": ["Bug", "Physical", 20, 25, .95, 0],
  "Leer": ["Normal", "Status", 30, 0, 1, 0, 1, 0, 0, 0, 0, 0, "None"],
  "Bite": ["Dark", "Physical", 25, 60, 1, 0], #
  "Growl": ["Normal", "Status", 40, 0, 10, 0, 0, 1, 0, 0, 0, 0, "None"],
  "Sing": ["Normal", "Status", 15, 0, .55, 0, 0, 0, 0, 0, 0, 0, "Asleep"], 
  #"Supersonic": ["Normal", "Status", 20, 0, .55], #
  #"Sonic Boom": ["Normal", "Special", 20, 0, .9], #Always does 20 damage
  "Acid": ["Poison", "Special", 30, 40, 1, 0],
  "Ember": ["Fire", "Special", 25, 40, 1, 0],
  "Flamethrower": ["Fire", "Special", 15, 90, 1, 0],
  "Water Gun": ["Water", "Special", 25, 40, 1, 0],
  "Hydro Pump": ["Water", "Special", 5, 110, .8, 0],
  "Surf": ["Water", "Special", 15, 90, 1, 0],
  "Ice Beam": ["Ice", "Special", 10, 90, 1, 0],
  "Blizzard": ["Ice", "Special", 5, 110, .7, 0],
  "Psybeam": ["Psychic", "Special", 20, 65, 1, 0], #Confuse
  "Bubble Beam": ["Water", "Special", 20, 65, 1, 0],
  "Aurora Beam": ["Ice", "Special", 20, 65, 1, 0],
  "Peck": ["Flying", "Physical", 35, 35, 1, 0],
  "Drill Peck": ["Flying", "Physical", 20, 80, 1, 0],
  "Submission": ["Fighting", "Physical", 20, 80, .8, .25],
  "Low Kick": ["Fighting", "Physical", 20, 50, .9, 0],
  #"Counter": ["Fighting", "Physical", 20, 0, 1, 0], #
  #"Seismic Toss": ["Fighting", "Physical", 20, 0, 1, 0], #
  "Strength": ["Normal", "Physical", 15, 80, 1, 0],
  "Absorb": ["Grass", "Special", 25, 20, 1, 0],
  "Mega Drain": ["Grass", "Special", 15, 40, 1, 0],
  #"Leech Seed": ["Grass", "Status", 10, 0, .9, 0, 0, 0, 0, 0, 0, 0, "None"], #
  "Growth": ["Normal", "Status", 20, 0, 10, 0, 1, 0, 1, 0, 0, 0, "None"],
  "Razor Leaf": ["Grass", "Physical", 25, 55, .95, 0],
  "Solar Beam": ["Grass", "Special", 10, 60, 1, 0], #
  "Poison Powder": ["Poison", "Status", 30, 0, .75, 0, 0, 0, 0, 0, 0, 0, "Poisoned"], 
  "Stun Spore": ["Grass", "Status", 30, 0, .75, 0, 0, 0, 0, 0, 0, 0, "Paralyzed"], 
  "Sleep Powder": ["Grass", "Status", 15, 0, .75, 0, 0, 0, 0, 0, 0, 0, "Asleep"], 
  "Petal Dance": ["Grass", "Special", 10, 120, 1, 0],
  "String Shot": ["Bug", "Status", 40, 0, .95, 0, 0, 0, 0, 0, 0, -2, "None"],
  #"Dragon Rage": ["Dragon", "Special", 10, 0, .1], #Always does 40 damage
  "Thunder Shock": ["Electric", "Special", 30, 40, 1, 0],
  "Thunderbolt": ["Electric", "Special", 15, 90, 1, 0],
  "Thunder Wave": ["Electric", "Status", 20, 0, .9, 0, 0, 0, 0, 0, 0, 0, "Paralyzed"], 
  "Thunder": ["Electric", "Special", 10, 110, .7, 0],
  "Rock Throw": ["Rock", "Physical", 15, 50, .9, 0],
  "Earthquake": ["Ground", "Physical", 10, 100, 1, 0],
  #"Fissure": ["Ground", "Physical", 5, 0, .3, 0], #Maybe check accuracy to see whether it one shots or not
  "Toxic": ["Poison", "Status", 10, 0, .9, 0, 0, 0, 0, 0, 0, 0, "Poisoned"], 
  "Confusion": ["Psychic", "Special", 25, 50, 1, 0], #
  "Psychic": ["Psychic", "Special", 10, 90, 1, 0],
  "Hypnosis": ["Psychic", "Status", 20, 0, .6, 0, 0, 0, 0, 0, 0, 0, "Asleep"], 
  "Meditate": ["Psychic", "Status", 40, 0, 10, 0, 1, 0, 0, 0, 0, 0, "None"],
  "Agility": ["Psychic", "Status", 30, 0, 10, 0, 0, 0, 0, 0, 2, 0, "None"],
  "Quick Attack": ["Normal", "Physical", 30, 40, 1, 0],
  "Rage": ["Normal", "Physical", 20, 20, 1, 0],
  "Teleport": ["Psychic", "Status", 20, 0, 10, 0, 0, 0, 0, 0, 0, 0, "None"], 
  "Night Shade": ["Ghost", "Special", 15, 0, 1, 0],
  "Screech": ["Normal", "Status", 40, 0, .85, 0, 2, 0, 0, 0, 0, 0, "None"],
  "Double Team": ["Normal", "Status", 15, 0, 10, 0, 0, 0, 0, 0, 0, -1, "None"],
  "Recover": ["Normal", "Status", 10, 0, 10, .5, 0, 0, 0, 0, 0, 0, "None"],
  "Harden": ["Normal", "Status", 30, 0, 10, 0, 0, 1, 0, 0, 0, 0, "None"],
  "Minimize": ["Normal", "Status", 10, 0, 10, 0, 0, 0, 0, 0, 0, 2, "None"],
  "Smokescreen": ["Normal", "Status", 20, 0, 1, 0, 0, 0, 0, 0, 0, -1, "None"],
  "Confuse Ray": ["Ghost", "Status", 10, 0, 1, 0, 0, 0, 0, 0, 0, 0, "None"], #Confuse
  "Withdraw": ["Water", "Status", 40, 0, 10, 0, 0, 1, 0, 0, 0, 0, "None"],
  "Defense Curl": ["Normal", "Status", 40, 0, 10, 0, 0, 1, 0, 0, 0, 0, "None"],
  "Barrier": ["Psychic", "Status", 20, 0, 10, 0, 0, 2, 0, 0, 0, 0, "None"],
  "Haze": ["Ice", "Status", 30, 0, 10, 0, 0, 0, 0, 0, 0, 0, "None"], 
  #"Focus Energy": ["Normal", "Status", 30, 0, 10, 0, 0, 0, 0, 0, 0, 0, "None"], #Crit ratio
  #"Bide": ["Normal", "Physical", 10, 0, 1, 0], #
  #"Metronome": ["Normal", "Physical", 10, 0, 10, 0], #Random move
  "Mirror Move": ["Flying", "Status", 20, 0, 10, 0], 
  "Self-Destruct": ["Normal", "Physical", 5, 200, 1, 1], 
  "Egg Bomb": ["Normal", "Physical", 10, 100, .75, 0],
  "Lick": ["Ghost", "Physical", 30, 30, 1, 0], 
  "Smog": ["Poison", "Special", 20, 30, .7, 0], 
  "Sludge": ["Poison", "Special", 20, 65, 1, 0],
  "Bone Club": ["Ground", "Physical", 20, 65, .85, 0],
  "Fire Blast": ["Fire", "Special", 5, 110, .85, 0],
  "Waterfall": ["Water", "Physical", 15, 80, 1, 0],
  #"Clamp": ["Water", "Physical", 15, 35, .85, 0], #
  "Swift": ["Normal", "Special", 20, 60, 10, 0],
  "Skull Bash": ["Normal", "Physical", 10, 65, 1, 0], #
  "Spike Cannon": ["Normal", "Physical", 15, 60, 1, 0], 
  "Constrict": ["Normal", "Physical", 35, 10, 1, 0], #
  "Amnesia": ["Psychic", "Status", 20, 0, 10, 0, 0, 0, 0, 2, 0, 0, "None"],
  "Kinesis": ["Psychic", "Status", 15, 0, .8, 0, 0, 0, 0, 0, 0, -1, "None"],
  "Soft-Boiled": ["Normal", "Status", 10, 0, 10, .5, 0, 0, 0, 0, 0, 0, "None"],
  "High Jump Kick": ["Fighting", "Physical", 10, 130, .9, 0], 
  "Glare": ["Normal", "Status", 30, 0, 1, 0, 0, 0, 0, 0, 0, 0, "Paralyzed"], 
  #"Dream Eater": ["Psychic", "Special", 15, 100, 1, 0], #
  "Poison Gas": ["Poison", "Status", 40, 0, .9, 0, 0, 0, 0, 0, 0, 0, "Poisoned"], 
  "Barrage": ["Normal", "Physical", 20, 45, 1, 0], 
  "Leech Life": ["Bug", "Physical", 10, 80, 1, 0], 
  "Lovely Kiss": ["Normal", "Status", 10, 0, 10, 0, 0, 0, 0, 0, 0, 0, "Asleep"], 
  "Sky Attack": ["Flying", "Physical", 5, 70, .9, 0], #
  #"Transform": ["Normal", "Status", 10, 0, 10, 0, 0, 0, 0, 0, 0, 0, "None"], #
  "Bubble": ["Water", "Special", 30, 40, 1, 0],
  "Dizzy Punch": ["Normal", "Physical", 10, 70, 1, 0],
  "Spore": ["Grass", "Status", 15, 0, 1, 0, 0, 0, 0, 0, 0, 0, "Asleep"], 
  "Flash": ["Normal", "Status", 20, 0, 1, 0, 0, 0, 0, 0, 0, -1, "None"],
  #"Psywave": ["Psychic", "Special", 15, 0, 1, 0], #
  "Splash": ["Normal", "Status", 40, 0, 10, 0, 0, 0, 0, 0, 0, 0, "None"],
  "Crabhammer": ["Water", "Physical", 10, 100, .9, 0],
  "Explosion": ["Normal", "Physical", 5, 250, 1, 1], 
  "Fury Swipes": ["Normal", "Physical", 15, 54, 1, 0], 
  "Bonemerang": ["Ground", "Physical", 10, 50, .9, 0],
  #"Rest": ["Psychic", "Status", 10, 0, 10, 1, 0, 0, 0, 0, 0, 0, "None"],
  "Rock Slide": ["Rock", "Physical", 10, 75, .9, 0], #Flinch
  "Hyper Fang": ["Normal", "Physical", 15, 80, .9, 0], #Flinch
  "Sharpen": ["Normal", "Status", 30, 0, 10, 0, 1, 0, 0, 0, 0, 0, "None"],
  "Tri Attack": ["Normal", "Special", 10, 80, 1, 0],
  "Super Fang": ["Normal", "Physical", 10, 0, .9, 0],
  "Slash": ["Normal", "Physical", 20, 70, 1, 0],
  #"Substitute": ["Normal", "Status", 10, 0, 10, 0, 0, 0, 0, 0, 0, 0, "None"], #
  "Struggle": ["Normal", "Physical", 1, 50, 10, .25], #
  "Dragon Breath": ["Dragon", "Special", 20, 60, 1, 0],
  "Fire Fang": ["Fire", "Physical", 15, 65, .95, 0],
  "Scary Face": ["Normal", "Status", 10, 0, 1, 0, 0, 0, 0, 0, 2, 0, "None"],
  "Inferno": ["Fire", "Special", 5, 100, .5, 0],
  "Flare Blitz": ["Fire", "Physical", 15, 120, 1, .33], 
  "Rapid Spin": ["Normal", "Physical", 40, 50, 1, 0], #
  "Water Pulse": ["Water", "Special", 20, 60, 1, 0],
  "Aqua Tail": ["Water", "Physical", 10, 90, .9, 0],
  "Shell Smash": ["Normal", "Status", 15, 0, 10, 0, 2, -1, 2, -1, 2, 0, "None"],
  "Iron Defense": ["Steel", "Status", 15, 0, 10, 0, 0, 2, 0, 0, 0, 0, "None"],
  "Seed Bomb": ["Grass", "Physical", 15, 80, 1, 0],
  "Sweet Scent": ["Normal", "Status", 20, 0, 1, 0, 0, 2, 0, 0, 0, -1, "None"],
  "Synthesis": ["Grass", "Status", 5, 0, 10, .5, 0, 0, 0, 0, 0, 0, "None"],
  "Twister": ["Dragon", "Special", 20, 40, 1, 0],
  "Feather Dance": ["Flying", "Status", 15, 0, 1, 0, 0, 2, 0, 0, 0, 0, "None"],
  "Roost": ["Flying", "Status", 10, 0, 10, .5, 0, 0, 0, 0, 0, 0, "None"],
  "Aerial Ace": ["Flfying", "Physical", 20, 60, 10, 0],
  "Air Slash": ["Flying", "Special", 15, 75, .95, 0],
  "Hurricane": ["Flying", "Special", 10, 110, .7, 0],
  "Assurance": ["Dark", "Physical", 10, 60, 1, 0], #
  "Crunch": ["Dark", "Physical", 15, 80, 1, 0], #
  "Sucker Punch": ["Dark", "Physical", 5, 70, 1, 0], #
  #"Endeavor": ["Normal", "Physical", 5, 0, 1, 0], #
  "Bug Bite": ["Bug", "Physical", 20, 60, 1, 0],
  "Bug Buzz": ["Bug", "Special", 10, 90, 1, 0], #
  "Quiver Dance": ["Bug", "Status", 20, 0, 10, 0, 0, 0, 1, 1, 1, 0, "None"],
  "Fury Cutter": ["Bug", "Physical", 20, 40, .95, 0], #
  "Venoshock": ["Poison", "Special", 10, 65, 1, 0], #
  "Poison Jab": ["Poison", "Physical", 20, 80, 1, 0],
  "Fell Stinger": ["Bug", "Physical", 25, 50, 1, 0], #
  "Drill Run": ["Ground", "Physical", 10, 80, .95, 0], #
  "Stockpile": ["Normal", "Status", 20, 0, 10, 0, 0, 1, 0, 1, 0, 0, "None"],
  "Acid Spray": ["Poison", "Special", 20, 40, 1, 0], #
  "Sludge Bomb": ["Poison", "Special", 10, 90, 1, 0],
  "Coil": ["Poison", "Status", 20, 0, 10, 0, 1, 1, 0, 0, 0, 1, "None"],
  "Gunk Shot": ["Poison", "Physical", 10, 120, .8, 0],
  "Ice Fang": ["Ice", "Physical", 15, 65, .95, 0], #
  "Charm": ["Fairy", "Status", 20, 0, 10, 0, 0, 2, 0, 0, 0, 0, "None"],
  "Nasty Plot": ["Dark", "Status", 20, 0, 10, 0, 0, 0, 2, 0, 0, 0, "None"],
  "Nuzzle": ["Electric", "Physical", 20, 20, 1, 0], #
  "Play Nice": ["Normal", "Status", 20, 0, 10, 0, 0, 1, 0, 0, 0, 0, "None"],
  "Spark": ["Electric", "Physical", 20, 65, 1, 0],
  "Discharge": ["Electric", "Special", 15, 80, 1, 0],
  "Bulldoze": ["Ground", "Physical", 20, 60, 1, 0],
  "Flatter": ["Dark", "Status", 15, 0, 10, 0, 0, 0, 1, 0, 0, 0, "None"], #
  "Earth Power": ["Ground", "Special", 10, 90, 1, 0], #
  "Sludge Wave": ["Poison", "Special", 10, 95, 1, 0],
  "Superpower": ["Fighting", "Physical", 5, 120, 1, 0], #
  "Megahorn": ["Bug", "Physical", 10, 120, .85, 0],
  "Copycat": ["Normal", "Status", 20, 0, 10, 0, 0, 0, 0, 0, 0, 0, "None"],
  "Disarming Voice": ["Fairy", "Special", 15, 40, 10, 0],
  "Life Dew": ["Water", "Status", 10, 0, 10, .25, 0, 0, 0, 0, 0, 0, "None"],
  "Meteor Mash": ["Steel", "Physical", 10, 90, .9, 0], #
  "Cosmic Power": ["Psychic", "Status", 20, 0, 10, 0, 0, 1, 0, 1, 0, 0, "None"],
  "Moonblast": ["Fairy", "Special", 15, 95, 1, 0], #
  "Incinerate": ["Fire", "Special", 15, 60, 1, 0], 
  "Will-O-Wisp": ["Fire", "Status", 15, 0, .85, 0, 0, 0, 0, 0, 0, 0, "Burned"],
  "Extrasensory": ["Psychic", "Special", 20, 80, 1, 0], #
  "Covet": ["Normal", "Physical", 25, 60, 1, 0], #
  "Round": ["Normal", "Special", 15, 60, 1, 0], 
  "Hyper Voice": ["Normal", "Special", 10, 90, 1, 0], 
  "Play Rough": ["Fairy", "Physical", 10, 90, .9, 0], #
  "Astonish": ["Ghost", "Physical", 15, 30, 1, 0], #Flinch
  "Poison Fang": ["Poison", "Physical", 15, 50, 1, 0],
  "Air Cutter": ["Flying", "Special", 25, 60, .95, 0], #
  "Giga Drain": ["Grass", "Special", 10, 75, 1, 0], 
  "X-Scissor": ["Bug", "Physical", 15, 80, 1, 0], 
  "Mud Shot": ["Ground", "Special", 15, 55, .95, 0], #
  "Circle Throw": ["Fighting", "Physical", 10, 60, .9, 0], #
  "Dynamic Punch": ["Fighting", "Physical", 5, 100, .5, 0], #Confuse
  "Struggle Bug": ["Bug", "Special", 20, 50, 1, 0], #
  "Zen Headbutt": ["Psychic", "Physical", 15, 80, .9, 0], #Flinch
  "Mud-Slap": ["Ground", "Special", 10, 20, 1, 0], #
  #"Soak": ["Water", "Status", 20, 0, 1, 0, 0, 0, 0, 0, 0, 0, "None"],
  #"Psych Up": ["Normal", "Status", 10, 0, 10, 0, 0, 0, 0, 0, 0, 0, "None"],
  "Swagger": ["Normal", "Status", 15, 0, .85, 0, 0, 2, 0, 0, 0, 0, "None"], #Confuse
  "Close Combat": ["Fighting", "Special", 5, 120, 1, 0], #
  "Stomping Tantrum": ["Ground", "Physical", 10, 75, 1, 0], #
  "Howl": ["Normal", "Status", 40, 0, 10, 0, 0, 1, 0, 0, 0, 0, "None"],
  "Flame Wheel": ["Fire", "Physical", 25, 60, 1, 0], 
  "Psycho Cut": ["Psychic", "Physical", 20, 70, 1, 0], #Crit
  "Psyshock": ["Psychic", "Special", 10, 80, 1, 0], #
  "Calm Mind": ["Psychic", "Status", 20, 0, 10, 0, 0, 0, 1, 1, 0, 0, "None"],
  #"Revenge": ["Fighting", "Physical", 10, 60, 1, 0], #
  "Low Sweep": ["Fighting", "Physical", 20, 65, 1, 0], #
  "Knock Off": ["Dark", "Physical", 20, 65, 1, 0], #Item
  "Vital Throw": ["Fighting", "Physical", 10, 70, 10, 0], #
  "Bulk Up": ["Fighting", "Status", 20, 0, 10, 0, 1, 1, 0, 0, 0, 0, "None"],
  "Cross Chop": ["Fighting", "Physical", 5, 100, .8, 0], #Crit
  "Leaf Storm": ["Grass", "Special", 5, 130, .9, 0], #
  "Leaf Blade": ["Grass", "Physical", 15, 90, 1, 0], #Crit
  "Hex": ["Ghost", "Special", 10, 65, 1, 0], #
  "Acid Armor": ["Poison", "Status", 20, 0, 10, 0, 0, 2, 0, 0, 0, 0, "None"],
  "Rock Polish": ["Rock", "Status", 20, 0, 10, 0, 0, 0, 0, 0, 2, 0, "None"],
  "Rock Blast": ["Rock", "Physical", 10, 75, 1, 0], #
  "Stone Edge": ["Rock", "Physical", 5, 100, .8, 0], #Crit
  "Flame Charge": ["Fire", "Physical", 20, 50, 1, 0], #
  "Smart Strike": ["Steel", "Physical", 10, 70, 10, 0], 
  "Slack Off": ["Normal", "Status", 10, 0, 10, .5, 0, 0, 0, 0, 0, 0, "None"],
  "Flash Cannon": ["Steel", "Special", 10, 80, 1, 0], #
  "Metal Sound": ["Steel", "Status", 40, 0, .85, 0, 0, 0, 0, 0, 2, 0, "None"],
  "Zap Cannon": ["Electric", "Special", 5, 120, .5, 0], #
  "False Swipe": ["Normal", "Physical", 40, 40, 1, 0], #
  "Brave Bird": ["Flying", "Physical", 15, 120, 1, .33], 
  "Pluck": ["Flying", "Physical", 20, 60, 1, 0], 
  "Lunge": ["Bug", "Physical", 15, 80, 1, 0], #
  "Icy Wind": ["Ice", "Special", 15, 55, .95, 0], #
  "Ice Shard": ["Ice", "Physical", 30, 40, 1, 0], #
  "Aqua Jet": ["Water", "Physical", 20, 40, 1, 0], #
  "Brine": ["Water", "Special", 10, 65, 1, 0], #
  "Razor Shell": ["Water", "Physical", 10, 75, .95, 0], #
  "Icicle Crash": ["Ice", "Physical", 10, 85, .9, 0], #Flinch
  "Icicle Spear": ["Ice", "Physical", 30, 75, 1, 0], 
  "Payback": ["Dark", "Physical", 10, 50, 1, 0], #
  "Dark Pulse": ["Dark", "Special", 15, 80, 1, 0], #Flinch
  "Shadow Ball": ["Ghost", "Special", 15, 80, 1, 0], #
  "Iron Tail": ["Steel", "Physical", 15, 100, .75, 0], #
  "Metal Claw": ["Steel", "Physical", 35, 50, .95, 0], #
  "Hammer Arm": ["Fighting", "Physical", 10, 100, .9, 0], #
  "Eerie Impulse": ["Electric", "Status", 15, 0, 1, 0, 0, 0, 0, 2, 0, 0, "None"],
  "Charge Beam": ["Electric", "Special", 10, 50, .9, 0], #
  "Bullet Seed": ["Grass", "Physical", 30, 75, 1, 0], 
  "Wood Hammer": ["Grass", "Physical", 15, 120, 1, .33], 
  "Bone Rush": ["Ground", "Physical", 10, 75, 1, 0], 
  "Brick Break": ["Fighting", "Physical", 15, 75, 1, 0], 
  #"Endure": ["Normal", "Status", 10, 0, 10, 0, 0, 0, 0, 0, 0, 0, "None"], #
  "Blaze Kick": ["Fire", "Physical", 10, 85, .9, 0], #Crit
  "Bullet Punch": ["Steel", "Physical", 30, 40, 1, 0], #
  "Drain Punch": ["Fighting", "Physical", 10, 75, 1, 0], #
  "Vacuum Wave": ["Fighting", "Special", 30, 40, 1, 0], #
  "Mach Punch": ["Fighting", "Physical", 30, 40, 1, 0], #
  "Power-Up Punch": ["Fighting", "Physical", 20, 40, 1, 0], #
  "Power Whip": ["Grass", "Physical", 10, 120, .85, 0], #
  "Clear Smog": ["Poison", "Special", 15, 50, 10, 0], #
  "Heat Wave": ["Fire", "Special", 10, 95, .9, 0], 
  "Ancient Power": ["Rock", "Special", 5, 60, 1, 0], #
  "Tickle": ["Normal", "Status", 20, 0, 1, 0, 1, 1, 0, 0, 0, 0, "None"], 
  "Dragon Pulse": ["Dragon", "Special", 10, 85, 1, 0], 
  "Dragon Dance": ["Dragon", "Status", 20, 0, 10, 0, 1, 0, 0, 0, 1, 0, "None"], 
  "Power Gem": ["Rock", "Special", 20, 80, 1, 0], 
  "Dazzling Gleam": ["Fairy", "Special", 10, 80, 1, 0], 
  #"Teeter Dance": ["Normal", "Status", 20, 0, 1, 0, 0, 0, 0, 0, 0, 0, "None"], #Confuse
  "Powder Snow": ["Ice", "Special", 25, 40, 1, 0], 
  "Fake Tears": ["Dark", "Status", 20, 0, 1, 0, 0, 0, 2, 0, 0, 0, "None"],
  "Shock Wave": ["Electric", "Special", 20, 60, 10, 0],
  "Lava Plume": ["Fire", "Special", 15, 80, 1, 0],
  "Storm Throw": ["Fighting", "Physical", 10, 60, 1, 0], #Crit
  "Work Up": ["Normal", "Status", 30, 0, 10, 0, 1, 0, 1, 0, 0, 0, "None"],
  "Sheer Cold": ["Ice", "Special", 5, 0, .3, 0], #
  "Baby-Doll Eyes": ["Fairy", "Status", 30, 0, 1, 0, 0, 1, 0, 0, 0, 0, "None"], #
  "Muddy Water": ["Water", "Special", 10, 90, .85, 0], #
  "Thunder Fang": ["Electric", "Physical", 15, 65, .95, 0], 
  "Liquidation": ["Water", "Physical", 10, 85, 1, 0], #
  "Night Slash": ["Dark", "Physical", 15, 70, 1, 0], #Crit
  "Iron Head": ["Steel", "Physical", 15, 80, 1, 0], #Flinch
  "Snore": ["Normal", "Special", 15, 50, 1, 0], #Flinch
  "High Horsepower": ["Ground", "Physical", 10, 95, .95, 0],
  "Freeze-Dry": ["Ice", "Special", 20, 70, 1, 0],
  "Burn Up": ["Fire", "Special", 5, 130, 1, 0], #No longer fire type
  "Dragon Rush": ["Dragon", "Physical", 10, 100, .75, 0], #Flinch
  "Extreme Speed": ["Normal", "Physical", 5, 80, 1, 0], #Priority
  "Aura Sphere": ["Fighting", "Special", 20, 80, 10, 0],
  "Psystrike": ["Psychic", "Special", 10, 100, 1, 0], #
}

move_progression = {
  "Bulbasaur": ["Growl", "Tackle", "Vine Whip", "Growth", "Razor Leaf", "Poison Powder", "Sleep Powder", "Seed Bomb", "Take Down", "Sweet Scent", "Synthesis", "Double-Edge", "Solar Beam"], 
  "Ivysaur": ["Growl", "Tackle", "Vine Whip", "Growth", "Razor Leaf", "Poison Powder", "Sleep Powder", "Seed Bomb", "Take Down", "Sweet Scent", "Synthesis", "Double-Edge", "Solar Beam"],
  "Venusaur": ["Growl", "Tackle", "Vine Whip", "Growth", "Razor Leaf", "Poison Powder", "Sleep Powder", "Seed Bomb", "Take Down", "Sweet Scent", "Synthesis", "Double-Edge", "Solar Beam"], 
  "Charmander": ["Growl", "Scratch", "Ember", "Smokescreen", "Dragon Breath", "Fire Fang", "Slash", "Flamethrower", "Air Slash", "Scary Face", "Inferno", "Flare Blitz"],
  "Charmeleon": ["Growl", "Scratch", "Ember", "Smokescreen", "Dragon Breath", "Fire Fang", "Slash", "Flamethrower", "Air Slash", "Scary Face", "Inferno", "Flare Blitz"],
  "Charizard": ["Growl", "Scratch", "Ember", "Smokescreen", "Dragon Breath", "Fire Fang", "Slash", "Flamethrower", "Air Slash", "Scary Face", "Inferno", "Flare Blitz"],
  "Squirtle": ["Tackle", "Tail Whip", "Water Gun", "Withdraw", "Rapid Spin", "Bite", "Water Pulse", "Aqua Tail", "Shell Smash", "Iron Defense", "Hydro Pump", "Skull Bash"],
  "Wartortle": ["Tackle", "Tail Whip", "Water Gun", "Withdraw", "Rapid Spin", "Bite", "Water Pulse", "Aqua Tail", "Shell Smash", "Iron Defense", "Hydro Pump", "Skull Bash"],
  "Blastoise": ["Tackle", "Tail Whip", "Water Gun", "Withdraw", "Rapid Spin", "Bite", "Water Pulse", "Aqua Tail", "Shell Smash", "Iron Defense", "Hydro Pump", "Skull Bash"],
  "Caterpie": ["String Shot", "Tackle", "Bug Bite"],
  "Metapod": ["Harden"],
  "Butterfree": ["Bug Bite", "Gust", "Harden", "String Shot", "Tackle", "Confusion", "Poison Powder", "Sleep Powder", "Stun Spore", "Psybeam", "Air Slash", "Bug Buzz", "Quiver Dance"],
  "Weedle": ["Poison Sting", "String Shot", "Bug Bite"],
  "Kakuna": ["Harden"],
  "Beedrill": ["Bug Bite", "Fury Attack", "Harden", "Poison Sting", "String Shot", "Fury Cutter", "Poison Sting", "Venoshock", "Assurance", "Pin Missile", "Poison Jab", "Agility", "Fell Stinger"], 
  "Pidgey": ["Tackle", "Sand Attack", "Gust", "Quick Attack", "Twister", "Feather Dance", "Agility", "Wing Attack", "Roost", "Aerial Ace", "Air Slash", "Hurricane"], 
  "Pidgeotto": ["Tackle", "Sand Attack", "Gust", "Quick Attack", "Twister", "Feather Dance", "Agility", "Wing Attack", "Roost", "Aerial Ace", "Air Slash", "Hurricane"],
  "Pidgeot": ["Tackle", "Sand Attack", "Gust", "Quick Attack", "Twister", "Feather Dance", "Agility", "Wing Attack", "Roost", "Aerial Ace", "Air Slash", "Hurricane"],
  "Rattata": ["Tackle", "Tail Whip", "Quick Attack", "Bite", "Take Down", "Assurance", "Crunch", "Sucker Punch", "Double-Edge"], 
  "Raticate": ["Tackle", "Tail Whip", "Quick Attack", "Bite", "Take Down", "Assurance", "Crunch", "Sucker Punch", "Double-Edge"],
  "Spearow": ["Growl", "Peck", "Leer", "Assurance", "Fury Attack", "Aerial Ace", "Wing Attack", "Take Down", "Agility", "Roost", "Drill Peck"], 
  "Fearow": ["Drill Run", "Growl", "Peck", "Leer", "Assurance", "Fury Attack", "Aerial Ace", "Wing Attack", "Take Down", "Agility", "Roost", "Drill Peck", "Drill Run"], 
  "Ekans": ["Leer", "Poison Sting", "Bite", "Glare", "Screech", "Acid", "Stockpile", "Acid Spray", "Sludge Bomb", "Haze", "Coil", "Gunk Shot"], 
  "Arbok": ["Bite", "Crunch", "Fire Fang", "Ice Fang", "Leer", "Poison Sting", "Bite", "Glare", "Screech", "Acid", "Stockpile", "Acid Spray", "Sludge Bomb", "Haze", "Coil", "Gunk Shot"],
  "Pikachu": ["Charm", "Growl", "Nasty Plot", "Nuzzle", "Play Nice", "Quick Attack", "Tail Whip", "Thunder Shock", "Thunder Wave", "Double Team", "Spark", "Agility", "Slam", "Discharge", "Thunderbolt", "Thunder"], 
  "Raichu": ["Charm", "Growl", "Nasty Plot", "Nuzzle", "Play Nice", "Quick Attack", "Tail Whip", "Thunder Shock", "Thunder Wave", "Double Team", "Spark", "Agility", "Slam", "Discharge", "Thunderbolt", "Thunder"],
  "Sandshrew": ["Defense Curl", "Scratch", "Poison Sting", "Sand Attack", "Fury Cutter", "Rapid Spin", "Bulldoze", "Swift", "Fury Swipes", "Agility", "Slash", "Swords Dance", "Earthquake"], 
  "Sandslash": ["Defense Curl", "Scratch", "Poison Sting", "Sand Attack", "Fury Cutter", "Rapid Spin", "Bulldoze", "Swift", "Fury Swipes", "Agility", "Slash", "Swords Dance", "Earthquake"],
  "Nidoran Female": ["Growl", "Poison Sting", "Scratch", "Tail Whip", "Fury Swipes", "Double Kick", "Bite", "Toxic", "Flatter", "Crunch", "Earth Power"], 
  "Nidorina": ["Growl", "Poison Sting", "Scratch", "Tail Whip", "Fury Swipes", "Double Kick", "Bite", "Toxic", "Flatter", "Crunch", "Earth Power"],
  "Nidoqueen": ["Growl", "Poison Sting", "Scratch", "Tail Whip", "Fury Swipes", "Double Kick", "Bite", "Toxic", "Flatter", "Crunch", "Earth Power", "Sludge Wave", "Superpower"],
  "Nidoran Male": ["Leer", "Poison Sting", "Peck", "Fury Attack", "Double Kick", "Horn Attack", "Toxic", "Flatter", "Poison Jab", "Earth Power"], 
  "Nidorino": ["Leer", "Poison Sting", "Peck", "Fury Attack", "Double Kick", "Horn Attack", "Toxic", "Flatter", "Poison Jab", "Earth Power"],
  "Nidoking": ["Leer", "Poison Sting", "Peck", "Fury Attack", "Double Kick", "Horn Attack", "Toxic", "Flatter", "Poison Jab", "Earth Power", "Megahorn", "Sludge Wave"],
  "Clefairy": ["Charm", "Copycat", "Defense Curl", "Disarming Voice", "Growl", "Pound", "Sing", "Splash", "Minimize", "Life Dew", "Meteor Mash", "Cosmic Power", "Moonblast"], 
  "Clefable": ["Charm", "Copycat", "Defense Curl", "Disarming Voice", "Growl", "Pound", "Sing", "Splash", "Minimize", "Life Dew", "Meteor Mash", "Cosmic Power", "Moonblast"],
  "Vulpix": ["Ember", "Tail Whip", "Quick Attack", "Incinerate", "Will-O-Wisp", "Extrasensory", "Flamethrower", "Inferno", "Fire Blast"], 
  "Ninetales": ["Ember", "Tail Whip", "Quick Attack", "Incinerate", "Will-O-Wisp", "Extrasensory", "Flamethrower", "Inferno", "Fire Blast", "Nasty Plot"],
  "Jigglypuff": ["Charm", "Copycat", "Defense Curl", "Disarming Voice", "Pound", "Sing", "Covet", "Stockpile", "Round", "Body Slam", "Hyper Voice", "Play Rough", "Double-Edge"], 
  "Wigglytuff": ["Charm", "Copycat", "Defense Curl", "Disarming Voice", "Pound", "Sing", "Covet", "Stockpile", "Round", "Body Slam", "Hyper Voice", "Play Rough", "Double-Edge"],
  "Zubat": ["Absorb", "Astonish", "Poison Fang", "Air Cutter", "Bite", "Haze", "Venoshock", "Air Slash", "Leech Life"], 
  "Golbat": ["Absorb", "Astonish", "Poison Fang", "Air Cutter", "Bite", "Haze", "Venoshock", "Air Slash", "Leech Life"],
  "Oddish": ["Absorb", "Growth", "Acid", "Sweet Scent", "Mega Drain", "Poison Powder", "Stun Spore", "Sleep Powder", "Giga Drain", "Toxic", "Moonblast", "Petal Dance"], 
  "Gloom": ["Absorb", "Growth", "Acid", "Sweet Scent", "Mega Drain", "Poison Powder", "Stun Spore", "Sleep Powder", "Giga Drain", "Toxic", "Moonblast", "Petal Dance"],
  "Vileplume": ["Absorb", "Growth", "Acid", "Sweet Scent", "Mega Drain", "Poison Powder", "Stun Spore", "Sleep Powder", "Giga Drain", "Toxic", "Moonblast", "Petal Dance"], 
  "Paras": ["Scratch", "Poison Powder", "Stun Spore", "Absorb", "Fury Cutter", "Spore", "Slash", "Growth", "Giga Drain", "X-Scissor"], 
  "Parasect": ["Scratch", "Poison Powder", "Stun Spore", "Absorb", "Fury Cutter", "Spore", "Slash", "Growth", "Giga Drain", "X-Scissor"],
  "Venonat": ["Struggle Bug", "Tackle", "Confusion", "Poison Powder", "Psybeam", "Stun Spore", "Mega Drain", "Sleep Powder", "Leech Life", "Zen Headbutt", "Poison Fang", "Psychic"], 
  "Venomoth": ["Bug Buzz", "Gust", "Quiver Dance", "Struggle Bug", "Tackle", "Confusion", "Poison Powder", "Psybeam", "Stun Spore", "Mega Drain", "Sleep Powder", "Leech Life", "Zen Headbutt", "Poison Fang", "Psychic", "Bug Buzz", "Quiver Dance"],
  "Diglett": ["Sand Attack", "Scratch", "Growl", "Astonish", "Mud-Slap", "Bulldoze", "Sucker Punch", "Slash", "Earth Power", "Earthquake"], 
  "Dugtrio": ["Sand Attack", "Scratch", "Growl", "Astonish", "Mud-Slap", "Bulldoze", "Sucker Punch", "Slash", "Earth Power", "Earthquake"],
  "Meowth": ["Growl", "Scratch", "Pay Day", "Bite", "Assurance", "Fury Swipes", "Screech", "Slash", "Nasty Plot", "Play Rough"], 
  "Persian": ["Growl", "Scratch", "Pay Day", "Bite", "Assurance", "Fury Swipes", "Screech", "Slash", "Nasty Plot", "Play Rough"],
  "Psyduck": ["Scratch", "Tail Whip", "Water Gun", "Confusion", "Fury Swipes", "Water Pulse", "Zen Headbutt", "Screech", "Aqua Tail", "Amnesia", "Hydro Pump"], 
  "Golduck": ["Scratch", "Tail Whip", "Water Gun", "Confusion", "Fury Swipes", "Water Pulse", "Zen Headbutt", "Screech", "Aqua Tail", "Amnesia", "Hydro Pump"],
  "Mankey": ["Covet", "Leer", "Low Kick", "Scratch", "Fury Swipes", "Mud-Slap", "Swagger", "Cross Chop", "Assurance", "Skull Bash", "Close Combat", "Screech", "Stomping Tantrum"], 
  "Primeape": ["Covet", "Leer", "Low Kick", "Scratch", "Fury Swipes", "Mud-Slap", "Swagger", "Cross Chop", "Assurance", "Skull Bash", "Close Combat", "Screech", "Stomping Tantrum"],
  "Growlithe": ["Ember", "Leer", "Howl", "Bite", "Flame Wheel", "Agility", "Fire Fang", "Crunch", "Take Down", "Flamethrower", "Play Rough", "Flare Blitz"], 
  "Arcanine": ["Ember", "Leer", "Howl", "Bite", "Flame Wheel", "Agility", "Fire Fang", "Crunch", "Take Down", "Flamethrower", "Play Rough", "Flare Blitz"],
  "Poliwag": ["Hypnosis", "Water Gun", "Pound", "Mud Shot", "Bubble Beam", "Body Slam", "Earth Power", "Hydro Pump", "Double-Edge"], 
  "Poliwhirl": ["Hypnosis", "Water Gun", "Pound", "Mud Shot", "Bubble Beam", "Body Slam", "Earth Power", "Hydro Pump", "Double-Edge"],
  "Poliwrath": ["Hypnosis", "Water Gun", "Pound", "Mud Shot", "Bubble Beam", "Body Slam", "Earth Power", "Hydro Pump", "Double-Edge", "Circle Throw", "Dynamic Punch", "Submission"],
  "Abra": ["Teleport"],
  "Kadabra": ["Confusion", "Kinesis", "Teleport", "Psybeam", "Psycho Cut", "Recover", "Psyshock", "Psychic", "Calm Mind"], 
  "Alakazam": ["Confusion", "Kinesis", "Teleport", "Psybeam", "Psycho Cut", "Recover", "Psyshock", "Psychic", "Calm Mind"],
  "Machop": ["Leer", "Low Kick", "Low Sweep", "Knock Off", "Scary Face", "Vital Throw", "Strength", "Bulk Up", "Dynamic Punch", "Cross Chop", "Double-Edge"], 
  "Machoke": ["Leer", "Low Kick", "Low Sweep", "Knock Off", "Scary Face", "Vital Throw", "Strength", "Bulk Up", "Dynamic Punch", "Cross Chop", "Double-Edge"],
  "Machamp": ["Leer", "Low Kick", "Low Sweep", "Knock Off", "Scary Face", "Vital Throw", "Strength", "Bulk Up", "Dynamic Punch", "Cross Chop", "Double-Edge"],
  "Bellsprout": ["Vine Whip", "Growth", "Sleep Powder", "Poison Powder", "Stun Spore", "Acid", "Knock Off", "Sweet Scent", "Razor Leaf", "Poison Jab", "Slam"], 
  "Weepinbell": ["Vine Whip", "Growth", "Sleep Powder", "Poison Powder", "Stun Spore", "Acid", "Knock Off", "Sweet Scent", "Razor Leaf", "Poison Jab", "Slam"],
  "Victreebel": ["Vine Whip", "Growth", "Sleep Powder", "Poison Powder", "Stun Spore", "Acid", "Knock Off", "Sweet Scent", "Razor Leaf", "Poison Jab", "Slam", "Leaf Storm", "Leaf Blade"],
  "Tentacool": ["Poison Sting", "Water Gun", "Acid", "Water Pulse", "Screech", "Bubble Beam", "Hex", "Acid Armor", "Poison Jab", "Surf", "Sludge Wave", "Hydro Pump"], 
  "Tentacruel": ["Poison Sting", "Water Gun", "Acid", "Water Pulse", "Screech", "Bubble Beam", "Hex", "Acid Armor", "Poison Jab", "Surf", "Sludge Wave", "Hydro Pump"],
  "Geodude": ["Defense Curl", "Tackle", "Rock Polish", "Harden", "Rock Throw", "Bulldoze", "Self-Destruct", "Rock Blast", "Earthquake", "Explosion", "Double-Edge", "Stone Edge"], 
  "Graveler": ["Defense Curl", "Tackle", "Rock Polish", "Harden", "Rock Throw", "Bulldoze", "Self-Destruct", "Rock Blast", "Earthquake", "Explosion", "Double-Edge", "Stone Edge"],
  "Golem": ["Defense Curl", "Tackle", "Rock Polish", "Harden", "Rock Throw", "Bulldoze", "Self-Destruct", "Rock Blast", "Earthquake", "Explosion", "Double-Edge", "Stone Edge"],
  "Ponyta": ["Growl", "Tackle", "Tail Whip", "Ember", "Flame Charge", "Agility", "Flame Wheel", "Stomp", "Take Down", "Inferno", "Fire Blast", "Flare Blitz"], 
  "Rapidash": ["Growl", "Tackle", "Megahorn", "Poison Jab", "Quick Attack", "Smart Strike", "Tail Whip", "Ember", "Flame Charge", "Agility", "Flame Wheel", "Stomp", "Take Down", "Inferno", "Fire Blast", "Flare Blitz"], 
  "Slowpoke": ["Tackle", "Growl", "Water Gun", "Confusion", "Water Pulse", "Headbutt", "Zen Headbutt", "Amnesia", "Surf", "Slack Off", "Psychic"], 
  "Slowbro": ["Tackle", "Growl", "Water Gun", "Confusion", "Water Pulse", "Headbutt", "Zen Headbutt", "Amnesia", "Surf", "Slack Off", "Psychic"],
  "Magnemite": ["Tackle", "Thunder Shock", "Thunder Wave", "Spark", "Screech", "Flash Cannon", "Discharge", "Metal Sound", "Zap Cannon"],
  "Magneton": ["Tackle", "Thunder Shock", "Thunder Wave", "Spark", "Screech", "Flash Cannon", "Discharge", "Metal Sound", "Zap Cannon"], 
  "Farfetch'd": ["Peck", "Sand Attack", "Leer", "Fury Cutter", "Cut", "Aerial Ace", "Air Cutter", "Knock Off", "False Swipe", "Slash", "Swords Dance", "Air Slash", "Leaf Blade", "Agility", "Brave Bird"], 
  "Doduo": ["Growl", "Peck", "Quick Attack", "Leer", "Fury Attack", "Wing Attack", "Pluck", "Agility", "Swords Dance", "Lunge", "Drill Peck"], 
  "Dodrio": ["Growl", "Peck", "Quick Attack", "Leer", "Fury Attack", "Wing Attack", "Pluck", "Agility", "Swords Dance", "Lunge", "Drill Peck"],
  "Seel": ["Headbutt", "Growl", "Water Gun", "Icy Wind", "Ice Shard", "Aurora Beam", "Aqua Jet", "Brine", "Take Down", "Aqua Tail", "Ice Beam"], 
  "Dewgong": ["Headbutt", "Growl", "Water Gun", "Icy Wind", "Ice Shard", "Aurora Beam", "Aqua Jet", "Brine", "Take Down", "Aqua Tail", "Ice Beam"],
  "Grimer": ["Poison Gas", "Pound", "Harden", "Mud-Slap", "Sludge", "Smog", "Minimize", "Sludge Bomb", "Sludge Wave", "Screech", "Gunk Shot", "Acid Armor"], 
  "Muk": ["Poison Gas", "Pound", "Harden", "Mud-Slap", "Sludge", "Smog", "Minimize", "Sludge Bomb", "Sludge Wave", "Screech", "Gunk Shot", "Acid Armor"],
  "Shellder": ["Tackle", "Water Gun", "Withdraw", "Ice Shard", "Leer", "Aurora Beam", "Razor Shell", "Iron Defense", "Ice Beam", "Shell Smash", "Hydro Pump"], 
  "Cloyster": ["Tackle", "Water Gun", "Withdraw", "Ice Shard", "Leer", "Aurora Beam", "Razor Shell", "Iron Defense", "Ice Beam", "Shell Smash", "Hydro Pump", "Icicle Crash", "Icicle Spear"],
  "Gastly": ["Confuse Ray", "Lick", "Hypnosis", "Payback", "Hex", "Night Shade", "Sucker Punch", "Dark Pulse", "Shadow Ball"], 
  "Haunter": ["Confuse Ray", "Lick", "Hypnosis", "Payback", "Hex", "Night Shade", "Sucker Punch", "Dark Pulse", "Shadow Ball"],
  "Gengar": ["Confuse Ray", "Lick", "Hypnosis", "Payback", "Hex", "Night Shade", "Sucker Punch", "Dark Pulse", "Shadow Ball"],
  "Onix": ["Harden", "Rock Throw", "Tackle", "Rock Polish", "Dragon Breath", "Rock Slide", "Screech", "Slam", "Iron Tail", "Stone Edge", "Double-Edge"], 
  "Drowzee": ["Hypnosis", "Pound", "Confusion", "Headbutt", "Poison Gas", "Hypnosis", "Psybeam", "Hypnosis", "Zen Headbutt", "Swagger", "Psychic", "Nasty Plot", "Psyshock"], 
  "Hypno": ["Hypnosis", "Pound", "Confusion", "Headbutt", "Poison Gas", "Hypnosis", "Psybeam", "Hypnosis", "Zen Headbutt", "Swagger", "Psychic", "Nasty Plot", "Psyshock"],
  "Krabby": ["Leer", "Water Gun", "Harden", "Metal Claw", "Mud Shot", "Bubble Beam", "Stomp", "Razor Shell", "Slam", "Swords Dance", "Crabhammer", "Guillotine"], 
  "Kingler": ["Hammer Arm", "Leer", "Water Gun", "Harden", "Metal Claw", "Mud Shot", "Bubble Beam", "Stomp", "Razor Shell", "Slam", "Swords Dance", "Crabhammer", "Guillotine"], 
  "Voltorb": ["Charge", "Tackle", "Thunder Shock", "Eerie Impulse", "Spark", "Screech", "Charge Beam", "Swift", "Self-Destruct", "Discharge", "Explosion"], 
  "Electrode": ["Charge", "Tackle", "Thunder Shock", "Eerie Impulse", "Spark", "Screech", "Charge Beam", "Swift", "Self-Destruct", "Discharge", "Explosion"],
  "Exeggcute": ["Absorb", "Hypnosis", "Mega Drain", "Confusion", "Synthesis", "Bullet Seed", "Giga Drain", "Extrasensory", "Worry Seed", "Solar Beam"], 
  "Exeggutor": ["Absorb", "Hypnosis", "Mega Drain", "Confusion", "Synthesis", "Bullet Seed", "Giga Drain", "Extrasensory", "Worry Seed", "Solar Beam", "Psyshock", "Seed Bomb", "Wood Hammer"],
  "Cubone": ["Growl", "Mud-Slap", "Tail Whip", "False Swipe", "Headbutt", "Stomping Tantrum", "Bone Rush", "Bonemerang", "Double-Edge"], 
  "Marowak": ["Growl", "Mud-Slap", "Tail Whip", "False Swipe", "Headbutt", "Stomping Tantrum", "Bone Rush", "Bonemerang", "Double-Edge"],
  "Hitmonlee": ["Brick Break", "Low Sweep", "Tackle", "Double Kick", "Low Kick", "Blaze Kick", "Mega Kick", "Close Combat", "High Jump Kick"], 
  "Hitmonchan": ["Bullet Punch", "Drain Punch", "Tackle", "Vacuum Wave", "Mach Punch", "Power-Up Punch", "Fire Punch", "Ice Punch", "Thunder Punch", "Agility", "Mega Punch", "Close Combat"], 
  "Lickitung": ["Defense Curl", "Lick", "Stomp", "Knock Off", "Screech", "Slam", "Power Whip"], 
  "Koffing": ["Poison Gas", "Tackle", "Smog", "Smokescreen", "Clear Smog", "Assurance", "Sludge", "Haze", "Self-Destruct", "Sludge Bomb", "Toxic", "Explosion"], 
  "Weezing": ["Heat Wave", "Poison Gas", "Tackle", "Smog", "Smokescreen", "Clear Smog", "Assurance", "Sludge", "Haze", "Self-Destruct", "Sludge Bomb", "Toxic", "Explosion"], 
  "Rhyhorn": ["Tackle", "Tail Whip", "Bulldoze", "Horn Attack", "Scary Face", "Stomp", "Rock Blast", "Drill Run", "Take Down", "Earthquake", "Stone Edge", "Megahorn", "Horn Drill"], 
  "Rhydon": ["Hammer Arm", "Tackle", "Tail Whip", "Bulldoze", "Horn Attack", "Scary Face", "Stomp", "Rock Blast", "Drill Run", "Take Down", "Earthquake", "Stone Edge", "Megahorn", "Horn Drill"], 
  "Chansey": ["Charm", "Copycat", "Covet", "Defense Curl", "Disarming Voice", "Minimize", "Pound", "Tail Whip", "Life Dew", "Sing", "Take Down", "Double-Edge", "Soft-Boiled"], 
  "Tangela": ["Absorb", "Stun Spore", "Growth", "Mega Drain", "Vine Whip", "Poison Powder", "Ancient Power", "Knock Off", "Giga Drain", "Sleep Powder", "Slam", "Tickle", "Power Whip"], 
  "Kangaskhan": ["Pound", "Tail Whip", "Growl", "Bite", "Stomp", "Headbutt", "Sucker Punch", "Crunch"], 
  "Horsea": ["Leer", "Water Gun", "Smokescreen", "Twister", "Dragon Breath", "Bubble Beam", "Agility", "Dragon Pulse", "Hydro Pump", "Dragon Dance"], 
  "Seadra": ["Leer", "Water Gun", "Smokescreen", "Twister", "Dragon Breath", "Bubble Beam", "Agility", "Dragon Pulse", "Hydro Pump", "Dragon Dance"],
  "Goldeen": ["Peck", "Tail Whip", "Water Pulse", "Horn Attack", "Agility", "Waterfall", "Megahorn", "Horn Drill"], 
  "Seaking": ["Peck", "Tail Whip", "Water Pulse", "Horn Attack", "Agility", "Waterfall", "Megahorn", "Horn Drill"],
  "Staryu": ["Harden", "Tackle", "Water Gun", "Rapid Spin", "Minimize", "Swift", "Psybeam", "Brine", "Power Gem", "Psychic", "Surf", "Recover", "Cosmic Power", "Hydro Pump"], 
  "Starmie": ["Harden", "Tackle", "Water Gun", "Rapid Spin", "Minimize", "Swift", "Psybeam", "Brine", "Power Gem", "Psychic", "Surf", "Recover", "Cosmic Power", "Hydro Pump"],
  "Mr. Mime": ["Copycat", "Pound", "Confusion", "Psybeam", "Sucker Punch", "Dazzling Gleam", "Psychic", "Teeter Dance"], 
  "Scyther": ["Leer", "Quick Attack", "Fury Cutter", "False Swipe", "Wing Attack", "Double Team", "Slash", "Agility", "X-Scissor", "Swords Dance"], 
  "Jynx": ["Copycat", "Lick", "Pound", "Powder Snow", "Confusion", "Covet", "Sing", "Fake Tears", "Ice Punch", "Psychic", "Lovely Kiss", "Blizzard"], 
  "Electabuzz": ["Charge", "Leer", "Quick Attack", "Thunder Shock", "Swift", "Shock Wave", "Thunder Wave", "Screech", "Thunder Punch", "Discharge", "Low Kick", "Thunderbolt", "Thunder"], 
  "Magmar": ["Ember", "Leer", "Smog", "Smokescreen", "Clear Smog", "Flame Wheel", "Scary Face", "Fire Punch", "Lava Plume", "Low Kick", "Flamethrower", "Fire Blast"], 
  "Pinsir": ["Harden", "Vise Grip", "Bug Bite", "Storm Throw", "Vital Throw", "X-Scissor", "Strength", "Swords Dance", "Submission", "Guillotine", "Superpower"], 
  "Tauros": ["Tackle", "Tail Whip", "Work Up", "Payback", "Assurance", "Horn Attack", "Scary Face", "Zen Headbutt", "Take Down", "Swagger", "Double-Edge"], 
  "Magikarp": ["Splash", "Tackle"],
  "Gyarados": ["Bite", "Leer", "Splash", "Tackle", "Twister", "Ice Fang", "Brine", "Scary Face", "Waterfall", "Crunch", "Aqua Tail", "Dragon Dance", "Hydro Pump", "Hurricane"], 
  "Lapras": ["Growl", "Water Gun", "Sing", "Life Dew", "Ice Shard", "Water Pulse", "Brine", "Body Slam", "Ice Beam", "Hydro Pump", "Sheer Cold"], 
  "Ditto": ["Tackle"],
  "Eevee": ["Covet", "Growl", "Tackle", "Tail Whip", "Sand Attack", "Quick Attack", "Baby-Doll Eyes", "Swift", "Bite", "Copycat", "Take Down", "Charm", "Double-Edge"], 
  "Vaporeon": ["Bite", "Charm", "Copycat", "Covet", "Double-Edge", "Growl", "Swift", "Tackle", "Tail Whip", "Take Down", "Water Gun", "Sand Attack", "Quick Attack", "Baby-Doll Eyes", "Haze" "Water Pulse", "Aurora Beam", "Muddy Water", "Acid Armor", "Hydro Pump"], 
  "Jolteon": ["Bite", "Charm", "Copycat", "Covet", "Double-Edge", "Growl", "Swift", "Tackle", "Tail Whip", "Take Down", "Thunder Shock", "Sand Attack", "Quick Attack", "Baby-Doll Eyes", "Thunder Wave", "Double Kick", "Thunder Fang", "Pin Missile", "Discharge", "Agility", "Thunder"], 
  "Flareon": ["Bite", "Charm", "Copycat", "Covet", "Double-Edge", "Ember", "Growl", "Swift", "Tackle", "Tail Whip", "Take Down", "Sand Attack", "Quick Attack", "Baby-Doll Eyes", "Smog", "Bite" "Fire Fang", "Lave Plume", "Scary Face", "Flare Blitz"], 
  "Porygon": ["Tackle", "Thunder Shock", "Psybeam", "Agility", "Recover", "Discharge", "Tri Attack", "Zap Cannon"], 
  "Omanyte": ["Withdraw", "Sand Attack", "Water Gun", "Leer", "Mud Shot", "Ancient Power", "Brine", "Rock Blast", "Surf", "Shell Smash", "Hydro Pump"], 
  "Omastar": ["Crunch", "Withdraw", "Sand Attack", "Water Gun", "Leer", "Mud Shot", "Ancient Power", "Brine", "Rock Blast", "Surf", "Shell Smash", "Hydro Pump"], 
  "Kabuto": ["Absorb", "Harden", "Scratch", "Sand Attack", "Aqua Jet", "Leer", "Mud Shot", "Ancient Power", "Brine", "Leech Life", "Liquidation", "Metal Sound", "Stone Edge"], 
  "Kabutops": ["Absorb", "Night Slash", "Harden", "Scratch", "Sand Attack", "Aqua Jet", "Leer", "Mud Shot", "Ancient Power", "Brine", "Leech Life", "Liquidation", "Metal Sound", "Stone Edge"], 
  "Aerodactyl": ["Ancient Power", "Bite", "Wing Attack", "Scary Face", "Rock Slide", "Crunch", "Iron Head", "Take Down", "Stone Edge", "Agility"], 
  "Snorlax": ["Covet", "Defense Curl", "Lick", "Screech", "Stockpile", "Tackle", "Bite", "Snore", "Crunch", "Body Slam", "Amnesia", "High Horsepower", "Hammer Arm"], 
  "Articuno": ["Gust", "Powder Snow", "Ice Shard", "Agility", "Ancient Power", "Freeze-Dry", "Roost", "Ice Beam", "Hurricane", "Blizzard", "Sheer Cold"], 
  "Zapdos": ["Peck", "Thunder Wave", "Thunder Shock", "Pluck", "Agility", "Ancient Power", "Charge", "Drill Peck", "Roost", "Discharge", "Thunder", "Zap Cannon"], 
  "Moltres": ["Gust", "Leer", "Ember", "Wing Attack", "Agility", "Ancient Power", "Incinerate", "Air Slash", "Roost", "Heat Wave", "Hurricane", "Burn Up", "Sky Attack"], 
  "Dratini": ["Leer", "Twister", "Thunder Wave", "Agility", "Slam", "Aqua Tail", "Dragon Rush", "Dragon Dance"], 
  "Dragonair": ["Leer", "Twister", "Thunder Wave", "Agility", "Slam", "Aqua Tail", "Dragon Rush", "Dragon Dance"],
  "Dragonite": ["Extreme Speed", "Fire Punch", "Hurricane", "Leer", "Roost", "Thunder Punch", "Thunder Wave", "Twister", "Wing Attack", "Agility", "Slam", "Aqua Tail", "Dragon Rush", "Dragon Dance"], 
  "Mewtwo": ["Confusion", "Life Dew", "Swift", "Ancient Power", "Psycho Cut", "Amnesia", "Aura Sphere", "Psychic", "Psystrike", "Recover"], #
  "Mew": ["Pound", "Amnesia", "Ancient Power", "Life Dew", "Nasty Plot", "Aura Sphere", "Psychic"]  
}