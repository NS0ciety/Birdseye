#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error
import requests
from bs4 import BeautifulSoup
import sys, os, time

os.system('clear')

class bcolors:
	GREEN = '\033[1;32m'
	BLUE = '\033[1;34m'
	RED = '\033[1;31m'

db = './db/birdseye.db'
headers = {'Accept-Language': 'en-US,en;q=0.5'}

banner = '''

		'''

commands = {
	'twitter':'twitter start',
	'search':'search user',
	'modifydb':'db edit',
	'optionList':'show options',
	'exit':'exit'
	}

dbHandler = {
	'updateUser':'update user',
#	'addCol':'add column',
	'delUser':'del user',
	'resetDB':'reset db',
	'#//':'#//'
	}
dataTypes = {
	'username':'username',
	'name':'name',
	'imgSrc':'image',
	'location':'location',
	'biography':'biography',
	'joindate':'joindate',
	'birthdate':'birthdate',
	}

try:
	conn = sqlite3.connect(db)
	cursor = conn.cursor()

	status = True
	while (status == True):
		statusTrue = bcolors.BLUE + ' DB Connection Status: ' + bcolors.GREEN + 'Connected\n'
		break
	else:
		statusFalse = bcolors.BLUE + ' DB Connection Status: ' + bcolors.RED + 'Disconnected\n'
		print statusFalse

except sqlite3.ConnectionError as cError:
	print 'Error: {} /' + bcolors.GREEN + 'Failed to connect to DB.'.format(cError) 

def createDB():
	try:
		cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
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
 
	except sqlite3.Error as Error:
	        print ' DB Connection Failed: {}'.format(Error)

def main_():
	print statusTrue
	print ' Use command ' + bcolors.RED + 'show options'+ bcolors.GREEN + ' for help.\n'
	cmd = raw_input(' Root: ')

	if cmd in commands['twitter']:

		os.system('clear')
		print statusTrue
		print ' Enter ' + bcolors.RED + '#//' + bcolors.GREEN + ' to go to the main menu.\n'
		ID = raw_input(' Enter Twitter ID: ')
		if ID == '#//':
			os.system('clear')		
			main_()

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
			if location == '':
				location = 'Not Available'
				print bcolors.GREEN + ' Location: ' + bcolors.RED + location  + bcolors.GREEN
			else:
				print bcolors.GREEN + ' Location: ' + location

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
				cursor.execute("INSERT INTO Users (USERNAME, NAME, USERIMAGE, LOCATION, BIOGRAPHY, JOINDATE, BIRTHDAY, MEDIACOUNT, TWEETCOUNT, FOLLOWING, FOLLOWERS) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID, fullname, imgSrc, location, biography, joinDate, bday, mediaCount, tweetCount, following, followers))
				conn.commit()
				print bcolors.RED + '\n ' + ID + bcolors.GREEN + ' was added to the DB successfully.\n'
				main_()
			except sqlite3.IntegrityError as iError:
				print bcolors.RED + '\n Error: {}\n'.format(iError) + bcolors.GREEN +' This username already exists. Output was not written to DB.\n Use the ' + bcolors.RED + 'search user ' + bcolors.GREEN + 'command to search for '+bcolors.RED+ID+bcolors.GREEN+' in the DB.\n'
				main_()

	elif cmd in commands['search']:
		os.system('clear')
		print statusTrue
		print ' Enter ' + bcolors.RED + '#//' + bcolors.GREEN + ' to go to the main menu\n'

		search = raw_input(' Enter username to search in DB: ')

		if search == '#//':
			os.system('clear')
			main_()

		else:
			os.system('clear')
			
			cursor.execute("SELECT * FROM Users WHERE USERNAME = ?", (search,))
 
			data = cursor.fetchone()

			for search in data[0]:
				uname = '\n Username: ' + data[0]
				fname = '\n Name: ' + data[1]
				img = '\n Image Src: ' + data[2]
				loc = '\n Location: ' + data[3]
				bio = '\n Biography Section: ' + data[4]
				joined = '\n Join Date: ' + data[5]
				birthday = '\n Birth Date: ' + data[6]
				mediaC = '\n Media Count: ' + data[7].replace('\n                \n                ', '').replace('            ', '').replace('\n', '')
				tweetC = '\n Tweet Count: ' + data[8].replace('\n            ', '')
				follow = '\n ' + data[9].replace('\n\nFollowing\n', '').replace('Following\n', 'Following: ').replace('\n\n', '')
				follower = '\n ' + data[10].replace('\n\nFollowers\n', '').replace('Followers\n', 'Followers: ').replace('\n\n', '')
				print uname + fname + img + loc + bio + joined + birthday + mediaC + tweetC + follow + follower + '\n'
				main_()


	elif cmd in commands['modifydb']:
		os.system('clear')
		print statusTrue

		updateRecord = bcolors.GREEN + '   Update existing user record			-	' + bcolors.RED + dbHandler['updateUser']
		#addRecordCol = bcolors.GREEN + '   Add new column to existing user record	-	' + bcolors.RED + dbHandler['addCol']
		delRecord = bcolors.GREEN + '   Delete a user record				-	' + bcolors.RED + dbHandler['delUser']
		resetDB = bcolors.GREEN + '   Reset DB					-	' + bcolors.RED + dbHandler['resetDB']
		exit = bcolors.GREEN + '   Exit	to main menu				-	' + bcolors.RED + dbHandler['#//']
		x = '\n'

		print x, updateRecord, x, delRecord, x, resetDB, x, exit, x + bcolors.GREEN # addRecordCol, x,

		dbEdit = raw_input(bcolors.RED + ' dbEditor#> ' + bcolors.GREEN)
		
		if dbEdit == dbHandler['updateUser']:
			os.system('clear')
			print statusTrue
			print bcolors.BLUE + ' Data types:\n'
			username = bcolors.GREEN + '   Username			-		' + bcolors.RED + dataTypes['username']
			name = bcolors.GREEN + '   Name				-		' + bcolors.RED + dataTypes['name']
			image = bcolors.GREEN + '   Image			-		' + bcolors.RED + dataTypes['imgSrc']
			location = bcolors.GREEN + '   Location			-		' + bcolors.RED + dataTypes['location']
			biography = bcolors.GREEN + '   Biography Section		-		' + bcolors.RED + dataTypes['biography']
			joindate = bcolors.GREEN + '   Join Date			-		' + bcolors.RED + dataTypes['joindate']	
			birthday = bcolors.GREEN + '   Birth Date			-		' + bcolors.RED + dataTypes['birthdate']
			x = '\n'

			print x, username, x, name, x, image, x , location, x, biography, x, joindate, x, birthday, x


			dataType = raw_input(' Choose data to modify: ' + bcolors.GREEN)
			unameToMod = raw_input(bcolors.RED + ' Enter username of user to modify: ' + bcolors.GREEN)

			print ' Checking if ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
			time.sleep(3)

 			uname = cursor.execute("SELECT * FROM Users WHERE USERNAME = ?", (unameToMod,))
			data = cursor.fetchone()
		
			if dataType == dataTypes['username']:
				for uname in data[0]:
					print ' Username: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
					newUname = raw_input(' Enter new username: ')
					cursor.execute("UPDATE Users SET USERNAME = ? WHERE USERNAME = ?", (newUname, unameToMod))
					conn.commit()
					os.system('clear')
					print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " username to " + bcolors.BLUE + newUname + "\n"
					main_()
				else:
					print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " username is still " + bcolors.RED + unameToMod + "\n"
					main_()

			elif dataType in dataTypes['name']:
				for uname in data[0]:
					nameToMod = data[1]
					print ' Name: ' + bcolors.RED + nameToMod + bcolors.GREEN + ' exists in DB.'
					newName = raw_input(' Enter new name: ')
					cursor.execute("UPDATE Users SET NAME = ? WHERE NAME = ?", (newName, nameToMod))
					conn.commit()
					os.system('clear')
					print " Successfully updated " + bcolors.RED + nameToMod + "'s" + bcolors.GREEN + " name to " + bcolors.BLUE + newName + "\n"
					main_()
				else:
					print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " name is still " + bcolors.BLUE + unameToMod + "\n"

			elif dataType in dataTypes['imgSrc']:
				for uname in data[0]:
					imgToMod = data[2]
					print ' Image Src: ' + bcolors.BLUE + imgToMod + bcolors.GREEN + ' for ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
					print bcolors.RED + ' NOTE: ' + bcolors.GREEN + 'Providing an invalid link will result in a broken image.'
					newSrc = raw_input(' Enter new image link: ')
					cursor.execute("UPDATE Users SET USERIMAGE = ? WHERE USERIMAGE = ?", (newSrc, imgToMod))
					conn.commit()
					os.system('clear')
					print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " image src to " + bcolors.BLUE + newSrc + "\n"
					main_()
				else:
					print bcolors.GREEN + " Failed to update " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " link. Image src is still " + bcolors.BLUE + imgToMod + "\n"

			elif dataType in dataTypes['location']:
				for uname in data[0]:
					locationToMod = data[3]
					print bcolors.GREEN + " Location: " + bcolors.RED + locationToMod + bcolors.GREEN + " exists in DB."
					newLocation = raw_input(' Enter new location: ')
					cursor.execute("UPDATE Users SET LOCATION = ? WHERE LOCATION = ?", (newLocation, locationToMod))
					conn.commit()
					os.system('clear')
					print " Successfully updated " + bcolors.RED + unameToMod + "'s " + bcolors.GREEN + "Location from " + bcolors.RED + locationToMod + bcolors.GREEN + " to " + bcolors.BLUE + newLocation + "\n"
					main_()
				else:
					print " Failed to update " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " location. Location is still " + bcolors.BLUE + locationToMod + "\n"

			elif dataType in dataTypes['biography']:
				for uname in data[0]:
					bioToMod = data[4]
					print ' Biography Section: ' + bcolors.RED + bioToMod + bcolors.GREEN + ' exists in DB.'

					newBio = raw_input(' Enter new biography section: ')
					cursor.execute("UPDATE Users SET BIOGRAPHY = ? WHERE BIOGRAPHY = ?", (newBio, bioToMod))
					conn.commit()
					os.system('clear')
					print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " biography section from " + bcolors.RED + bioToMod + bcolors.GREEN + " to " + bcolors.BLUE + newBio + "\n"
					main_()
				else:
					print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " biography section. Bio is still " + bcolors.BLUE + bioToMod + "\n"

			elif dataType in dataTypes['joindate']:
				for uname in data[0]:
					joindateToMod = data[5]
					print ' Join Date: ' + bcolors.RED + joindateToMod + bcolors.GREEN + ' exists in DB.'
					newJoindate = raw_input(' Enter new join date: ')
					cursor.execute("UPDATE Users SET JOINDATE = ? WHERE JOINDATE = ?", (newJoindate, joindateToMod))
					conn.commit()
					os.system('clear')
					print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " joindate from " + bcolors.RED + joindateToMod + bcolors.GREEN + " to " + bcolors.BLUE + newJoindate + "\n"
					main_()
				else:
					print " Failed to update " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " join date. Join date is still " + bcolors.BLUE + joindateToMod + "\n"

			elif dataType in dataTypes['birthdate']:
				for uname in data[0]:
					bdayToMod = data[6]
					print ' Birth Date: ' + bcolors.RED + bdayToMod + bcolors.GREEN + ' exists in DB.'
					newBday = raw_input(' Enter new birth date: ')
					cursor.execute("UPDATE Users SET BIRTHDAY = ? WHERE BIRTHDAY = ?", (newBday, bdayToMod))
					conn.commit()
					os.system('clear')
					print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " birth date from " + bdayToMod + bcolors.GREEN + " to " + bcolors.BLUE + newBday + "\n"
					main_()
				else:
					print " Failed to update " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " birth date. Birth date is still " + bcolors.BLUE + joindateToMod + "\n"

			else:
				os.system('clear')
				print bcolors.RED + ' Invalid DataType: Exiting to main menu.' + bcolors.GREEN
				main_()

#		elif dbEdit == dbHandler['addCol']:
#			os.system('clear')
#			newCol = raw_input(' Enter new column name: ')
#			os.system('clear')		
#			if newCol != '':
#				cursor.execute("ALTER TABLE Users ADD COLUMN '"+newCol+"' 'TEXT'")
#				conn.commit()
				
#				print ' Success: new column ' + bcolors.RED + newCol + bcolors.GREEN + ' was added to DB table ' + bcolors.RED + 'Users \n' + bcolors.GREEN
#				main_()
#			else:
#				os.system('clear')
#				print bcolors.RED + ' Invalid Column Name. Exiting to main menu.\n' + bcolors.GREEN
#				main_()

		elif dbEdit == dbHandler['delUser']:
			os.system('clear')
			print statusTrue
			userToDel = raw_input(' Enter username of record to delete: ')

			print ' Checking if ' + bcolors.RED + userToDel + bcolors.GREEN + ' exists in DB.'
			time.sleep(3)

 			uname = cursor.execute("SELECT * FROM Users WHERE USERNAME = ?", (userToDel,))
			data = cursor.fetchone()

			for uname in data[0]:
				print ' Username: ' + bcolors.RED + userToDel + bcolors.GREEN + ' exists in DB.'
				confirmDel = raw_input(' Confirm deletion [y/n]: ')
				if confirmDel == 'y' or 'Y':
					cursor.execute("DELETE FROM Users WHERE USERNAME = ?", (userToDel,))
					conn.commit() 
					delCheck = cursor.execute("SELECT * FROM Users WHERE USERNAME = ?", (userToDel,))
					os.system('clear')
					print bcolors.RED + ' ' + userToDel + bcolors.GREEN + ' was deleted from the DB.\n'
					main_()

				elif confirmDel == 'n' or 'N':
					os.system('clear')
					print bcolors.RED + userToDel + bcolors.GREEN + ' was not be deleted from DB.\n'
					main_()

				else:
					print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.'
			else:
				os.system('clear')
				print bcolors.RED + userToDel + bcolors.GREEN + ' does not exist in the DB.\n'
				main_()

		elif dbEdit == dbHandler['resetDB']:
			os.system('clear')
			print statusTrue

			delConfirmation = raw_input(' Are you sure you want to reset DB [y/n]: ')
			if delConfirmation == 'y' or 'Y':
				print bcolors.RED + ' Resetting DB.\n'
				cursor.execute("DROP TABLE IF EXISTS Users")
				time.sleep(2)
				os.system('clear')
				print bcolors.GREEN + ' Database has been reset.\n'
				main_()

			elif delConfirmation == 'n' or 'N':
				print bcolors.RED + ' Exiting to the main menu.'
				time.sleep(2)
				os.system('clear')
				main_()
			else:
				print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.'

		elif dbEdit == dbHandler['#//']:
			os.system('clear')
			main_()
		else:
			print bcolors.RED + ' Invalid Syntax. Exiting to main menu.'
			main_()

	elif cmd in commands['optionList']:
		os.system('clear')
		print bcolors.BLUE + ' Commands:'
		twitter = bcolors.GREEN + '   Gather info from Twitter Account	-	' + bcolors.RED + commands['twitter']
		search = bcolors.GREEN + '   Search DB for a user			-	' + bcolors.RED + commands['search']
		editDB = bcolors.GREEN + '   Edit a DB record			-	' + bcolors.RED + commands['modifydb']
		exit = bcolors.GREEN + '   Exit					-	' + bcolors.RED + commands['exit']
		x = '\n'

		print x, twitter, x, search, x, editDB, x, exit, x
		main_()

	elif cmd in commands['exit']:
		print bcolors.RED + ' Disconnecting from DB...'
		time.sleep(2)
		conn.close()
		os.system('clear')
		print bcolors.GREEN + ' DB has disconnected.'
		print bcolors.RED + ' Exiting...'
		time.sleep(2)
		os.system('clear')
		sys.exit()
	else:
		os.system('clear')
		print bcolors.RED + '	Invalid Syntax.\n'
		main_()

createDB()
main_()
