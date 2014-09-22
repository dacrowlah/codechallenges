#!/usr/bin/python
"""
The code challenge question is: 
write an algorithm to determine whether or not a string
has any duplicated characters
"scan_characters()" satisfies this
"sorter_scan()" does this with fewer iterations on the string,
but the time complexity that is hidden will increase a bit in
order to do the sorting.
"""
unique_characters = 'abcdefghijk'
non_unique = 'acabbdeffg'

def sorter_scan(string_to_scan):
    string_to_scan = sorted(string_to_scan)
    i = 0
    while i + 1 < len(string_to_scan):
        if string_to_scan[i] == string_to_scan[i+1]:
            print 'found a duplicated character at %s - %s' % (i+1, string_to_scan[i+1])
        i += 1


def scan_characters(string_to_scan):
    i = 0
    has_duplicates = False

    while i < len(string_to_scan):
        n = i + 1
        while n < len(string_to_scan):
            if string_to_scan[i] == string_to_scan[n]:
                has_duplicates = True
                print '%s - is duplicated at %s' % (string_to_scan[i], n + 1)
            n +=1
        i += 1

    if not has_duplicates:
        print 'no duplicates found'


if __name__ == '__main__':
    scan_characters(unique_characters)
    print '---------------------------'
    scan_characters(non_unique)
    print '---------------------------'
    sorter_scan(non_unique)
