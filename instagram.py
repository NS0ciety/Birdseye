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
		print bcolors.RED + ' Instagram Link: ' + bcolors.BLUE + url + bcolors.GREEN
		print bcolors.RED + ' Instagram ID: ' + bcolors.GREEN + ID + bcolors.GREEN
		
		scripts = soup.select('script[type="application/ld+json"]')
		scripts_content = json.loads(scripts[0].text.strip())

		#User Info
		print bcolors.BLUE + '\n User Details:' + bcolors.GREEN
		
		user_type = scripts_content['@type']
		print bcolors.RED + ' User Type: ' + bcolors.GREEN + user_type

		for names in soup.select('title'):
			name_split = names.get_text()
			name_s = name_split.split('(', 1)
			name = name_s[0].replace('\n', '')
			print bcolors.RED + ' Full Name: ' + bcolors.GREEN + name
			
		description = scripts_content['description']
		print bcolors.RED + ' Description: ' + bcolors.GREEN + description
		
		main_entity = scripts_content['mainEntityofPage']
		page_type = main_entity['@type']
		print bcolors.RED + ' Page Type: ' + bcolors.GREEN + page_type
		
		interactions = main_entity['interactionStatistic']
		followers = interactions['userInteractionCount']
		print bcolors.RED + ' Followers: ' + bcolors.GREEN + followers
		
		userscript = soup.select('script')[4].text
		
		following = userscript.split(',')[17].replace('"edge_follow":{"count":', '').replace('}', '')
		print bcolors.RED + ' Following: ' + bcolors.GREEN + following

		posts = userscript.split(',')[44].replace('"edge_owner_to_timeline_media":{"count":', '').replace('\n', '')
		print bcolors.RED + ' Post Count: ' + bcolors.GREEN + posts
		
		highlights = userscript.split(',')[23].replace('"highlight_reel_count":', '').replace('\n', '')
		print bcolors.RED + ' Highlight Reel Count: ' + bcolors.GREEN + highlights

		videos = userscript.split(',')[40].replace('"edge_felix_video_timeline":{"count":', '').replace('\n', '')
		print bcolors.RED + ' Video Count: ' + bcolors.GREEN + videos

		isPrivate = userscript.split(',')[31].replace('"is_private":', '').replace('\n', '')
		print bcolors.RED + ' Private Account: ' + bcolors.GREEN + isPrivate
		
		isVerified = userscript.split(',')[32].replace('"is_verified":', '').replace('\n', '')
		print bcolors.RED + ' Verified Account: ' + bcolors.GREEN + isVerified
		
		fbConnected = userscript.split(',')[39].replace('"connected_fb_page":', '').replace('\n', '')
		if 'null' in fbConnected:
			fbConnected = 'false'
			print bcolors.RED + ' Connected to Facebook Account: ' + bcolors.GREEN + fbConnected


		#Post 1
		print bcolors.BLUE + '\n Post 1:' + bcolors.GREEN
		post1_id = userscript.split(',')[48].replace('"id":"', '').replace('"', '')
		print bcolors.RED + ' Post 1 - Post ID: ' + bcolors.GREEN + post1_id
		post1_owner_id = userscript.split(',')[57].replace('"owner":{"id":"', '').replace('"', '')
		print bcolors.RED + ' Post 1 - Owner ID: ' + bcolors.GREEN + post1_owner_id
		post1_timestamp = userscript.split(',')[65].replace('"taken_at_timestamp":', '').replace('\n', '')
		print bcolors.RED + ' Post 1 - Timestamp: ' + bcolors.GREEN + post1_timestamp
		post1_isVideo = userscript.split(',')[59].replace('"is_video":', '').replace('\n', '')
		print bcolors.RED + ' Post 1 - Is Video: ' + bcolors.GREEN + post1_isVideo
		accessibility_caption_1st = userscript.split(',')[60].replace('"accessibility_caption":"', '').replace('\n', '') 
		accessibility_caption_2nd = userscript.split(',')[61].replace('"', '') 
		accessibility_caption = accessibility_caption_1st + accessibility_caption_2nd
		print bcolors.RED + ' Post 1 - Accessibility Caption: ' + bcolors.GREEN + accessibility_caption
		post1_user_caption = userscript.split(',')[62].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}', '')
		print bcolors.RED + ' Post 1 - User Caption: ' + bcolors.GREEN + post1_user_caption
		post1_comments = userscript.split(',')[63].replace('"edge_media_to_comment":{"count":', '').replace('}', '')
		print bcolors.RED + ' Post 1 - Comments: ' + bcolors.GREEN + post1_comments
		post1_comments_disabled = userscript.split(',')[64].replace('"comments_disabled":', '').replace('\n', '')
		print bcolors.RED + ' Post 1 - Comments Disabled: ' + bcolors.GREEN + post1_comments_disabled
		post1_likedBy = userscript.split(',')[66].replace('"edge_liked_by":{"count":', '').replace('}', '')
		print bcolors.RED + ' Post 1 - Liked By: ' + bcolors.GREEN + post1_likedBy
		post1_location = userscript.split(',')[68].replace('"location":', '').replace('\n', '')
		print bcolors.RED + ' Post 1 = Location: ' + bcolors.GREEN + post1_location
		
		#Post2
		print bcolors.BLUE + '\n Post 2:' + bcolors.GREEN
		post2_id = userscript.split(',')[86].replace('"id":"', '').replace('"', '')
		print bcolors.RED + ' Post 2 - Post ID: ' + bcolors.GREEN + post2_id
		post2_owner_id = userscript.split(',')[95].replace('"owner":{"id":"', '').replace('"', '')
		print bcolors.RED + ' Post 2 - Owner ID: ' + bcolors.GREEN + post2_owner_id
		post2_timestamp = userscript.split(',')[103].replace('"taken_at_timestamp":', '').replace('\n', '')
		print bcolors.RED + ' Post 2 - Timestamp: ' + bcolors.GREEN + post2_timestamp
		post2_isVideo = userscript.split(',')[97].replace('"is_video":', '').replace('\n', '')
		print bcolors.RED + ' Post 2 - Is Video: ' + bcolors.GREEN + post2_isVideo
		post2_accessibility_caption_1st = userscript.split(',')[98].replace('"accessibility_caption":"', '').replace('\n', '') 
		post2_accessibility_caption_2nd = userscript.split(',')[99].replace('"', '') 
		post2_accessibility_caption = post2_accessibility_caption_1st + post2_accessibility_caption_2nd
		print bcolors.RED + ' Post 2 - Accessibility Caption: ' + bcolors.GREEN + post2_accessibility_caption
		post2_user_caption = userscript.split(',')[100].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}', '')
		print bcolors.RED + ' Post 2 - User Caption: ' + bcolors.GREEN + post2_user_caption
		post2_comments = userscript.split(',')[101].replace('"edge_media_to_comment":{"count":', '').replace('}', '')
		print bcolors.RED + ' Post 2 - Comments: ' + bcolors.GREEN + post2_comments
		post2_comments_disabled = userscript.split(',')[102].replace('"comments_disabled":', '').replace('\n', '')
		print bcolors.RED + ' Post 2 - Comments Disabled: ' + bcolors.GREEN + post2_comments_disabled
		post2_likedBy = userscript.split(',')[104].replace('"edge_liked_by":{"count":', '').replace('}', '')
		print bcolors.RED + ' Post 2 - Liked By: ' + bcolors.GREEN + post2_likedBy
		post2_location = userscript.split(',')[106].replace('"location":', '').replace('\n', '')
		print bcolors.RED + ' Post 2 = Location: ' + bcolors.GREEN + post2_location + '\n'
		
		try:
			cursor.execute("INSERT INTO InstagramUsers (USERTYPE, NAME, DESCRIPTION, PAGETYPE, FOLLOWERS, FOLLOWING, POSTS, HIGHLIGHTS, VIDEOS, ISPRIVATE, ISVERIFIED, FBCONNECTED) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_type, name, description, page_type, followers, following, posts, highlights, videos, isPrivate, isVerified, fbConnected))
			conn.commit()
			print bcolors.RED + ' ' + name + bcolors.GREEN + ' was added to the DB successfully.\n'
				

		except sqlite3.IntegrityError as iError:
			print bcolors.RED + ' ' + ID + bcolors.GREEN + ' Already exists in DB.\n'
				
	else:
		os.system('clear')
		print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.' + bcolors.GREEN
