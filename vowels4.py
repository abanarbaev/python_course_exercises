vowels=['a', 'e', 'i', 'o', 'u']
word=input("Provide a word to search for vowels:")
mim={}
mim['a']=0
mim['e']=0
mim['i']=0
mim['o']=0
mim['u']=0
for letter in word:
    if letter in vowels:
        mim[letter]+=1
for k,v in sorted(mim.items()):
    print(k, 'was found', v, 'time(s).')
