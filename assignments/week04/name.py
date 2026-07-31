name = input("What is your name: ")
name = "pipatpon"
letters = list(name)
print(letters)
counter = 0

for char in letters:
    if char =='a' or char =='A':
        counter = counter + 1
        print('a')

    if char =='e' or char =='E':
        counter = counter + 1
        print('e')

    if char =='i' or char =='I':
        counter = counter + 1
        print('i')

    if char =='o' or char =='O':
        counter = counter + 1
        print('o')

    if char =='u' or char =='U':
        counter = counter + 1
        print('u')

a = letters.count('A')
e = letters.count('E')
i = letters.count('I')
o = letters.count('O')
u = letters.count('U')

vowel = a + e + i + o + u








