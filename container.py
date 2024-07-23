from datetime import datetime

class Container:
    # any entity that can contain cells
    def __init__(self):
        # initate container with no cells
        self.cell_count = 0 # current cell count
        self.transfer_date = None
        self.parent = None

        
    def transfer_cells(self, to, ratio, timestamp):
        to.parent = self
        # to another container
        to.cell_count = int(self.cell_count * ratio)
        to.timestamp = timestamp


class Flask(Container):
    # A flask is a container which maintains cells on its surface
    
    def __init__(self, name=None, surface_area=None):
        super().__init__()
        self.name = name
        self.surface_area = 25 #cm**2

    def time_since_seed(self):
        now = datetime.now()
        elapsed = now - self.timestamp
        return elapsed
    
    def growth_function(self, elapsed_time_hours, start_cells, doubling_time_hours):
        now_cells = start_cells * (2 ** (elapsed_time_hours/doubling_time_hours))
        return now_cells

    def current_cells(self):
        elapsed_time_hours = self.time_since_seed().total_seconds()/3600
        start_cells = self.cell_count
        doubling_time_hours = self.parent.cell.doubling_time

        value = self.growth_function(elapsed_time_hours, start_cells, doubling_time_hours)
        return int(value)
    
    def __repr__(self):
        time_since_seed = self.time_since_seed().total_seconds()/3600
        curr_cell_num = self.current_cells()

        return f"Flask(Time={time_since_seed:.2f}h, cells={curr_cell_num:_})"


class FrozenVial(Container):
    # A container source of a number of frozen cells
    def __init__(self, cell, cell_count):
        super().__init__()
        self.cell = cell
        self.cell_count = cell_count

    def __repr__(self):
        return f"FrozenVial(cell={self.cell})"