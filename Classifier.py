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

     def run(self):
        """
        Finds news that haven't been classified and updates info in database.
        Info updated:
        * is_classified -> set to True.
        * is_violent -> asks to the classifier if the news content
            was found as violent or not.
        """
        for article in self._db.test.find({constants.HAS_BEEN_CLASSIFIED: False}):
            self._db.test.update_one(
                {constants.MONGO_ID: ObjectId(article[constants.MONGO_ID])},
                {
                    "$set": {
                        constants.HAS_BEEN_CLASSIFIED: True,
                        constants.IS_VIOLENT: self.is_violent(
                            self.text_to_tokens(
                                [article[constants.TEXT]]))
                    }
                }
            )
        self._client.close()
