def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """







    # return "".join(char.swapcase() for char in phrase if char.lower() == to_swap.lower())

    # phrase_list = list(phrase)

    # return "".join([char.swapcase() for char in phrase_list if char.lower() == to_swap.lower()])

    # print('Before the for loop')
    # for char in phrase_list:
    #     print('entering for loop')
    #     to_swap = to_swap.lower()
    #     print('this is to_swap', to_swap)
    #     lower_case_char = char.lower()
    #     print('this is lower_case_char', lower_case_char)
    #     if to_swap == lower_case_char:
    #         print('to_swap and lower_case are the same')
    #         char = char.swapcase()

    #         if (char == char.lower()):
    #             print("if char == char.lower() makes it here")
    #             char = char.upper()
    #             print('This is char', char)
    #         else:
    #             print("gets to the else statement instead")
    #             char = char.lower()
    # return "".join(phrase_list)