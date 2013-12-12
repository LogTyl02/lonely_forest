#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import random



a = 'You are standing at the base of a gentle hill.'
b = 'To the north, the Lonely forest yawns.'
c = 'Your home is to the west.'

message_buffer = [a, b, c]
def print_message():
	for line in message_buffer:
		print line






#cabin_coords = (cabin_y, cabin_x)

#start = forest[start_y][start_x]


class Room(object):
	def __init__(self, y, x, glyph, mush=None):
		self.y = y
		self.x = x
		self.mush = mush
		self.glyph = glyph

		forest[self.y][self.x] = self.glyph

class Minotaur(object):
	def __init__(self, y, x):
		self.y = y
		self.x = x
		self.glyph = '&'

		forest[self.y][self.x] = self.glyph

	def wander(self):
		self.rng = random.randint(0, 100)
		forest[self.y][self.x] = '.'
		if 0 <= self.rng <= 25:
			print 'Moving West'
			self.x = self.x - 1
		elif 26 <= self.rng <= 50:
			print 'Moving North'
			self.y = self.y -1
		elif 51 <= self.rng <= 75:
			print 'Moving East'
			self.x = self.x + 1
		elif 76 <= self.rng <= 100:
			print 'Moving South'
			self.y = self.y + 1

		forest[self.y][self.x] = self.glyph

class Item(object):
	def __init__(self, name, value):
		self.name = name
		self.value = value

	def get_name(self):
		return self.name

	def get_value(self):
		return self.value

class Player(object):
	def __init__(self, y, x):
		self.y = y
		self.x = x
		self.glyph = '@'
		self.fear = 'LOW'
		self.inventory = [Item('A bottle of whiskey', 0)]

	def show_inv(self):
		self.gubbins = ['Crushed hopes', 'Some lint', 'A paper clip', 'A wooden tooth', 'Charcoal dust']
		print "Your trusty satchel contains:\n"
		for item in self.inventory:
			print item.name
		print random.choice(self.gubbins)

	def search(self):
		print "You have a look around, but find nothing."

	def move(self, direction):
		if direction == 'north':
			player.y = player.y - 1
		elif direction == 'south':
			player.y = player.y + 1
		elif direction == 'west':
			player.x = player.x - 1
		elif direction == 'east':
			player.x = player.x + 1

class Game(object):
	def __init__(self):
		os.system('cls')
		print "Welcome to the Lonely Forest.\nBeware the Minotaur.\n\nPress Any Key To Begin..."
		#begin = raw_input()	# Replace with getch functionality
		self.plant_minotaur()
		self.display_menu()

	def display_menu(self):
		os.system('cls')
		print_message()
		print '============================================'
		print '(N)orth		(S)outh'
		print '(E)ast		(W)est'

	def plant_minotaur(self):
		self.howard = Minotaur(3, 3)

	def tick(self):
		self.howard.wander()
		for line in forest:
			print line

player = Player(4, 7)

class Map(object):
	def __init__(self, length=None, width=None):
		self.length = length
		self.width = width
		self.seed = open('lvl1.txt', 'r')
		self.grid = [[char for char in line.strip()] for line in self.seed]

		# Assign the character's glyph to its spot on the map
		self.grid[player.y][player.x] = player.glyph

	def show_map(self):
		for line in self.grid:
			print line

	def update_actors(self):
		self.grid[player.y][player.x] = player.glyph

lonely_forest = Map()

def tick():
	lonely_forest.update_actors()
	lonely_forest.show_map()

tick()
player.move('north')
tick()





