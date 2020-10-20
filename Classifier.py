#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Classifier. Tells if the news content is violent or not,
then updates the document in the database.
"""
__title__ = 'Classifier'
__author__ = 'Ivan Fernando Galaviz Mendoza'
import pickle
from threading import Thread

from pymongo import MongoClient
from bson.objectid import ObjectId

import constants

class Classifier(Thread):
    def __init__(self):
        super().__init__()
        self._vectorizer = deserialize(
            constants.SERIALIZED_COUNT_VECTORIZER_FILENAME)
        self._classifier = deserialize(constants.SERIALIZED_CLASSIFIER_FILENAME)
        self._client = MongoClient()
        self._db = self._client['test']
        self.set_stop_words()
        self.start()