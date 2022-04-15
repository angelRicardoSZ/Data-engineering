import argparse
import logging
logging.basicConfig(level=logging.INFO)
import news_page_object as news
from common import config

logger = logging.getLogger(__name__)


def _news_scraper(news_site_uid):
    host = config()["new_sites"][news_site_uid]["url"]
    logging.info('beggining scrapper for {}'.format(host))
    logging.info('FIndind links')
    homepage = news.HomePage(news_site_uid, host)

    for link in homepage.article_links:
        print(link)

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    new_sites_choices = list(config()["new_sites"].keys())
    parser.add_argument("new_site",help="The new site that you want to scrape",type=str,choices=new_sites_choices)
    args = parser.parse_args()
    _news_scraper(args.new_site)

