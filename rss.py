import feedparser
import config

#The personal key of the moodle User has (for now) be added to the RSS-URL (insert yours for the URL to work)
personal_key = config.key

def refreshFeed():
    new_feed = feedparser.parse(f'https://isis.tu-berlin.de/rss/file.php/1970720/{personal_key}/mod_forum/64807/rss.xml')
    new_entries = new_feed['entries']

    return new_entries

refreshFeed()
