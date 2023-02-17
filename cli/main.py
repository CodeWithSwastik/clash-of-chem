from conversions import generate_conversion_problem, find_conversion_path

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
WHITE = "\033[1;37m"
ENDC = "\033[0m"

print(RED + "\n\nClash of Chemists CLI\n\n" + ENDC)
for qno in range(1, int(input("How many conversions do you want to practice?:")) + 1):
    s, e = generate_conversion_problem()
    print(f"Q{qno}. Convert {GREEN + s + ENDC} to {GREEN + e + ENDC}")
    input("Press enter to see 1 possible solution.")
    cs = find_conversion_path(s, e)
    for i, x in enumerate(cs):
        reactant, reagent, product = x
        print(f"{WHITE}Step {RED}{i+1}: {YELLOW + reactant + RED} + {GREEN + reagent + RED} → {WHITE + product + ENDC}")
    print("\n\n")
