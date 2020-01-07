#!/usr/bin/python

class bcolors:
	GREEN = '\033[1;32m'
	BLUE = '\033[1;34m'
	RED = '\033[1;31m'

def twitterScrape():
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

	twitterDataTypes = {
		'username':'username',
		'name':'name',
		'imgSrc':'image',
		'location':'location',
		'biography':'biography',
		'joindate':'joindate',
		'birthdate':'birthdate'
		}

	os.system('clear')
	print statusTrue
	print ' Enter ' + bcolors.RED + '#//' + bcolors.GREEN + ' to go to the main menu.\n'
	ID = raw_input(bcolors.RED + ' Enter Twitter ID: ' + bcolors.GREEN)
	if ID == '#//':
		os.system('clear')

	else:
		os.system('clear')
		url = 'https://twitter.com/'+ID
		pageres = requests.get(url, headers=headers)
		soup = BeautifulSoup(pageres.content, 'html.parser')

		print bcolors.RED + '\n Twitter Link: ' + bcolors.BLUE + url + bcolors.GREEN

		for name in soup.find('a', class_='ProfileHeaderCard-nameLink u-textInheritColor js-nav'):
			if name != '':
				fullname = name
				print bcolors.GREEN + ' Name: ' + bcolors.GREEN + fullname
			else:
				fullname = 'Not Available'
				print bcolors.GREEN + ' Name: ' + bcolors.RED + fullname

		link = soup.select('img', class_='ProfileAvatar-image', src=True)[4]
		imgSrc = link.get('src')
		imgSrc = str(imgSrc)
		print ' ' + ID + "'s image: " + bcolors.BLUE + imgSrc

		location = soup.select('a', class_='ProfileHeaderCard-locationText u-dir')[70].get_text()
		location = str(location)
		if location != '':
			location = location
			print bcolors.GREEN + ' Location: ' + location
		else:
			location = 'Not Available'
			print bcolors.GREEN + ' Location: ' + bcolors.RED + location  + bcolors.GREEN

		for biography in soup.find('p', class_='ProfileHeaderCard-bio u-dir'):
			if biography == '':
				biography =  bcolors.RED + 'Empty' + bcolors.GREEN
				print ' Biography Section: ' + biography
			else:
				print ' Biography Section: ' + biography

		for joinDate in soup.find('span', class_='ProfileHeaderCard-joinDateText js-tooltip u-dir'):
			print ' Joindate: ' + joinDate

		for birthdate in soup.find('span', class_='ProfileHeaderCard-birthdateText u-dir'):
			bday = birthdate.replace('\n', '')	
			if bday == '':
				bday = bcolors.RED + 'Not available'  + bcolors.GREEN
				print ' Birth Date: ' + bday
			else:
				print ' Birth Date: ' + dbay


		for mediaCount in soup.find('a', class_='PhotoRail-headingWithCount js-nav'):
			print ' Media Count: ' + mediaCount.replace('\n                \n                ', '').replace('            ', '').replace('\n', '').replace('\n                \n                ', '')

		for tweetCount in soup.find('span', class_='ProfileNav-value'):
			print ' Total Tweets: ' + tweetCount.replace('\n            ', '')

		following = soup.find(class_='ProfileNav-item ProfileNav-item--following').get_text()
		print following.replace('\n\nFollowing\n', '').replace('Following\n', ' Following ').replace('\n\n', '')

		followers = soup.find(class_='ProfileNav-item ProfileNav-item--followers').get_text()
		print followers.replace('\n\nFollowers\n', '').replace('Followers\n', ' Followers ').replace('\n\n', '')

		try:
			cursor.execute("INSERT INTO TwitterUsers (USERNAME, NAME, USERIMAGE, LOCATION, BIOGRAPHY, JOINDATE, BIRTHDAY, MEDIACOUNT, TWEETCOUNT, FOLLOWING, FOLLOWERS) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID, fullname, imgSrc, location, biography, joinDate, bday, mediaCount, tweetCount, following, followers))
			conn.commit()
			print bcolors.RED + '\n ' + ID + bcolors.GREEN + ' was added to the DB successfully.\n'
		
		except sqlite3.IntegrityError as iError:
			print bcolors.RED + '\n Error: {}\n'.format(iError) + bcolors.GREEN +' This username already exists. Output was not written to DB.\n Use the ' + bcolors.RED + 'search user ' + bcolors.GREEN + 'command to search for '+bcolors.RED+ID+bcolors.GREEN+' in the DB.\n'
