#!/usr/bin/python3
def best_score(a_dictionary):
    bestScore, key = 0, None
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > bestScore:
                bestScore = v
                key = k
    return key
