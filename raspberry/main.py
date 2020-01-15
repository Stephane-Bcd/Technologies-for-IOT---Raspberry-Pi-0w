from aggregators.models import RssAggregator, RssEntry, CountryAggregator
from aggregators.models import DataForGPIO
import json

'''
	This is the script that will be executed every day:
	1. Retrieve data from RSS
	2. Parse it
	3. Use it to light up/down the leds
	4. Send it to a database
'''

dfg = DataForGPIO("https://www.gdacs.org/xml/rss_24h.xml",minalertscore=2)

print("Data for GPIO:")
print(json.dumps(dfg.gpio_data,indent=4))
print("")

