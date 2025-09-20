a = {1,2,3}
b = a
print(f"Set a: {a}")
print(f"Set b: {b}")

a.add(4)
print(f"Set a: {a}")
print(f"Set b: {b}")

print(f"Sets are immutable: {not(a is b)}")