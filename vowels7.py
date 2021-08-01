vowels = set('aeiou')
word = input("Vvedi slovo dlya poiska glasnyh: ")
found = vowels.intersection(set(word))
print(sorted(list(found)))
