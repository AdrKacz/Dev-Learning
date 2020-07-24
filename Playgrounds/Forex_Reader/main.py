import requests
from bs4 import BeautifulSoup

"""
Program that look for currency value (FOREX)
"""

class Website:
	"""
	Useful information and method about the website to crawl
	"""
	def __init__(self, name, url):
		self.name = name
		self.url = url


class Crawler:
	def get_page(self, url):
		try:
			request = requests.get(url)
		except requests.exceptions.RequestException:
			return None
		return BeautifulSoup(request.text, 'html.parser')

	def search(self, website):
		soup = self.get_page(website.url)
		return soup


website = Website("Yahoo Finance", "https://fr.finance.yahoo.com/quote/EURUSD=X?p=EURUSD=X&.tsrc=fin-srch")

crawler = Crawler()

soup = crawler.search(website)