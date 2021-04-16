import requests
from bs4 import BeautifulSoup
import csv

url = 'https://database.lichess.org'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
r = soup.find_all(class_='right')

t= soup.find_all('table')[8].find_all('tr')

data=[]
for m in range(1, len(t)-1):
	item = t[m]
	i=item.find_all('td')
	date = i[0].text
	sz = i[1].text
	if sz[-2:] == "GB":
		sz = float(sz[0:-3]) * 1000
	elif sz[-2:] == "MB":
		sz = float(sz[0:-3])
	else:
		print("Warning: Unsupported file size: " + sz)
	count = int(i[2].text.replace(",",""))
	data.append([date,sz,count])

data.append(["Date", "Size (MB)", "Count"])
data.reverse()

with open('chess.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(data)
