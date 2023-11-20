from reagents import DMEM


class Cell:
    def __init__(self, name, if_adherant, doubling_time) -> None:
        self.name = name # human readable name
        self.if_adherant = if_adherant # boolean
        self.doubling_time = doubling_time # in hours

    def __repr__(self):
        return f"Cell(name={self.name}, adherant={self.if_adherant}, doubling_time={self.doubling_time})"


class HeLa(Cell):
    def __init__(self, name="HeLa", if_adherant=True, doubling_time=24) -> None:
        super().__init__(name, if_adherant, doubling_time)
        # media for this cell
        self.media = DMEM(fbs=10, if_antibiotics=False)


class HumanFibroblasts(Cell):
    pass


class U2OS:
    pass


class A549:
    pass


class MEF:
    pass
