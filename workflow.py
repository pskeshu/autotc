class Workflow:
    # a bunch of Process
    pass


class Process:
    # a bunch of Actions
    pass


class Action:
    # Actions on Actionables (Flasks, Cells, Media) 
    pass


def growth_function(start_time, end_time, start_cells, doubling_time):
    end_cells = 0
    
    return end_cells


class CellCulture:
    thaw = Process()
    # from FrozenVial to Flask
    # select FrozenVial Action()
    # warm Media Action()
    # new Flask Action()
    # add Cells to Flask Action()


    grow = Process()
    # from Flask to ConfluentFlask
    # for a Flask, growth_fn with seed_time, seed_density, cell_doublingtime


    split = Process()
    # from Flask make SeedableCells
    # from SeedableCells to Dish
    # from SeedableCells to Flask 
