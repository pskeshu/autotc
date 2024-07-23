from reagents import DMEM


class AdherantCell:
    def __init__(self, name, doubling_time) -> None:
        self.name = name # human readable name
        self.doubling_time = doubling_time # in hours

    def __repr__(self):
        return f"Cell(name={self.name}, doubling_time={self.doubling_time})"


class HeLa(AdherantCell):
    def __init__(self, name="HeLa", doubling_time=24) -> None:
        super().__init__(name, doubling_time)
        # media for this cell
        self.media = DMEM(fbs=10, if_antibiotics=False)


class HumanFibroblasts(AdherantCell):
    pass


class U2OS(AdherantCell):
    def __init__(self, name="U2OS", doubling_time=24) -> None:
        super().__init__(name, doubling_time)
        # media for this cell
        self.media = DMEM(fbs=10, if_antibiotics=False)

class A549:
    pass


class MEF:
    pass
