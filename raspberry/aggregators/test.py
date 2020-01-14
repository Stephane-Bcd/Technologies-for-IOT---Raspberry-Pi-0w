from rssaggregator import RssAggregator, RssEntry
from countriesaggregator import CountryAggregator
import json

ca =  CountryAggregator()
print("region for usa:")
print(ca.get_country_region("USA"))

print("All regions:")
print(ca.get_all_regions())

print("All sub-regions:")
print(ca.get_all_subregions())



#Getting data from RSS
#rssobject = RssAggregator("https://www.gdacs.org/xml/rss_eq_48h_low.xml", verbose=False)

# Printing in dict format
'''
print("Get all in dict format")
print(json.dumps(rssobject.get_all_data_dict(),indent=4))
'''

# Print only 4 first entries
#print(json.dumps(rssobject.get_entries_dict()[:4],indent=4))
