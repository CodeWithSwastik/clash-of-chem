import json
with open("reactions.json","r") as f:
    reactions = json.load(f)

def convert(from_compound, to_compound):
    for sub in reactions:        
        for reag, prod in reactions[sub].items():
            if prod == to_compound:
                x = f" + {reag} --> {prod}"
                if sub == from_compound:
                    return sub + x
                else:
                    c = convert(from_compound, sub)
                    if c:
                        return c + x

print(convert("methane", "butane"))
