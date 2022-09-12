from conversions import generate_conversion_problem, convert

print("\n\nClash of Chemists CLI\n\n")
s, e = generate_conversion_problem()
print(f"Q. Convert {s} to {e}")
input("Press enter to see 1 possible solution.")
print(convert(s,e))