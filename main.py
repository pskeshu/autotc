from devices import Incubator, Microscope
from organisms import HeLa
from consumables import T25
from workflow import CellCulture
from reagents import MMS, NQO

if __name__ == "__main__":
    # config
    ex = CellCulture()
    ex.with_cells(HeLa())
    ex.incubator(Incubator())
    ex.microscope(Microscope())
    
    # application
    ex.image_cells(groups=["control", MMS, NQO])