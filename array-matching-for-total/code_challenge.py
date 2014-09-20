#!/usr/bin/python
import sys
import select

input = [-1, -1, 4, 2, 1, 25, 0, 3, 2]
target = 3


def include_match(matches, match):
    # reverse the order and see if its already
    # in the list of matches
    reverse_match_exists = (match[::-1] in matches)
    exact_match_exists = (match in matches)

    if match[0] < 0 or match[1] < 0:
        # one of the items is negative,
        # we only want it if there is
        # not already a match in reverse
        # order
        return not reverse_match_exists

    elif match[0] == 1:
        # if its a 1, dont include it if
        # an exact match exists
        return not exact_match_exists

    elif match[0] > 1:
        # item in the 2nd array is greater
        # than one, and we don't want these
        # if there is a match already
        return reverse_match_exists

    else:
        return not reverse_match_exists


def from_memory(data):
    # this is already faster than O(n^2) because it
    # removes the 3 from the list without iterating
    # that value against the rest of them.
    matches = []
    for x in filter(lambda x: x != 3, data):
        for y in filter(lambda y: y + x == target, data):
            # this list could get kinda big in memory
            # if there is a lot of matches, but we'll
            # assume for now that only storing matches
            # and taking steps to de-duplicate will
            # keep this manageable
            match = (x, y)
            if include_match(matches, match):
                matches.append(match)

    for match in matches:
        print '%s, %s' % match


def strip_str(v):
    # utility method to cleanup input from file
    return v.strip('\n').strip()


def eval_int(v):
    # two ways to do this, could silently fail and
    # return it to the caller as a string
    # or let it fail as a type conversion error
    # for the purposes of this challenge we'll assume
    # it's all good data. which doesn't happen in real
    # life.  how this would be implemented would be
    # based on real life business requirements
    # if v and v.isdigit():
    if v and type(v) == int:
        return v

    return int(strip_str(v))


def from_file():
    # first we'll write the supplied list to a file
    # so I don't need to attach any other files
    with open('f1.txt', 'w') as f:
        [f.write('%s \n' % item) for item in input]

    matches = []
    with open('f1.txt', 'r') as f1, open('f1.txt', 'r') as f2:
        for x in filter(lambda x: eval_int(x) != 3, f1):
            x = eval_int(x)
            f2.seek(0)  # reset to beginning of read stream
            for y in filter(lambda y: eval_int(y) + x == target, f2):
                match = (x, eval_int(y))
                if include_match(matches, match):
                    matches.append(match)

    for match in matches:
        print '%s, %s' % match


if __name__ == '__main__':
    # this is for streaming the file to python from bash
    # this should be called with the following syntax:
    # $ cat f1.txt | python code_challenge.py
    # running this file with the command "python code_challenge.py"
    # will create f1.txt
    # this will throw type conversion errors on invalid data.
    # first things first: check to see if data is being streamed via bash
    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        print '========== FROM STDIN ============='
        from_memory([eval_int(line) for line in sys.stdin])

    else:
        print '========== FROM MEMORY ============'
        from_memory(input)

        print '========== FROM FILE =============='
        from_file()
