import enums

class Element(object):
    __slots__ = (
        #A list of the element's charges
        "charges",
        #The ion's name"
        "ion",
        #The ElementKind of the element
        "kind",
        #Name of the element
        "name",
        #Atomic number of the element
        "number",
        #Symbol of the element
        "symbol",
    )
    
    count = 1
    instances = []
    registry  = {}
    noble_gasses = []
    
    def __new__(cls, charges, ion, kind, name, symbol):
        self = object.__new__(cls)
        self.charges = charges
        self.ion = str(ion)
        self.kind = kind
        self.name = str(name)
        self.number = cls.count
        self.symbol = str(symbol)
        
        cls.count += 1
        cls.instances.append(self)
        cls.registry[self.symbol] = self
        cls.registry[self.name] = self
        
        if kind is enums.ElementKind.NobleGas:
            cls.noble_gasses.append(self)        
        return self
        
        
    def __repr__(self):
        charges = []
        for i in self.charges:
            if i is not None:
                charges.append(i)
        s = f"{str(self.number).zfill(3)}: {self.name}({self.symbol}){charges}"
        return s
    
    def zeff(self):
        for ng in self.noble_gasses[::-1]:
            if ng.number < self.number:
                return self.number - ng.number
        else:
            return self.number
    
### ---State the element types --- ###
HydrogenKind = enums.ElementKind.Hydrogen
Metal = enums.ElementKind.Metal
Metalloid = enums.ElementKind.Metalloid
NobleGas = enums.ElementKind.NobleGas
NonMetal = enums.ElementKind.NonMetal
Unusable = enums.ElementKind.Unusable

### --- Define the elements --- ###
#Period 1
Hydrogen = Element([1, -1], "hydride", HydrogenKind, "Hydrogen", "H")
Helium = Element([0], None, NobleGas, "Helium", "He")

#Period 2
Lithium = Element([1], None, Metal, "Lithium", "Li")
Beryllium = Element([2], None, Metal, "Beryllium", "Be")
Boron = Element([-3], "boride", Metalloid, "Boron", "B")
Carbon = Element([-4], "carbonide", NonMetal, "Carbon", "C")
Nitrogen = Element([-3], "nitride", NonMetal, "Nitrogen", "N")
Oxygen = Element([-2], "oxide", NonMetal, "Oxygen", "O")
Flourine = Element([-1], "flouride", NonMetal, "Flourine", "F")
Neon = Element([0], None, NobleGas, "Neon", "Ne")

#Period 3
Sodium = Element([1], None, Metal, "Sodium", "Na")
Magnesium = Element([2], None, Metal, "Magnesium", "Mg")
Aluminum = Element([3], None, Metal, "Aluminium", "Al")
Silicon = Element([-4], "silicide", Metalloid, "Silicon", "Si")
Phosphrous = Element([-3], "phosphide", NonMetal, "Phosphrous", "P")
Sulfur = Element([-2], "sulfide", NonMetal, "Sulfur", "S")
Chlorine = Element([-1], "chloride", NonMetal, "Chlorine", "Cl")
Argon = Element([0], None, NobleGas, "Argon", "Ar")

#Period 4
Potassium = Element([1], None, Metal, "Potassium", "K")
Calcium = Element([2], None, Metal, "Calcium", "Ca")
Scandium = Element([3], None, Metal, "Scandium", "Sc")
Titanium = Element([4], None, Metal, "Titanium", "Ti")
Vanadium = Element([3, 4, 5], None, Metal, "Vanadium", "V")
Chromium = Element([2, 3, 6], None, Metal, "Chromium", "Cr")
Manganese = Element([2, 4, 7], None, Metal, "Manganese", "Mn")
Iron = Element([2, 3], None, Metal, "Iron", "Fe")
Cobalt = Element([2, 3], None, Metal, "Cobalt", "Co")
Nickel = Element([2, 3], None, Metal, "Nickel", "Ni")
Copper = Element([1, 2], None, Metal, "Copper", "Cu")
Zinc = Element([2], None, Metal, "Zinc", "Zn")
Gallium = Element([3], None, Metal, "Gallium", "Ga")
Germanium = Element([4], None , Metal, "Germanium", "Ge")
Arsenic = Element([-3], "arsenide", Metalloid, "Arsenic", "As")
Selenium = Element([-2], "selenide", NonMetal, "Selenium", "Se")
Bromine = Element([-1], "bromide", NonMetal, "Bromine", "Br")
Krypton = Element([0], None, NobleGas, "Krypton", "Kr")

#Period 5
Rubidium = Element([1], None, Metal, "Rubidium", "Rb")
Strontium = Element([2], None, Metal, "Strontium", "Sr")
Yittrium = Element([3], None, Metal, "Yittrium", "Y")
Zirconium = Element([4], None, Metal, "Zirconium", "Zr")
Niobium = Element([5], None, Metal, "Niobium", "Nb")
Molybdenum = Element([4, 6], None, Metal, "Molybdenum", "Mo")
Technetium = Element([4, 7], None, Metal, "Technetium", "Tc")
Ruthenium = Element([3, 4], None, Metal, "Ruthenium", "Ru")
Rhodium = Element([3], None, Metal, "Rhodium", "Rh")
Palladium = Element([2, 4], None, Metal, "Palladium", "Pd")
Silver = Element([1], None, Metal, "Silver", "Ag")
Cadmium = Element([2], None, Metal, "Cadmium", "Cd")
Indium = Element([3], None, Metal, "Indium", "In")
Tin = Element([2, 4], None, Metal, "Tin", "Sn")
Antimony = Element([3, 5], None, Metal, "Antimony", "Sb")
Tellurium = Element([-2], "telluride", Metalloid, "Tellurium", "Te")
Iodine = Element([-1], "iodine", NonMetal, "Iodine", "I")
Xenon = Element([0], None, NobleGas, "Xenon", "Xe")

#Early Period 6 
Caesium = Element([1], None, Metal, "Caesium", "Cs")
Barium = Element([2], None, Metal, "Barium", "Ba")

#Lanthanides
Lanthanum = Element([3], None, Metal, "Lanthanum", "La")
Cerium = Element([3], None, Metal, "Cerium", "Ce")
Praseodymium = Element([3], None, Metal, "Praseodymium", "Pm")
Neodymium = Element([3], None, Metal, "Neodymium", "Nd")
Promethium = Element([3], None, Metal, "Promethium", "Pr")
Samarium = Element([3], None, Metal, "Samarium", "Sm")
Europium = Element([3], None, Metal, "Europium", "Eu")
Gadolinium = Element([3], None, Metal, "Gadolinium", "Gd")
Terbium = Element([3], None, Metal, "Terbium", "Tb")
Drysprosium = Element([3], None, Metal, "Drysprosium", "Dy")
Holmium = Element([3], None, Metal, "Holmium", "Ho")
Erbium = Element([3], None, Metal, "Erbium", "Er")
Thulium = Element([3], None, Metal, "Thulium", "Tm")
Ytterbium = Element([3], None, Metal, "Ytterbium", "Yb")
Lutetium = Element([3], None, Metal, "Lutetium", "Lu")

#Late Period 6
Hafnium = Element([4], None, Metal, "Hafnium", "Hf")
Tantalum = Element([3, 5], None, Metal, "Tantalum", "Ta")
Tungsten = Element([4, 6], None, Metal, "Tungsten", "W")
Rhenium = Element([7], None, Metal, "Rhenium", "Re")
Osmium = Element([4], None, Metal, "Osmium", "Os")
Irdium = Element([3, 4], None, Metal, "Irdium", "Ir")
Platinum = Element([2, 4], None, Metal, "Platinum", "Pt")
Gold = Element([1, 3], None, Metal, "Gold", "Au")
Mercury = Element([1, 2], None, Metal, "Mercury", "Hg")
Thallium = Element([1, 3], None, Metal, "Thallium", "Tl")
Lead = Element([2, 4], None, Metal, "Lead", "Pb")
Bismuth = Element([3, 5], None, Metal, "Bismuth", "Bi")
Polonium = Element([2, 4], None, Metal, "Polonium", "Po")
Astatine = Element([-1], "astatide", Metalloid, "Astatine", "At")
Radon = Element([0], None, NobleGas, "Radon", "Rn")

#Early Period 7
Francium = Element([1], None, Metal, "Francium", "Fr")
Radium = Element([2], None, Metal, "Radium", "Ra")

#Actinides
Actinium = Element([3], None, Metal, "Actinium", "Ac")
Thorium = Element([4], None, Metal, "Thorium", "Th")
Protactinium = Element([5], None, Metal, "Protactinium", "Pa")
Uranium = Element([6], None, Metal, "Uranium", "U")
Neptunium = Element([4, 7], None, Metal, "Neptunium", "Np")
Plutonium = Element([4], None, Metal, "Plutonium", "Pu")
Americium = Element([3], None, Metal, "Americium", "Am")
Curium = Element([3], None, Metal, "Curium", "Cm")
Berkelium = Element([3], None, Metal, "Berkelium", "Bk")
Californium = Element([3], None, Metal, "Californium", "Cf")
Einsteinium = Element([3], None, Metal, "Einsteinium", "Es")
Fermium = Element([3], None, Metal, "Fermium", "Fm")
Mendelevium = Element([3], None, Metal, "Mendelevium", "Md")
Nobelium = Element([2], None, Metal, "Nobelium", "No")
Lawrencium = Element([3], None, Metal, "Lawrencium", "Lr")

#Late Period 7
Rutherfordium = Element([4], None, Metal, "Rutherfordium", "Rf")

#Period 7 elements with undetermined charges
Dubnium = Element([], None, Unusable, "Dubnium", "Db")
Seaborgium = Element([], None, Unusable, "Seaborgium", "Sg")
Bohrium = Element([], None, Unusable, "Bohrium", "Bh")
Hassium = Element([], None, Unusable, "Hassium", "Hs")
Meitnerium = Element([], None, Unusable, "Meitnerium", "Mt")
Darmstadtium = Element([], None, Unusable, "Darmstadtium", "Ds")
Roentgentium = Element([], None, Unusable, "Roentgentium", "Rg")
Copernicium = Element([], None, Unusable, "Copernicium", "Cn")
Nihonium = Element([], None, Unusable, "Nihonium", "Nh")
Flerovium = Element([], None, Unusable, "Flerovium", "Fl")
Moscovium = Element([], None, Unusable, "Moscovium", "Mc")
Livermorium =Element([], None, Unusable, "Livermorium", "Lv")
Tennessine = Element([], None, Unusable, "Tennessine", "Tn")
Oganesson = Element([], None, Unusable, "Oganesson", "Og")

