import feedparser
from dateutil.parser import parse
from datetime import datetime, timedelta
from colorama import Fore, Style
import pytz

URLS = {
    ('South and Central Asia', 'https://www.state.gov/rss-feed/south-and-central-asia/feed/'),
    ('Counterterrorism', 'https://www.state.gov/rss-feed/counterterrorism/feed/'),
    ('Arms Control / International Security', 'https://www.state.gov/rss-feed/arms-control-and-international-security/feed/'),
    ('US Embassy Kabul', 'https://af.usembassy.gov/feed')

}


def show_rss_titles(feed_title:str, url:str):
    feed = feedparser.parse(url)
    print(f'--------{feed_title}--------')
    for entry in feed.get('entries'):
        valid_datetime = parse(entry.get('updated'))
        not_newer = (datetime.now(tz=pytz.timezone('US/Pacific')) - valid_datetime) > timedelta(days=1)
        color = Fore.LIGHTCYAN_EX if not_newer else Fore.YELLOW
        print(valid_datetime.strftime('%c'), '-', color, entry.get('title'), Style.RESET_ALL)

        if not not_newer:
            print(entry.get('summary'))


def main():
    for feed_title, url in URLS:
        show_rss_titles(feed_title, url)


if __name__=='__main__':
    main()