#!/usr/bin/python3

def multiple_returns(sentence):
    sentence_len = len(sentence)
    if sentence != '':
        char_first = sentence[0]
    else:
        char_first = None
    return (sentence_len, char_first)
