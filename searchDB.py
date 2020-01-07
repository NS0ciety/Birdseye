#!/usr/bin/python

class bcolors:
	GREEN = '\033[1;32m'
	BLUE = '\033[1;34m'
	RED = '\033[1;31m'

def dbsearch():
	import sqlite3
	from sqlite3 import Error
	import sys, os, time

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
	print ' Enter ' + bcolors.RED + '#//' + bcolors.GREEN + ' to go to the main menu\n'

	print bcolors.BLUE + ' Tables' + bcolors.GREEN + ' to search:\n'
	print '   Facebook		-	' + bcolors.RED + '	facebook'
	print bcolors.GREEN + '   Twitter		-	' + bcolors.RED + '	twitter\n'

	choice = raw_input(' Choose table: ' + bcolors.GREEN + '')

	if choice == '#//':
		os.system('clear')				

	elif choice == 'facebook':
		facebooksearch = raw_input(bcolors.RED + ' Enter Facebook ID to search in DB: ' + bcolors.GREEN + '')
		cursor.execute("SELECT * FROM FacebookUsers WHERE USERNAME = ?", (facebooksearch,))
		data = cursor.fetchone()

		try:
			if facebooksearch == data[0]:
				x = '\n'
				IDtag = '\n Facebook ID: ' + bcolors.RED + data[0] + bcolors.GREEN
				name = '\n Name: ' + data[1]
				contactinfo = '\n Contact Infomation: ' + data[2]
				location = '\n Location: ' + data[3]
				aboutuser = '\n About ' + bcolors.GREEN + ': ' + data[4]
				skills = '\n Professional Skills: ' + data[5]
				education = '\n Education: ' + data[6]
				friends = '\n Friends Count: ' + data[7]
				photocount = '\n Photo Count: ' + data[8]
				photo1 = '\n Photo links: ' + bcolors.BLUE + data[9] + bcolors.GREEN
				photo2 = '\n Photo links: ' + bcolors.BLUE + data[10] + bcolors.GREEN
				photo3 = '\n Photo links: ' + bcolors.BLUE + data[11] + bcolors.GREEN + x

				print IDtag, name, contactinfo, location, aboutuser, skills, education, friends, photocount, photo1, photo2, photo3

		except TypeError as tError:
			os.system('clear')
			print ' ' + bcolors.RED + facebooksearch + bcolors.GREEN + ' does not exist in the DB.\n'						

	elif choice == 'twitter':
		twittersearch = raw_input(bcolors.RED + ' Enter Twitter ID to search in DB: ' + bcolors.GREEN + '')			
		cursor.execute("SELECT * FROM TwitterUsers WHERE USERNAME = ?", (twittersearch,))
		data = cursor.fetchone()

		try:
			if twittersearch == data[0]:
				uname = '\n Username: ' + data[0]
				fname = '\n Name: ' + data[1]
				img = '\n Image Src: ' + bcolors.BLUE + data[2] + bcolors.GREEN
				loc = '\n Location: ' + data[3].replace('\n            Photos and videos\n          ', ' ' + bcolors.RED + 'Not available.')
				bio = '\n Biography Section: ' + data[4]
				joined = '\n Join Date: ' + data[5]
				birthday = '\n Birth Date: ' + data[6]
				mediaC = '\n Media Count: ' + data[7].replace('\n                \n                ', '').replace('            ', '').replace('\n', '')
				tweetC = '\n Tweet Count: ' + data[8].replace('\n            ', '')
				follow = '\n ' + data[9].replace('\n\nFollowing\n', '').replace('Following\n', 'Following: ').replace('\n\n', '')
				follower = '\n ' + data[10].replace('\n\nFollowers\n', '').replace('Followers\n', 'Followers: ').replace('\n\n', '')
				print uname + fname + img + loc + bio + joined + birthday + mediaC + tweetC + follow + follower + '\n'

		except TypeError as tError:
			os.system('clear')
			print ' ' + bcolors.RED + twittersearch + bcolors.GREEN + ' does not exist in the DB.\n'

	else:
		os.system('clear')
		print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.' + bcolors.GREEN

