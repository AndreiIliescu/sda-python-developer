word = 'Python is great'
# print(word[0:0])
# print(type(word[0:0]))
# print(len(word[0:0]))
for letter in word:
    print(letter)
    if letter == 'h':
        continue
    # if letter == 'r':
    #     break
else:
    print('Finished iterating letters')
