from container import FrozenVial, Flask
from organisms import U2OS
from action import transfer

if __name__ == "__main__":
    # config
    frozenvial =  FrozenVial(cell=U2OS(), cell_count=10E6)
    t25_flasks = [Flask(surface_area=25)] * 2
    transfer(frozenvial, t25_flasks, [0.5, 0.5])


