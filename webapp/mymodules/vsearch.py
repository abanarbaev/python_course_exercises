def search4vowels(word: str) ->set:
    # Выводит гласные найденные в введенном слове
    '''интересная шняга: mim - у меня, в книге found'''
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(phrase: str, letters: str='aeiou') ->set:
    '''выводит буквы которые есть в слове'''
    return set(letters).intersection(set(phrase))
