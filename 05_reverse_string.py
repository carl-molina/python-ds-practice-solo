def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    phrase_list = list(phrase)
    phrase_list.reverse()

    backwards_phrase = ''

    for letter in phrase_list:
        backwards_phrase += letter

    return backwards_phrase
