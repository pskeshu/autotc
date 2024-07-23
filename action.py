from container import Container


def transfer(from_container, to_containers, to_proportions):
    # one to one or many container transfer
    if not isinstance(from_container, Container):
        raise(TypeError)
    
    for to_container, to_proportion in zip(to_containers, to_proportions):
        from_container.transfer_cells(to_container, to_proportion)

        

