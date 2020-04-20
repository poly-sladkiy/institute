import time
import requests
from bs4 import BeautifulSoup

WEB_SITE = 'https://стопкоронавирус.рф'
headers = {'User-Agent': 'Mozilla/5.0'}

class Covid(object):

	value = None

	def __init__(self):
		self.value = self.check_covid()
		pass

	def print_covid(self):
		print(self.value[26].text)
		print('Случаи заболевания:', int(self.value[22].text.replace(' ', '')))
		print('За сутки:', int(self.value[23].text.replace(' ', '')))
		print('Выздоровевшие:', int(self.value[24].text.replace(' ', '')))
		print('Погибло:', int(self.value[25].text.replace(' ', '')), end='\n\n')
		pass

	def check_covid(self):
		full_page = requests.get(WEB_SITE, headers=headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')

		self.value = soup.findAll('span', {'class': ''})

		return self.value

print('Russia:')
covid = Covid()
covid.print_covid()

while True:
	if covid.value != covid.check_covid():
		covid.print_covid()
	time.sleep(5)
	pass
