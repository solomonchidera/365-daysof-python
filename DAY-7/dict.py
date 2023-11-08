dict = {'Name': 'John', 'Age': '29', 'Marriage status': 'Single', 'City': 'New York'}
name = dict['Name']
print(name)
if 'Age' in dict:
    print("Name exist in dictionary")
keys = dict.keys()
value = dict.values()
dict['Country'] = 'USA'

for key in dict:
    print(key, dict[key])

for key, value in dict.items():
    print(key, value)
