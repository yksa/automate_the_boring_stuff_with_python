import requests

res = requests.get('https://novelfull.com/against-the-gods/chapter-1721-blood-soaked-eternal-heaven-3.html')

playFile = open('RomeoAndJuliet.html', 'wb')

for chunk in res.iter_content():
	playFile.write(chunk)

playFile.close()