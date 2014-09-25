#!/usr/bin/python
"""
This is one that tripped me up in an interview.
For some reason I was wanting to use a hashmap,
but after the call ended I realized how I should
have done it.  Pretty obvious - I think I just
got a little flustered from him wanting to do it
in Java (which I don't know) and couldn't remember
C# syntax.  He wouldn't let me do it in Python.

As I work through all of these in different
languages .. I'll know for next time!
"""


def find_first_non_repeating_character(string):
    str_len = len(string)
    i = 0
    seen = set()
    possibles = set()
    while i < str_len:
        l = string[i]
        if l not in seen:
            possibles.add(l)
            seen.add(l)
        elif l in seen:
            possibles.discard(l)

        i += 1

    # I don't really like this syntax.
    # I can't figure out any better way
    # do it in (what I feel is) a cleaner
    # way.
    for i in possibles:
        return i

if __name__ == '__main__':
    strings = [
        'abcbc',
        'abcadc',
        'abcabc'
    ]
    for string in strings:
        print (find_first_non_repeating_character(string))
