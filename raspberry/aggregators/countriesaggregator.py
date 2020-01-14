import requests
import json


class CountryAggregator():
	
	api_url = ""
	
	def __init__(self):
		self.api_url = "https://restcountries.eu/rest/v2/"
	

	def get_country_region(self, country):
		r = requests.get(self.api_url+"name/"+country+"?fullText=true&fields=region")
		return json.loads(r.text)[0]["region"]


	def get_all_regions(self):
		r = requests.get(self.api_url+"all?fields=region")
		l = []
		j = json.loads(r.text)
		
		for elem in j:
			if elem["region"] not in l:
				l.append(elem["region"])
		
		return l

	def get_all_subregions(self):
		r = requests.get(self.api_url+"all?fields=subregion")
		l = []
		j = json.loads(r.text)
		
		for elem in j:
			if elem["subregion"] not in l:
				l.append(elem["subregion"])
		
		return l
