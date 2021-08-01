def search4letters(phrase:str, letters:str) -> set:
    """Возвращает множество букв из 'letters', найденных
    в указанной фразе."""
    return set(letters).intersection(set(phrase))
