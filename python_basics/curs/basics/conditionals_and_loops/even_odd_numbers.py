input_number = int(input("Verify a number if it is odd or even? "))

if input_number % 2 == 0:
    print('Even!')
else:
    print("Odd!")
print('-'*30)
if input_number % 5 == 0:
    print('Divizibil cu 5')
elif input_number % 3 == 0:
    print('Divizibil cu 3')
elif input_number % 7 == 0:
    print('Divizibil cu 7')
else:
    print('Nedivizibil cu 3, 5 si 7')

print('-'*30)
if input_number % 5 == 0:
    print('Divizibil cu 5')
if input_number % 3 == 0:
    print('Divizibil cu 3')
if input_number % 7 == 0:
    print('Divizibil cu 7')
