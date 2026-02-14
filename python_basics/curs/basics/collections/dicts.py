empty_dict = {}
empty_dict = dict()

a_dict = {'key': 'value', 'age': 30, 'job': 'Developer'}
print(a_dict)

print(a_dict.get('age'))
a_dict['age'] = 40
print(a_dict.get('age'))
print(a_dict['age'])

print(a_dict.get('location', 'Another location'))
# print(a_dict['location'])
print(a_dict.keys())
print(a_dict.values())
print(a_dict.items())

for key in a_dict:
    print(key, a_dict[key])

for key, value in a_dict.items():
    print(key, value)
