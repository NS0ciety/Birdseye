#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error
import requests
from bs4 import BeautifulSoup
import sys, os, time

sys.dont_write_bytecode = True

os.system('clear')

class bcolors:
	GREEN = '\033[1;32m'
	BLUE = '\033[1;34m'
	RED = '\033[1;31m'

headers = {'Accept-Language': 'en-US,en;q=1'}

db = './db/test.db'
conn = sqlite3.connect(db)
cursor = conn.cursor()

status = True
while (status == True):
	statusTrue = bcolors.BLUE + ' DB Connection Status: ' + bcolors.GREEN + 'Connected\n'
	break

else:
	statusFalse = bcolors.BLUE + ' DB Connection Status: ' + bcolors.RED + 'Disconnected\n'
	print statusFalses

try:
	cursor.execute('''CREATE TABLE IF NOT EXISTS FacebookUsers(
				USERNAME 	TEXT	PRIMARY KEY,
				NAME		TEXT,
				CONTACTINFO	TEXT,
				LOCATION	TEXT,
				ABOUTUSER	TEXT,
				SKILLS		DATE,
				EDUCATION	TEXT,
				FRIENDS		TEXT,
				PHOTOCOUNT	TEXT,
				PHOTO1		TEXT,
				PHOTO2		TEXT,
				PHOTO3		TEXT)
								''')

	conn.commit()
	print bcolors.GREEN + ' Loading ' + bcolors.BLUE + 'Database Tables' + bcolors.GREEN + '...\n'
	time.sleep(1)
	print bcolors.BLUE + '   Facebook' + bcolors.GREEN + ' user table was successfully loaded.'

except sqlite3.Error as Error:
	print ' DB Facebook table load failed: {}'.format(Error)

try:
	cursor.execute('''CREATE TABLE IF NOT EXISTS TwitterUsers(
				USERNAME 	TEXT	PRIMARY KEY,
				NAME		TEXT,
				USERIMAGE	TEXT,
				LOCATION	TEXT,
				BIOGRAPHY	TEXT,
				JOINDATE	DATE,
				BIRTHDAY	TEXT,
				MEDIACOUNT	TEXT,
				TWEETCOUNT	TEXT,
				FOLLOWING	TEXT,
				FOLLOWERS	TEXT)
								''')

	conn.commit()
	print bcolors.BLUE + '   Twitter' + bcolors.GREEN + ' user table was successfully loaded.'
	time.sleep(1)

except sqlite3.Error as Error:
        print ' Twitter table load failed: {}'.format(Error)

try:
	cursor.execute('''CREATE TABLE IF NOT EXISTS InstagramUsers(
				USERNAME 	TEXT	PRIMARY KEY,
				NAME		TEXT,
				CONTACTINFO	TEXT,
				LOCATION	TEXT,
				ABOUTUSER	TEXT,
				SKILLS		DATE,
				EDUCATION	TEXT,
				FRIENDS		TEXT,
				PHOTOCOUNT	TEXT,
				PHOTO1		TEXT,
				PHOTO2		TEXT,
				PHOTO3		TEXT)
										''')

	conn.commit()
	time.sleep(1)
 	print bcolors.BLUE + '   Instagram ' + bcolors.GREEN + 'user table was successfully loaded.\n'

except sqlite3.Error as Error:
	print ' DB Instagram table load failed: {}'.format(Error)
	birdseye()

def birdseye():
	import twitter
	from twitter import twitterScrape
	import facebook
	from facebook import facebookScrape
	import instagram
	from instagram import instagramScrape

	import searchDB
	from searchDB import dbsearch
	import dbModifier
	from dbModifier import dbModify

	commands = {
		'facebook':'facebook',
		'twitter':'twitter',
		'instagram':'instagram',
		'search':'search user',
		'modifydb':'db edit',
		'optionList':'show options',
		'exit':'exit'
		}

	banner = '''

			'''

	print statusTrue
	print ' Use command ' + bcolors.RED + 'show options'+ bcolors.GREEN + ' for help.\n'
	cmd = raw_input(bcolors.RED + ' Root: '  + bcolors.GREEN)

	if cmd in commands['facebook']:
		facebookScrape()

	elif cmd in commands['twitter']:
		twitterScrape()

	elif cmd in commands['instagram']:
#		instagramScrape()
		os.system('clear')
		print bcolors.RED + ' [!]' + bcolors.GREEN + 'FEATURE COMING SOON'  + bcolors.RED + '[!]\n'  
		birdseye()

	elif cmd in commands['search']:
		dbsearch()

	elif cmd in commands['modifydb']:
		dbModify()

	elif cmd in commands['optionList']:
		os.system('clear')
		print statusTrue
		print bcolors.BLUE + ' Commands:\n'
		facebook = bcolors.GREEN + '      Gather info from Facebook Account		-	' + bcolors.RED + commands['facebook']
		twitter = bcolors.GREEN + '      Gather info from Twitter Account		-	' + bcolors.RED + commands['twitter']
		instagram = bcolors.GREEN + '      Gather info from Instagram Account	-	' + bcolors.RED + commands['instagram']
		search = bcolors.GREEN + '      Search DB for a user			-	' + bcolors.RED + commands['search']
		editDB = bcolors.GREEN + '      Edit a DB record				-	' + bcolors.RED + commands['modifydb']
		exit = bcolors.GREEN + '      Exit					-	' + bcolors.RED + commands['exit']
		x = '\n'

		print bcolors.BLUE + '   Scraping:' + bcolors.GREEN
		print x, facebook, x, twitter, x, instagram, x
		print bcolors.BLUE + '   Database:' + bcolors.GREEN
		print x, search, x, editDB, x, exit, x

	elif cmd in commands['exit']:
		print bcolors.RED + ' Disconnecting from DB...'
		time.sleep(2)
		conn.close()
		os.system('clear')
		print bcolors.GREEN + ' DB has disconnected.'
		print bcolors.RED + ' Exiting...'
		time.sleep(2)
		os.system('clear')
		filelist = [ f for f in os.listdir('/root/rebuild/') if f.endswith(".pyc") ]
		for f in filelist:
			os.remove(os.path.join('root/rebuild/', f))
			sys.exit()
	else:
		os.system('clear')
		print bcolors.RED + '	Invalid Syntax.\n'
	birdseye()
birdseye()
