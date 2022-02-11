import enums
import elements

class PolyatomicCompound(object):
    __slots__ = (
        #The charge of the polyatomic compound
        "charge",
        #The quantities of its elements (list of pairs). 
        "components",
        #Its kind
        "kind",
        #The name of the polyatomic compound
        "name"
    )
    
    registry = {}
    
    def __new__(cls, charge, components, name):
        self = object.__new__(cls)
        self.charge = int(charge)
        self.components = components
        self.name = name
    
        if self.charge < 0:
            self.kind = enums.PolyatomicKind.Negative
        elif self.charge > 0:
            self.kind = enums.PolyatomicKind.Positive
        else:
            self.kind = enums.PolyatomicKind.Uncharged
            
        cls.registry[self.symbol()] = self
        cls.registry[self.name] = self
        
        return self
    
    @classmethod
    def oxycompounds(cls, element, num_oxygens, charge):
        prefixes = ["Per", "", "", "hypo"]
        suffixes = ["ate", "ate", "ite", "ite"]
        results = []
        count = 0
        
        for i in range(num_oxygens + 1, num_oxygens - 3, -1):
            results.append(cls(charge, [(element, 1), (elements.Oxygen, i)], prefixes[count] + element.ion[0:-3] + suffixes[count]))
            count+=1
        return results
    
    def symbol(self):
        s = self.uncharged_symbol()
        if self.charge > 0:
            s += "+"
        s += str(self.charge)
        if abs(self.charge) == 1:
            return s[0:-1]
        return s
    
    def uncharged_symbol(self):
        s = ""
        for element, count in self.components:
            s += element.symbol
            if count != 1:
                s += str(count)
        return s
        
    
    def __repr__(self):
        return self.symbol()

### --- Oxycompounds --- ###
#Halogen compounds
Perflourate, Flourate, Flourite, Hypoflourite = \
    PolyatomicCompound.oxycompounds(elements.Flourine, 3, -1)
Perchlorate, Chlorate, Chlorite, Hypochlorite = \
    PolyatomicCompound.oxycompounds(elements.Chlorine, 3, -1)
Perbromate, Bromate, Bromite, Hypobromite = \
    PolyatomicCompound.oxycompounds(elements.Bromine, 3, -1)
Periodate, Iodate, Iodite, Hypoiodate = \
    PolyatomicCompound.oxycompounds(elements.Iodine, 3, -1)

#Period 1 compounds (excluding flourine series)
Percarbonate, Carbonate, Carbonite, Hypocarbonate = \
    PolyatomicCompound.oxycompounds(elements.Carbon, 3, -2)
Pernitrate, Nitrate, Nitrite, Hyponitrite = \
    PolyatomicCompound.oxycompounds(elements.Nitrogen, 3, -1)

#Period 2 compounds (excluding chlorine series)
Perphosphate, Phosphate, Phosphite, Hypophosphite = \
    PolyatomicCompound.oxycompounds(elements.Phosphrous, 4, -3)
Persulfate, Sulfate, Sulfite, Hyposulfite = \
    PolyatomicCompound.oxycompounds(elements.Sulfur, 4, -2)

#Period 3 compounds
Perarsenate, Arsenate, Arsenite, Hypoarsenite = \
    PolyatomicCompound.oxycompounds(elements.Arsenic, 4, -3)
Perselenate, Selenate, Selenite, Hyposelenite = \
    PolyatomicCompound.oxycompounds(elements.Selenium, 4, -2)

### --- Other compounds ---###
Bicarbonate = PolyatomicCompound(-1, [
    (elements.Hydrogen, 1), (elements.Carbon, 1), (elements.Oxygen, 3)
], "bicarbonate");

Hydroxide = PolyatomicCompound(-1, [
    (elements.Oxygen, 1), (elements.Hydrogen, 1),
], "hydroxide")

Ammonia = PolyatomicCompound(0, [
    (elements.Nitrogen, 1), (elements.Hydrogen, 3)
],  "ammonia")

Ammonium = PolyatomicCompound(1, [
    (elements.Nitrogen, 1), (elements.Hydrogen, 4)
], "ammonium")

Acetate = PolyatomicCompound(-1, [
    (elements.Carbon, 1), (elements.Hydrogen, 3), (elements.Carbon, 1),
    (elements.Oxygen, 1), (elements.Oxygen, 1)
], "acetate")

#Register simplified acetate in registry
PolyatomicCompound.registry["C2H3O2"] = Acetate

Peroxide = PolyatomicCompound(-2, [
    (elements.Oxygen, 2)
], "peroxide")

