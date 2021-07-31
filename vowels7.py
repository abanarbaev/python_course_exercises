vowels=set('aeiou')
word=input("Provide a word to search for vowels:")
mim=vowels.intersection(set(word))
for  vowel in mim:
    print(vowel)


