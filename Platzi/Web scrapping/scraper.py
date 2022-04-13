import requests
import lxml.html as html

XPATH_LINK_TO_ARTICLE = '//h2/a/@href' 
XPATH_TITLE = '//h2/a/text()' 
XPATH_SUMMARY = '//div[@class="lead"]/p/text()' 
XPATH_BODY = '//div[@class="html-content"]/p[not(@class)]/text()' 

