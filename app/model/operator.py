class Operator:
    """
    class to represent object from operators.db
    """
    def __init__(self, *args):
        """
        constructor
        """
        self.id,\
        self.unit,\
        self.origin,\
        self.alias,\
        self.nationality,\
        self.faction,\
        self.rarity,\
        self.season,\
        self.ref_status,\
        self.ref1,\
        self.ref2,\
        self.ref3 = args
        