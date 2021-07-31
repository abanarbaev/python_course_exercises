vowels=['a', 'e', 'i', 'o', 'u']
word=input("Provide a word to search for vowels:")
mim={}
for letter in word:
    if letter in vowels:
        if letter not in mim:
            mim.append(letter)
for vowel in mim:
    print(vowel)
