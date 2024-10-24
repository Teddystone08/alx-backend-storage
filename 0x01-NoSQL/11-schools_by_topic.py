#!/usr/bin/env python3
""" Python function to operate mangos """


def schools_by_topic(mongo_collection, topic):
    """ returns the list of school having a specific topic """
    results = mongo_collection.find({"topics": topic})
    return list(results)
