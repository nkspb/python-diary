#!/usr/bin/env python3
import datetime, sys
from collections import OrderedDict

from peewee import *


db = SqliteDatabase('diary.db')

class Entry(Model):
  # TextField holds any amount of text, CharField has to have length
  content = TextField()
  # we leave paranthesis cause peewee will run it as function when needed
  # and we don't want our entries to have same timestamp
  timestamp = DateTimeField(default=datetime.datetime.now)
  
  class Meta:
    database = db
    

def initialize():
  '''Create database and table if they don't exist.'''
  db.connect()
  db.create_tables([Entry], safe=True)
    
def menu_loop():
  '''Show the menu'''
  # we haven't chosen anything when we run the app
  choice = None
  # show menu until user enteres q
  while choice != 'q':
    print("Enter 'q' to quit.")
    # go through menu dict
    for key, value in menu.items():
      # print menu items
      print('{}) {}'.format(key, value.__doc__))
      
    choice = input('Action: ').lower().strip()
    
    # perform selected action
    # as value is a function, we call it with ()
    if choice in menu:
      menu[choice]()
      
def add_entry():
  '''Add an entry.'''
  print("Enter your entry. Press Ctrl-D when finished.")
  #sys.stdin accepts data until EOF
  data = sys.stdin.read().strip()
  #if user entered some data, offer to save it
  if data:
    if input('Save entry? [Yn] ').lower() != 'n':
      # create a row with data
      Entry.create(content=data)
      print("Saved successfully!")
      
def view_entries():
  '''View previous entries.'''
  
def delete_entry(entry):
  '''Delete an entry.'''

menu = OrderedDict([
  ('a', add_entry),
  ('v', view_entries)    
])
  
if __name__ == '__main__':
  initialize()
  menu_loop()
