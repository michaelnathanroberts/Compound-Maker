import elements
import enums
import polyatoms

def form(product):
    if product.kind in (
        enums.ElementKind.Metal, enums.ElementKind.NobleGas, enums.ElementKind.Hydrogen, 
        enums.PolyatomicKind.Positive, enums.PolyatomicKind.Uncharged, enums.ElementKind.Unusable
    ):
        print("Only unmetallic metalloids, non-metals (excluding hydrogen and noble gasses),", 
              "and negative polyatomic ions may form acids")
        return False
    
    if product in (elements.Oxygen, polyatoms.Hydroxide):
        print("Formula: H2O")
        print("IUPAC Name: dihydrogen monoxide")
        print("Lewis Diagram: H-**O**-H")
        return True
    
    hydrogen = elements.Hydrogen
    num_hydrogens = 0
    symbol = ""
    if isinstance(product, elements.Element):
        num_hydrogens = abs(product.charges[-1])
        symbol = product.symbol
    else:
        num_hydrogens = abs(product.charge)
        symbol = product.uncharged_symbol()
    
    if num_hydrogens == 1:
        num_hydrogens = ""
    

    print(f"Formula: H{num_hydrogens}{symbol}")

    
    if isinstance(product, elements.Element):
        if product is elements.Sulfur:
            product_name = "sulfur"
        else:
            product_name = product.ion[0: -3]
        print(f"IUPAC Name: hydro{product_name}ic acid")
    else:
        if product in [polyatoms.Persulfate, polyatoms.Sulfate, polyatoms.Sulfite, polyatoms.Hyposulfite]:
            product_name = "sulfur"
        else:
            product_name = product.name[0: -3]
        suffix = ""
        if product.name[-3:] == "ite":
            suffix = "ous"
        if product.name[-3:] == "ate":
            suffix = "ic"
        print(f"IUPAC Name: {product_name}{suffix} acid")
    print(f"Lewis Diagram {num_hydrogens}[H]+ [{symbol}]-{num_hydrogens}")
    print("\n")
    return True
    
