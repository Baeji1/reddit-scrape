import scrapy
import subprocess

class RedditTitleSpider(scrapy.Spider):
	
	name = "reddit_spider"
	start_urls = [
			'https://www.reddit.com/',
		]
	
	def parse(self,response):
		
		num = getattr(self,'page',None)
		num = str(int(num)*int(25))
		content = response.css('div.sitetable.linklisting')
		next_page = content.css('div.nav-buttons span.next-button a::attr(href)').extract()
		next_page = ''.join(next_page)
		i = 30
		x = ''
		
		while next_page[i] != '&':
			x += next_page[i]
			i += 1

		yield{
				'page ' + str(int(x)/25): {	
					'votes': content.css('div.midcol.unvoted div.score.unvoted::text').extract(),
					'title': content.css('div.entry.unvoted a.title.may-blank::text').extract(),
					'subreddit': content.css('div.entry.unvoted a.subreddit.hover.may-blank::text').extract(),
					'user': content.css('div.entry.unvoted a.author.may-blank::text').extract(),
					},
				}
		
		if next_page is not None and x != num:
			yield response.follow(next_page, callback = self.parse)

		if x==num:
			subprocess.Popen("/home/baeji/Desktop/testrun/data.py",shell=True)
