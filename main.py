from conversions import generate_conversion_problem, convert

RED = "\033[1;31;40m"
GREEN = "\033[1;32;40m"
YELLOW = "\033[1;33;40m"
WHITE = "\033[1;37;40m"
ENDC = "\033[0m"

print(RED + "\n\nClash of Chemists CLI\n\n" + ENDC)
s, e = generate_conversion_problem()
print(f"Q. Convert {GREEN + s + ENDC} to {GREEN + e + ENDC}")
input("Press enter to see 1 possible solution.")
cs = convert(s,e).split(" ")
for i,x in enumerate(cs):
    if x in "+→":
        print(WHITE + x + ENDC, end = ' ')
    elif x in (s,e) or cs[i-1]=="→":
        print(GREEN + x + ENDC, end = ' ')
    else:
        print(YELLOW + x + ENDC, end = ' ')

print("\n\n")