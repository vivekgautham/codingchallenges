
class Person(object):

    def __init__(self, name):
        self.name = name
        self.preferred = None
        self.engagedTo = None

    def setPreferred(self, preferred):
        self.preferred = preferred

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def engage(self, person):
        self.engagedTo = person

    def disengage(self):
        self.engagedTo = None

    def isEngaged(self):
        return self.engagedTo != None

class Gal(Person):

    def __init__(self, name):
        super(Gal, self).__init__(name)

    def disengage(self):
        self.engagedTo.disengage()
        super(Gal).disengage()

    def processProposal(self, guy):
        status = False
        if not self.engagedTo:
            self.engage(guy)
            guy.engage(self)
            status = True
        elif self.engagedTo and (guy in self.preferred) and (self.preferred.index(self.engagedTo) > self.preferred[guy]):
            self.disengage()
            self.engage(guy)
            guy.engage(self)
            status = True
        return status

class Guy(Person):

    def __init__(self, name):
        super(Guy, self).__init__(name)
        self.proposedWomen = set()

    def _getAvailableGal(self):
        for each in self.preferred:
            if each not in self.proposedWomen:
                return each
        raise Exception("There are no women available and guy is not engaged! Something went seriously wrong")

    def proposeToAvailableGal(self):
        res = False
        if self.engagedTo is None:
            gal = self._getAvailableGal()
            res = gal.processProposal(self)
            self.proposedWomen.add(gal)
        return res

class StableMarriage(object):

    def __init__(self, guyPrefs, galPrefs):
        self.guyPrefs = guyPrefs
        self.galPrefs = galPrefs
        self.guys = [Guy(each) for each in self.guyPrefs]
        self.gals = [Gal(each) for each in self.galPrefs]
        [guy.setPreferred([self._getGal(gal) for gal in self.guyPrefs[guy.name]]) for guy in self.guys]
        [gal.setPreferred([self._getGuy(gal) for guy in self.galPrefs[gal.name]]) for gal in self.gals]

    def _getGal(self, galName):
        for each in self.gals:
            if each.name == galName:
                return each

    def _getGuy(self, guyName):
        for each in self.guys:
            if each.name == guyName:
                return each

    def fix(self):
        while True:
            guys = [each for each in self.guys if not each.isEngaged()]
            if not guys: break
            for guy in guys:
                guy.proposeToAvailableGal()
        res = {}
        for guy in self.guys:
            res[guy.name] = guy.engagedTo.name
        return res

