a = None
i = 20

if i % 2 == 0:
    a = 'abc'
else:
    a = 'cde'

a = 'abc' if i % 2 == 0 else 'cde'

result = []
number_list = [2, 3, 4, 5]

for i in number_list:
    result.append(i ** 2)
print(f'result={result}')

result = [i ** 2 for i in number_list]
# result = (i ** 2 for i in number_list)
print(f'result={result}')

result_dict = {}
for i in number_list:
    result_dict[i] = i ** 2
print(f'result_dict={result_dict}')

# result_dict = {i: i ** 2 for i in number_list}
result_dict = {i: i ** 2 if i % 2 == 0 else i ** 3 for i in number_list}
print(f'result_dict={result_dict}')


def print_full_name(name: str, surname: str) -> list:
    print(f"{name} {surname}")
    return
    print()

a = print_full_name(123, 456)
print(a)
