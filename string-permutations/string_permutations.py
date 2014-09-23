#!/usr/bin/python
string_one = '1234567890abcdefg'
string_two = 'abcdefg1234567890'
string_dux = 'abcdefghijklmnopq'
string_mux = 'ABCDEFGHIJKLMNOPQ'

def check_strings(one, two, case_insensitive = False):

    if len(one) != len(two):
        return False

    if case_insensitive:
        one = one.lower()
        two = two.lower()

    one = ''.join(sorted(one))
    two = ''.join(sorted(two))

    if one == two:
        return True

    return False

def another_way(one, two, case_insensitive = False):

    if len(one) != len(two):
        return False

    if case_insensitive:
        one = one.lower()
        two = two.lower()

    one_chars = {}
    two_chars = {}
    
    def check_chars(chars, counter):
        for char in chars:
            counter[char] = counter.get(char, 0) + 1

    check_chars(one, one_chars)
    check_chars(two, two_chars)
  
    is_permutation = True
    for key in one_chars:
        if one_chars.get(key) != two_chars.get(key):
            is_permutation = False
            break

    return is_permutation

if __name__ == '__main__':
    another_way(string_one, string_two)
    another_way(string_one, string_dux)
    another_way(string_dux, string_mux)

    another_way(string_one, string_two, case_insensitive = True)
    another_way(string_one, string_dux, case_insensitive = True)
    another_way(string_dux, string_mux, case_insensitive = True)

    print 'one, two, sensitive? %s' % check_strings(string_one, string_two)
    print 'one, two, sensitive? %s' % check_strings(string_one, string_dux)
    print 'one, two, sensitive? %s' % check_strings(string_dux, string_mux)

    print 'one, two, insensitive? %s' % check_strings(string_one, string_two, case_insensitive = True)
    print 'one, dux, insensitive? %s' % check_strings(string_one, string_dux, case_insensitive = True)
    print 'dux, mux, insensitive? %s' % check_strings(string_dux, string_mux, case_insensitive = True)
