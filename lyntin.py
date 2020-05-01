#!/usr/bin/env python
#######################################################################
# This file is part of Lyntin.
# copyright (c) Free Software Foundation 2001, 2020
#
# Lyntin is distributed under the GNU General Public License license.
# See the file LICENSE for distribution details.
#######################################################################
bootoptions = {
    "ui": "tk",
    "datadir": "",
    "moduledir": [],
    "readfile": [],
    "snoopdefault": 1,
}

if __name__ == "__main__":
    import lyntin.engine

    lyntin.engine.main(bootoptions)
