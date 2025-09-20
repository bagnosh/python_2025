import sys
from q07 import Person

persons = []

def sort_persons_by(names, direction):
    #if direction is not ("first" or "last"):
    #    raise ValueError("must have 'first' or 'last' as sorting directive")
    if direction is "first":
        sorted_persons = sorted(names, key = lambda person: person.first)
    if direction is "last":
        sorted_persons = sorted(names, key = lambda person: person.last)
    return sorted_persons

if len(sys.argv) < 2:
    raise ValueError("Must include file in command line")
with open(sys.argv[1], "r") as f:
    for line in f:
        name = line.split()
        new_person = Person(name[0], name[1])
        persons.append(new_person)

for item in persons:
    print(f"{item.first} {item.last}")

persons_by_first = sort_persons_by(persons, "first")
print("\nSorted by first name: \n")
for item in persons_by_first:
    print(f"{item.first} {item.last}")

persons_by_last = sort_persons_by(persons, "last")
print("\nSorted by last name: \n")
for item in persons_by_last:
    print(f"{item.first} {item.last}")
