import feedparser
import config

#The personal key of the moodle User has (for now) be added to the RSS-URL (insert yours for the URL to work)
personal_key = config.key

def refreshFeed(course_id, forum_id):
    new_feed = feedparser.parse(f'https://isis.tu-berlin.de/rss/file.php/{course_id}/{personal_key}/mod_forum/{forum_id}/rss.xml')
    new_entries = new_feed['entries']

    return new_entries

