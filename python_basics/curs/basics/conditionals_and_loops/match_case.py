t = 1
a = 2
if t == 0:
    print(0)
elif t == 1:
    print(1)
elif t == 2:
    print(2)
else:
    print('other')

match t:
    case 0:
        print(0)
    case 1:
        print(1)
    case 2:
        print(2)
    case _:
        print('other')
