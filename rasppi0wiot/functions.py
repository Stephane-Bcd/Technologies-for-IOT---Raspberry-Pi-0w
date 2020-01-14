import requests

'''
	Function to retrieve rss data
'''
def get_rss_json (get_url = "https://www.gdacs.org/xml/rss_24h.xml"):
	r = requests.get(get_url)
	res_text = r.text
	
	
	
	print(res_text)


