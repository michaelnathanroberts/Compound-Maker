#Define ionic (and metallic) bonding

import classes
import elements
import enums
import math

def bond(first, second):
    if second.kind is enums.ElementKind.Metal:
        if first.kind is enums.ElementKind.Metal:
            print(f"Formula: {first.symbol}{second.symbol}")
            print(f"IUPAC Name: {first.name.lower()};{second.name.lower()}")
            print(f"Lewis Diagram: N/A\n")
            return True
    
    if first.kind in (enums.ElementKind.Metalloid, enums.ElementKind.NonMetal):
        print("Covalent compounds are not supported")
        return False
    
    if second.kind is enums.PolyatomicKind.Positive:
        print("Polyatomic compounds cannot form metallic bonds")   
        return False
            
    
    if first.kind is enums.PolyatomicKind.Negative:
        print("Polyatomic compounds cannot form covalent bonds")   
        return False  
    
    if first.kind is enums.ElementKind.NobleGas or second.kind is enums.ElementKind.NobleGas:
        print("Noble gasses are not supported")
        return False
    
    if first.kind is enums.PolyatomicKind.Uncharged or second.kind is enums.PolyatomicKind.Uncharged:
        print("Uncharged polyatomic compounds are not supported")   
        return False
    
    if first.kind is enums.ElementKind.Unusable or second.kind is enums.ElementKind.Unusable:
        print("Unusuable elements (elements with undetermined charges) are not supported")
        return False
    
    if isinstance(first, elements.Element):
        charges = [c for c in first.charges if c > 0]
    else:
        charges = [first.charge]
    for first_charge in charges:
        if first_charge is ...:
            break
        if isinstance(second, elements.Element):
            second_charge = abs(second.charges[-1])
        else:
            second_charge = abs(second.charge)
        gcf = math.gcd(first_charge, second_charge)
        first_number = first_charge // gcf;
        second_number = second_charge // gcf;
        if first_number == 1:
            first_number = ""
        if second_number == 1:
            second_number  = ""
        
        first_symbol = None
        second_symbol = None
        second_ion_name = None
        first_formula = ""
        if isinstance(first, elements.Element):
            first_symbol = first.symbol
            first_formula = f"Formula: {first_symbol}{second_number}"
        else:
            first_symbol = first.uncharged_symbol() 
            if second_number != "":
                first_formula = f"Formula:({first_symbol}){second_number}"
            else:
                first_formula = f"Formula:({first_symbol})"            
        if isinstance(second, elements.Element):
            second_symbol = second.symbol
            second_ion_name = second.ion
            print(first_formula + f"{second_symbol}{first_number}")
        else:
            second_symbol = second.uncharged_symbol()
            second_ion_name = second.name
            if first_number != "":
                print(first_formula + f"({second_symbol}){first_number}")
            else:
                print(first_formula + f"{second_symbol}")   
                  
            
        
        numeral = ""
        if len(charges) > 1:
            numeral = f"({roman_numeral(first_charge)})"
            
        print(f"IUPAC Name: {first.name}{numeral} {second_ion_name}")
        
        first_charge = "" if first_charge == 1 else first_charge
        second_charge = "" if second_charge == 1 else second_charge
        print(f"Lewis Diagram: {(second_number)}[{first_symbol}]+{first_charge}",
              f"{(first_number)}[{second_symbol}]-{second_charge}", sep=" ")
        print("\n")
        
    return True
              
        
def roman_numeral(num):
    if isinstance(num, str):
        num = 1
    s = ""
    if num >= 9:
        raise AssertionError("Unsupported number")
    if 4 < num:
        s += "V"
    if num % 5 == 4:
        s += "IV"
    else:
        s += "I" * (num % 5)
    return s

    
    
    
        
    
    
    

    
 
        
    
    