#!/usr/bin/python


def find_longest_palindrome(string, case_insensitive=False):

    str_length = len(string)
    i = 0
    min_length = 2
    the_match = None
    longest = 0

    if str_length < min_length:
        return

    if case_insensitive:
        string = string.lower()

    while i < str_length - 1:
        n = min_length
        while n <= str_length:
            value = string[i:n]
            value_length = len(value)
            if value == value[::-1] and value_length > longest:
                the_match = value
                longest = value_length

            n += 1
        i += 1

    return the_match


if __name__ == "__main__":

    input_strings = [
        'abcradar1234mom',
        'abcraDar1234mom',
        'abcradaR1234mom',
        'radar',
        'ada',
        'aa',
        'a'
    ]

    print 'case sensitive'
    for input_str in input_strings:
        print find_longest_palindrome(input_str)

    print 'case insensitive'
    for input_str in input_strings:
        print find_longest_palindrome(input_str, case_insensitive=True)
