def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    return phrase[::-1]

    phrase_list = list(phrase)
    phrase_list.reverse()

    # can turn list into a string in join
    return "".join(phrase_list)

    backwards_phrase = ''

    for letter in phrase_list:
        backwards_phrase += letter

    # return backwards_phrase

