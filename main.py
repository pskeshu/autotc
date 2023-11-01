class Cell:
    def __init__(self, name, if_adherant, doubling_time) -> None:
        self.name = name # human readable name
        self.if_adherant = if_adherant # boolean
        self.doubling_time = doubling_time # in hours

    def __repr__(self):
        return f"Cell(name={self.name}, adherant={self.if_adherant}, doubling_time={self.doubling_time})"


class Media:
    def __init__(self, name, fbs, if_antibiotics):
        self.name = name # human readable name
        self.fbs = fbs # % of FBS in media
        self.if_antibiotics = if_antibiotics # boolean

    def __repr__(self):
        return f"Media(name={self.name}, FBS={self.fbs}%, antibiotics={self.if_antibiotics})"

class FrozenVial:
    def __init__(self, cell=None, cell_conc=None, date_frozen=None, frozen_by=None):
        self.cell = cell
        self.cell_conc = cell_conc
        self.date_frozen = date_frozen
        self.frozen_by = frozen_by

    def thaw(self, flask):
        flask.initiate_from_vial(self)

    def __repr__(self):
        return f"FrozenVial(cell={self.cell}, cell_conc={self.cell_conc}, date_frozen={self.date_frozen})"


class Flask:
    def __init__(self, _type=None, seeded_on=None, media=None, cell=None, cell_conc=None):
        self._type = _type
        self.seeded_on = seeded_on
        self.media = media
        self.cell = cell
        self.cell_conc = cell_conc

    def initiate_from_vial(self, vial):
        self.cell = vial.cell
        self.cell_conc = vial.cell_conc

    def split(self):
        return Flask()

    def __repr__(self):
        return f"Flask(type={self._type}, cell={self.cell}, seeded_on={self.seeded_on}, media={self.media})"


hela = Cell(name="WT HeLa", if_adherant=True, doubling_time=24)
media = Media(name="DMEM", fbs=10, if_antibiotics=False)

if __name__ == "__main__":
    vial = FrozenVial(cell=hela, cell_conc=20000, date_frozen="20/01/2020")
    initial_flask = Flask("t25", seeded_on="25/10/23", media=media)
    vial.thaw(initial_flask)
  
    # splitted_flask = new_flask.split()