#!/usr/bin/python3
"""Module defines JSON file-reading function"""
import json

def load_from_json_file(filename):
    """Creates Python object from given JSON file"""
    with open(filename) as fo:
        return json.load(fo)

