# -*- coding: utf-8 -*-

"""Text Case"""

from albertv0 import *

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Text Case"
__version__ = "1.0"
__trigger__ = "tc "
__author__ = "Dorin Duminica"
__dependencies__ = []

iconPath = iconLookup("accessories-dictionary")

def handleQuery(query):
    if not query.isTriggered:
        return None
    
    results = []
    
    # original text
    s = query.string.strip().lower()
    
    # init with lower case
    cases = [s]
    
    # upper case
    cases.append(s.upper())
    
    # scream case #1
    scs = ""
    for i in range(0, len(s)):
        if i % 2 == 0:
            scs += s[i].upper()
        else:
            scs += s[i]
    cases.append(scs)
    
    # scream case #2 inverted scs1
    cases.append(scs.swapcase())
    
    for i in cases:
        results.append(Item(
            id = __prettyname__,
            icon = iconPath,
            text = i,
            actions = [
                ClipAction("Copy to clipboard", i)
            ]
        ))

    return results


