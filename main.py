class Flask:
    def __init__(self, _type=None, seed_date=None, media=None, cell=None, cell_conc=None):
        self._type = _type
        self.seed_date = seed_date
        self.media = media
        self.cell = cell
        self.cell_conc = cell_conc

    def initiate_from_vial(self):
        pass

    def split(self):
        pass

    def __repr__(self):
        return f"Flask(type={self._type}, seeded_on={self.seed_date}, media={self.media})"

class FrozenVial:
    def __init__(self, cell=None, cell_conc=None, date_frozen=None):
        self.cell = cell
        self.cell_conc = cell_conc
        self.date_frozen = date_frozen

    def thaw(self, flask):
        flask.initiate_from_vial()

    def __repr__(self):
        return f"FrozenVial(cell={self.cell}, cell_conc={self.cell_conc}, date_frozen={self.date_frozen})"

if __name__ == "__main__":
    vial = FrozenVial(cell="WT HeLa", cell_conc=20000, date_frozen="20/01/2020")
    new_flask = Flask("t25", seed_date="25/10/23", media="DMEM")
    vial.thaw(new_flask)
