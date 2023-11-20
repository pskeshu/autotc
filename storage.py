
class FrozenVial:
    def __init__(self, date_frozen=None, frozen_by=None):
        self.contains = dict()
        self.date_frozen = date_frozen
        self.frozen_by = frozen_by

    def __repr__(self):
        return f"FrozenVial(contains={self.contains})"