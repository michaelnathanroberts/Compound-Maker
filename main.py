import acids
import elements
import ionic
import polyatoms

def get_input():
    messages = ["First element: ", "Second element: "]
    results = [None, None]
    
    for i in range(2):
        data = input(messages[i])
        value = None
        elem = elements.Element.registry.get(data.strip(), None)
        polyatom = polyatoms.PolyatomicCompound.registry.get(data.strip(), None)
        elem_name = elements.Element.registry.get(data.strip()[0].upper() + data.strip()[1:].lower(), None)
        patm_name = polyatoms.PolyatomicCompound.registry.get(data.strip()[0].upper() + data.strip()[1:], None)
        if elem is not None:
            value = elem
        elif polyatom is not None:
            value = polyatom
        elif elem_name is not None:
            value = elem_name
        elif patm_name is not None:
            value = patm_name
        else:
            print(f"{data} not an element or a polyatomic compound or unsupported")
            return False, None
        results[i] = value
    return True, results

def main():
    stop = False
    while (not stop):
        sucess, results = get_input()
        if sucess:
            print("\n")
            if results[0] is elements.Hydrogen and results[1] is not polyatoms.Peroxide:
                acids.form(results[1])
            else:
                ionic.bond(*results)
        else:
            print("\n")        
        stop = not input("Again (y/n): ")[0] == 'y'
      
if __name__ == "__main__":
    main()
        
    
            
    
