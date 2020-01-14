from rssaggregator import RssAggregator, RssEntry
from countriesaggregator import CountryAggregator
import json

#Getting data from RSS
#rssobject = RssAggregator("https://www.gdacs.org/xml/rss_eq_48h_low.xml", verbose=False)
ca =  CountryAggregator()
print(ca.get_country_region("USA"))
print(ca.get_all_regions())


# Printing in dict format
'''
print("Get all in dict format")
print(json.dumps(rssobject.get_all_data_dict(),indent=4))
'''

# Print only 4 first entries
#print(json.dumps(rssobject.get_entries_dict()[:4],indent=4))
