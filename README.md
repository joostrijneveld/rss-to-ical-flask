## Converting RSS to iCal

This repository contains a one-off script that was written to convert a specific RSS feed into iCal format, so that it could be easily imported into calendar clients. It runs as a Flask application to make it easy to persistently deploy. The only parameter it takes is an environment variable called `RSS_FEED_URL`, listing the URL at which the RSS feed is available.

While the script is likely sufficiently specific not to serve anyone's purpose directly, it may come in useful as a starting point for someone trying to achieve something similar for a differently structured RSS feed.
