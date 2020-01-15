from aggregators.models import RssAggregator, RssEntry, CountryAggregator
from aggregators.models import DataForGPIO
from powerled.test_led import GPIOController
import json

'''
	This is the script that will be executed every day:
	1. Retrieve data from RSS
	2. Parse it
	3. Use it to light up/down the leds
	4. Send it to a database
'''

RSS_SOURCE = "https://www.gdacs.org/xml/rss_24h.xml"
MIN_ALERT_SCORE = 2


'''dfg = DataForGPIO(RSS_SOURCE,minalertscore=2)

print("Data for GPIO:")
print(json.dumps(dfg.gpio_data,indent=4))
print("")'''


gpc = GPIOController()

print(gpc)

gpc.bite("")