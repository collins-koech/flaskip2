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