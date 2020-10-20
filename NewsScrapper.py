#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
News scraper, scrapes articles from a newspaper then adds them to a database.
"""
__title__ = 'NewsScraper'
__author__ = 'Ivan Fernando Galaviz Mendoza'

from datetime import datetime
from time import mktime
import json
import logging
from pymongo import MongoClient
from newspaper import Article, build
import feedparser as fp
import constants
from classifier import Classifiers


logging.basicConfig(filename=constants.LOG_FILENAME,
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

# TODO: Assign timezones accordingly to the region (e.g. Jalisco)
# TODO: Create a temp dict to use when losing connection to the db
# TODO: Create index from the data to prevent repeated registers (db.profiles.create_index())


def try_to_get_utc(date, link):
    try:
        return datetime.utcfromtimestamp(mktime(date))
    except Exception:
        logging.warning(
            'Could not get UTC time from {}'.format(link), exc_info=True)
        return date


def log_invalid_text(link):
    logging.warning('Ignoring {} due to invalid body.'.format(link))


def start_classification():
    Classifier()


def scrape_news():
    # Loads the JSON file with news sites
    with open(constants.NEWSPAPERS_PATH) as newspapers_file:
        companies = json.load(newspapers_file)

    # Initialize database connection
    client = MongoClient()

    # Assign database
    db = client.test
or company, info in companies.items():
        # If a RSS link is provided in the JSON file,
        # this will be the first choice.
        # Reason for this is that,
        # RSS feeds often give more consistent and correct data.
        # If you do not want to scrape from the RSS-feed,
        # just leave the RSS attr empty in the JSON file.
        if 'rss' in info:
            parse_rss(company, info, db)
        else:
            parse_link(company, info, db)

    # Close DB connection
    client.close()

    start_classification()

