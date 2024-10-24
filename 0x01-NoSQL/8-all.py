#!/usr/bin/env python3
"""function for mando operation with python"""

from pymongo import MongoClient

def list_all(mongo_collection):
    """ list all document in python"""
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
