#!/usr/bin/env python3

from peewee import *
import datetime

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
  
def add_entry():
  '''Add an entry.'''
  
def view_entries():
  '''View previous entries.'''
  
def delete_entry(entry):
  '''Delete an entry.'''
  
if __name__ == '__main__':
  initialize()
  menu_loop()