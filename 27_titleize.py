def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.lower()
    phrase = phrase.split(" ")
    # print('This is phrase', phrase)
    titled_phrase = []
    for word in phrase:
        titled_word = word[0].upper() + word[1:]
        titled_phrase.append(titled_word)
    return " ".join(titled_phrase)