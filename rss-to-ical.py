from flask import Flask
import icalendar
import feedparser
import pytz
import datetime
import os

app = Flask(__name__)

if not os.environ['RSS_FEED_URL']:
    sys.exit(1)

@app.route("/")
def get_feed():
    feed = feedparser.parse(os.environ['RSS_FEED_URL'])
    cal = icalendar.Calendar()

    cal.add('prodid', '-//rss-to-ical-flask//')
    cal.add('version', '2.0')

    for post in feed.entries:
        event = icalendar.Event()
        event.add('dtstart', datetime.datetime(*post.published_parsed[:6],
                                               tzinfo=pytz.timezone("GMT")))
        event.add('dtend', datetime.datetime(*post.published_parsed[:6],
                                             tzinfo=pytz.timezone("GMT")) +
                           datetime.timedelta(hours=2))
        event.add('dtstamp', datetime.datetime(*post.published_parsed[:6],
                                               tzinfo=pytz.timezone("GMT")))
        event.add('summary', post.title)
        event.add('url', post.link)

        cal.add_component(event)
    return cal.to_ical()
