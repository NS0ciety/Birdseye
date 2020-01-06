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
	'facebook':'facebook start',
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

twitterDataTypes = {
	'username':'username',
	'name':'name',
	'imgSrc':'image',
	'location':'location',
	'biography':'biography',
	'joindate':'joindate',
	'birthdate':'birthdate'
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
				cursor.execute("INSERT INTO TwitterUsers (USERNAME, NAME, USERIMAGE, LOCATION, BIOGRAPHY, JOINDATE, BIRTHDAY, MEDIACOUNT, TWEETCOUNT, FOLLOWING, FOLLOWERS) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID, fullname, imgSrc, location, biography, joinDate, bday, mediaCount, tweetCount, following, followers))
				conn.commit()
				print bcolors.RED + '\n ' + ID + bcolors.GREEN + ' was added to the DB successfully.\n'
				main_()
			except sqlite3.IntegrityError as iError:
				print bcolors.RED + '\n Error: {}\n'.format(iError) + bcolors.GREEN +' This username already exists. Output was not written to DB.\n Use the ' + bcolors.RED + 'search user ' + bcolors.GREEN + 'command to search for '+bcolors.RED+ID+bcolors.GREEN+' in the DB.\n'
				main_()

	elif cmd in commands['facebook']:

		os.system('clear')
		print statusTrue
		print ' Enter ' + bcolors.RED + '#//' + bcolors.GREEN + ' to go to the main menu.\n'
		ID = raw_input(' Enter facebook ID: ')
		if ID == '#//':
			os.system('clear')		
			main_()

		elif ID != '' or ' ':
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
 
			except sqlite3.Error as Error:
			        print ' DB Connection Failed: {}'.format(Error)


			os.system('clear')
			url = 'https://facebook.com/'+ID
			pageres = requests.get(url, headers=headers)
			soup = BeautifulSoup(pageres.content, 'html.parser')
			x = '\n'

			print statusTrue
			print bcolors.RED + '\n Facebook Link: ' + bcolors.BLUE + url + bcolors.GREEN
			print bcolors.RED + ' Facebook ID: ' + bcolors.GREEN + ID + bcolors.GREEN

			for name in soup.find_all('a', class_='_2nlw _2nlv'):
				name = name.get_text()
				print ' Name: ' + name
			
			for contactinfo in soup.find_all('span', class_='_50f8 _2iem'):
				contactinfo = contactinfo.get_text()
				print ' Contact Information: ' + contactinfo

			for location in soup.find_all('span', class_='_2iel _50f7'):
				location = location.get_text()
				print ' Current City: ' + location

			for aboutuser in soup.find_all('span', class_='_c24 _2iem'):
				aboutuser = aboutuser.get_text()
				print ' About ' + bcolors.RED + name + bcolors.GREEN + ': ' + x + x + aboutuser + x

			for skills in soup.find_all('a', class_='_3l7z _39g6'):
				skills = skills.get_text()
				print ' Professional Skills: ' + skills

			for education in soup.find_all('div', class_='_2lzr _50f5 _50f7'):
				education = education.get_text()
				print ' Education: ' + education

			for friends in soup.find_all('span', class_='_4sl-'):
				friends = friends.get_text()
				print ' Friends: ' + friends
			else:
				friends = 'Private'
				print ' Friends ' + bcolors.RED + 'private.' + bcolors.GREEN 

			for likes in soup.find_all('div', class_='mediaPageName'):
				likes = likes.get_text()
				print bcolors.RED + ' Likes: ' + bcolors.GREEN + likes

			for otherlikes in soup.find_all('div', class_='uiCollapsedList uiCollapsedListHidden uiCollapsedListNoSeparate pagesListData'):
				otherlikes = otherlikes.get_text()
				print bcolors.RED + ' Other Likes: \n   ' + bcolors.GREEN + '-' + otherlikes.replace(', ', '\n   -').replace('and more', '')

			for photocount in soup.find_all('div', class_='_2a2q _1m6c'):
				photocount = photocount.get_text()
				print ' Photo Count: ' + photocount

			for photo1 in soup.find_all('img', class_='scaledImageFitHeight img', src=True):
				photo1 = photo1.get('src')
				print ' Photo links: ' + bcolors.BLUE + photo1 + bcolors.GREEN

			for photo2 in soup.find_all('img', class_='_46-i img', src=True):
				photo2 = photo2.get('src')
				print ' Photo links: ' + bcolors.BLUE + photo2 + bcolors.GREEN

			for photo3 in soup.find_all('img', class_='scaledImageFitWidth img', src=True):
				photo3 = photo3.get('src')
				print ' Photo links: ' + bcolors.BLUE + photo3 + bcolors.GREEN + x

			try:
				cursor.execute("INSERT INTO FacebookUsers (USERNAME, NAME, CONTACTINFO, LOCATION, ABOUTUSER, SKILLS, EDUCATION, FRIENDS, PHOTOCOUNT, PHOTO1, PHOTO2, PHOTO3) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ID, name, contactinfo, location, aboutuser, skills, education, friends, photocount, photo1, photo2, photo3))
				conn.commit()
				print bcolors.RED + ' ' + name + bcolors.GREEN + ' was added to the DB successfully.\n'
				savelikes = raw_input(' Would you like to save ' + bcolors.RED + 'Likes & Other Likes ' + bcolors.GREEN + '[y/n]: ')

				if savelikes == 'n':
					os.system('clear')
					print bcolors.RED + ' Likes & Other Likes ' + bcolors.GREEN + 'were not saved.\n' + bcolors.RED + ' Exiting to the main menu.\n'
					main_()

				elif savelikes == 'y':
					cursor.execute("ALTER TABLE FacebookUsers ADD COLUMN 'Likes' 'TEXT'")
					cursor.execute("ALTER TABLE FacebookUsers ADD COLUMN 'Other Likes' 'TEXT'")
					conn.commit()

					cursor.execute("UPDATE FacebookUsers SET LIKES = ? WHERE USERNAME = ?", (likes, ID,))
					print ' Writing ' + bcolors.RED + 'Likes...' + bcolors.GREEN + ' to the DB.'
					time.sleep(2)
					cursor.execute("UPDATE FacebookUsers SET LIKES = ? WHERE USERNAME = ?", (likes, ID,))
					print ' Writing ' + bcolors.RED + 'Other Likes...' + bcolors.GREEN + ' to the DB.'
					time.sleep(2)

					os.system('clear')
					print bcolors.RED + ' Likes & Other Likes ' + bcolors.GREEN + 'were successfully saved.\n' + bcolors.RED + ' Exiting to the main menu.\n'
					main_()

				else:
					os.system('clear')
					print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.\n ' + bcolors.RED + 'Likes & Other Likes ' + bcolors.GREEN + 'were not saved.\n'
					main_()

			except sqlite3.IntegrityError as iError:
					print bcolors.RED + ' ' + ID + bcolors.GREEN + ' Already exists in DB.\n'
					main_()








		else:
			os.system('clear')
			print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.' + bcolors.GREEN
			main_()			


	elif cmd in commands['search']:
		os.system('clear')
		print statusTrue
		print ' Enter ' + bcolors.RED + '#//' + bcolors.GREEN + ' to go to the main menu\n'

		print bcolors.BLUE + ' Tables' + bcolors.GREEN + ' to search:\n'
		print 'Facebook		-	' + bcolors.RED + '	facebook'
		print bcolors.GREEN + 'Twitter			-	' + bcolors.RED + '	twitter\n'

		choice = raw_input(' Choose table: ' + bcolors.GREEN + '')
		search = raw_input(bcolors.RED + ' Enter username to search in DB: ' + bcolors.GREEN + '')

		if choice == '#//':
			os.system('clear')
			main_()

		elif choice == 'facebook':
			os.system('clear')
			
			cursor.execute("SELECT * FROM FacebookUsers WHERE USERNAME = ?", (search,))
 
			data = cursor.fetchone()

			for search in data[0]:
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
				main_()

		elif choice == 'twitter':
			os.system('clear')
			
			cursor.execute("SELECT * FROM TwitterUsers WHERE USERNAME = ?", (search,))
 
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
		else:
			os.system('clear')
			print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.' + bcolors.GREEN
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

			print bcolors.BLUE + ' Tables' + bcolors.GREEN + ' to search:\n'
			print 'Facebook		-	' + bcolors.RED + '	facebook'
			print bcolors.GREEN + 'Twitter			-	' + bcolors.RED + '	twitter\n'

			choice = raw_input(bcolors.RED + ' Choose Site Record to update: ' + bcolors.GREEN)
			unameToMod = raw_input(bcolors.RED + ' Enter username of user to modify: ' + bcolors.GREEN)

			if choice == 'facebook':
				os.system('clear')
				print statusTrue
				print bcolors.BLUE + ' Data types:\n'
				ID = bcolors.GREEN + '   ID				-		' + bcolors.RED + facebookDataTypes['id']
				name = bcolors.GREEN + '   Name				-		' + bcolors.RED + facebookDataTypes['name']
				contactinfo = bcolors.GREEN + '   Contact Information		-		' + bcolors.RED + facebookDataTypes['contactinfo']
				location = bcolors.GREEN + '   Location			-		' + bcolors.RED + facebookDataTypes['location']
				aboutuser = bcolors.GREEN + '   About user			-		' + bcolors.RED + facebookDataTypes['aboutuser']
				skills = bcolors.GREEN + '   Professional Skills		-		' + bcolors.RED + facebookDataTypes['skills']
				education = bcolors.GREEN + '   Education		-		' + bcolors.RED + facebookDataTypes['education']	
				friends = bcolors.GREEN + '   Friends			-		' + bcolors.RED + facebookDataTypes['friends']
				photocount = bcolors.GREEN + '   Photo Count			-		' + bcolors.RED + facebookDataTypes['photocount']
				photo1 = bcolors.GREEN + '   Photo Link 1			-		' + bcolors.RED + facebookDataTypes['photo1']
				photo2 = bcolors.GREEN + '   Photo Link 2			-		' + bcolors.RED + facebookDataTypes['photo2']
				photo3 = bcolors.GREEN + '   Photo Link 3			-		' + bcolors.RED + facebookDataTypes['photo3']
				x = '\n'

				print x, ID, x, name, x, contactinfo, x , location, x, aboutuser, x, skills, x, education, x, friends, x, photocount, x, photo1, x, photo2, x, photo3, x

				dataType = raw_input(' Choose data to modify: ' + bcolors.GREEN)
				print ' Checking if ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
				time.sleep(3)

 				uname = cursor.execute("SELECT * FROM FacebookUsers WHERE USERNAME = ?", (unameToMod,))
				data = cursor.fetchone()
		
				if dataType == facebookDataTypes['id']:
					for uname in data[0]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newUname = raw_input(' Enter new ID: ')
						cursor.execute("UPDATE FacebookUsers SET USERNAME = ? WHERE USERNAME = ?", (newUname, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " ID to " + bcolors.BLUE + newUname + "\n"
						main_()
					else:
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " ID.\n"
						main_()

				elif dataType == facebookDataTypes['name']:
					for uname in data[1]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newName = raw_input(' Enter new name: ')
						cursor.execute("UPDATE FacebookUsers SET NAME = ? WHERE USERNAME = ?", (newName, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " name to " + bcolors.BLUE + newName + "\n"
						main_()
					else:
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " name.\n"
						main_()

				elif dataType == facebookDataTypes['contactinfo']:
					for uname in data[2]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newContact = raw_input(' Enter new contact information: ')
						cursor.execute("UPDATE FacebookUsers SET CONTACTINFO = ? WHERE USERNAME = ?", (newContact, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " Contact Information to " + bcolors.BLUE + newContact + "\n"
						main_()
					else:
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " Contact Information.\n"
						main_()

				elif dataType == facebookDataTypes['location']:
					for uname in data[3]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newLocation = raw_input(' Enter new location: ')
						cursor.execute("UPDATE FacebookUsers SET LOCATION = ? WHERE USERNAME = ?", (newLocation, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " location to " + bcolors.BLUE + newLocation + "\n"
						main_()
					else:
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " location.\n"
						main_()

				elif dataType == facebookDataTypes['aboutuser']:
					for uname in data[4]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newAbout = raw_input(' Enter new about user: ')
						cursor.execute("UPDATE FacebookUsers SET ABOUTUSER = ? WHERE USERNAME = ?", (newAbout, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " about to " + bcolors.BLUE + newAbout + "\n"
						main_()
					else:
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " about.\n"
						main_()

				elif dataType == facebookDataTypes['skills']:
					for uname in data[5]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newSkills = raw_input(' Enter new skills: ')
						cursor.execute("UPDATE FacebookUsers SET SKILLS = ? WHERE USERNAME = ?", (newSkills, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " professional skills to " + bcolors.BLUE + newSkills + "\n"
						main_()
					else:
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " professional skills.\n"
						main_()

				elif dataType == facebookDataTypes['education']:
					for uname in data[6]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newEducation = raw_input(' Enter new education: ')
						cursor.execute("UPDATE FacebookUsers SET EDUCATION = ? WHERE USERNAME = ?", (newEducation, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " education to " + bcolors.BLUE + newEducation + "\n"
						main_()
					else:
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " education.\n"
						main_()

				elif dataType == facebookDataTypes['friends']:
					for uname in data[7]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newFriends = raw_input(' Enter new friend count: ')
						cursor.execute("UPDATE FacebookUsers SET FRIENDS = ? WHERE USERNAME = ?", (newFriends, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " friends count to " + bcolors.BLUE + newFriends + "\n"
						main_()
					else:
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " friends count.\n"
						main_()

				elif dataType == facebookDataTypes['photocount']:
					for uname in data[8]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newPhotoC = raw_input(' Enter new photo count: ')
						cursor.execute("UPDATE FacebookUsers SET PHOTOCOUNT = ? WHERE USERNAME = ?", (newPhotoC, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " photo count to " + bcolors.BLUE + newPhotoC + "\n"
						main_()
					else:
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " photo count.\n"
						main_()

				elif dataType == facebookDataTypes['photo1']:
					for uname in data[9]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newPhoto1 = raw_input(' Enter new photo 1 link: ')
						cursor.execute("UPDATE FacebookUsers SET PHOTO1 = ? WHERE USERNAME = ?", (newPhoto1, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " photo 1 link to " + bcolors.BLUE + newPhoto1 + "\n"
						main_()
					else:
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " photo 1 link.\n"
						main_()

				elif dataType == facebookDataTypes['photo2']:
					for uname in data[10]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newPhoto2 = raw_input(' Enter new photo 2 link: ')
						cursor.execute("UPDATE FacebookUsers SET PHOTO2 = ? WHERE USERNAME = ?", (newPhoto2, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " photo 2 link to " + bcolors.BLUE + newPhoto2 + "\n"
						main_()
					else:
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " photo 2 link.\n"
						main_()

				elif dataType == facebookDataTypes['photo3']:
					for uname in data[11]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newPhoto3 = raw_input(' Enter new photo 3 link: ')
						cursor.execute("UPDATE FacebookUsers SET PHOTO3 = ? WHERE USERNAME = ?", (newPhoto3, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " photo 3 link to " + bcolors.BLUE + newPhoto3 + "\n"
						main_()
					else:
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " photo 3 link.\n"
						main_()

				else:
					os.system('clear')
					print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.' + bcolors.GREEN
					main_()

			elif choice == 'twitter':
				os.system('clear')
				print statusTrue
				print bcolors.BLUE + ' Data types:\n'
				username = bcolors.GREEN + '   Username			-		' + bcolors.RED + twitterDataTypes['username']
				name = bcolors.GREEN + '   Name				-		' + bcolors.RED + twitterDataTypes['name']
				image = bcolors.GREEN + '   Image			-		' + bcolors.RED + twitterDataTypes['imgSrc']
				location = bcolors.GREEN + '   Location			-		' + bcolors.RED + twitterDataTypes['location']
				biography = bcolors.GREEN + '   Biography Section		-		' + bcolors.RED + twitterDataTypes['biography']
				joindate = bcolors.GREEN + '   Join Date			-		' + bcolors.RED + twitterDataTypes['joindate']	
				birthday = bcolors.GREEN + '   Birth Date			-		' + bcolors.RED + twitterDataTypes['birthdate']
				x = '\n'

				print x, username, x, name, x, image, x , location, x, biography, x, joindate, x, birthday, x

				dataType = raw_input(' Choose data to modify: ' + bcolors.GREEN)
				print ' Checking if ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
				time.sleep(3)

 				uname = cursor.execute("SELECT * FROM TwitterUsers WHERE USERNAME = ?", (unameToMod,))
				data = cursor.fetchone()
		
				if dataType == twitterDataTypes['username']:
					for uname in data[0]:
						print ' Username: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newUname = raw_input(' Enter new username: ')
						cursor.execute("UPDATE TwitterUsers SET USERNAME = ? WHERE USERNAME = ?", (newUname, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " username to " + bcolors.BLUE + newUname + "\n"
						main_()
					else:
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " username is still " + bcolors.RED + unameToMod + "\n"
						main_()

				elif dataType in twitterDataTypes['name']:
					for uname in data[0]:
						nameToMod = data[1]
						print ' Name: ' + bcolors.RED + nameToMod + bcolors.GREEN + ' exists in DB.'
						newName = raw_input(' Enter new name: ')
						cursor.execute("UPDATE TwitterUsers SET NAME = ? WHERE NAME = ?", (newName, nameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + nameToMod + "'s" + bcolors.GREEN + " name to " + bcolors.BLUE + newName + "\n"
						main_()
					else:
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " name is still " + bcolors.BLUE + unameToMod + "\n"

				elif dataType in twitterDataTypes['imgSrc']:
					for uname in data[0]:
						imgToMod = data[2]
						print ' Image Src: ' + bcolors.BLUE + imgToMod + bcolors.GREEN + ' for ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						print bcolors.RED + ' NOTE: ' + bcolors.GREEN + 'Providing an invalid link will result in a broken image.'
						newSrc = raw_input(' Enter new image link: ')
						cursor.execute("UPDATE TwitterUsers SET USERIMAGE = ? WHERE USERIMAGE = ?", (newSrc, imgToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " image src to " + bcolors.BLUE + newSrc + "\n"
						main_()
					else:
						print bcolors.GREEN + " Failed to update " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " link. Image src is still " + bcolors.BLUE + imgToMod + "\n"

				elif dataType in twitterDataTypes['location']:
					for uname in data[0]:
						locationToMod = data[3]
						print bcolors.GREEN + " Location: " + bcolors.RED + locationToMod + bcolors.GREEN + " exists in DB."
						newLocation = raw_input(' Enter new location: ')
						cursor.execute("UPDATE TwitterUsers SET LOCATION = ? WHERE LOCATION = ?", (newLocation, locationToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s " + bcolors.GREEN + "Location from " + bcolors.RED + locationToMod + bcolors.GREEN + " to " + bcolors.BLUE + newLocation + "\n"
						main_()
					else:
						print " Failed to update " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " location. Location is still " + bcolors.BLUE + locationToMod + "\n"

				elif dataType in twitterDataTypes['biography']:
					for uname in data[0]:
						bioToMod = data[4]
						print ' Biography Section: ' + bcolors.RED + bioToMod + bcolors.GREEN + ' exists in DB.'

						newBio = raw_input(' Enter new biography section: ')
						cursor.execute("UPDATE TwitterUsers SET BIOGRAPHY = ? WHERE BIOGRAPHY = ?", (newBio, bioToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " biography section from " + bcolors.RED + bioToMod + bcolors.GREEN + " to " + bcolors.BLUE + newBio + "\n"
						main_()
					else:
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " biography section. Bio is still " + bcolors.BLUE + bioToMod + "\n"

				elif dataType in twitterDataTypes['joindate']:
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

				elif dataType in twitterDataTypes['birthdate']:
					for uname in data[0]:
						bdayToMod = data[6]
						print ' Birth Date: ' + bcolors.RED + bdayToMod + bcolors.GREEN + ' exists in DB.'
						newBday = raw_input(' Enter new birth date: ')
						cursor.execute("UPDATE TwitterUsers SET BIRTHDAY = ? WHERE BIRTHDAY = ?", (newBday, bdayToMod))
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

			else:
				os.system('clear')
				print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.\n' + bcolors.GREEN 
				main_()

#		elif dbEdit == dbHandler['addCol']:
#			os.system('clear')
#			newCol = raw_input(' Enter new column name: ')
#			os.system('clear')		
#			if newCol != '':
#				cursor.execute("ALTER TABLE TwitterUsers ADD COLUMN '"+newCol+"' 'TEXT'")
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
			print bcolors.BLUE + ' Sites:\n'
			print bcolors.GREEN + '   Facebook		-		' + bcolors.RED + 'facebook'
			print bcolors.GREEN + '   Twitter		-		' + bcolors.RED + 'twitter'

			choice = raw_input(bcolors.RED + ' Choose from site to delete user: ' + bcolors.GREEN)
			userToDel = raw_input(bcolors.RED + ' Enter username of record to delete: ' + bcolors.GREEN)

			if choice == 'facebook':
				os.system('clear')
				print ' Checking if ' + bcolors.RED + userToDel + bcolors.GREEN + ' exists in DB.'
				time.sleep(3)

	 			uname = cursor.execute("SELECT * FROM FacebookUsers WHERE USERNAME = ?", (userToDel,))
				data = cursor.fetchone()

				for uname in data[0]:
					print ' Username: ' + bcolors.RED + userToDel + bcolors.GREEN + ' exists in DB.\m' + bcolors.RED
					confirmDel = raw_input(' Confirm deletion [y/n]: ' + bcolors.GREEN)
					if confirmDel == 'y' or 'Y':
						cursor.execute("DELETE FROM FacebookUsers WHERE USERNAME = ?", (userToDel,))
						conn.commit() 
						delCheck = cursor.execute("SELECT * FROM FacebookUsers WHERE USERNAME = ?", (userToDel,))
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

			elif choice == 'twitter':
				os.system('clear')
				print ' Checking if ' + bcolors.RED + userToDel + bcolors.GREEN + ' exists in DB.'
				time.sleep(3)

	 			uname = cursor.execute("SELECT * FROM TwitterUsers WHERE USERNAME = ?", (userToDel,))
				data = cursor.fetchone()

				for uname in data[0]:
					print ' Username: ' + bcolors.RED + userToDel + bcolors.GREEN + ' exists in DB.\n' + bcolors.RED
					confirmDel = raw_input(' Confirm deletion [y/n]: ' + bcolors.GREEN)
					if confirmDel == 'y' or 'Y':
						cursor.execute("DELETE FROM TwitterUsers WHERE USERNAME = ?", (userToDel,))
						conn.commit() 
						delCheck = cursor.execute("SELECT * FROM TwitterUsers WHERE USERNAME = ?", (userToDel,))
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

			else:
				os.system('clear')
				print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.\n'
				main_() 

		elif dbEdit == dbHandler['resetDB']:
			os.system('clear')
			print statusTrue

			delConfirmation = raw_input(' Are you sure you want to reset DB [y/n]: ')
			if delConfirmation == 'y' or 'Y':
				print bcolors.RED + ' Resetting DB.\n'
				cursor.execute("DROP TABLE IF EXISTS TwitterUsers")
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
			os.system('clear')
			print bcolors.RED + ' Invalid Syntax. Exiting to main menu.'
			main_()

	elif cmd in commands['optionList']:
		os.system('clear')
		print bcolors.BLUE + ' Commands:'
		twitter = bcolors.GREEN + '   Gather info from Twitter Account	-	' + bcolors.RED + commands['twitter']
		facebook = bcolors.GREEN + '   Gather info from Facebook Account	-	' + bcolors.RED + commands['facebook']
		search = bcolors.GREEN + '   Search DB for a user			-	' + bcolors.RED + commands['search']
		editDB = bcolors.GREEN + '   Edit a DB record			-	' + bcolors.RED + commands['modifydb']
		exit = bcolors.GREEN + '   Exit					-	' + bcolors.RED + commands['exit']
		x = '\n'

		print x, twitter, x, facebook, x, search, x, editDB, x, exit, x
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
