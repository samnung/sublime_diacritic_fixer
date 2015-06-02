#!/usr/bin/env python

import sublime, sublime_plugin

def fix_diacritics(text):    
    mapping_dict = {
        u'̌' : {
            u'e': u'ě',
            u'r': u'ř',
            u't': u'ť',
            u'z': u'ž',
            u's': u'š',
            u'd': u'ď',
            u'c': u'č',
            u'n': u'ň',
        },
        u'́' : {
            u'e': u'é',
            u'u': u'ú',
            u'i': u'í',
            u'o': u'ó',
            u'a': u'á',
            u'y': u'ý',
        },
        u'̊' : {
            u'u': u'ů',
        },
    }

    for diacritic_char, group in mapping_dict.items():
        for normal_char, normal_diacritic_char in group.items():
            text = text.replace(normal_char + diacritic_char, normal_diacritic_char)
            text = text.replace(normal_char.upper() + diacritic_char, normal_diacritic_char.upper())
    
    return text

class DiacriticFixSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        
        for region in selection:
            region_text = self.view.substr(region)
            fixed_text = fix_diacritics(region_text)
            self.view.replace(edit, region, fixed_text)
