c = {"a","b","c"}
d = frozenset(c)
print(f"Set c: {c}")
print(f"Set d: {d}")

c.add("d")
print(f"Set c: {c}")
print(f"Set d: {d}")

print(f"Frozensets are immutable: {not(c is d)}")