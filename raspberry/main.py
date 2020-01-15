from aggregators.models import RssAggregator, RssEntry, CountryAggregator
from aggregators.models import DataForGPIO
from powerled.models import GPIOController
import json
import time

'''
	This is the script that will be executed every day:
	1. Retrieve data from RSS
	2. Parse it
	3. Use it to light up/down the leds
	4. Send it to a database
'''

RSS_SOURCE = "https://www.gdacs.org/xml/rss_24h.xml"
MIN_ALERT_SCORE = 2


dfg = DataForGPIO(RSS_SOURCE,minalertscore=MIN_ALERT_SCORE)

print("Data for GPIO:")
print(json.dumps(dfg.gpio_data,indent=4))
print("")


gpc = GPIOController()

gpc.switch_leds_states(dfg.gpio_data)

'''
time.sleep(10)

gpc.switch_leds_states(regions_booleans = {
			"Eastern Asia": False,
			"Europe": False,
			"Africa": False,
			"Oceania": False,
			"Northern America": False,
			"South America": False,
			"Western Asia": False
		})
'''

print("\nData sent to messageries and to influxdb: ")
print(json.dumps(dfg.joined_data,indent=4))
