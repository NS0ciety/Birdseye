#!/usr/bin/python
# -*- coding: utf-8 -*-

class bcolors:
	GREEN = '\033[1;32m'
	BLUE = '\033[1;34m'
	RED = '\033[1;31m'

def instagramScrape():
	import sqlite3
	from sqlite3 import Error
	import requests
	from bs4 import BeautifulSoup
	import fileinput
	import json
	import sys, os, time

	reload(sys)
	sys.setdefaultencoding('utf8')

	headers = {'Accept-Language': 'en-US,en;q=0.5'}

	db = './db/birdseye.db'
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
	ID = raw_input(bcolors.RED + ' Enter Instagram ID: ' + bcolors.GREEN + '')
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
		
		scripts = soup.select('script[type="application/ld+json"]')
		scripts_content = json.loads(scripts[0].text.strip())

		#User Info
		print bcolors.BLUE + '\n User Details:' + bcolors.GREEN
		
		user_type = scripts_content['@type']
		print ' User Type: ' + user_type

		for names in soup.select('title'):
			name_split = names.get_text()
			name_s = name_split.split('(', 1)
			name = name_s[0].replace('\n', '')
			print ' Full Name: ' + name
			
		description = scripts_content['description']
		print ' Description: ' + description
		
		main_entity = scripts_content['mainEntityofPage']
		page_type = main_entity['@type']
		print ' Page Type: ' + page_type
		
		interactions = main_entity['interactionStatistic']
		followers = interactions['userInteractionCount']
		print ' Followers: ' + followers
		
		userscript = soup.select('script')[4].text
		datapack = open("./tmp/instadata.txt","w+")
		datapack.write(userscript)
		datapack.close()
		
		for line in fileinput.input('/root/Birdseye/tmp/instadata.txt', inplace=True):
			print line.replace(',', '\n'),

		datapack = open("./tmp/instadata.txt", "r")
		data_to_read = datapack.readlines()
		datapack.close()
		
		following = data_to_read[17].replace('"edge_follow":{"count":', '')
		print ' Following: ' + following.replace('}\n', '')

		posts = data_to_read[44].replace('"edge_owner_to_timeline_media":{"count":', '').replace('\n', '')
		print ' Post Count: ' + posts
		
		highlights = data_to_read[23].replace('"highlight_reel_count":', '').replace('\n', '')
		print ' Highlight Reel Count: ' + highlights

		videos = data_to_read[40].replace('"edge_felix_video_timeline":{"count":', '').replace('\n', '')
		print ' Video Count: ' + videos

		isPrivate = data_to_read[31].replace('"is_private":', '').replace('\n', '')
		print ' Private Account: ' + isPrivate
		
		isVerified = data_to_read[32].replace('"is_verified":', '').replace('\n', '')
		print ' Verified Account: ' + isVerified
		
		fbConnected = data_to_read[39].replace('"connected_fb_page":', '').replace('\n', '')
		if 'null' in fbConnected:
			fbConnected = 'false'
			print ' Connected to Facebook Account: ' + fbConnected


		#Post 1
		print bcolors.BLUE + '\n Post 1:' + bcolors.GREEN
		post1_id = data_to_read[48].replace('"id":"', '').replace('"\n', '')
		print ' Post 1 - Post ID: ' + post1_id
		post1_owner_id = data_to_read[57].replace('"owner":{"id":"', '').replace('"\n', '')
		print ' Post 1 - Owner ID: ' + post1_owner_id
		post1_timestamp = data_to_read[65].replace('"taken_at_timestamp":', '').replace('\n', '')
		print ' Post 1 - Timestamp: ' + post1_timestamp
		post1_isVideo = data_to_read[59].replace('"is_video":', '').replace('\n', '')
		print ' Post 1 - Is Video: ' + post1_isVideo
		accessibility_caption_1st = data_to_read[60].replace('"accessibility_caption":"', '').replace('\n', '') 
		accessibility_caption_2nd = data_to_read[61].replace('\n', '') 
		accessibility_caption = accessibility_caption_1st + accessibility_caption_2nd
		print ' Post 1 - Accessibility Caption: ' + accessibility_caption
		post1_user_caption = data_to_read[62].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}\n', '')
		print ' Post 1 - User Caption: ' + post1_user_caption
		post1_comments = data_to_read[63].replace('"edge_media_to_comment":{"count":', '').replace('}\n', '')
		print ' Post 1 - Comments' + post1_comments
		post1_comments_disabled = data_to_read[64].replace('"comments_disabled":', '').replace('\n', '')
		print ' Post 1 - Comments Disabled: ' + post1_comments_disabled
		post1_likedBy = data_to_read[66].replace('"edge_liked_by":{"count":', '').replace('}\n', '')
		print ' Post 1 - Liked By: ' + post1_likedBy
		post1_location = data_to_read[68].replace('"location":', '').replace('\n', '')
		print ' Post 1 = Location: ' + post1_location
		
		#Post2
		print bcolors.BLUE + '\n Post 2:' + bcolors.GREEN
		post2_id = data_to_read[86].replace('"id":"', '').replace('"\n', '')
		print ' Post 2 - Post ID: ' + post2_id
		post2_owner_id = data_to_read[95].replace('"owner":{"id":"', '').replace('"\n', '')
		print ' Post 2 - Owner ID: ' + post2_owner_id
		post2_timestamp = data_to_read[103].replace('"taken_at_timestamp":', '').replace('\n', '')
		print ' Post 2 - Timestamp: ' + post2_timestamp
		post2_isVideo = data_to_read[97].replace('"is_video":', '').replace('\n', '')
		print ' Post 2 - Is Video: ' + post2_isVideo
		post2_accessibility_caption_1st = data_to_read[98].replace('"accessibility_caption":"', '').replace('\n', '') 
		post2_accessibility_caption_2nd = data_to_read[99].replace('\n', '') 
		post2_accessibility_caption = post2_accessibility_caption_1st + post2_accessibility_caption_2nd
		print ' Post 2 - Accessibility Caption: ' + post2_accessibility_caption
		post2_user_caption = data_to_read[100].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}\n', '')
		print ' Post 2 - User Caption: ' + post2_user_caption
		post2_comments = data_to_read[101].replace('"edge_media_to_comment":{"count":', '').replace('}\n', '')
		print ' Post 2 - Comments' + post2_comments
		post2_comments_disabled = data_to_read[102].replace('"comments_disabled":', '').replace('\n', '')
		print ' Post 2 - Comments Disabled: ' + post2_comments_disabled
		post2_likedBy = data_to_read[104].replace('"edge_liked_by":{"count":', '').replace('}\n', '')
		print ' Post 2 - Liked By: ' + post2_likedBy
		post2_location = data_to_read[106].replace('"location":', '').replace('\n', '')
		print ' Post 2 = Location: ' + post2_location + '\n'
		
		try:
			cursor.execute("INSERT INTO InstagramUsers (USERTYPE, NAME, DESCRIPTION, PAGETYPE, FOLLOWERS, FOLLOWING, POSTS, HIGHLIGHTS, VIDEOS, ISPRIVATE, ISVERIFIED, FBCONNECTED) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_type, name, description, page_type, followers, following, posts, highlights, videos, isPrivate, isVerified, fbConnected))
			conn.commit()
			print bcolors.RED + ' ' + name + bcolors.GREEN + ' was added to the DB successfully.\n'
				

		except sqlite3.IntegrityError as iError:
			print bcolors.RED + ' ' + ID + bcolors.GREEN + ' Already exists in DB.\n'
				

	else:
		os.system('clear')
		print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.' + bcolors.GREEN

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

