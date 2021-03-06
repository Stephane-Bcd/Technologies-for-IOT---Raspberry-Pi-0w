from models import RssAggregator, RssEntry, CountryAggregator
from models import DataForGPIO
import json

run_all_tests = False

ca =  CountryAggregator()



	print("region for usa:")
	print(ca.get_country_region("USA"))
	print("")

	print("All regions and subregions:")
	print(json.dumps(ca.get_all_regions_and_subregions(),indent=4))
	print("")
	print("All regions and subregions (for gpio):")
	print(json.dumps(ca.get_all_regions_and_subregions_for_gpio(),indent=4))
	print("")


if run_all_tests: 
	ca =  CountryAggregator()

	print("region for usa:")
	print(ca.get_country_region("USA"))
	print("")

	print("region (for gpio) for usa:")
	print(ca.get_country_region_for_gpio("USA"))
	print("")

	print("All regions and subregions:")
	print(json.dumps(ca.get_all_regions_and_subregions(),indent=4))
	print("")
	print("All regions and subregions (for gpio):")
	print(json.dumps(ca.get_all_regions_and_subregions_for_gpio(),indent=4))
	print("")


	print("All regions (for gpio):")
	print(json.dumps(ca.get_all_regions_for_gpio(),indent=4))
	print("")

	# Getting data from RSS
	rssobject = RssAggregator("https://www.gdacs.org/xml/rss_eq_48h_low.xml", verbose=False)

	# Printing in dict format
	'''
	print("Get all in dict format")
	print(json.dumps(rssobject.get_all_data_dict(),indent=4))
	'''

	# Print only 4 first entries
	print("Get 4 first entries in dict format")
	print(json.dumps(rssobject.get_entries_dict()[:4],indent=4))

dfg = DataForGPIO("https://www.gdacs.org/xml/rss_24h.xml",minalertscore=2)

print(json.dumps(dfg.gpio_data,indent=4))





