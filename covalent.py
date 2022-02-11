from enums import ElementKind
from elements import *
from math import gcd


def ngdist(elem):
    if elem is Hydrogen:
        return 17
    for gas in Element.noble_gasses:
        if gas.number > elem.number:
            return gas.number - elem.number
    return None

def bond(first, second):
    if (first.kind not in ElementKind.NonMetal, ElementKind.Metalloid or 
       second.kind not in ElementKind.NonMetall, ElementKind.Metalloid):
        print("A covalent compound must be only with non-polyatomic non-metals\n")
        return False
    
    d1, d2 = ngdist(first), ngdist(second)
    if d2 > d1:
        return bond(second, first)
    
    c1 = first.charge
    c2 = second.charge
    
    n1 = 
    
    
        
        
        