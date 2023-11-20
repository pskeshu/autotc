class Media:
    def __init__(self, name):
        self.name = name # human readable name
        self.contains = list()

    def add(self, item):
        self.contains.append(item)

    def __repr__(self):
        return f"Media(name={self.name}, contains={self.contains})"



class DMEM(Media):
    def __init__(self, name="DMEM", fbs=None, if_antibiotics=None):
        super().__init__(name=name)
        self.fbs = fbs
        self.if_antibiotics = if_antibiotics

class Reagent:
    def __init__(self, name, expiry) -> None:
        self.name = name
        self.expiry = expiry


class MMS(Reagent):
    pass

class NQO(Reagent):
    pass
