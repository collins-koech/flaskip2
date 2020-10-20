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
