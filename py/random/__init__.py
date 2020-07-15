# -*- coding: utf-8 -*-

"""Random"""

import random

from albertv0 import *

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Random"
__version__ = "1.0"
__trigger__ = "rnd "
__author__ = "Dorin Duminica"
__dependencies__ = []

def handleQuery(query):
    if not query.isTriggered:
        return None
    
    results = []
    
    # original text
    s = query.string.strip()
    
    # split into word list
    words = s.split()
    
    # randomize words
    random.shuffle(words)
    
    # return list of words in the randomized order
    for word in words:
        results.append(Item(
            id = __prettyname__,
            icon = "",
            text = word,
            actions = [
                ClipAction("Copy to clipboard", word)
            ]
        ))

    return results


