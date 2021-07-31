vowels=['a', 'e', 'i', 'o', 'u']
word=input("Provide a word to search for vowels:")
mim={}
for letter in word:
    if letter in vowels:
        mim.setdefault(letter,0)
        mim[letter]+=1
for k,v in sorted(mim.items()):
    print(k, 'was found', v, 'time(s).')
