#!/usr/bin/python

source_string = 'aaabbccccccddefgg'
compacted_string = 'abcdefg'

def minimize(str_in):

    symbols = {}
    for char in str_in:
        symbols[char] = symbols.get(char, 0) + 1
    
    str_out = ''
    for char in symbols:
        str_out += '%s%s' % (char, symbols.get(char))

    if len(str_out) >= len(str_in):
        return str_in

    return str_out


if __name__ == '__main__':
    print minimize(source_string)
    print minimize(compacted_string)
