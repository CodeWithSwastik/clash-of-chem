import json
with open("reactions.json","r") as f:
    reactions = json.load(f)

def convert(from_compound: str, to_compound: str, avoid: list | None = None):
    """
    Uses backtracking to convert from_compound to to_compound.
    avoid is an optional list of compounds to avoid during conversion.
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

print(convert("ethene", "ethene"))
