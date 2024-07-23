from container import FrozenVial, Flask
from organisms import U2OS
from action import transfer

if __name__ == "__main__":
    # define containers
    frozenvial =  FrozenVial(cell=U2OS(), cell_count=10E5)
    t25_flasks = [Flask(surface_area=25)] * 2

    # thaw frozenvials to flasks
    transfer(frozenvial, t25_flasks, [0.5, 0.5], when=(2024, 7, 22, 11, 15))


