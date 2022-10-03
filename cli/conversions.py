import json
import os
from typing import Optional

reactions_filepath = os.path.join(os.path.dirname( __file__ ), '..', "reactions.json")
with open(reactions_filepath, "r") as f:
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
                x = f" + {reag} → {prod}"
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

    return start, end


def generate_problem():
    """
    Generate a problem set
    Problem set contains start substrate,end substrate, solution, solution set
    Returns a tuple
    """
    from random import choice

    start = choice(list(reactions))
    solution = choice(list(reactions[start]))
    solutions = [solution]
    for i in range(2):
        buffer = choice(list(reactions[choice(list(reactions))]))
        if buffer not in solutions:
            solutions.append(buffer)
    end = reactions[start][solution]
    return start, end, solution, solutions
