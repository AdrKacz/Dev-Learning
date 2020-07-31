import requests
from bs4 import BeautifulSoup
from time import time

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
	"""
	Crawler that its made for Yahoo Finance
	"""
	def __init__(self, website):
		self.website = website

	def get_page(self, url):
		try:
			request = requests.get(url)
		except requests.exceptions.RequestException:
			return None
		return BeautifulSoup(request.text, 'html.parser')

	def get_value(self):
		soup = self.get_page(self.website.url)
		quote = soup.select("#quote-header-info")[0]
		section = quote.select("div")
		return float(section[-2].select("span")[0].get_text().replace(",", "."))


website = Website("Yahoo Finance", "https://fr.finance.yahoo.com/quote/EURUSD=X?p=EURUSD=X&.tsrc=fin-srch")

crawler = Crawler(website)

def measure():
	t1 = time()
	print(crawler.get_value())
	return time() - t1