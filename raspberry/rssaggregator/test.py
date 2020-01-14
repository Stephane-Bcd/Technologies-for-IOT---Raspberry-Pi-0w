from rssaggregator import RssAggregator, RssEntry
import json

#Getting data from RSS
rssobject = RssAggregator("https://www.gdacs.org/xml/rss_eq_48h_low.xml", verbose=False)


# Printing in dict format
'''
print("Get all in dict format")
print(json.dumps(rssobject.get_all_data_dict(),indent=4))
'''

# Print only 4 first entries


print(json.dumps(rssobject.get_entries_dict(),indent=4))
