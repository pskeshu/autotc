class Flask:
    def __init__(self, name=None, surface_area=None):
        self.name = name
        self.contains = list()
        self.surface_area = None #cm**2

    def add(self, item):
        self.contains.append(item)

    def __repr__(self):
        return f"Flask(type={self._type}, contains={self.contains}, surface={self.surface_area}"



class T25(Flask):
    def __init__(self, name="t25", contains=None, surface_area=25):
        super().__init__(name, contains, surface_area)
        
    
     