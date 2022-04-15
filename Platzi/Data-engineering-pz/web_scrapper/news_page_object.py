import requests
from common import config
import bs4


class HomePage:

    def __init__(self, news_site_uid, url):
        self._config = config()["news_sites"][news_site_uid]
        self._queries = self._config["queries"]
        self._html = None

    @property
    def article_links(self):
        links_list = []
        for link in self._select(self._queries["homepage_article_links"]):
            if link and link.has_attr("href"):
                link_list.append(link)
        return set(link["href"] for link in link_lis)

    def _select(self,query_string):
        return self._html.select(query_string)


    def _visit(self,url):
        response = requests.get(url)
        response.raise_for_status()
        self._html = bs4.BeautifulSoup(response.text,"html.parser")

