import enum

### --- Kinds of Elements --- ###

class ElementKind(enum.Enum):
    #Hydrogen is in its own category
    Hydrogen = enum.auto()
    #Metals
    Metal = enum.auto()
    #Metalloids
    Metalloid = enum.auto()
    #Noble gasses
    NobleGas = enum.auto()
    #Non-metals
    NonMetal = enum.auto()
    #Unusables
    Unusable = enum.auto()
    
### --- Kinds of PolyatomicIons --- ###
class PolyatomicKind(enum.Enum):
    Positive = enum.auto()
    Negative = enum.auto()
    Uncharged = enum.auto()