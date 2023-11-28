def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    freq_counter = {}
    for num in nums:
        freq_counter[num] = freq_counter.get(num, 0) + 1

        # if num not in freq_counter:
        #     freq_counter[num] = 1
        # else:
        #     freq_counter[num] += 1

        # can replace if/else statement in for loop
        freq_counter[num] = freq_counter.get(num, 0) + 1


    highest_frequency = max(freq_counter.values())

    for key in freq_counter.keys():
        if freq_counter[key] == highest_frequency:
            return key



# frequency counter function definition for reference:

# def freq_counter(items):
#     freq_counter = {}
#     for item in items:
#         freq_counter[item] = freq_counter.get(item, 0) + 1
#     return freq_counter