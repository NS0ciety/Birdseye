#!/usr/bin/python

class bcolors:
	GREEN = '\033[1;32m'
	BLUE = '\033[1;34m'
	RED = '\033[1;31m'

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

def dbModify():
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

	dbHandler = {
		'updateUser':'update user',
	#	'addCol':'add column',
		'delUser':'del user',
		'resetDB':'reset db',
		'#//':'#//'
		}

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
		print '   Facebook		-	' + bcolors.RED + '	facebook'
		print bcolors.GREEN + '   Twitter		-	' + bcolors.RED + '	twitter\n'

		choice = raw_input(bcolors.RED + ' Choose Site Record to update: ' + bcolors.GREEN)

		if choice == 'facebook':
			os.system('clear')
			print statusTrue
			print bcolors.BLUE + ' Data types:'
			ID = bcolors.GREEN + '   ID				-		' + bcolors.RED + facebookDataTypes['id']
			name = bcolors.GREEN + '   Name				-		' + bcolors.RED + facebookDataTypes['name']
			contactinfo = bcolors.GREEN + '   Contact Information		-		' + bcolors.RED + facebookDataTypes['contactinfo']
			location = bcolors.GREEN + '   Location			-		' + bcolors.RED + facebookDataTypes['location']
			aboutuser = bcolors.GREEN + '   About user			-		' + bcolors.RED + facebookDataTypes['aboutuser']
			skills = bcolors.GREEN + '   Professional Skills		-		' + bcolors.RED + facebookDataTypes['skills']
			education = bcolors.GREEN + '   Education			-		' + bcolors.RED + facebookDataTypes['education']	
			friends = bcolors.GREEN + '   Friends			-		' + bcolors.RED + facebookDataTypes['friends']
			photocount = bcolors.GREEN + '   Photo Count			-		' + bcolors.RED + facebookDataTypes['photocount']
			photo1 = bcolors.GREEN + '   Photo Link 1			-		' + bcolors.RED + facebookDataTypes['photo1']
			photo2 = bcolors.GREEN + '   Photo Link 2			-		' + bcolors.RED + facebookDataTypes['photo2']
			photo3 = bcolors.GREEN + '   Photo Link 3			-		' + bcolors.RED + facebookDataTypes['photo3']
			x = '\n'

			print x, ID, x, name, x, contactinfo, x , location, x, aboutuser, x, skills, x, education, x, friends, x, photocount, x, photo1, x, photo2, x, photo3, x

			dataType = raw_input(' Choose data to modify: ' + bcolors.GREEN)
			unameToMod = raw_input(bcolors.RED + ' Enter username of user to modify: ' + bcolors.GREEN)
			print ' Checking if ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
			time.sleep(3)

			try:
	 			uname = cursor.execute("SELECT * FROM FacebookUsers WHERE USERNAME = ?", (unameToMod,))
				data = cursor.fetchone()
  
				if dataType == '#//':
					os.system('clear')
		
				elif dataType == facebookDataTypes['id']:
					for uname in data[0]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newUname = raw_input(bcolors.RED + ' Enter new ID: ' + bcolors.GREEN)
						cursor.execute("UPDATE FacebookUsers SET USERNAME = ? WHERE USERNAME = ?", (newUname, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " ID to " + bcolors.BLUE + newUname + "\n"
						break

					else:
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " ID.\n"
					

				elif dataType == facebookDataTypes['name']:
					for uname in data[0]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newName = raw_input(bcolors.RED + ' Enter new name: ' + bcolors.GREEN)
						cursor.execute("UPDATE FacebookUsers SET NAME = ? WHERE USERNAME = ?", (newName, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " name to " + bcolors.BLUE + newName + "\n"
						break
					else:
						os.system('clear')
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " name.\n"
						

				elif dataType == facebookDataTypes['contactinfo']:
					for uname in data[0]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newContact = raw_input(bcolors.RED + ' Enter new contact information: ' + bcolors.GREEN)
						cursor.execute("UPDATE FacebookUsers SET CONTACTINFO = ? WHERE USERNAME = ?", (newContact, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " Contact Information to " + bcolors.BLUE + newContact + "\n"
						break					
					else:
						os.system('clear')
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " Contact Information.\n"

				elif dataType == facebookDataTypes['location']:
					for uname in data[0]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newLocation = raw_input(bcolors.RED + ' Enter new location: ' + bcolors.GREEN)
						cursor.execute("UPDATE FacebookUsers SET LOCATION = ? WHERE USERNAME = ?", (newLocation, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " location to " + bcolors.BLUE + newLocation + "\n"
						break					
					else:
						os.system('clear')
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " location.\n"
					

				elif dataType == facebookDataTypes['aboutuser']:
					for uname in data[0]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newAbout = raw_input(bcolors.RED + ' Enter new about user: ' + bcolors.GREEN)
						cursor.execute("UPDATE FacebookUsers SET ABOUTUSER = ? WHERE USERNAME = ?", (newAbout, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " about to " + bcolors.BLUE + newAbout + "\n"
						break					
					else:
						os.system('clear')
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " about.\n"
					

				elif dataType == facebookDataTypes['skills']:
					for uname in data[0]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newSkills = raw_input(bcolors.RED + ' Enter new skills: ' + bcolors.GREEN)
						cursor.execute("UPDATE FacebookUsers SET SKILLS = ? WHERE USERNAME = ?", (newSkills, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " professional skills to " + bcolors.BLUE + newSkills + "\n"
						break							
					else:
						os.system('clear')
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " professional skills.\n"
					

				elif dataType == facebookDataTypes['education']:
					for uname in data[0]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newEducation = raw_input(bcolors.RED + ' Enter new education: ' + bcolors.GREEN)
						cursor.execute("UPDATE FacebookUsers SET EDUCATION = ? WHERE USERNAME = ?", (newEducation, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " education to " + bcolors.BLUE + newEducation + "\n"
						break
					else:
						os.system('clear')
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " education.\n"
					

				elif dataType == facebookDataTypes['friends']:
					for uname in data[0]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newFriends = raw_input(bcolors.RED + ' Enter new friend count: ' + bcolors.GREEN)
						cursor.execute("UPDATE FacebookUsers SET FRIENDS = ? WHERE USERNAME = ?", (newFriends, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " friends count to " + bcolors.BLUE + newFriends + "\n"
						break					
					else:
						os.system('clear')
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " friends count.\n"
					

				elif dataType == facebookDataTypes['photocount']:
					for uname in data[0]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newPhotoC = raw_input(bcolors.RED + ' Enter new photo count: ' + bcolors.GREEN)
						cursor.execute("UPDATE FacebookUsers SET PHOTOCOUNT = ? WHERE USERNAME = ?", (newPhotoC, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " photo count to " + bcolors.BLUE + newPhotoC + "\n"
						break					
					else:
						os.system('clear')
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " photo count.\n"
					

				elif dataType == facebookDataTypes['photo1']:
					for uname in data[0]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newPhoto1 = raw_input(bcolors.RED + ' Enter new photo 1 link: ' + bcolors.GREEN)
						cursor.execute("UPDATE FacebookUsers SET PHOTO1 = ? WHERE USERNAME = ?", (newPhoto1, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " photo 1 link to " + bcolors.BLUE + newPhoto1 + "\n"
						break
					else:
						os.system('clear')
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " photo 1 link.\n"
					

				elif dataType == facebookDataTypes['photo2']:
					for uname in data[0]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newPhoto2 = raw_input(bcolors.RED + ' Enter new photo 2 link: ' + bcolors.GREEN)
						cursor.execute("UPDATE FacebookUsers SET PHOTO2 = ? WHERE USERNAME = ?", (newPhoto2, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " photo 2 link to " + bcolors.BLUE + newPhoto2 + "\n"
						break
					else:
						os.system('clear')
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " photo 2 link.\n"
					

				elif dataType == facebookDataTypes['photo3']:
					for uname in data[0]:
						print ' Facebook ID: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newPhoto3 = raw_input(bcolors.RED + ' Enter new photo 3 link: ' + bcolors.GREEN)
						cursor.execute("UPDATE FacebookUsers SET PHOTO3 = ? WHERE USERNAME = ?", (newPhoto3, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " photo 3 link to " + bcolors.BLUE + newPhoto3 + "\n"
						break
					else:
						os.system('clear')
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " photo 3 link.\n"

				else:
					os.system('clear')
					print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.' + bcolors.GREEN

			except TypeError as tError:
				os.system('clear')
				print ' ' + bcolors.RED + unameToMod + bcolors.GREEN + ' does not exist in DB.\n ' + bcolors.RED + 'Exiting to the main menu.\n' + bcolors.GREEN				

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

			print x, username, x, name, x, image, x, location, x, biography, x, joindate, x, birthday, x

			dataType = raw_input(' Choose data to modify: ' + bcolors.GREEN)
			unameToMod = raw_input(bcolors.RED + ' Enter username of user to modify: ' + bcolors.GREEN)
			print ' Checking if ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
			time.sleep(3)

			try:
	 			uname = cursor.execute("SELECT * FROM TwitterUsers WHERE USERNAME = ?", (unameToMod,))
				data = cursor.fetchone()
		
				if dataType == twitterDataTypes['username']:
					for uname in data[0]:
						print ' Username: ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						newUname = raw_input(bcolors.RED + ' Enter new username: ' + bcolors.GREEN)
						cursor.execute("UPDATE TwitterUsers SET USERNAME = ? WHERE USERNAME = ?", (newUname, unameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " username to " + bcolors.BLUE + newUname + "\n"
						break
					else:
						os.system('clear')
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " username is still " + bcolors.RED + unameToMod + "\n"

				elif dataType in twitterDataTypes['name']:
					for uname in data[0]:
						nameToMod = data[1]
						print ' Name: ' + bcolors.RED + nameToMod + bcolors.GREEN + ' exists in DB.'
						newName = raw_input(bcolors.RED + ' Enter new name: ' + bcolors.GREEN)
						cursor.execute("UPDATE TwitterUsers SET NAME = ? WHERE NAME = ?", (newName, nameToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + nameToMod + "'s" + bcolors.GREEN + " name to " + bcolors.BLUE + newName + "\n"
						break
					else:
						os.system('clear')
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " name is still " + bcolors.BLUE + unameToMod + "\n"
					

				elif dataType in twitterDataTypes['imgSrc']:
					for uname in data[0]:
						imgToMod = data[2]
						print ' Image Src: ' + bcolors.BLUE + imgToMod + bcolors.GREEN + ' for ' + bcolors.RED + unameToMod + bcolors.GREEN + ' exists in DB.'
						print bcolors.RED + ' NOTE: ' + bcolors.GREEN + 'Providing an invalid link will result in a broken image.'
						newSrc = raw_input(bcolors.RED + ' Enter new image link: ' + bcolors.GREEN)
						cursor.execute("UPDATE TwitterUsers SET USERIMAGE = ? WHERE USERIMAGE = ?", (newSrc, imgToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " image src to " + bcolors.BLUE + newSrc + "\n"
						break	
					else:
						os.system('clear')
						print bcolors.GREEN + " Failed to update " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " link. Image src is still " + bcolors.BLUE + imgToMod + "\n"
					

				elif dataType in twitterDataTypes['location']:
					for uname in data[0]:
						locationToMod = data[3]
						print bcolors.GREEN + " Location: " + bcolors.RED + locationToMod + bcolors.GREEN + " exists in DB."
						newLocation = raw_input(bcolors.RED + ' Enter new location: ' + bcolors.GREEN)
						cursor.execute("UPDATE TwitterUsers SET LOCATION = ? WHERE LOCATION = ?", (newLocation, locationToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s " + bcolors.GREEN + "Location from " + bcolors.RED + locationToMod + bcolors.GREEN + " to " + bcolors.BLUE + newLocation + "\n"
						break
					else:
						os.system('clear')
						print " Failed to update " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " location. Location is still " + bcolors.BLUE + locationToMod + "\n"
					

				elif dataType in twitterDataTypes['biography']:
					for uname in data[0]:
						bioToMod = data[4]
						print ' Biography Section: ' + bcolors.RED + bioToMod + bcolors.GREEN + ' exists in DB.'

						newBio = raw_input(bcolors.RED + ' Enter new biography section: ' + bcolors.GREEN)
						cursor.execute("UPDATE TwitterUsers SET BIOGRAPHY = ? WHERE BIOGRAPHY = ?", (newBio, bioToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " biography section from " + bcolors.RED + bioToMod + bcolors.GREEN + " to " + bcolors.BLUE + newBio + "\n"
						break				
					else:
						os.system('clear')
						print " Update failed " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " biography section. Bio is still " + bcolors.BLUE + bioToMod + "\n"
					

				elif dataType in twitterDataTypes['joindate']:
					for uname in data[0]:
						joindateToMod = data[5]
						print ' Join Date: ' + bcolors.RED + joindateToMod + bcolors.GREEN + ' exists in DB.'
						newJoindate = raw_input(bcolors.RED + ' Enter new join date: ' + bcolors.GREEN)
						cursor.execute("UPDATE TwitterUsers SET JOINDATE = ? WHERE JOINDATE = ?", (newJoindate, joindateToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " joindate from " + bcolors.RED + joindateToMod + bcolors.GREEN + " to " + bcolors.BLUE + newJoindate + "\n"
						break
					else:
						os.system('clear')
						print " Failed to update " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " join date. Join date is still " + bcolors.BLUE + joindateToMod + "\n"
					

				elif dataType in twitterDataTypes['birthdate']:
					for uname in data[0]:
						bdayToMod = data[6]
						print ' Birth Date: ' + bcolors.RED + bdayToMod + bcolors.GREEN + ' exists in DB.'
						newBday = raw_input(bcolors.RED + ' Enter new birth date: ' + bcolors.GREEN)
						cursor.execute("UPDATE TwitterUsers SET BIRTHDAY = ? WHERE BIRTHDAY = ?", (newBday, bdayToMod))
						conn.commit()
						os.system('clear')
						print " Successfully updated " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " birth date from " + bdayToMod + bcolors.GREEN + " to " + bcolors.BLUE + newBday + "\n"
						break							
					else:
						os.system('clear')
						print " Failed to update " + bcolors.RED + unameToMod + "'s" + bcolors.GREEN + " birth date. Birth date is still " + bcolors.BLUE + joindateToMod + "\n"

				else:
					os.system('clear')
					print bcolors.RED + ' Invalid DataType: Exiting to main menu.' + bcolors.GREEN
				
			except TypeError as tError:
				os.system('clear')
				print ' ' + bcolors.RED + unameToMod + bcolors.GREEN + ' does not exist in DB.\n ' + bcolors.RED + 'Exiting to the main menu.\n' + bcolors.GREEN

		else:
			os.system('clear')
			print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.\n' + bcolors.GREEN
			

#	elif dbEdit == dbHandler['addCol']:
#		os.system('clear')
#		newCol = raw_input(' Enter new column name: ')
#		os.system('clear')		
#		if newCol != '':
#			cursor.execute("ALTER TABLE TwitterUsers ADD COLUMN '"+newCol+"' 'TEXT'")
#			conn.commit()
				
#			print ' Success: new column ' + bcolors.RED + newCol + bcolors.GREEN + ' was added to DB table ' + bcolors.RED + 'Users \n' + bcolors.GREEN
#			
#		else:
#			os.system('clear')
#			print bcolors.RED + ' Invalid Column Name. Exiting to main menu.\n' + bcolors.GREEN


	elif dbEdit == dbHandler['delUser']:
		os.system('clear')
		print statusTrue
		print bcolors.BLUE + ' Sites:\n'
		print bcolors.GREEN + '   Facebook		-		' + bcolors.RED + 'facebook'
		print bcolors.GREEN + '   Twitter		-		' + bcolors.RED + 'twitter\n'

		choice = raw_input(bcolors.RED + ' Choose from site to delete user: ' + bcolors.GREEN)
		userToDel = raw_input(bcolors.RED + ' Enter username of record to delete: ' + bcolors.GREEN)

		if choice == 'facebook':
			os.system('clear')
			print ' Checking if ' + bcolors.RED + userToDel + bcolors.GREEN + ' exists in DB.'
			time.sleep(3)
			try:
		 		uname = cursor.execute("SELECT * FROM FacebookUsers WHERE USERNAME = ?", (userToDel,))
				data = cursor.fetchone()

				for uname in data[0]:
					print ' Username: ' + bcolors.RED + userToDel + bcolors.GREEN + ' exists in DB.\m'
					confirmDel = raw_input(bcolors.RED + ' Confirm deletion [y/n]: ' + bcolors.GREEN)
					if confirmDel == 'y':
						cursor.execute("DELETE FROM FacebookUsers WHERE USERNAME = ?", (userToDel,))
						conn.commit() 
						delCheck = cursor.execute("SELECT * FROM FacebookUsers WHERE USERNAME = ?", (userToDel,))
						os.system('clear')
						print bcolors.RED + ' ' + userToDel + bcolors.GREEN + ' was deleted from the DB.\n'
						break
	
					elif confirmDel == 'n':
						os.system('clear')
						print bcolors.RED + userToDel + bcolors.GREEN + ' was not be deleted from DB.\n'
						break
					else:
						os.system('clear')
						print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.'
				else:
					print bcolors.GREEN + ' There was a problem loading user: ' + bcolors.GREEN + userToDel  

			except TypeError as tError:
				os.system('clear')
				print ' ' + bcolors.RED + userToDel + bcolors.GREEN + ' does not exist in the DB.\n'
				

		elif choice == 'twitter':
			os.system('clear')
			print ' Checking if ' + bcolors.RED + userToDel + bcolors.GREEN + ' exists in DB.'
			time.sleep(3)

			try:
		 		uname = cursor.execute("SELECT * FROM TwitterUsers WHERE USERNAME = ?", (userToDel,))
				data = cursor.fetchone()

				for uname in data[0]:
					print ' Username: ' + bcolors.RED + userToDel + bcolors.GREEN + ' exists in DB.\n'
					confirmDel = raw_input(bcolors.RED + ' Confirm deletion [y/n]: ' + bcolors.GREEN)
					if confirmDel == 'y':
						cursor.execute("DELETE FROM TwitterUsers WHERE USERNAME = ?", (userToDel,))
						conn.commit() 
						delCheck = cursor.execute("SELECT * FROM TwitterUsers WHERE USERNAME = ?", (userToDel,))
						os.system('clear')
						print bcolors.RED + ' ' + userToDel + bcolors.GREEN + ' was deleted from the DB.\n'
						break
	
					elif confirmDel == 'n':
						os.system('clear')
						print bcolors.RED + userToDel + bcolors.GREEN + ' was not be deleted from DB.\n'
						break
					else:
						os.system('clear')
						print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.'
					
				else:
					os.system('clear')
					print bcolors.RED + userToDel + bcolors.GREEN + ' does not exist in the DB.\n'

			except TypeError as tError:
				os.system('clear')
				print ' ' + bcolors.RED + userToDel + bcolors.GREEN + ' does not exist in the DB.\n'
				
		else:
			os.system('clear')
			print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.\n'
			 

	elif dbEdit == dbHandler['resetDB']:
		os.system('clear')
		print statusTrue

		delConfirmation = raw_input(bcolors.RED + ' Are you sure you want to reset DB [y/n]: ' + bcolors.GREEN)
		if delConfirmation == 'y':
			print bcolors.RED + ' Resetting DB.\n'
			cursor.execute("DROP TABLE IF EXISTS TwitterUsers")
			time.sleep(2)
			os.system('clear')
			print bcolors.GREEN + ' Database has been reset.\n'

		elif delConfirmation == 'n' or 'N':
			print bcolors.RED + ' Exiting to the main menu.'
			time.sleep(2)
			os.system('clear')

		else:
			os.system('clear')
			print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.'
			

	elif dbEdit == dbHandler['#//']:
		os.system('clear')
				
	else:
		os.system('clear')
		print bcolors.RED + ' Invalid Syntax. Exiting to main menu.'
				


