a = {1,2,3}
b = [4,5]

# vvv TypeError: unhashable type: 'list' vvv

# a.add(b)

# ^^^ reason: ^^^
# set elements need to be hashable,
# and since lists are mutable, they're unhashable
# and therefore cannot be added to sets.
# (כתבתי באנגלית כי נוח יותר להסביר)