import scrapy

# Titulo = //h1/a/text()
# citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten tags = '//div[contains(@class,"tags-box")]//span[@class="tag-item"]/a/text()'
#  next page button = response.xpath('//ul/[@class="pager"]//li[@class="next"]/a/@href').get

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]
    custom_settings = {
        'FEED_URI': 'quotes.json',
        'FEED_FORMAT': 'json',
        'CONCURRENT_REQUESTS':24,
        'MEMUSAGE_LIMIT_MB':2048,
        'MEMUSAGE_NOTIFY_MAIL':['wa@hotmail'],
        'ROBOTSTXT_OBEY':True,
        'USER_AGENT': 'Angel',
        'FEED_EXPORT_ENCODING':'utf-8'
    }
    def parse_only_quotes(self,response, **kwargs):
        if kwargs:
            quotes = kwargs['quotes']
            authors = kwargs['authors']
        quotes.extend(response.xpath('//small[@class="author" and @itemprop="author"]/text()').getall())
        authors.extend(response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall())
        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link,callback = self.parse_only_quotes, cb_kwargs = {'quotes':quotes,'authors': authors})
        else:
            yield {
                'quotes':  list(zip(quotes, authors))
            }
    
    
    def parse(self,response):
        #print('*' * 10)
        #print('\n\n\n')
        title = response.xpath('//h1/a/text()').get()
        #print(f'Titulo: {title}')
        #print('\n\n')
        authors = response.xpath('//small[@class="author" and @itemprop="author"]/text()').getall()
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        #print('Citas: ')
        #for quote in quotes:
        #    print(f'-{quote}')
        #print('\n\n')
        #print(response.status, response.headers)
        top_ten_tags = response.xpath('//div[contains(@class,"tags-box")]//span[@class="tag-item"]/a/text()').getall()        
        #print('Top ten tags:')
        #for tag in top_ten_tags:
        #    print(f'- {tag}')
        #print('\n\n')
        #print('\n\n')
        #print('*' * 10)
        
        # Declarando los atributos
        top = getattr(self, 'top', None)
        if top: 
            top = int(top)
            top_ten_tags = top_ten_tags[:top]
            
        yield {
            'title': title,
        #    'quotes': quotes,
            'top_ten_tags': top_ten_tags
        }
        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link,callback = self.parse_only_quotes, cb_kwargs = {'quotes':quotes,'authors': authors})
        