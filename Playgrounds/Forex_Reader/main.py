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

	def get_device_url(self, devise):
		devise = devise.replace("/", "")
		return f"https://fr.finance.yahoo.com/quote/{devise}%3DX?p={devise}%3DX"


class Crawler:
	"""
	Crawler that its made for Yahoo Finance
	"""

	# All in the devises webpage
	_MAJORS = [	"EUR/USD",
				"GBP/USD",
				"USD/JPY",
				"USD/CHF",
				"EUR/JPY",
				"USD/CAD",
				]

	# CAUTION: Only the first two in the devises webpage
	_CROSSES = ["GBP/JPY",
				"EUR/GBP",
				"CAD/JPY",
				"AUD/CAD",
				"EUR/AUD",
				"NZD/JPY",
				]

	def __init__(self, website):
		self.website = website

	def get_page(self, url):
		try:
			request = requests.get(url)
		except requests.exceptions.RequestException:
			return None
		return BeautifulSoup(request.text, 'html.parser')

	def get_value(self, devise):
		soup = self.get_page(self.website.get_device_url(devise))
		quote = soup.select("#quote-header-info")[0]
		section = quote.select("div")
		return float(section[-2].select("span")[0].get_text().replace(",", "."))

	def get_last_values(self, devises_to_check):
		soup = self.get_page(self.website.url)
		items = soup.get_text(separator='_').split(sep='_')
		devises = dict()
		for i in range(len(items)):
			if items[i] in devises_to_check:
				devises[items[i]] = float(items[i+1].replace(",", "."))
		return devises



# website = Website("Yahoo Finance", "https://fr.finance.yahoo.com/quote/EURUSD%3DX?p=EURUSD%3DX")
website = Website("Yahoo Finance", "https://fr.finance.yahoo.com/devisas/")

crawler = Crawler(website)