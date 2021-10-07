import feedparser
from dateutil.parser import parse
from datetime import datetime, timedelta
from colorama import Fore, Style
import pytz
from send_email import text_alert
import time

URLS = {
    ('South and Central Asia', 'https://www.state.gov/rss-feed/south-and-central-asia/feed/'),
    ('Counterterrorism', 'https://www.state.gov/rss-feed/counterterrorism/feed/'),
    ('Arms Control / International Security', 'https://www.state.gov/rss-feed/arms-control-and-international-security/feed/'),
    ('US Embassy Kabul', 'https://af.usembassy.gov/feed'),
    ('The White House', 'https://www.whitehouse.gov/feed')
}


def show_rss_titles(feed_title:str, url:str):
    feed = feedparser.parse(url)
    print(f'\n--------{feed_title}--------')

    for entry in feed.get('entries'):
        valid_datetime = parse(entry.get('updated'))
        older = (datetime.now(tz=pytz.timezone('US/Pacific')) - valid_datetime) > timedelta(hours=1)
        color = Fore.LIGHTCYAN_EX if older else Fore.YELLOW
        title = entry.get('title')
        print(valid_datetime.strftime('%c'), '-', color, title, Style.RESET_ALL)


        if not older:
            print(entry.get('summary'))
            print()
            if 'US Embassy Kabul' in feed_title or 'Afghanistan'.lower() in title.lower():
                text_alert(feed_title, title)


def main():
    for feed_title, url in URLS:
        show_rss_titles(feed_title, url)


if __name__=='__main__':
    main()