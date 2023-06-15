#!/usr/bin/python3
def best_score(a_dictionary):
    winner = ()
    
    if a_dictionary == None:
        return None
    sorted_dict = sorted(a_dictionary.items(), key=lambda x: x[1])
    winner = sorted_dict[len(sorted_dict) - 1]

    return winner[0]
