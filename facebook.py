#!/usr/bin/python

class bcolors:
	GREEN = '\033[1;32m'
	BLUE = '\033[1;34m'
	RED = '\033[1;31m'

def facebookScrape():
	import sqlite3
	from sqlite3 import Error
	import requests
	from bs4 import BeautifulSoup
	import sys, os, time

	facebookDataTypes = {
		'id':'id',
		'name':'name',
		'contactinfo':'contact',
		'location':'location',
		'aboutuser':'about user',
		'skills':'skills',
		'education':'education',
		'friends':'friends',
		'photocount':'photo count',
		'photo1':'photo 1',
		'photo2':'photo 2',
		'photo3':'photo 3'
		}

	ID = ''
	name = ''
	contactinfo = ''
	location = ''
	aboutuser = ''
	skills = ''
	education = ''
	friendcount = ''
	photocount = ''
	photo1 = ''
	photo2 = ''
	photo3 = ''

	savelikes = ''
	likes = ''
	otherlikes = ''

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
	print bcolors.RED + ' Facebook' + bcolors.GREEN +' uses security techniques to block scraping attempts.\n Use a tool such as' + bcolors.GREEN + ' Torghost' + bcolors.GREEN + ' to change your IP frequently.\n\n' + bcolors.BLUE + ' Torghost' + bcolors.GREEN + ' can be found at...\n\n ' + bcolors.BLUE + '	https://github.com/SusmithKrishnan/torghost\n\n' + bcolors.RED + ' Alternatively,' + bcolors.GREEN + ' if you have a web browser open, restart it.\n'

	ID = raw_input(bcolors.RED + ' Enter facebook ID: ' + bcolors.GREEN)
	if ID == '#//':
		os.system('clear')			

	elif ID != '':
		os.system('clear')
		url = 'https://facebook.com/'+ID
		pageres = requests.get(url, headers=headers)
		soup = BeautifulSoup(pageres.content, 'html.parser')
		x = '\n'
		friends = bcolors.RED + ' Private' + bcolors.GREEN

		print statusTrue
		print bcolors.RED + ' Facebook Link: ' + bcolors.BLUE + url + bcolors.GREEN
		print bcolors.RED + ' Facebook ID: ' + bcolors.GREEN + ID + bcolors.GREEN

		for names in soup.find_all('a', class_='_2nlw _2nlv'):
			name = names.get_text()
			print ' Name: ' + name

		for contactinfo in soup.find_all('span', class_='_50f8 _2iem'):
			contactinfo = contactinfo.get_text()
			print ' Contact Information: ' + contactinfo

		for location in soup.find_all('span', class_='_2iel _50f7'):
			location = location.get_text()
			print ' Location: ' + location

		for aboutuser in soup.find_all('span', class_='_c24 _2iem'):
			aboutuser = aboutuser.get_text()
			print ' About ' + bcolors.RED + name + bcolors.GREEN + ': ' + x + x + aboutuser + x

		for skills in soup.find_all('a', class_='_3l7z _39g6'):
			skills = skills.get_text()
			print ' Professional Skills: ' + skills

		for education in soup.find_all('div', class_='_2lzr _50f5 _50f7'):
			education = education.get_text()
			print ' Education: ' + education

		for friendcount in soup.find_all('span', class_='_4sl-'):
			friendcount = friendcount.get_text()
			print ' Friends: ' + friendcount

		for likes in soup.find_all('div', class_='mediaPageName'):
			likes = likes.get_text()
			print bcolors.RED + ' Likes: ' + bcolors.GREEN + likes

		for otherlikes in soup.find_all('div', class_='uiCollapsedList uiCollapsedListHidden uiCollapsedListNoSeparate pagesListData'):
			otherlikes = otherlikes.get_text()
			print bcolors.RED + ' Other Likes: \n   ' + bcolors.GREEN + '-' + otherlikes.replace(', ', '\n   -').replace('and more', '')

		for photocount in soup.find_all('div', class_='_2a2q _1m6c'):
			photocount = photocount.get_text()
			print ' Photo Count: ' + photocount

		for photolink1 in soup.find_all('img', class_='scaledImageFitHeight img', src=True):
			photo1 = photolink1.get('src')
			print ' Photo link: ' + bcolors.BLUE + photo1 + bcolors.GREEN

		for photolink2 in soup.find_all('img', class_='_46-i img', src=True):
			photo2 = photolink2.get('src')
			print ' Photo link: ' + bcolors.BLUE + photo2 + bcolors.GREEN

		for photolink3 in soup.find_all('img', class_='scaledImageFitWidth img', src=True):
			photo3 = photolink3.get('src')
			print ' Photo link: ' + bcolors.BLUE + photo3 + bcolors.GREEN + x

		try:
			cursor.execute("INSERT INTO FacebookUsers (USERNAME, NAME, CONTACTINFO, LOCATION, ABOUTUSER, SKILLS, EDUCATION, FRIENDS, PHOTOCOUNT, PHOTO1, PHOTO2, PHOTO3) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID, name, contactinfo, location, aboutuser, skills, education, friendcount, photocount, photo1, photo2, photo3,))
			conn.commit()
			print bcolors.RED + ' ' + name + bcolors.GREEN + ' was added to the DB successfully.\n'

		except sqlite3.IntegrityError as Ierror:
			print ' ' + bcolors.RED + name + bcolors.GREEN + ' already exists in the DB.\n'

		savelikes = raw_input(' Would you like to save ' + bcolors.RED + 'Likes & Other Likes ' + bcolors.GREEN + '[y/n]: ')
		if savelikes == 'n':
			os.system('clear')
			print bcolors.RED + ' Likes & Other Likes ' + bcolors.GREEN + 'were not saved.\n' + bcolors.RED + ' Exiting to the main menu.\n'
				
		elif savelikes == 'y':
			try:
				cursor.execute("ALTER TABLE FacebookUsers ADD COLUMN 'LIKES' 'TEXT'")
				cursor.execute("ALTER TABLE FacebookUsers ADD COLUMN 'OTHERLIKES' 'TEXT'")
				conn.commit()

				cursor.execute("UPDATE FacebookUsers SET LIKES = ? WHERE USERNAME = ?", (likes, ID,))
				conn.commit()
				print ' Writing ' + bcolors.RED + 'Likes...' + bcolors.GREEN + ' to the DB.'
				time.sleep(2)
				cursor.execute("UPDATE FacebookUsers SET OTHERLIKES = ? WHERE USERNAME = ?", (otherlikes, ID,))
				conn.commit()
				print ' Writing ' + bcolors.RED + 'Other Likes...' + bcolors.GREEN + ' to the DB.'
				time.sleep(2)
	
				os.system('clear')
				print bcolors.RED + ' Likes & Other Likes ' + bcolors.GREEN + 'were successfully saved.\n' + bcolors.RED + ' Exiting to the main menu.\n'

			except sqlite3.OperationalError as eError:
				os.system('clear')

		else:
			os.system('clear')
			print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.\n ' + bcolors.RED + 'Likes & Other Likes ' + bcolors.GREEN + 'were not saved.\n'


	else:
		os.system('clear')
		print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.' + bcolors.GREEN

