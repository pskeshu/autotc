class Container:
    # any entity that can contain cells
    def __init__(self):
        # initate container with no cells
        self.cell_count = 0

    def transfer_cells(self, to, ratio):
        # to another container
        to.cell_count = int(self.cell_count * ratio)


class Flask(Container):
    # A flask is a container which maintains cells on its surface
    
    def __init__(self, name=None, surface_area=None):
        super().__init__()
        self.name = name
        self.surface_area = None #cm**2
        
    def __repr__(self):
        return f"Flask(cells={self.cell_count:_}"

class FrozenVial(Container):
    # A container source of a number of frozen cells
    def __init__(self, cell, cell_count):
        super().__init__()
        self.cell = cell
        self.cell_count = cell_count

    def thaw_to(self,flasks=None, counts_ratio=None):
        
        pass
        

    def __repr__(self):
        return f"FrozenVial(cell={self.cell})"