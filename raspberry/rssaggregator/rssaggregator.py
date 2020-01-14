import feedparser
import json


class RssEntry():
	
	data = {}
	
	def __init__(self, data):
		self.data = data

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
		print("Creating RssAgregator:")
		print("Used url: " + paramrssurl)
		print("")
		
		self.entries = []
		self.data = {}
		self.data["feedurl"] = paramrssurl
		
		if verbose: print(json.dumps(self.thefeed.__dict__,indent=4))
		
		self.parse(verbose)

	def parse(self, verbose=False):
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
			
			
			self.entries.append(RssEntry(entry_data))
			entries_count += 1
		
		
		self.data["entries_count"] = entries_count
			
		print("Finished\n")
		
	def get_dict(self):
		return self.data
		
	def get_entries_dict(self):
		entries_json = []
		for entry in self.entries:
			entries_json.append(entry.data)
		return entries_json
	
	def get_all_data_dict(self):
		data = self.data
		data["entries"] = self.get_entries_dict()
		return data

	def __str__(self):
		return "Data: \n" + json.dumps(self.data, indent=4) + "\n\nEntries: \n" + json.dumps(self.get_entries_dict(), indent=4)


