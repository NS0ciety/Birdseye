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
			
		description = scripts_content['description'].replace('\n', '')
		print bcolors.RED + ' Description: ' + bcolors.GREEN + description
		
		main_entity = scripts_content['mainEntityofPage']
		page_type = main_entity['@type']
		print bcolors.RED + ' Page Type: ' + bcolors.GREEN + page_type
		
		interactions = main_entity['interactionStatistic']
		followers = interactions['userInteractionCount']
		print bcolors.RED + ' Followers: ' + bcolors.GREEN + followers
		
		userscript = soup.select('script')[4].text.strip()
		splitdata = userscript.split(',')
		userdata = []
		
		userdata.append(splitdata)
		# Following
		if '"edge_follow":{"count":' in userdata[0][14]:
			following = userdata[0][14].replace('"edge_follow":{"count":', '').replace('}','')
			print bcolors.RED + ' Following: ' + bcolors.GREEN + following
		elif '"edge_follow":{"count":' in userdata[0][15]:
			following = userdata[0][15].replace('"edge_follow":{"count":', '').replace('}','')
			print bcolors.RED + ' Following: ' + bcolors.GREEN + following
		elif '"edge_follow":{"count":' in userdata[0][16]:
			following = userdata[0][16].replace('"edge_follow":{"count":', '').replace('}','')
			print bcolors.RED + ' Following: ' + bcolors.GREEN + following
		elif '"edge_follow":{"count":' in userdata[0][17]:
			following = userdata[0][17].replace('"edge_follow":{"count":', '').replace('}','')
			print bcolors.RED + ' Following: ' + bcolors.GREEN + following
		elif '"edge_follow":{"count":' in userdata[0][18]:
			following = userdata[0][18].replace('"edge_follow":{"count":', '').replace('}','')
			print bcolors.RED + ' Following: ' + bcolors.GREEN + following
		elif '"edge_follow":{"count":' in userdata[0][19]:
			following = userdata[0][19].replace('"edge_follow":{"count":', '').replace('}','')
			print bcolors.RED + ' Following: ' + bcolors.GREEN + following
		elif '"edge_follow":{"count":' in userdata[0][20]:
			following = userdata[0][20].replace('"edge_follow":{"count":', '').replace('}','')
			print bcolors.RED + ' Following: ' + bcolors.GREEN + following
		else:
			following = ' Could not gather data'
			print bcolors.RED + ' Following: ' + bcolors.GREEN + following
			
		# Post Count
		if '"edge_owner_to_timeline_media":{"count":' in userdata[0][41]:
			posts = userdata[0][41].replace('"edge_owner_to_timeline_media":{"count":', '').replace('}','')
			print bcolors.RED + ' Posts: ' + bcolors.GREEN + posts
		elif '"edge_owner_to_timeline_media":{"count":' in userdata[0][42]:
			posts = userdata[0][42].replace('"edge_owner_to_timeline_media":{"count":', '').replace('}','')
			print bcolors.RED + ' Posts: ' + bcolors.GREEN + posts
		elif '"edge_owner_to_timeline_media":{"count":' in userdata[0][43]:
			posts = userdata[0][43].replace('"edge_owner_to_timeline_media":{"count":', '').replace('}','')
			print bcolors.RED + ' Posts: ' + bcolors.GREEN + posts
		elif '"edge_owner_to_timeline_media":{"count":' in userdata[0][44]:
			posts = userdata[0][44].replace('"edge_owner_to_timeline_media":{"count":', '').replace('}','')
			print bcolors.RED + ' Posts: ' + bcolors.GREEN + posts
		elif '"edge_owner_to_timeline_media":{"count":' in userdata[0][45]:
			posts = userdata[0][45].replace('"edge_owner_to_timeline_media":{"count":', '').replace('}','')
			print bcolors.RED + ' Posts: ' + bcolors.GREEN + posts
		elif '"edge_owner_to_timeline_media":{"count":' in userdata[0][46]:
			posts = userdata[0][46].replace('"edge_owner_to_timeline_media":{"count":', '').replace('}','')
			print bcolors.RED + ' Posts: ' + bcolors.GREEN + posts
		elif '"edge_owner_to_timeline_media":{"count":' in userdata[0][47]:
			posts = userdata[0][47].replace('"edge_owner_to_timeline_media":{"count":', '').replace('}','')
			print bcolors.RED + ' Posts: ' + bcolors.GREEN + posts
		else:
			posts = ' Could not gather data'
			print bcolors.RED + ' Posts: ' + bcolors.GREEN + posts
			
		# Highlights Reel Count
		if '"highlight_reel_count":' in userdata[0][20]:
			highlights = userdata[0][20].replace('"highlight_reel_count":', '').replace('}','')
			print bcolors.RED + ' Highlights: ' + bcolors.GREEN + highlights
		elif '"highlight_reel_count":' in userdata[0][21]:
			highlights = userdata[0][21].replace('"highlight_reel_count":', '').replace('}','')
			print bcolors.RED + ' Highlights: ' + bcolors.GREEN + highlights
		elif '"highlight_reel_count":' in userdata[0][22]:
			highlights = userdata[0][22].replace('"highlight_reel_count":', '').replace('}','')
			print bcolors.RED + ' Highlights: ' + bcolors.GREEN + highlights
		elif '"highlight_reel_count":' in userdata[0][23]:
			highlights = userdata[0][23].replace('"highlight_reel_count":', '').replace('}','')
			print bcolors.RED + ' Highlights: ' + bcolors.GREEN + highlights
		elif '"highlight_reel_count":' in userdata[0][24]:
			highlights = userdata[0][24].replace('"highlight_reel_count":', '').replace('}','')
			print bcolors.RED + ' Highlights: ' + bcolors.GREEN + highlights
		elif '"highlight_reel_count":' in userdata[0][25]:
			highlights = userdata[0][25].replace('"highlight_reel_count":', '').replace('}','')
			print bcolors.RED + ' Highlights: ' + bcolors.GREEN + highlights
		elif '"highlight_reel_count":' in userdata[0][26]:
			highlights = userdata[0][26].replace('"highlight_reel_count":', '').replace('}','')
			print bcolors.RED + ' Highlights: ' + bcolors.GREEN + highlights
		else:
			highlights = ' Could not gather data'
			print bcolors.RED + ' Highlights: ' + bcolors.GREEN + highlights
		
		#Video Count
		if '"edge_felix_video_timeline":{"count":' in userdata[0][37]:
			videos = userdata[0][37].replace('"edge_felix_video_timeline":{"count":', '').replace('}','')
			print bcolors.RED + ' Videos: ' + bcolors.GREEN + videos
		elif '"edge_felix_video_timeline":{"count":' in userdata[0][38]:
			videos = userdata[0][38].replace('"edge_felix_video_timeline":{"count":', '').replace('}','')
			print bcolors.RED + ' Videos: ' + bcolors.GREEN + videos
		elif '"edge_felix_video_timeline":{"count":' in userdata[0][39]:
			videos = userdata[0][39].replace('"edge_felix_video_timeline":{"count":', '').replace('}','')
			print bcolors.RED + ' Videos: ' + bcolors.GREEN + videos
		elif '"edge_felix_video_timeline":{"count":' in userdata[0][40]:
			videos = userdata[0][40].replace('"edge_felix_video_timeline":{"count":', '').replace('}','')
			print bcolors.RED + ' Videos: ' + bcolors.GREEN + videos
		elif '"edge_felix_video_timeline":{"count":' in userdata[0][41]:
			videos = userdata[0][41].replace('"edge_felix_video_timeline":{"count":', '').replace('}','')
			print bcolors.RED + ' Videos: ' + bcolors.GREEN + videos
		elif '"edge_felix_video_timeline":{"count":' in userdata[0][42]:
			videos = userdata[0][42].replace('"edge_felix_video_timeline":{"count":', '').replace('}','')
			print bcolors.RED + ' Videos: ' + bcolors.GREEN + videos
		elif '"edge_felix_video_timeline":{"count":' in userdata[0][43]:
			videos = userdata[0][43].replace('"edge_felix_video_timeline":{"count":', '').replace('}','')
			print bcolors.RED + ' Videos: ' + bcolors.GREEN + videos
		else:
			videos = ' Could not gather data'
			print bcolors.RED + ' Videos: ' + bcolors.GREEN + videos

		# Account Private/Public
		if '"is_private":' in userdata[0][28]:
			isPrivate = userdata[0][28].replace('"is_private":', '').replace('}','')
			print bcolors.RED + ' Private Account: ' + bcolors.GREEN + isPrivate
		elif '"is_private":' in userdata[0][29]:
			isPrivate = userdata[0][29].replace('"is_private":', '').replace('}','')
			print bcolors.RED + ' Private Account: ' + bcolors.GREEN + isPrivate
		elif '"is_private":' in userdata[0][30]:
			isPrivate = userdata[0][30].replace('"is_private":', '').replace('}','')
			print bcolors.RED + ' Private Account: ' + bcolors.GREEN + isPrivate
		elif '"is_private":' in userdata[0][31]:
			isPrivate = userdata[0][31].replace('"is_private":', '').replace('}','')
			print bcolors.RED + ' Private Account: ' + bcolors.GREEN + isPrivate
		elif '"is_private":' in userdata[0][32]:
			isPrivate = userdata[0][32].replace('"is_private":', '').replace('}','')
			print bcolors.RED + ' Private Account: ' + bcolors.GREEN + isPrivate
		elif '"is_private":' in userdata[0][33]:
			isPrivate = userdata[0][33].replace('"is_private":', '').replace('}','')
			print bcolors.RED + ' Private Account: ' + bcolors.GREEN + isPrivate
		elif '"is_private":' in userdata[0][34]:
			isPrivate = userdata[0][34].replace('"is_private":', '').replace('}','')
			print bcolors.RED + ' Private Account: ' + bcolors.GREEN + isPrivate
		else:
			isPrivate = ' Could not gather data'
			print bcolors.RED + ' Private Account: ' + bcolors.GREEN + isPrivate

		# Account Verified
		if '"is_verified":' in userdata[0][29]:
			isVerified = userdata[0][29].replace('"is_verified":', '').replace('}','')
			print bcolors.RED + ' Verified Account: ' + bcolors.GREEN + isVerified
		elif '"is_verified":' in userdata[0][30]:
			isVerified = userdata[0][30].replace('"is_verified":', '').replace('}','')
			print bcolors.RED + ' Verified Account: ' + bcolors.GREEN + isVerified
		elif '"is_verified":' in userdata[0][31]:
			isVerified = userdata[0][31].replace('"is_verified":', '').replace('}','')
			print bcolors.RED + ' Verified Account: ' + bcolors.GREEN + isVerified
		elif '"is_verified":' in userdata[0][32]:
			isVerified = userdata[0][32].replace('"is_verified":', '').replace('}','')
			print bcolors.RED + ' Verified Account: ' + bcolors.GREEN + isVerified
		elif '"is_verified":' in userdata[0][33]:
			isVerified = userdata[0][33].replace('"is_verified":', '').replace('}','')
			print bcolors.RED + ' Verified Account: ' + bcolors.GREEN + isVerified
		elif '"is_verified":' in userdata[0][34]:
			isVerified = userdata[0][34].replace('"is_verified":', '').replace('}','')
			print bcolors.RED + ' Verified Account: ' + bcolors.GREEN + isVerified
		elif '"is_verified":' in userdata[0][35]:
			isVerified = userdata[0][35].replace('"is_verified":', '').replace('}','')
			print bcolors.RED + ' Verified Account: ' + bcolors.GREEN + isVerified
		else:
			isVerified = ' Could not gather data'
			print bcolors.RED + ' Verified Account: ' + bcolors.GREEN + isVerified
		
		# Connected to Facebook Account
		if '"connected_fb_page":' in userdata[0][36]:
			fbConnected = userdata[0][36].replace('"connected_fb_page":', '').replace('}','')
			if 'null' in fbConnected:
				fbConnected = 'false'
				print bcolors.RED + ' Connected to Facebook Account: ' + bcolors.GREEN + fbConnected
		elif '"connected_fb_page":' in userdata[0][37]:
			fbConnected = userdata[0][37].replace('"connected_fb_page":', '').replace('}','')
			if 'null' in fbConnected:
				fbConnected = 'false'
				print bcolors.RED + ' Connected to Facebook Account: ' + bcolors.GREEN + fbConnected
		elif '"connected_fb_page":' in userdata[0][38]:
			fbConnected = userdata[0][38].replace('"connected_fb_page":', '').replace('}','')
			if 'null' in fbConnected:
				fbConnected = 'false'
				print bcolors.RED + ' Connected to Facebook Account: ' + bcolors.GREEN + fbConnected
		elif '"connected_fb_page":' in userdata[0][39]:
			fbConnected = userdata[0][39].replace('"connected_fb_page":', '').replace('}','')
			if 'null' in fbConnected:
				fbConnected = 'false'
				print bcolors.RED + ' Connected to Facebook Account: ' + bcolors.GREEN + fbConnected
		elif '"connected_fb_page":' in userdata[0][40]:
			fbConnected = userdata[0][40].replace('"connected_fb_page":', '').replace('}','')
			if 'null' in fbConnected:
				fbConnected = 'false'
				print bcolors.RED + ' Connected to Facebook Account: ' + bcolors.GREEN + fbConnected
		elif '"connected_fb_page":' in userdata[0][41]:
			fbConnected = userdata[0][41].replace('"connected_fb_page":', '').replace('}','')
			if 'null' in fbConnected:
				fbConnected = 'false'
				print bcolors.RED + ' Connected to Facebook Account: ' + bcolors.GREEN + fbConnected
		elif '"connected_fb_page":' in userdata[0][42]:
			fbConnected = userdata[0][42].replace('"connected_fb_page":', '').replace('}','')
			if 'null' in fbConnected:
				fbConnected = 'false'
				print bcolors.RED + ' Connected to Facebook Account: ' + bcolors.GREEN + fbConnected
		else:
			fbConnected = ' Could not gather data'
			print bcolors.RED + ' Connected to Facebook Account: ' + bcolors.GREEN + fbConnected
		
		
		### Post 1
		print bcolors.BLUE + '\n Post 1:' + bcolors.GREEN		
		# Post 1 ID
		if '"id":"' in userdata[0][45]:
			post1_id = userdata[0][45].replace('"id":"', '').replace('"','')
			print bcolors.RED + ' Post ID: ' + bcolors.GREEN + post1_id
		elif '"id":"' in userdata[0][46]:
			post1_id = userdata[0][46].replace('"id":"', '').replace('"','')
			print bcolors.RED + ' Post ID: ' + bcolors.GREEN + post1_id
		elif '"id":"' in userdata[0][47]:
			post1_id = userdata[0][47].replace('"id":"', '').replace('"','')
			print bcolors.RED + ' Post ID: ' + bcolors.GREEN + post1_id
		elif '"id":"' in userdata[0][48]:
			post1_id = userdata[0][48].replace('"id":"', '').replace('"','')
			print bcolors.RED + ' Post ID: ' + bcolors.GREEN + post1_id
		elif '"id":"' in userdata[0][49]:
			post1_id = userdata[0][49].replace('"id":"', '').replace('"','')
			print bcolors.RED + ' Post ID: ' + bcolors.GREEN + post1_id
		elif '"id":"' in userdata[0][50]:
			post1_id = userdata[0][50].replace('"id":"', '').replace('"','')
			print bcolors.RED + ' Post ID: ' + bcolors.GREEN + post1_id
		elif '"id":"' in userdata[0][51]:
			post1_id = userdata[0][51].replace('"id":"', '').replace('"','')
			print bcolors.RED + ' Post ID: ' + bcolors.GREEN + post1_id
		else:
			post1_id = ' Could not gather data'
			print bcolors.RED + ' Post ID: ' + bcolors.GREEN + post1_id

		# Post 1 Owner ID
		if '"owner":{"id":"' in userdata[0][54]:
			post1_owner_id = userdata[0][54].replace('"owner":{"id":"', '').replace('"','')
			print bcolors.RED + ' Owner ID: ' + bcolors.GREEN + post1_owner_id
		elif '"owner":{"id":"' in userdata[0][55]:
			post1_owner_id = userdata[0][55].replace('"owner":{"id":"', '').replace('"','')
			print bcolors.RED + ' Owner ID: ' + bcolors.GREEN + post1_owner_id
		elif '"owner":{"id":"' in userdata[0][56]:
			post1_owner_id = userdata[0][56].replace('"owner":{"id":"', '').replace('"','')
			print bcolors.RED + ' Owner ID: ' + bcolors.GREEN + post1_owner_id
		elif '"owner":{"id":"' in userdata[0][57]:
			post1_owner_id = userdata[0][57].replace('"owner":{"id":"', '').replace('"','')
			print bcolors.RED + ' Owner ID: ' + bcolors.GREEN + post1_owner_id
		elif '"owner":{"id":"' in userdata[0][58]:
			post1_owner_id = userdata[0][58].replace('"owner":{"id":"', '').replace('"','')
			print bcolors.RED + ' Owner ID: ' + bcolors.GREEN + post1_owner_id
		elif '"owner":{"id":"' in userdata[0][59]:
			post1_owner_id = userdata[0][59].replace('"owner":{"id":"', '').replace('"','')
			print bcolors.RED + ' Owner ID: ' + bcolors.GREEN + post1_owner_id
		elif '"owner":{"id":"' in userdata[0][60]:
			post1_owner_id = userdata[0][60].replace('"owner":{"id":"', '').replace('"','')
			print bcolors.RED + ' Owner ID: ' + bcolors.GREEN + post1_owner_id
		else:
			post1_owner_id = ' Could not gather data'
			print bcolors.RED + ' Owner ID: ' + bcolors.GREEN + post1_owner_id
			
		# Post 1 Timestamp
		if '"taken_at_timestamp":' in userdata[0][62]:
			post1_timestamp = userdata[0][62].replace('"taken_at_timestamp":', '')
			print bcolors.RED + ' Timestamp: ' + bcolors.GREEN + post1_timestamp
		elif '"taken_at_timestamp":' in userdata[0][63]:
			post1_timestamp = userdata[0][63].replace('"taken_at_timestamp":', '')
			print bcolors.RED + ' Timestamp: ' + bcolors.GREEN + post1_timestamp
		elif '"taken_at_timestamp":' in userdata[0][64]:
			post1_timestamp = userdata[0][64].replace('"taken_at_timestamp":', '')
			print bcolors.RED + ' Timestamp: ' + bcolors.GREEN + post1_timestamp
		elif '"taken_at_timestamp":' in userdata[0][65]:
			post1_timestamp = userdata[0][65].replace('"taken_at_timestamp":', '')
			print bcolors.RED + ' Timestamp: ' + bcolors.GREEN + post1_timestamp
		elif '"taken_at_timestamp":' in userdata[0][66]:
			post1_timestamp = userdata[0][66].replace('"taken_at_timestamp":', '')
			print bcolors.RED + ' Timestamp: ' + bcolors.GREEN + post1_timestamp
		elif '"taken_at_timestamp":' in userdata[0][67]:
			post1_timestamp = userdata[0][67].replace('"taken_at_timestamp":', '')
			print bcolors.RED + ' Timestamp: ' + bcolors.GREEN + post1_timestamp
		elif '"taken_at_timestamp":' in userdata[0][68]:
			post1_timestamp = userdata[0][68].replace('"taken_at_timestamp":', '')
			print bcolors.RED + ' Timestamp: ' + bcolors.GREEN + post1_timestamp
		else:
			post1_timestamp = ' Could not gather data'
			print bcolors.RED + ' Timestamp: ' + bcolors.GREEN + post1_timestamp
			
		# Post 1 is Video
		if '"is_video":' in userdata[0][56]:
			post1_isVideo = userdata[0][56].replace('"is_video":', '')
			print bcolors.RED + ' Is Video: ' + bcolors.GREEN + post1_isVideo
		elif '"is_video":' in userdata[0][57]:
			post1_isVideo = userdata[0][57].replace('"is_video":', '')
			print bcolors.RED + ' Is Video: ' + bcolors.GREEN + post1_isVideo
		elif '"is_video":' in userdata[0][58]:
			post1_isVideo = userdata[0][58].replace('"is_video":', '')
			print bcolors.RED + ' Is Video: ' + bcolors.GREEN + post1_isVideo
		elif '"is_video":' in userdata[0][59]:
			post1_isVideo = userdata[0][59].replace('"is_video":', '')
			print bcolors.RED + ' Is Video: ' + bcolors.GREEN + post1_isVideo
		elif '"is_video":' in userdata[0][60]:
			post1_isVideo = userdata[0][60].replace('"is_video":', '')
			print bcolors.RED + ' Is Video: ' + bcolors.GREEN + post1_isVideo
		elif '"is_video":' in userdata[0][61]:
			post1_isVideo = userdata[0][61].replace('"is_video":', '')
			print bcolors.RED + ' Is Video: ' + bcolors.GREEN + post1_isVideo
		elif '"is_video":' in userdata[0][62]:
			post1_isVideo = userdata[0][62].replace('"is_video":', '')
			print bcolors.RED + ' Is Video: ' + bcolors.GREEN + post1_isVideo
			
		else:
			post1_isVideo = ' Could not gather data'
			print bcolors.RED + ' Is Video: ' + bcolors.GREEN + post1_isVideo
		
		# Post 1 Accessibility Caption
		if '"accessibility_caption":"' in userdata[0][56]:
			accessibility_caption_1st = userdata[0][56].replace('"accessibility_caption":"', '').replace('"', '')
			accessibility_caption_2nd = userdata[0][57].replace('"', '') 
			accessibility_caption = accessibility_caption_1st + accessibility_caption_2nd
			print bcolors.RED + ' Accessibility Caption: ' + bcolors.GREEN + accessibility_caption
		elif '"accessibility_caption":"' in userdata[0][58]:
			accessibility_caption_1st = userdata[0][58].replace('"accessibility_caption":"', '').replace('"', '')
			accessibility_caption_2nd = userdata[0][59].replace('"', '') 
			accessibility_caption = accessibility_caption_1st + accessibility_caption_2nd
			print bcolors.RED + ' Accessibility Caption: ' + bcolors.GREEN + accessibility_caption
		elif '"accessibility_caption":"' in userdata[0][59]:
			accessibility_caption_1st = userdata[0][59].replace('"accessibility_caption":"', '').replace('"', '')
			accessibility_caption_2nd = userdata[0][60].replace('"', '') 
			accessibility_caption = accessibility_caption_1st + accessibility_caption_2nd
			print bcolors.RED + ' Accessibility Caption: ' + bcolors.GREEN + accessibility_caption
		elif '"accessibility_caption":"' in userdata[0][60]:
			accessibility_caption_1st = userdata[0][60].replace('"accessibility_caption":"', '').replace('"', '')
			accessibility_caption_2nd = userdata[0][61].replace('"', '') 
			accessibility_caption = accessibility_caption_1st + accessibility_caption_2nd
			print bcolors.RED + ' Accessibility Caption: ' + bcolors.GREEN + accessibility_caption
		elif '"accessibility_caption":"' in userdata[0][61]:
			accessibility_caption_1st = userdata[0][61].replace('"accessibility_caption":"', '').replace('"', '')
			accessibility_caption_2nd = userdata[0][62].replace('"', '') 
			accessibility_caption = accessibility_caption_1st + accessibility_caption_2nd
			print bcolors.RED + ' Accessibility Caption: ' + bcolors.GREEN + accessibility_caption
		elif '"accessibility_caption":"' in userdata[0][62]:
			accessibility_caption_1st = userdata[0][62].replace('"accessibility_caption":"', '').replace('"', '')
			accessibility_caption_2nd = userdata[0][63].replace('"', '') 
			accessibility_caption = accessibility_caption_1st + accessibility_caption_2nd
			print bcolors.RED + ' Accessibility Caption: ' + bcolors.GREEN + accessibility_caption
		elif '"accessibility_caption":"' in userdata[0][63]:
			accessibility_caption_1st = userdata[0][63].replace('"accessibility_caption":"', '').replace('"', '')
			accessibility_caption_2nd = userdata[0][64].replace('"', '') 
			accessibility_caption = accessibility_caption_1st + accessibility_caption_2nd
			print bcolors.RED + ' Accessibility Caption: ' + bcolors.GREEN + accessibility_caption
		else:
			accessibility_caption = ' Could not gather data. Possibly a Video.'
			print bcolors.RED + ' Accessibility Caption:' + bcolors.GREEN + accessibility_caption
			
		# Post 1 User Caption
		if '"edge_media_to_caption":{"edges":[{"node":{"text":"' in userdata[0][59]:
			post1_user_caption = userdata[0][59].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}', '')
			print bcolors.RED + ' User Caption: ' + bcolors.GREEN + post1_user_caption
		elif '"edge_media_to_caption":{"edges":[{"node":{"text":"' in userdata[0][60]:
			post1_user_caption = userdata[0][60].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}', '')
			print bcolors.RED + ' User Caption: ' + bcolors.GREEN + post1_user_caption
		elif '"edge_media_to_caption":{"edges":[{"node":{"text":"' in userdata[0][61]:
			post1_user_caption = userdata[0][61].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}', '')
			print bcolors.RED + ' User Caption: ' + bcolors.GREEN + post1_user_caption
		elif '"edge_media_to_caption":{"edges":[{"node":{"text":"' in userdata[0][62]:
			post1_user_caption = userdata[0][62].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}', '')
			print bcolors.RED + ' User Caption: ' + bcolors.GREEN + post1_user_caption
		elif '"edge_media_to_caption":{"edges":[{"node":{"text":"' in userdata[0][63]:
			post1_user_caption = userdata[0][63].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}', '')
			print bcolors.RED + ' User Caption: ' + bcolors.GREEN + post1_user_caption
		elif '"edge_media_to_caption":{"edges":[{"node":{"text":"' in userdata[0][64]:
			post1_user_caption = userdata[0][64].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}', '')
			print bcolors.RED + ' User Caption: ' + bcolors.GREEN + post1_user_caption
		elif '"edge_media_to_caption":{"edges":[{"node":{"text":"' in userdata[0][65]:
			post1_user_caption = userdata[0][65].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}', '')
			print bcolors.RED + ' User Caption: ' + bcolors.GREEN + post1_user_caption
		else:
			post1_user_caption = ' Could not gather data'
			print bcolors.RED + ' User Caption: ' + bcolors.GREEN + post1_user_caption
		
		# Post 1 Comments
		if '"edge_media_to_comment":{"count":' in userdata[0][59]:
			post1_comments = userdata[0][59].replace('"edge_media_to_comment":{"count":', '').replace('}', '')
			print bcolors.RED + ' Comments: ' + bcolors.GREEN + post1_comments
		elif '"edge_media_to_comment":{"count":' in userdata[0][60]:
			post1_comments = userdata[0][60].replace('"edge_media_to_comment":{"count":', '').replace('}', '')
			print bcolors.RED + ' Comments: ' + bcolors.GREEN + post1_comments
		elif '"edge_media_to_comment":{"count":' in userdata[0][61]:
			post1_comments = userdata[0][61].replace('"edge_media_to_comment":{"count":', '').replace('}', '')
			print bcolors.RED + ' Comments: ' + bcolors.GREEN + post1_comments
		elif '"edge_media_to_comment":{"count":' in userdata[0][62]:
			post1_comments = userdata[0][62].replace('"edge_media_to_comment":{"count":', '').replace('}', '')
			print bcolors.RED + ' Comments: ' + bcolors.GREEN + post1_comments
		elif '"edge_media_to_comment":{"count":' in userdata[0][63]:
			post1_comments = userdata[0][63].replace('"edge_media_to_comment":{"count":', '').replace('}', '')
			print bcolors.RED + ' Comments: ' + bcolors.GREEN + post1_comments
		elif '"edge_media_to_comment":{"count":' in userdata[0][64]:
			post1_comments = userdata[0][64].replace('"edge_media_to_comment":{"count":', '').replace('}', '')
			print bcolors.RED + ' Comments: ' + bcolors.GREEN + post1_comments
		elif '"edge_media_to_comment":{"count":' in userdata[0][65]:
			post1_comments = userdata[0][65].replace('"edge_media_to_comment":{"count":', '').replace('}', '')
			print bcolors.RED + ' Comments: ' + bcolors.GREEN + post1_comments
		else:
			post1_comments = ' Could not gather data'
			print bcolors.RED + ' Comments: ' + bcolors.GREEN + post1_comments

		# Post 1 Comments Disabled
		if '"comments_disabled":' in userdata[0][61]:
			post1_comments_disabled = userdata[0][61].replace('"comments_disabled":', '')
			print bcolors.RED + ' Comments Disabled: ' + bcolors.GREEN + post1_comments_disabled
		elif '"comments_disabled":' in userdata[0][62]:
			post1_comments_disabled = userdata[0][62].replace('"comments_disabled":', '')
			print bcolors.RED + ' Comments Disabled: ' + bcolors.GREEN + post1_comments_disabled
		elif '"comments_disabled":' in userdata[0][63]:
			post1_comments_disabled = userdata[0][63].replace('"comments_disabled":', '')
			print bcolors.RED + ' Comments Disabled: ' + bcolors.GREEN + post1_comments_disabled
		elif '"comments_disabled":' in userdata[0][64]:
			post1_comments_disabled = userdata[0][64].replace('"comments_disabled":', '')
			print bcolors.RED + ' Comments Disabled: ' + bcolors.GREEN + post1_comments_disabled
		elif '"comments_disabled":' in userdata[0][65]:
			post1_comments_disabled = userdata[0][65].replace('"comments_disabled":', '')
			print bcolors.RED + ' Comments Disabled: ' + bcolors.GREEN + post1_comments_disabled
		elif '"comments_disabled":' in userdata[0][66]:
			post1_comments_disabled = userdata[0][66].replace('"comments_disabled":', '')
			print bcolors.RED + ' Comments Disabled: ' + bcolors.GREEN + post1_comments_disabled
		elif '"comments_disabled":' in userdata[0][67]:
			post1_comments_disabled = userdata[0][67].replace('"comments_disabled":', '')
			print bcolors.RED + ' Comments Disabled: ' + bcolors.GREEN + post1_comments_disabled
		else:
			post1_comments_disabled = ' Could not gather data'
			print bcolors.RED + ' Comments Disabled: ' + bcolors.GREEN + post1_comments_disabled

		# Post 1 Liked By
		if '"edge_liked_by":{"count":' in userdata[0][63]:
			post1_likedBy = userdata[0][63].replace('"edge_liked_by":{"count":', '').replace('}', '')
			print bcolors.RED + ' Liked By: ' + bcolors.GREEN + post1_likedBy
		elif '"edge_liked_by":{"count":' in userdata[0][64]:
			post1_likedBy = userdata[0][64].replace('"edge_liked_by":{"count":', '').replace('}', '')
			print bcolors.RED + ' Liked By: ' + bcolors.GREEN + post1_likedBy
		elif '"edge_liked_by":{"count":' in userdata[0][65]:
			post1_likedBy = userdata[0][65].replace('"edge_liked_by":{"count":', '').replace('}', '')
			print bcolors.RED + ' Liked By: ' + bcolors.GREEN + post1_likedBy
		elif '"edge_liked_by":{"count":' in userdata[0][66]:
			post1_likedBy = userdata[0][66].replace('"edge_liked_by":{"count":', '').replace('}', '')
			print bcolors.RED + ' Liked By: ' + bcolors.GREEN + post1_likedBy
		elif '"edge_liked_by":{"count":' in userdata[0][67]:
			post1_likedBy = userdata[0][67].replace('"edge_liked_by":{"count":', '').replace('}', '')
			print bcolors.RED + ' Liked By: ' + bcolors.GREEN + post1_likedBy
		elif '"edge_liked_by":{"count":' in userdata[0][68]:
			post1_likedBy = userdata[0][68].replace('"edge_liked_by":{"count":', '').replace('}', '')
			print bcolors.RED + ' Liked By: ' + bcolors.GREEN + post1_likedBy
		elif '"edge_liked_by":{"count":' in userdata[0][69]:
			post1_likedBy = userdata[0][69].replace('"edge_liked_by":{"count":', '').replace('}', '')
			print bcolors.RED + ' Liked By: ' + bcolors.GREEN + post1_likedBy
		else:
			post1_likedBy = ' Could not gather data'
			print bcolors.RED + ' Liked By: ' + bcolors.GREEN + post1_likedBy
			
		# Post 1 Location
		if '"location":' in userdata[0][65]:
			post1_location = userdata[0][65].replace('"location":', '')
			if post1_location == 'null':
				post1_location_null = 'No location data'				
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post1_location_null
			else:
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post1_location

		elif '"location":' in userdata[0][66]:
			post1_location = userdata[0][66].replace('"location":', '')
			if post1_location == 'null':
				post1_location_null = 'No location data'				
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post1_location_null
			else:
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post1_location

		elif '"location":' in userdata[0][67]:
			post1_location = userdata[0][67].replace('"location":', '')
			if post1_location == 'null':
				post1_location_null = 'No location data'				
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post1_location_null
			else:
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post1_location

		elif '"location":' in userdata[0][68]:
			post1_location = userdata[0][68].replace('"location":', '')
			if post1_location == 'null':
				post1_location_null = 'No location data'				
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post1_location_null
			else:
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post1_location

		elif '"location":' in userdata[0][69]:
			post1_location = userdata[0][69].replace('"location":', '')
			if post1_location == 'null':
				post1_location_null = 'No location data'				
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post1_location_null
			else:
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post1_location

		elif '"location":' in userdata[0][70]:
			post1_location = userdata[0][70].replace('"location":', '')
			if post1_location == 'null':
				post1_location_null = 'No location data'				
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post1_location_null
			else:
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post1_location

		elif '"location":' in userdata[0][71]:
			post1_location = userdata[0][71].replace('"location":', '')
			if post1_location == 'null':
				post1_location_null = 'No location data'				
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post1_location_null
			else:
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post1_location
		else:
			post1_location = 'Could not gather data'
			print bcolors.RED + ' Location: ' + bcolors.GREEN + post1_location

		### Post 2
		print bcolors.BLUE + '\n Post 2:' + bcolors.GREEN
		# Post 2 ID
		if '"id":"' in userdata[0][83]:
			post2_id = userdata[0][83].replace('"id":"', '').replace('"','')
			print bcolors.RED + ' Post ID: ' + bcolors.GREEN + post2_id
		elif '"id":"' in userdata[0][84]:
			post2_id = userdata[0][84].replace('"id":"', '').replace('"','')
			print bcolors.RED + ' Post ID: ' + bcolors.GREEN + post2_id
		elif '"id":"' in userdata[0][85]:
			post2_id = userdata[0][85].replace('"id":"', '').replace('"','')
			print bcolors.RED + ' Post ID: ' + bcolors.GREEN + post2_id
		elif '"id":"' in userdata[0][86]:
			post2_id = userdata[0][86].replace('"id":"', '').replace('"','')
			print bcolors.RED + ' Post ID: ' + bcolors.GREEN + post2_id
		elif '"id":"' in userdata[0][87]:
			post2_id = userdata[0][87].replace('"id":"', '').replace('"','')
			print bcolors.RED + ' Post ID: ' + bcolors.GREEN + post2_id
		elif '"id":"' in userdata[0][88]:
			post2_id = userdata[0][88].replace('"id":"', '').replace('"','')
			print bcolors.RED + ' Post ID: ' + bcolors.GREEN + post2_id
		elif '"id":"' in userdata[0][89]:
			post2_id = userdata[0][89].replace('"id":"', '').replace('"','')
			print bcolors.RED + ' Post ID: ' + bcolors.GREEN + post2_id
		else:
			post2_id = ' Could not gather data'
			print bcolors.RED + ' Post ID: ' + bcolors.GREEN + post2_id
		
		# Post 2 Owner ID
		if '"owner":{"id":"' in userdata[0][92]:
			post2_owner_id = userdata[0][92].replace('"owner":{"id":"', '').replace('"','')
			print bcolors.RED + ' Owner ID: ' + bcolors.GREEN + post2_owner_id
		elif '"owner":{"id":"' in userdata[0][93]:
			post2_owner_id = userdata[0][93].replace('"owner":{"id":"', '').replace('"','')
			print bcolors.RED + ' Owner ID: ' + bcolors.GREEN + post2_owner_id
		elif '"owner":{"id":"' in userdata[0][94]:
			post2_owner_id = userdata[0][94].replace('"owner":{"id":"', '').replace('"','')
			print bcolors.RED + ' Owner ID: ' + bcolors.GREEN + post2_owner_id
		elif '"owner":{"id":"' in userdata[0][95]:
			post2_owner_id = userdata[0][95].replace('"owner":{"id":"', '').replace('"','')
			print bcolors.RED + ' Owner ID: ' + bcolors.GREEN + post2_owner_id
		elif '"owner":{"id":"' in userdata[0][96]:
			post2_owner_id = userdata[0][96].replace('"owner":{"id":"', '').replace('"','')
			print bcolors.RED + ' Owner ID: ' + bcolors.GREEN + post2_owner_id
		elif '"owner":{"id":"' in userdata[0][97]:
			post2_owner_id = userdata[0][97].replace('"owner":{"id":"', '').replace('"','')
			print bcolors.RED + ' Owner ID: ' + bcolors.GREEN + post2_owner_id
		elif '"owner":{"id":"' in userdata[0][98]:
			post2_owner_id = userdata[0][98].replace('"owner":{"id":"', '').replace('"','')
			print bcolors.RED + ' Owner ID: ' + bcolors.GREEN + post2_owner_id
		else:
			post2_owner_id = ' Could not gather data'
			print bcolors.RED + ' Owner ID: ' + bcolors.GREEN + post2_owner_id

		# Post 2 Timestamp
		if '"taken_at_timestamp":' in userdata[0][100]:
			post2_timestamp = userdata[0][100].replace('"taken_at_timestamp":', '')
			print bcolors.RED + ' Timestamp: ' + bcolors.GREEN + post2_timestamp
		elif '"taken_at_timestamp":' in userdata[0][101]:
			post2_timestamp = userdata[0][101].replace('"taken_at_timestamp":', '')
			print bcolors.RED + ' Timestamp: ' + bcolors.GREEN + post2_timestamp
		elif '"taken_at_timestamp":' in userdata[0][102]:
			post2_timestamp = userdata[0][102].replace('"taken_at_timestamp":', '')
			print bcolors.RED + ' Timestamp: ' + bcolors.GREEN + post2_timestamp
		elif '"taken_at_timestamp":' in userdata[0][103]:
			post2_timestamp = userdata[0][103].replace('"taken_at_timestamp":', '')
			print bcolors.RED + ' Timestamp: ' + bcolors.GREEN + post2_timestamp
		elif '"taken_at_timestamp":' in userdata[0][104]:
			post2_timestamp = userdata[0][104].replace('"taken_at_timestamp":', '')
			print bcolors.RED + ' Timestamp: ' + bcolors.GREEN + post2_timestamp
		elif '"taken_at_timestamp":' in userdata[0][105]:
			post2_timestamp = userdata[0][105].replace('"taken_at_timestamp":', '')
			print bcolors.RED + ' Timestamp: ' + bcolors.GREEN + post2_timestamp
		elif '"taken_at_timestamp":' in userdata[0][106]:
			post2_timestamp = userdata[0][106].replace('"taken_at_timestamp":', '')
			print bcolors.RED + ' Timestamp: ' + bcolors.GREEN + post2_timestamp
		else:
			post2_timestamp = ' Could not gather data'
			print bcolors.RED + ' Timestamp: ' + bcolors.GREEN + post2_timestamp
			
		# Post 2 is Video
		if '"is_video":' in userdata[0][94]:
			post2_isVideo = userdata[0][94].replace('"is_video":', '')
			print bcolors.RED + ' Is Video: ' + bcolors.GREEN + post2_isVideo
		elif '"is_video":' in userdata[0][95]:
			post2_isVideo = userdata[0][95].replace('"is_video":', '')
			print bcolors.RED + ' Is Video: ' + bcolors.GREEN + post2_isVideo
		elif '"is_video":' in userdata[0][96]:
			post2_isVideo = userdata[0][96].replace('"is_video":', '')
			print bcolors.RED + ' Is Video: ' + bcolors.GREEN + post2_isVideo
		elif '"is_video":' in userdata[0][97]:
			post2_isVideo = userdata[0][97].replace('"is_video":', '')
			print bcolors.RED + ' Is Video: ' + bcolors.GREEN + post2_isVideo
		elif '"is_video":' in userdata[0][98]:
			post2_isVideo = userdata[0][98].replace('"is_video":', '')
			print bcolors.RED + ' Is Video: ' + bcolors.GREEN + post2_isVideo
		elif '"is_video":' in userdata[0][99]:
			post2_isVideo = userdata[0][99].replace('"is_video":', '')
			print bcolors.RED + ' Is Video: ' + bcolors.GREEN + post2_isVideo
		elif '"is_video":' in userdata[0][100]:
			post2_isVideo = userdata[0][100].replace('"is_video":', '')
			print bcolors.RED + ' Is Video: ' + bcolors.GREEN + post2_isVideo
			
		else:
			post2_isVideo = ' Could not gather data'
			print bcolors.RED + ' Is Video: ' + bcolors.GREEN + post2_isVideo
		
		# Post 2 Accessibility Caption
		if '"accessibility_caption":"' in userdata[0][95]:
			accessibility_caption2_1st = userdata[0][95].replace('"accessibility_caption":"', '').replace('"', '')
			accessibility_caption2_2nd = userdata[0][96].replace('"', '') 
			accessibility_caption2 = accessibility_caption2_1st + accessibility_caption2_2nd
			print bcolors.RED + ' Accessibility Caption: ' + bcolors.GREEN + accessibility_caption2
		elif '"accessibility_caption":"' in userdata[0][96]:
			accessibility_caption2_1st = userdata[0][96].replace('"accessibility_caption":"', '').replace('"', '')
			accessibility_caption2_2nd = userdata[0][97].replace('"', '') 
			accessibility_caption2 = accessibility_caption2_1st + accessibility_caption2_2nd
			print bcolors.RED + ' Accessibility Caption: ' + bcolors.GREEN + accessibility_caption2
		elif '"accessibility_caption":"' in userdata[0][97]:
			accessibility_caption2_1st = userdata[0][97].replace('"accessibility_caption":"', '').replace('"', '')
			accessibility_caption2_2nd = userdata[0][98].replace('"', '') 
			accessibility_caption2 = accessibility_caption2_1st + accessibility_caption2_2nd
			print bcolors.RED + ' Accessibility Caption: ' + bcolors.GREEN + accessibility_caption2
		elif '"accessibility_caption":"' in userdata[0][98]:
			accessibility_caption2_1st = userdata[0][98].replace('"accessibility_caption":"', '').replace('"', '')
			accessibility_caption2_2nd = userdata[0][99].replace('"', '') 
			accessibility_caption2 = accessibility_caption2_1st + accessibility_caption2_2nd
			print bcolors.RED + ' Accessibility Caption: ' + bcolors.GREEN + accessibility_caption2
		elif '"accessibility_caption":"' in userdata[0][99]:
			accessibility_caption2_1st = userdata[0][99].replace('"accessibility_caption":"', '').replace('"', '')
			accessibility_caption2_2nd = userdata[0][100].replace('"', '') 
			accessibility_caption2 = accessibility_caption2_1st + accessibility_caption2_2nd
			print bcolors.RED + ' Accessibility Caption: ' + bcolors.GREEN + accessibility_caption2
		elif '"accessibility_caption":"' in userdata[0][100]:
			accessibility_caption2_1st = userdata[0][100].replace('"accessibility_caption":"', '').replace('"', '')
			accessibility_caption2_2nd = userdata[0][101].replace('"', '') 
			accessibility_caption2 = accessibility_caption2_1st + accessibility_caption2_2nd
			print bcolors.RED + ' Accessibility Caption: ' + bcolors.GREEN + accessibility_caption2
		elif '"accessibility_caption":"' in userdata[0][101]:
			accessibility_caption2_1st = userdata[0][101].replace('"accessibility_caption":"', '').replace('"', '')
			accessibility_caption2_2nd = userdata[0][102].replace('"', '') 
			accessibility_caption2 = accessibility_caption2_1st + accessibility_caption2_2nd
			print bcolors.RED + ' Accessibility Caption: ' + bcolors.GREEN + accessibility_caption2
		else:
			accessibility_caption = ' Could not gather data. Possibly a Video.'
			print bcolors.RED + ' Accessibility Caption:' + bcolors.GREEN + accessibility_caption2

		# Post 2 User Caption
		if '"edge_media_to_caption":{"edges":[{"node":{"text":"' in userdata[0][97]:
			post2_user_caption = userdata[0][97].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}', '')
			print bcolors.RED + ' User Caption: ' + bcolors.GREEN + post2_user_caption
		elif '"edge_media_to_caption":{"edges":[{"node":{"text":"' in userdata[0][98]:
			post2_user_caption = userdata[0][98].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}', '')
			print bcolors.RED + ' User Caption: ' + bcolors.GREEN + post2_user_caption
		elif '"edge_media_to_caption":{"edges":[{"node":{"text":"' in userdata[0][99]:
			post2_user_caption = userdata[0][99].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}', '')
			print bcolors.RED + ' User Caption: ' + bcolors.GREEN + post2_user_caption
		elif '"edge_media_to_caption":{"edges":[{"node":{"text":"' in userdata[0][100]:
			post2_user_caption = userdata[0][100].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}', '')
			print bcolors.RED + ' User Caption: ' + bcolors.GREEN + post2_user_caption
		elif '"edge_media_to_caption":{"edges":[{"node":{"text":"' in userdata[0][101]:
			post2_user_caption = userdata[0][101].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}', '')
			print bcolors.RED + ' User Caption: ' + bcolors.GREEN + post2_user_caption
		elif '"edge_media_to_caption":{"edges":[{"node":{"text":"' in userdata[0][102]:
			post2_user_caption = userdata[0][102].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}', '')
			print bcolors.RED + ' User Caption: ' + bcolors.GREEN + post2_user_caption
		elif '"edge_media_to_caption":{"edges":[{"node":{"text":"' in userdata[0][103]:
			post2_user_caption = userdata[0][103].replace('"edge_media_to_caption":{"edges":[{"node":{"text":"', '').replace('"}}]}', '')
			print bcolors.RED + ' User Caption: ' + bcolors.GREEN + post2_user_caption
		else:
			post2_user_caption = ' Could not gather data'
			print bcolors.RED + ' User Caption: ' + bcolors.GREEN + post2_user_caption

		# Post 2 Comments
		if '"edge_media_to_comment":{"count":' in userdata[0][98]:
			post2_comments = userdata[0][98].replace('"edge_media_to_comment":{"count":', '').replace('}', '')
			print bcolors.RED + ' Comments: ' + bcolors.GREEN + post2_comments
		elif '"edge_media_to_comment":{"count":' in userdata[0][99]:
			post2_comments = userdata[0][99].replace('"edge_media_to_comment":{"count":', '').replace('}', '')
			print bcolors.RED + ' Comments: ' + bcolors.GREEN + post2_comments
		elif '"edge_media_to_comment":{"count":' in userdata[0][100]:
			post2_comments = userdata[0][100].replace('"edge_media_to_comment":{"count":', '').replace('}', '')
			print bcolors.RED + ' Comments: ' + bcolors.GREEN + post2_comments
		elif '"edge_media_to_comment":{"count":' in userdata[0][101]:
			post2_comments = userdata[0][101].replace('"edge_media_to_comment":{"count":', '').replace('}', '')
			print bcolors.RED + ' Comments: ' + bcolors.GREEN + post2_comments
		elif '"edge_media_to_comment":{"count":' in userdata[0][102]:
			post2_comments = userdata[0][102].replace('"edge_media_to_comment":{"count":', '').replace('}', '')
			print bcolors.RED + ' Comments: ' + bcolors.GREEN + post2_comments
		elif '"edge_media_to_comment":{"count":' in userdata[0][103]:
			post2_comments = userdata[0][103].replace('"edge_media_to_comment":{"count":', '').replace('}', '')
			print bcolors.RED + ' Comments: ' + bcolors.GREEN + post2_comments
		elif '"edge_media_to_comment":{"count":' in userdata[0][104]:
			post2_comments = userdata[0][104].replace('"edge_media_to_comment":{"count":', '').replace('}', '')
			print bcolors.RED + ' Comments: ' + bcolors.GREEN + post2_comments
		else:
			post2_comments = ' Could not gather data'
			print bcolors.RED + ' Comments: ' + bcolors.GREEN + post2_comments

		# Post 2 Comments Disabled
		if '"comments_disabled":' in userdata[0][99]:
			post2_comments_disabled = userdata[0][99].replace('"comments_disabled":', '')
			print bcolors.RED + ' Comments Disabled: ' + bcolors.GREEN + post2_comments_disabled
		elif '"comments_disabled":' in userdata[0][100]:
			post2_comments_disabled = userdata[0][100].replace('"comments_disabled":', '')
			print bcolors.RED + ' Comments Disabled: ' + bcolors.GREEN + post2_comments_disabled
		elif '"comments_disabled":' in userdata[0][101]:
			post2_comments_disabled = userdata[0][101].replace('"comments_disabled":', '')
			print bcolors.RED + ' Comments Disabled: ' + bcolors.GREEN + post2_comments_disabled
		elif '"comments_disabled":' in userdata[0][102]:
			post2_comments_disabled = userdata[0][102].replace('"comments_disabled":', '')
			print bcolors.RED + ' Comments Disabled: ' + bcolors.GREEN + post2_comments_disabled
		elif '"comments_disabled":' in userdata[0][103]:
			post2_comments_disabled = userdata[0][103].replace('"comments_disabled":', '')
			print bcolors.RED + ' Comments Disabled: ' + bcolors.GREEN + post2_comments_disabled
		elif '"comments_disabled":' in userdata[0][104]:
			post2_comments_disabled = userdata[0][104].replace('"comments_disabled":', '')
			print bcolors.RED + ' Comments Disabled: ' + bcolors.GREEN + post2_comments_disabled
		elif '"comments_disabled":' in userdata[0][105]:
			post2_comments_disabled = userdata[0][105].replace('"comments_disabled":', '')
			print bcolors.RED + ' Comments Disabled: ' + bcolors.GREEN + post2_comments_disabled
		else:
			post2_comments_disabled = ' Could not gather data'
			print bcolors.RED + ' Comments Disabled: ' + bcolors.GREEN + post2_comments_disabled

		# Post 2 Liked By
		if '"edge_liked_by":{"count":' in userdata[0][101]:
			post2_likedBy = userdata[0][101].replace('"edge_liked_by":{"count":', '').replace('}', '')
			print bcolors.RED + ' Liked By: ' + bcolors.GREEN + post2_likedBy
		elif '"edge_liked_by":{"count":' in userdata[0][102]:
			post2_likedBy = userdata[0][102].replace('"edge_liked_by":{"count":', '').replace('}', '')
			print bcolors.RED + ' Liked By: ' + bcolors.GREEN + post2_likedBy
		elif '"edge_liked_by":{"count":' in userdata[0][103]:
			post2_likedBy = userdata[0][103].replace('"edge_liked_by":{"count":', '').replace('}', '')
			print bcolors.RED + ' Liked By: ' + bcolors.GREEN + post2_likedBy
		elif '"edge_liked_by":{"count":' in userdata[0][104]:
			post2_likedBy = userdata[0][104].replace('"edge_liked_by":{"count":', '').replace('}', '')
			print bcolors.RED + ' Liked By: ' + bcolors.GREEN + post2_likedBy
		elif '"edge_liked_by":{"count":' in userdata[0][105]:
			post2_likedBy = userdata[0][105].replace('"edge_liked_by":{"count":', '').replace('}', '')
			print bcolors.RED + ' Liked By: ' + bcolors.GREEN + post2_likedBy
		elif '"edge_liked_by":{"count":' in userdata[0][106]:
			post2_likedBy = userdata[0][106].replace('"edge_liked_by":{"count":', '').replace('}', '')
			print bcolors.RED + ' Liked By: ' + bcolors.GREEN + post2_likedBy
		elif '"edge_liked_by":{"count":' in userdata[0][107]:
			post2_likedBy = userdata[0][107].replace('"edge_liked_by":{"count":', '').replace('}', '')
			print bcolors.RED + ' Liked By: ' + bcolors.GREEN + post2_likedBy
		else:
			post2_likedBy = ' Could not gather data'
			print bcolors.RED + ' Liked By: ' + bcolors.GREEN + post2_likedBy
			
		# Post 2 Location
		if '"location":' in userdata[0][103]:
			post2_location = userdata[0][103].replace('"location":', '')
			if post2_location == 'null':
				post2_location_null = 'No location data\n'
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post2_location_null
			else:
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post2_location + '\n'

		elif '"location":' in userdata[0][104]:
			post2_location = userdata[0][104].replace('"location":', '')
			if post2_location == 'null':
				post2_location_null = 'No location data\n'				
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post2_location_null
			else:
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post2_location + '\n'

		elif '"location":' in userdata[0][105]:
			post2_location = userdata[0][105].replace('"location":', '')
			if post2_location == 'null':
				post2_location_null = 'No location data\n'
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post2_location_null
			else:
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post2_location + '\n'

		elif '"location":' in userdata[0][106]:
			post2_location = userdata[0][106].replace('"location":', '')
			if post2_location == 'null':
				post2_location_null = 'No location data\n'
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post2_location_null
			else:
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post2_location + '\n'

		elif '"location":' in userdata[0][107]:
			post2_location = userdata[0][107].replace('"location":', '')
			if post2_location == 'null':
				post2_location_null = 'No location data\n'
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post2_location_null
			else:
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post2_location + '\n'

		elif '"location":' in userdata[0][108]:
			post2_location = userdata[0][108].replace('"location":', '')
			if post2_location == 'null':
				post2_location_null = 'No location data\n'				
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post2_location_null
			else:
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post2_location + '\n'

		elif '"location":' in userdata[0][109]:
			post2_location = userdata[0][109].replace('"location":', '')
			if post2_location == 'null':
				post2_location_null = 'No location data\n'				
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post2_location_null
			else:
				print bcolors.RED + ' Location: ' + bcolors.GREEN + post2_location + '\n'
		else:
			post2_location = 'Could not gather data\n'
			print bcolors.RED + ' Location: ' + bcolors.GREEN + post2_location
		
		try:
			cursor.execute("INSERT INTO InstagramUsers (USERTYPE, NAME, DESCRIPTION, PAGETYPE, FOLLOWERS, FOLLOWING, POSTS, HIGHLIGHTS, VIDEOS, ISPRIVATE, ISVERIFIED, FBCONNECTED) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_type, name, description, page_type, followers, following, posts, highlights, videos, isPrivate, isVerified, fbConnected))
			conn.commit()
			print bcolors.RED + ' ' + name + bcolors.GREEN + ' was added to the DB successfully.\n'
				

		except sqlite3.IntegrityError as iError:
			print bcolors.RED + ' ' + ID + bcolors.GREEN + ' Already exists in DB.\n'
			
	else:
		os.system('clear')
		print bcolors.RED + ' Invalid Syntax. Exiting to the main menu.' + bcolors.GREEN
