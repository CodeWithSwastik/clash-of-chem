import json
from re import L
from typing import Optional

with open("reactions.json","r") as f:
    reactions = json.load(f)

def convert(from_compound: str, to_compound: str, avoid: Optional[list] = None):
    """
    Uses backtracking to convert from_compound to to_compound.
    avoid is an optional list of compounds to avoid during conversion.
    Does not find the most optimal solution, this function only returns the
    first solution it finds.
    """
    if avoid is None:
        avoid = []
    
    for sub in reactions:        
        for reag, prod in reactions[sub].items():
            if prod == to_compound and sub not in avoid:
                x = f" + {reag} --> {prod}"
                avoid.append(sub)
                if sub == from_compound:
                    return sub + x
                else:
                    c = convert(from_compound, sub, avoid)
                    if c:
                        return c + x


def generate_conversion_problem(start: Optional[str] = None, length: int = 3):
    """
    Generates a conversion problem that can be solved in upto `length` steps.
    """
    import random

    if start is None:
        start = random.choice(list(reactions))

    c = 0
    end = start

    while length:
        prev = end
        end = random.choice(list(reactions[prev].values()))
        
        if c == 10000:
            break

        if length > 0 and end not in reactions:
            c += 1
            end = prev
            continue
        length -= 1

    return start,end


print("\n\nClash of Chemists CLI")
s, e = generate_conversion_problem()
print(f"Q. Convert {s} to {e}")
input("Press enter to see 1 possible solution.")
print(convert(s,e))
