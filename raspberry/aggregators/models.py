import feedparser
import json
import requests
import os

def path():
	return str(os.path.abspath(__file__))


'''
	RssEntry and RssAgregator are used to get RSSdata from rss source passed in contructor parameter.
	Then to parse it into json and to filter needed data
'''

class RssEntry():
	
	data = {}
	
	def __init__(self, data):
		print("Starting: "+path()+"/RssEntry/__init__")
		self.data = data
		print("Ending: "+path()+"/RssEntry/__init__")

	def __str__(self):
		return json.dumps(self.data, indent=4)

class RssAggregator():
	
	# list of entries in xml file
	entries = [] 
	
	# data parsed for our purpose
	data = {} 
	
	# data parsed by feedparser lib (check it with an online json parser)
	thefeed = {} 

	def __init__(self, paramrssurl, verbose=False):
		print("Starting: "+path()+"/RssAggregator/__init__")
		print("Used url: " + paramrssurl)
		print("")
		
		self.entries = []
		self.data = {}
		self.data["feedurl"] = paramrssurl
		self.parse(verbose)
		
		# if verbose: print(self.thefeed)
		print("Ending: "+path()+"/RssAggregator/__init__")
		

	def parse(self, verbose=False):
		print("Starting: "+path()+"/RssAggregator/parse")
		self.thefeed = feedparser.parse(self.data["feedurl"])
		
		thefeed = self.thefeed
		feed = thefeed.feed

		print("Getting Feed Data")
		
		#add selected data here
		self.data["title"] = feed.get("title", "")
		self.data["subtitle"] = feed.get("subtitle", "")
		self.data["link"] = feed.get("link", "")
		self.data["description"] = feed.get("description", "")
		self.data["published"] = feed.get("published", "")
		self.data["author"] = feed.get("author", "")
		
		if verbose: print (json.dumps(self.data, indent=4))
		
		entries_count = 0

		for entry in thefeed.entries:
			entry_data = {}
			
			#add selected data here
			entry_data["guid"] = entry.get("guid", "")
			entry_data["title"] = entry.get("title", "")
			entry_data["link"] = entry.get("link", "")
			entry_data["description"] = entry.get("description", "")
			entry_data["links"] = entry.get("links", "")
			entry_data["geo_lat"] = entry.get("geo_lat", "")
			entry_data["geo_long"] = entry.get("geo_long", "")
			entry_data["gdacs_country"] = entry.get("gdacs_country", [])
			entry_data["gdacs_iscurrent"] = entry.get("gdacs_iscurrent", "")
			entry_data["gdacs_durationinweek"] = entry.get("gdacs_durationinweek", "")
			entry_data["gdacs_icon"] = entry.get("gdacs_icon", "")
			entry_data["gdacs_severity"] = entry.get("gdacs_severity", "")
			entry_data["gdacs_population"] = entry.get("gdacs_population", "")
			entry_data["gdacs_alertlevel"] = entry.get("gdacs_alertlevel", "")
			entry_data["gdacs_alertscore"] = entry.get("gdacs_alertscore", "")
			
			
			self.entries.append(RssEntry(entry_data))
			entries_count += 1
		
		
		self.data["entries_count"] = entries_count
			
		print("Ending: "+path()+"/RssAggregator/parse")
		
	def get_dict(self):
		return self.data
		
	def get_entries_dict(self):
		print("Starting: "+path()+"/RssAggregator/get_entries_dict")
		entries_json = []
		for entry in self.entries:
			entries_json.append(entry.data)
		print("Ending: "+path()+"/RssAggregator/get_entries_dict")
		return entries_json
	
	def get_all_data_dict(self):
		print("Starting: "+path()+"/RssAggregator/get_all_data_dict")
		data = self.data
		data["entries"] = self.get_entries_dict()
		print("Ending: "+path()+"/RssAggregator/get_all_data_dict")
		return data

	def __str__(self):
		return "Data: \n" + json.dumps(self.data, indent=4) + "\n\nEntries: \n" + json.dumps(self.get_entries_dict(), indent=4)




'''
	Country Aggregator is usefull to get regions, countries and sub regions informations from a REST API: https://restcountries.eu/rest/v2/
'''

class CountryAggregator():
	
	def __init__(self):
		print("Starting: "+path()+"/CountryAggregator/__init__")
		self.api_url = "https://restcountries.eu/rest/v2/"
		
		self.api_country_region = {}
		self.api_country_region_gpio = {}
		self.api_all_regions = []
		self.api_all_regions_gpio = []
		self.api_all_subregions = []
		self.api_all_regions_and_subregions = {}
		self.api_all_regions_and_subregions_gpio = {}
		print("Ending: "+path()+"/CountryAggregator/__init__")
	

	def get_country_region(self, country):
		print("Starting: "+path()+"/CountryAggregator/get_country_region")
		if country in self.api_country_region:
			print("Ending: "+path()+"/CountryAggregator/get_country_region")
			return self.api_country_region[country]
		else:
			r = requests.get(self.api_url+"name/"+country+"?fullText=true&fields=region")
			returned_region = json.loads(r.text)[0]["region"]
			self.api_country_region[country] = returned_region
			print("Ending: "+path()+"/CountryAggregator/get_country_region")
			return returned_region
		
	def format_region_for_gpio(self, region_to_format, subregion):
		print("Starting: "+path()+"/CountryAggregator/format_region_for_gpio")
		if region_to_format in ["Europe", "Africa", "Oceania", "Polar", ""]:
			print("Ending: "+path()+"/CountryAggregator/format_region_for_gpio")
			return region_to_format
		else:
			if region_to_format in ["Americas"]:
				if "Northern" in subregion or "Caribbean" in subregion:
					print("Ending: "+path()+"/CountryAggregator/format_region_for_gpio")
					return "Northern America"
				else:
					print("Ending: "+path()+"/CountryAggregator/format_region_for_gpio")
					return "South America"
			elif region_to_format in ["Asia"]:
				if "Western" in subregion or "Central" in subregion:
					print("Ending: "+path()+"/CountryAggregator/format_region_for_gpio")
					return "Western Asia"
				else:
					print("Ending: "+path()+"/CountryAggregator/format_region_for_gpio")
					return "Eastern Asia"
			else: 
				print("Ending: "+path()+"/CountryAggregator/format_region_for_gpio")
				return ""

	def get_country_region_for_gpio(self, country):
		print("Starting: "+path()+"/CountryAggregator/get_country_region_for_gpio")
		print(country)
		if country in self.api_country_region_gpio:
			print("Ending: "+path()+"/CountryAggregator/get_country_region_for_gpio")
			return self.api_country_region_gpio[country]
		else:
			r = requests.get(self.api_url+"name/"+country+"?fullText=true&fields=region;subregion")
			if r.text != '{"status":404,"message":"Not Found"}':
				region_to_format = json.loads(r.text)[0]["region"]
				subregion = json.loads(r.text)[0]["subregion"]
				region_formatted = self.format_region_for_gpio(region_to_format, subregion)
				self.api_country_region_gpio[country] = region_formatted
				print("Ending: "+path()+"/CountryAggregator/get_country_region_for_gpio")
				return region_formatted
			else:
				self.api_country_region_gpio[country] = "Not found"
				print("Ending: "+path()+"/CountryAggregator/get_country_region_for_gpio")
				return "Not found"


	def get_all_regions(self):
		print("Starting: "+path()+"/CountryAggregator/get_all_regions")
		if len(self.api_all_regions)>0:
			print("Ending: "+path()+"/CountryAggregator/get_all_regions")
			return self.api_all_regions
		else:
			r = requests.get(self.api_url+"all?fields=region")
			j = json.loads(r.text)
			l = []
			
			for elem in j:
				if elem["region"] not in l:
					l.append(elem["region"])
			
			self.api_all_regions = l
			print("Ending: "+path()+"/CountryAggregator/get_all_regions")
			return l

	def get_all_subregions(self):
		print("Starting: "+path()+"/CountryAggregator/get_all_subregions")
		if len(self.api_all_subregions)>0:
			print("Ending: "+path()+"/CountryAggregator/get_all_subregions")
			return self.api_all_subregions
		else:
			r = requests.get(self.api_url+"all?fields=subregion")
			j = json.loads(r.text)
			l = []
			
			for elem in j:
				if elem["subregion"] not in l:
					l.append(elem["subregion"])
					
			self.api_all_subregions = l
			print("Ending: "+path()+"/CountryAggregator/get_all_subregions")
			return l
		
	def get_all_regions_and_subregions(self):
		print("Starting: "+path()+"/CountryAggregator/get_all_regions_and_subregions")
		if self.api_all_regions_and_subregions != {}:
			print("Ending: "+path()+"/CountryAggregator/get_all_regions_and_subregions")
			return self.api_all_regions_and_subregions
		else:
			r = requests.get(self.api_url+"all?fields=subregion;region")
			j = json.loads(r.text)
			res = {}
			
			for elem in j:
				if elem["region"] not in res:
					res[elem["region"]] = []
				if  elem["subregion"] not in res[elem["region"]]:
					res[elem["region"]].append(elem["subregion"])
			self.api_all_regions_and_subregions = res
			print("Ending: "+path()+"/CountryAggregator/get_all_regions_and_subregions")
			return res

		
	def get_all_regions_and_subregions_for_gpio(self):
		print("Starting: "+path()+"/CountryAggregator/get_all_regions_and_subregions_for_gpio")
		if self.api_all_regions_and_subregions_gpio != {}:
			print("Ending: "+path()+"/CountryAggregator/get_all_regions_and_subregions_for_gpio")
			return self.api_all_regions_and_subregions_gpio
		else:
			r = requests.get(self.api_url+"all?fields=subregion;region")
			j = json.loads(r.text)
			res = {}
			
			for elem in j:
				elem["region"] = self.format_region_for_gpio(elem["region"], elem["subregion"])
				if elem["region"] not in res:
					res[elem["region"]] = []
				if  elem["subregion"] not in res[elem["region"]]:
					res[elem["region"]].append(elem["subregion"])
					
			self.api_all_regions_and_subregions_gpio = res
			print("Ending: "+path()+"/CountryAggregator/get_all_regions_and_subregions_for_gpio")
			return res

		
	def get_all_regions_for_gpio(self):
		print("Starting: "+path()+"/CountryAggregator/get_all_regions_for_gpio")
		if len(self.api_all_regions_gpio)>0:
			print("Ending: "+path()+"/CountryAggregator/get_all_regions_for_gpio")
			return self.api_all_regions_gpio
		else:
			r = requests.get(self.api_url+"all?fields=subregion;region")
			j = json.loads(r.text)
			res = []
			
			for elem in j:
				elem["region"] = self.format_region_for_gpio(elem["region"], elem["subregion"])
				if elem["region"] not in res and elem["region"] not in [None, "", "Not found", "Polar"]:
					res.append(elem["region"])
				
			self.api_all_regions_gpio = res
			print("Ending: "+path()+"/CountryAggregator/get_all_regions_for_gpio")
			return res


'''
	JoinRSSRegions will make possible to retrieve rss data and country,regions,subregions data to join them and prepare resulting json
	that will be used by raspberry gpio
'''

class DataForGPIO():
	
	ca = None
	rss = None
	joined_data = None
	gpio_data = None
	
	def __init__(self, rss_url="https://www.gdacs.org/xml/rss_eq_48h_low.xml",minalertscore=3):
		print("Starting: "+path()+"/DataForGPIO/__init__")
		self.ca =  CountryAggregator()
		self.rss = RssAggregator(rss_url, verbose=False)
		self.fill_joined_data()
		self.filter_joined_data(minalertscore)
		self.fill_gpio_data()
		print("Ending: "+path()+"/DataForGPIO/__init__")
	
	def fill_joined_data(self):
		print("Starting: "+path()+"/DataForGPIO/fill_joined_data")
		self.joined_data = {}
		dict_data = self.rss.get_entries_dict()
		
		for entry in dict_data:
			entry_countries = entry["gdacs_country"].split(", ")
			for entry_country in entry_countries:
				entry_region = self.ca.get_country_region_for_gpio(entry_country)
				if entry_region not in [None, "", "Not found", "Polar"]:
					if entry_region not in self.joined_data:
						self.joined_data[entry_region]= []
					self.joined_data[entry_region].append(entry)
		
		
		print("Ending: "+path()+"/DataForGPIO/fill_joined_data")
		
	def filter_joined_data(self, minalertscore=3):
		print("Starting: "+path()+"/DataForGPIO/filter_joined_data")
		filtered_joined_data = {}
		
		for  region in self.joined_data:
			entries = self.joined_data[region]
			for entry in entries:
				if float(entry["gdacs_alertscore"]) >= float(minalertscore):
					if region not in filtered_joined_data:
						filtered_joined_data[region]= []
					filtered_joined_data[region].append(entry)
					
		self.joined_data = filtered_joined_data
		print("Ending: "+path()+"/DataForGPIO/filter_joined_data")
		
	def fill_gpio_data(self):
		print("Starting: "+path()+"/DataForGPIO/fill_gpio_data")
		self.gpio_data = {}
		regions = self.ca.get_all_regions_for_gpio()
		
		for region in regions:
			
			if region in self.joined_data:
				self.gpio_data[region] = True
			else:
				self.gpio_data[region] = False
			
			
		print("Ending: "+path()+"/DataForGPIO/fill_gpio_data")
			
		
