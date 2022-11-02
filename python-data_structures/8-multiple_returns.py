#!/usr/bin/pyhton3
# Returning a tuple with a length of string


def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
