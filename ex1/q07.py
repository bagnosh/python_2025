import csv

data = {}

with open('streets.csv', newline = '') as input_file:
    reader = csv.DictReader(input_file)
    for row in reader:
        key = row['street_name']
        if key in data:
            data[key] += 1
        else:
            data[key] = 1

sorted_data = dict(sorted(data.items(), key = lambda item: item[1], reverse = True))

top_ten = dict(list(sorted_data.items())[:10])

print("The most common street names are:")
print("----------")
for key, value in top_ten.items():
    print(f"Street: {key[::-1]},  amount: {value}")