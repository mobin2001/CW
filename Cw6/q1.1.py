class Vehicle:
    def __init__(self,make,model,year):
        self._make = make
        self._model = model
        self._year = year

    def display(self):
        return self.model,self.year,self.make
    @property
    def make(self):
        return self._make
    @make.setter
    def make(self,value):
        self._make = value.upper()
v1 = Vehicle('i','b',3)
# print(v1.display())
#v1.make('hi')

raise ValueError('erorrrrrr')