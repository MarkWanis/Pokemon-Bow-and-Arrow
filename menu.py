# Our modules
from replit import db
from tkinter import *
import yaml
import time
import sys
import os
from base_stats import *
from colors import *


with open(r'Data/list_of_usernames.yaml') as file:
  list_of_usernames = yaml.full_load(file)["List of Usernames"]

username = os.environ["REPL_OWNER"]

if username in list_of_usernames:
  print("\nWelcome back " + username + "!")
  while True:
    user_choice = input("Would you like to continue on you current journey or start a new journey? ")

    if "continue" in user_choice or "current" in user_choice:
      with open(r'Data/' + username + '.yaml') as file:
        data = yaml.full_load(file)
        
      break

    elif "start" in user_choice or "new" in user_choice:
      with open(r'Data/blank.yaml') as file: #This sets data equal to the blank file
        data = yaml.full_load(file) 

      with open('Data/' + username + '.yaml', 'w') as file: #This sets the user's file equal to the blank file, clearing the data
        yaml.dump(data, file)

      break

    else:
      print("\nThat is not a valid choice. Try the key words 'continue', 'current', 'start', or 'new.'")

else:
  list_of_usernames.append(username) #This adds the new username to the list and stores it into the yaml file
  with open('Data/list_of_usernames.yaml', 'w') as file:
    yaml.dump({"List of Usernames": list_of_usernames}, file)
  
  with open(r'Data/blank.yaml') as file: #This sets data equal to the blank file
    data = yaml.full_load(file) 
    
  with open('Data/' + username + '.yaml', 'w') as file: #This sets the user's file equal to the blank file
    yaml.dump(data, file)


for key_element in [*data]:
  db[key_element] = data[key_element]

db["User Name"] = username