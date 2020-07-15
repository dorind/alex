# -*- coding: utf-8 -*-

"""Word unscrambler"""

import os.path

from albertv0 import *

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Word Unscramble"
__version__ = "1.0"
__trigger__ = "wu "
__author__ = "Dorin Duminica"
__dependencies__ = []

file_word_list_full = os.path.dirname(__file__) + "/words"
file_word_list_fallback = "/usr/share/dict/words"
file_word_list = ""

iconPath = iconLookup("accessories-dictionary")
max_results = 9

def handleQuery(query):
    if not query.isTriggered:
        return None

    results = []

    global file_word_list

    if os.path.isfile(file_word_list_full):
        file_word_list = file_word_list_full
    elif os.path.isfile(file_word_list_fallback):
        file_word_list = file_word_list_fallback
    else:
        results.append(Item(
            id = __prettyname__,
            icon = iconPath,
            text = __prettyname__ + " ERROR:",
            subtext = "Missing dictionary files in /usr/share/dict",
            actions = []
        ))
        return results

    try:
        unscramble_word(query.string.strip(), results)
    except Exception as e:
        results.append(Item(
            id = __prettyname__,
            icon = iconPath,
            text = "ERROR: " + str(e),
            subtext = file_word_list,
            actions = [
                ClipAction("Copy error to clipboard", str(e))
            ]
        ))

    return results

def unscramble_word(w: str, results):
    word = w.replace(" ", "").lower()
    sorted_word = list(word)
    sorted_word.sort()
    # store word length, we'll use it in a loop
    len_word = len(word)
    # sanity check
    if len_word < 1:
        return
    cnt = 0
    # open word list file and search for words
    with open(file_word_list) as f:
        # read line by line, each line is one word
        for line in f:
            # strip new line delim
            sline = line.strip().lower()
            if len(sline) != len_word:
                # skip processing current word
                continue
            else:
                sorted_line = list(sline)
                sorted_line.sort()
                # check if word contains same chars
                if sorted_word == sorted_line:
                    cnt += 1
                    results.append(Item(
                        id = __prettyname__,
                        icon = iconPath,
                        text = sline,
                        subtext = "Copy to clipboard",
                        actions = [
                            ClipAction("Copy word to clipboard", sline)
                        ]
                    ))
                if cnt > max_results:
                    break


