import feedparser


class RssAggregator():
	feedurl = ""

	def __init__(self, paramrssurl):
		print(paramrssurl)
		print("")
		self.feedurl = paramrssurl

	def parse(self):
		thefeed = feedparser.parse(self.feedurl)

		print("Getting Feed Data")
		print(thefeed.feed.get("title", ""))
		print(thefeed.feed.get("link", ""))
		print(thefeed.feed.get("description", ""))
		print(thefeed.feed.get("published", ""))
		print(thefeed.feed.get("published_parsed", thefeed.feed.published_parsed))
		print("\n\n")

		for thefeedentry in thefeed.entries:
			print("__________")
			print(thefeedentry.get("guid", ""))
			print(thefeedentry.get("title", ""))
			print(thefeedentry.get("link", ""))
			print(thefeedentry.get("description", ""))
			print("__________")


rssobject = WhizRssAggregator("https://www.gdacs.org/xml/rss_24h.xml")
rssobject.parse()
