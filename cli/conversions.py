import json
import os
import random
from typing import Optional, Tuple, List
from collections import deque

reactions_filepath = os.path.join(os.path.dirname(__file__), "..", "reactions.json")
with open(reactions_filepath, "r") as f:
    reactions = json.load(f)


def find_conversion_path(starting_compound: str, target_compound: str) -> Optional[List[Tuple[str, str, str]]]:
    """
    Finds a conversion path from `starting_compound` to `target_compound` using the given `reactions` dictionary.

    Args:
    - starting_compound (str): The starting compound for the conversion path.
    - target_compound (str): The target compound for the conversion path.

    Returns:
    - A list of tuples representing the conversion path from `starting_compound` to `target_compound`, where each tuple
      represents a reaction step and contains three strings: the reactant, reagent, and product. If no conversion path
      exists, returns None.
    """
    queue = deque([(starting_compound, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == target_compound:
            return path

        visited.add(current)

        for reagent, product in reactions.get(current, {}).items():
            if product not in visited:
                new_path = path + [(current, reagent, product)]
                queue.append((product, new_path))

    return None


def generate_conversion_problem(start: Optional[str] = None, max_steps: int = 3) -> Tuple[str, str]:
    """
    Generates a conversion problem that can be solved in up to `max_steps` steps.
    Returns the starting and target compound.
    """
    available_compounds = list(reactions.keys())
    if start is None:
        start = random.choice(available_compounds)
    else:
        available_compounds.remove(start)
        
    target = None
    while target is None:
        target = random.choice(available_compounds)
        if target == start or target in reactions[start].values():
            target = None
        else:
            for _ in range(max_steps - 1):
                try:
                    available_reagents = [reagent for reagent, product in reactions[target].items() if product not in (start, target)]
                    if not available_reagents:
                        target = None
                        break
                    reagent = random.choice(available_reagents)
                    target = reactions[target][reagent]
                    if target == start:
                        target = None
                        break
                except KeyError:
                    target = None
                    break

    return start, target


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
