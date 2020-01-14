from rssaggregator import RssAggregator, RssEntry
import json

#Getting data from RSS
rssobject = RssAggregator("https://www.gdacs.org/xml/rss_24h.xml", verbose=False)


# Printing in json format
print(json.dumps(rssobject.get_all_data_dict(),indent=4))

