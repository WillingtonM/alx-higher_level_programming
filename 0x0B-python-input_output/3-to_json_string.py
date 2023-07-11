#!/usr/bin/python3
"""This module defines string-to-JSON function"""
import json


def to_json_string(my_obj):
    """Returns JSON representation of string object"""
    return json.dumps(my_obj)

