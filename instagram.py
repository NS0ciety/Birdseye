#!/usr/bin/python

class bcolors:
	GREEN = '\033[1;32m'
	BLUE = '\033[1;34m'
	RED = '\033[1;31m'

def instagramScrape():
	import sqlite3
	from sqlite3 import Error
	import requests
	from bs4 import BeautifulSoup
	import sys, os, time

	headers = {'Accept-Language': 'en-US,en;q=0.5'}

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

	os.system('clear')
	print statusTrue
	print ' Enter ' + bcolors.RED + '#//' + bcolors.GREEN + ' to go to the main menu.\n'
	ID = raw_input(' Enter Instagram ID: ')
	if ID == '#//':
		os.system('clear')		
		

	elif ID != '' or ' ':
		os.system('clear')
		url = 'https://instagram.com/'+ID
		pageres = requests.get(url, headers=headers)
		soup = BeautifulSoup(pageres.content, 'html.parser')
		x = '\n'

		print statusTrue
		print bcolors.RED + '\n Instagram Link: ' + bcolors.BLUE + url + bcolors.GREEN
		print bcolors.RED + ' Instagram ID: ' + bcolors.GREEN + ID + bcolors.GREEN

		for name in soup.find_all('a', class_='_2nlw _2nlv'):
			name = name.get_text()
			print ' Name: ' + name
			
		for contactinfo in soup.find_all('span', class_='_50f8 _2iem'):
			contactinfo = contactinfo.get_text()
			print ' Contact Information: ' + contactinfo

		for location in soup.find_all('span', class_='_2iel _50f7'):
			location = location.get_text()
			print ' Current City: ' + location

			try:
				cursor.execute("INSERT INTO InstagramUsers (USERNAME, NAME, CONTACTINFO, LOCATION, ABOUTUSER, SKILLS, EDUCATION, FRIENDS, PHOTOCOUNT, PHOTO1, PHOTO2, PHOTO3) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID, name, contactinfo, location, aboutuser, skills, education, friends, photocount, photo1, photo2, photo3))
				conn.commit()
				print bcolors.RED + ' ' + name + bcolors.GREEN + ' was added to the DB successfully.\n'
				

			except sqlite3.IntegrityError as iError:
				print bcolors.RED + ' ' + ID + bcolors.GREEN + ' Already exists in DB.\n'
				

		else:
			os.system('clear')
			print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.' + bcolors.GREEN

