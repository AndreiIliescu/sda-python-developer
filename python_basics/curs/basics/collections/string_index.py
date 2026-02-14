s = 'System of a Down'
l = len(s)
i = 0
ia = 0

for x in range(l):
    print(s[x], sep='', end='')

print()

a = "1aaa2bbb3ccc"

i1 = a.index('1')
i2 = a.index('2')
i3 = a.index('3')

print(f"{a[i1 + 1:i2]}  {a[i2 + 1:i3]} {a[i3 + 1:]}")
