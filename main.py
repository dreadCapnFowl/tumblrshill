# -*- coding: utf-8 -*-
import pytumblr
import time
import threading
import os
import random
import sys
import json

# Credentials from the application page
key = ''
secret = ''
# https://www.tumblr.com/dashboard?oauth_token=w67b7QAbqOUYEt1U8Rp2DsoitZyxOJ47mwmmrlCHTsMAE8L8Vk&oauth_verifier=rm6hxsiTMOdUl4PA5gp18yslPNTbRgyyfL8iJViJadh413cP9O
otoken = ''
osecret = ''

client = pytumblr.TumblrRestClient(
	key,
	secret,
	otoken,
	osecret
)
if 'meta' in client.info():
	s = client.info()['meta']['status']
	if s == 429:
		print("Limit exceeded.")
		sys.exit(0)
"""
tags = [
	'trans',
	'mtf',
	'transgender',
	'lgbt',
	'lgbtq',
	'cute',
	'femboy',
	'chastity',
]
"""
tags = [
	'trans',
	'mtf',
	'transgender',
	'lgbt',
	'lgbtq',
	'cute',
	'femboy',
	'chastity',
	's&m',
	'hrt',
	'sissy',
]
"""
lines = [ 
	'Hi, please join our server',
	'Trappy and comfy serber',
	'All traps welcome',
	'All transgirls welcome',
	'Join our trappy Discord',
	'hewwo pwease join our cyute twap serwer~ ;3'
]
invite = 'EsZHfYt'
"""

def doFollows(client, tags):
	posts = []
	for tag in tags:
		posts += client.tagged(tag)

	l = len(posts)
	print('Tags found {} posts.'.format(l))
	notes = []
	
	for i in range(10):
		post = random.choice(posts)
		print('Followed ', post['blog_name'].encode('utf-8'))
		r = client.follow(post['blog_name'])
		print(r['blog']['description'].encode('utf-8'))
	
	# Reblog random post
	"""
	for i in range(25):
		repost = random.choice(posts)
		blogName = client.info()['user']['blogs'][0]['name']
		client.reblog(blogName, id=repost['id'], reblog_key=repost['reblog_key'], comment=f'💜 {random.choice(lines)} <b>http://discord.gg/{invite}</b> 💜')
		print("Reblogged " + repost['blog_name'])
			#print(str(post).encode('utf-8'))
			#print(post['blog_name'])
			#print(post['blog_name'])
	"""
	"""
	post = random.choice(posts)
	print(post)
	blogName = client.info()
	print(blogName)
	client.reblog(blogName, id=post['id'], reblog_key="reblog_key")
	print(f'{len(notes)} notes found on all posts.')

	# Eliminate duplicates
	notes = {frozenset(note['blog_name']) : note for note in notes}.values()

	f = open('followed.txt', 'r')
	#followed = f.read().split('\n')
	f.close()
	blog_names = []
	for note in notes:
		#if not note['blog_name'] in followed:
		blog_names.append(note['blog_name'])

	for post in posts:
		blog_names.append(post['blog_name'])
		
	blog_names = set(blog_names)
	print(f'{len(blog_names)} individual blog names.')

	#f=open("followed.txt", "a+")
	for name in blog_names:
		r = client.follow(name)
		#f.write(f'{name}\n')
	#f.close()
	"""
def followsLoop(client):
	while True:
		print('Initiating follow routine.')
		doFollows(client, tags)
		print('Waiting...')
		time.sleep(60)
	return
def doPosts(client):
	while True:
		if 'meta' in client.info():
			s = client.info()['meta']['status']
			if s == 429:
				print("Limit exceeded.")
				sys.exit(0)
				
		blogName = client.info()['user']['blogs'][0]['name']
		#client.create_text(blogName, state="published", slug="testing-text-posts", title=f'http://discord.gg/{invite}', body="testing1 2 3 4")
		#print(client.create_link(blogName, title="cutegen", url=f'http://discord.gg/{invite}', description="Join are trans friendly discord server.", tags = ['traps'], data='test.png'))
		fn = 'banners/' + random.choice(os.listdir("banners"))
		r = client.create_photo(blogName, state="published",format='markdown', tags=tags, caption='💜 {random.choice(lines)} **[/cutegen/](http://discord.gg/{invite} "Discord invite http://discord.gg/{invite}")** 💜'.format(invite), data=fn)
		print("Created a blog post.")
		time.sleep(60 * 5)
	return

#doFollows(client, tags)
t_posts = threading.Thread(target = doPosts, args = (client, ))
t_posts.daemon = True
#t_posts.start()

t_follows = threading.Thread(target = followsLoop, args = (client, ))
t_follows.daemon = True
t_follows.start()


while True:
	r = input('> ')
	if r == 'q':
		break;
