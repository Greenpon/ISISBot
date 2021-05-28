import feedparser
import config

#The personal key of the moodle User has (for now) be added to the RSS-URL (insert yours for the URL to work)
personal_key = config.key

feed = feedparser.parse(f'https://isis.tu-berlin.de/rss/file.php/1970720/{personal_key}/mod_forum/64807/rss.xml')

entries = feed['entries']

def refreshFeed():
    new_feed = feedparser.parse(f'https://isis.tu-berlin.de/rss/file.php/1970720/{personal_key}/mod_forum/64807/rss.xml')
    new_entries = new_feed['entries']
    curr_entries = new_entries

    for x in new_entries:
        for y in entries:
            if(x['id'] == y['id']):
                new_entries.remove(x)



refreshFeed()
