import time
import requests
from bs4 import BeautifulSoup

WEB_SITE = 'https://www.worldometers.info/coronavirus/country/russia/'
headers = {'User-Agent': 'Mozilla/5.0'}

class Covid():

	def __init__(self):
		self.value = self.check_covid()
		pass

	def print_covid(self):
		print(time.strftime('%I:%M:%S %p'))
		print('Active:', int(self.value[1].text.replace(',', '')))
		print('Deaths:', int(self.value[2].text.replace(',', '')))
		print('Recovered:', int(self.value[3].text.replace(',', '')), end='\n\n')

	def check_covid(self):
		full_page = requests.get(WEB_SITE, headers=headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')

		self.value = soup.findAll('span', {'class': ''})

		return self.value

covid = Covid()
print('Russia')
covid.print_covid()

while True:
	if covid.value != covid.check_covid():
		covid.print_covid()
	time.sleep(5)
	pass
