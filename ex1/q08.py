import sys

def parts(input_set):
    new_set = set()
    for item in input_set:
        current_set = new_set.copy()
        for in_set in current_set:
            new_set.add(set(in_set).add(item))
        new_set.add(item)
    new_set.add("")
    return new_set

print(parts({"a","b","c"}))