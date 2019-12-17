from challenges.src.algos import matching

import unittest

class Test_Matching(unittest.TestCase):

    def test_stableMarriable(self):
        guy_preferences = {
            'andrew': ['caroline', 'abigail', 'betty'],
            'bill': ['caroline', 'betty', 'abigail'],
            'chester': ['betty', 'caroline', 'abigail'],
        }
        gal_preferences = {
            'abigail': ['andrew', 'bill', 'chester'],
            'betty': ['bill', 'andrew', 'chester'],
            'caroline': ['bill', 'chester', 'andrew']
        }
        smp = matching.StableMarriage(guy_preferences, gal_preferences)
        res = smp.fix()
        self.assertEquals(len(res), 3)
        self.assertEquals(res['bill'], 'abigail')
        self.assertEquals(res['andrew'], 'caroline')
        self.assertEquals(res['chester'], 'betty')
        guy_preferences = {
            "reese": ["morgan", "groves", "carter", "shaw"],
            "finch": ["morgan", "carter", "shaw", "groves"],
            "fusco": ["shaw", "carter", "groves", "morgan"],
            "elias": ["groves", "carter", "shaw", "morgan"]
        }

        gal_preferences = {
            "carter": ["reese", "fusco", "elias", "finch"],
            "shaw": ["elias", "reese", "fusco", "finch"],
            "groves": ["reese", "fusco", "elias", "finch"],
            "morgan": ["finch", "fusco", "elias", "reese"]
        }
        smp = matching.StableMarriage(guy_preferences, gal_preferences)
        res = smp.fix()
        self.assertEquals(len(res), 4)
        self.assertEquals(res['fusco'], 'shaw')
        self.assertEquals(res['reese'], 'morgan')
        self.assertEquals(res['elias'], 'groves')
        self.assertEquals(res['finch'], 'carter')

        guy_preferences = {
            '0' : ['7', '5', '6', '4'],
            '1' : ['5', '4', '6', '7'],
            '2' : ['4', '5', '6', '7'],
            '3' : ['4', '5', '6', '7'],
        }
        gal_preferences = {
            '4': ['0', '1', '2', '3'],
            '5': ['0', '1', '2', '3'],
            '6': ['0', '1', '2', '3'],
            '7': ['0', '1', '2', '3'],
        }

        smp = matching.StableMarriage(guy_preferences, gal_preferences)
        res = smp.fix()
        self.assertEquals(len(res), 4)
        self.assertEquals(res['2'], '4')
        self.assertEquals(res['1'], '5')
        self.assertEquals(res['3'], '6')
        self.assertEquals(res['0'], '7')


