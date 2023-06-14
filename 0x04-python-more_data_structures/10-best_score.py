#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_k = max(a_dictionary, key=lambda x: a_dictionary[x])
    return max_k
