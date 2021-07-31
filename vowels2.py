vowels=['a', 'e', 'i', 'o', 'u']
word="Milliways"
mim=[]
for letter in word:
    if letter in vowels:
        if letter not in mim:
            mim.append(letter)
print(mim)
