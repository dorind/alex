# -*- coding: utf-8 -*-

"""
X11 window finder

based on "window_switcher.py" part of albert default install
by Ed Perez and Manuel Schneider

changes from original:
- added comments
- search in window title
- trigger, this extension can live together with the original "window_switcher.py"
"""

import subprocess
from collections import namedtuple
from shutil import which

from albertv0 import *

Window = namedtuple("Window", ["wid", "desktop", "wm_class", "host", "wm_name"])

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Window Finder"
__version__ = "1.0"
__trigger__ = "x "
__author__ = "Ed Perez, Manuel Schneider, Dorin Duminica"
__dependencies__ = ["wmctrl"]

if which("wmctrl") is None:
    raise Exception("'wmctrl' is not in $PATH.")

def handleQuery(query):
    if not query.isTriggered:
        return None
    stripped = query.string.strip().lower()
    if stripped:
        results = []
        #
        # output sample of 
        #
        # $ wmctrl -lx
        # -----------+---------+-------------------------------+---------+----------------------------------------------------
        # wid        | desktop | wm_class                      | host    | wm_name
        # -----------+---------+-------------------------------+---------+----------------------------------------------------
        # 0x0380b2e3 | 0       | xfce4-terminal.Xfce4-terminal | user-pc | Terminal - user@user-pc: ~/Desktop/nix-goodies/misc
        # -----------+---------+-------------------------------+---------+----------------------------------------------------
        #
        # we can now find the Terminal window that contains "nix-goodies" in title
        # by invoking albert and typing "x nix", where "x" is the trigger and "nix" is the keyword
        #
        for line in subprocess.check_output(['wmctrl', '-lx']).splitlines():
            win = Window(*[token.decode() for token in line.split(None, 4)])
            # ignore windows that are displayed on all desktops, i.e. -1
            if win.desktop != "-1" and (
                # look into window class as originally intended
                (stripped in win.wm_class.split('.')[0].lower()) or 
                # but also in window title
                (stripped in win.wm_name.lower())):
                # format and display result
                results.append(Item(id="%s%s" % (__prettyname__, win.wm_class),
                                    icon=iconLookup(win.wm_class.split('.')[0]),
                                    text="%s - <i>Desktop %s</i>" % (win.wm_class.split('.')[-1].replace('-',' '), win.desktop),
                                    subtext=win.wm_name,
                                    actions=[ProcAction("Switch Window",
                                                        ["wmctrl", '-i', '-a', win.wid] ),
                                             ProcAction("Move window to this desktop",
                                                        ["wmctrl", '-i', '-R', win.wid] ),
                                             ProcAction("Close the window gracefully.",
                                                        ["wmctrl", '-c', win.wid])]))
        return results
