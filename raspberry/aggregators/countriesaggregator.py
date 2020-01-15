import requests
import json


class CountryAggregator():
	
	api_url = ""
	
	def __init__(self):
		self.api_url = "https://restcountries.eu/rest/v2/"
	

	def get_country_region(self, country):
		r = requests.get(self.api_url+"name/"+country+"?fullText=true&fields=region")
		return json.loads(r.text)[0]["region"]
		
	def format_region_for_gpio(self, region_to_format, subregion):
		if region_to_format in ["Europe", "Africa", "Oceania", "Polar", ""]:
			return region_to_format
		else:
			if region_to_format in ["Americas"]:
				if "Northern" in subregion or "Caribbean" in subregion:
					return "Northern America"
				else:
					return "South America"
			elif region_to_format in ["Asia"]:
				if "Western" in subregion or "Central" in subregion:
					return "Western Asia"
				else:
					return "Eastern Asia"
			else: return ""

	def get_country_region_for_gpio(self, country):
		r = requests.get(self.api_url+"name/"+country+"?fullText=true&fields=region;subregion")
		region_to_format = json.loads(r.text)[0]["region"]
		subregion = json.loads(r.text)[0]["subregion"]
		
		return self.format_region_for_gpio(region_to_format, subregion)


	def get_all_regions(self):
		r = requests.get(self.api_url+"all?fields=region")
		j = json.loads(r.text)
		l = []
		
		for elem in j:
			if elem["region"] not in l:
				l.append(elem["region"])
		
		return l

	def get_all_subregions(self):
		r = requests.get(self.api_url+"all?fields=subregion")
		j = json.loads(r.text)
		l = []
		
		for elem in j:
			if elem["subregion"] not in l:
				l.append(elem["subregion"])
		
		return l
		
	def get_all_regions_and_subregions(self):
		r = requests.get(self.api_url+"all?fields=subregion;region")
		j = json.loads(r.text)
		res = {}
		
		for elem in j:
			if elem["region"] not in res:
				res[elem["region"]] = []
			if  elem["subregion"] not in res[elem["region"]]:
				res[elem["region"]].append(elem["subregion"])

		return res

		
	def get_all_regions_and_subregions_for_gpio(self):
		r = requests.get(self.api_url+"all?fields=subregion;region")
		j = json.loads(r.text)
		res = {}
		
		for elem in j:
			elem["region"] = self.format_region_for_gpio(elem["region"], elem["subregion"])
			if elem["region"] not in res:
				res[elem["region"]] = []
			if  elem["subregion"] not in res[elem["region"]]:
				res[elem["region"]].append(elem["subregion"])

		return res

		
	def get_all_regions_for_gpio(self):
		r = requests.get(self.api_url+"all?fields=subregion;region")
		j = json.loads(r.text)
		res = []
		
		for elem in j:
			elem["region"] = self.format_region_for_gpio(elem["region"], elem["subregion"])
			if elem["region"] not in res:
				res.append(elem["region"])
			

		return res
		


