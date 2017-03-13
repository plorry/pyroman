"""
Module to interpret Roman Numeral strings and convert them to integers

>>> integer_to_numeral(22)
'XXII'
>>> numeral_to_integer('XXII')
22
"""

NUMERAL_MAPPING = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',
}

INTEGER_MAPPING = {val: key for key, val in NUMERAL_MAPPING.items()}

CLEAN_MAPPING = {
    'IIII': 'IV',
    'VIIII': 'IX',
    'XXXX': 'XL',
    'LXXXX': 'XC',
    'CCCC': 'CD',
    'DCCCC': 'CM',
}


def integer_to_numeral(integer):
    '''
    Takes an integer and converts it to a Roman Numeral, which is returned as a string

    >>> integer_to_numeral(5)
    'V'
    >>> integer_to_numeral(10)
    'X'
    >>> integer_to_numeral(11)
    'XI'
    >>> integer_to_numeral(3991)
    'MMMCMXCI'
    '''
    return build_string(integer)


def build_string(integer, numeral=''):
    '''
    Recursively build Numeral string until integer value is 0

    >>> build_string(5, 'I')
    'IV'
    >>> build_string(19, 'XX')
    'XXXIX'
    '''
    (cha, new_value) = find_highest_mapping(integer)
    numeral = clean_numeral(numeral + cha)
    return numeral if new_value is 0 else build_string(new_value, numeral)


def find_highest_mapping(integer):
    '''
    Takes an integer and returns the highest single Roman Numeral less than its value
    and returns the Numeral and the integer minus the Numeral value

    >>> find_highest_mapping(1)
    ('I', 0)
    >>> find_highest_mapping(20)
    ('X', 10)
    '''
    (integer < 1 and raise_zero_exception())
    return next((NUMERAL_MAPPING[value], integer - value)
                for value in sorted(NUMERAL_MAPPING.keys(), reverse=True)
                if integer >= value)


def clean_numeral(numeral):
    '''
    Check the last five/four digits of numeral for any necessary cleanup according to
    Roman numeral rules

    >>> clean_numeral('IIII')
    'IV'
    >>> clean_numeral('VIIII')
    'IX'
    >>> clean_numeral('XVIIII')
    'XIX'
    '''
    substr5 = numeral[-5:]
    substr4 = numeral[-4:]
    return numeral[:-5] + CLEAN_MAPPING[substr5] if substr5 in CLEAN_MAPPING \
        else numeral[:-4] + CLEAN_MAPPING[substr4] if substr4 in CLEAN_MAPPING \
        else numeral


def numeral_to_integer(numeral):
    '''
    Takes a Roman Numeral string and converts it to an integer, which is returned.
    Raises an error in the case that an improperly formed Roman Numeral is passed in.

    >>> numeral_to_integer('II')
    2
    >>> numeral_to_integer('MCMXCVI')
    1996
    '''
    integer = compute_integer(numeral)
    expected = integer_to_numeral(integer)
    (expected != numeral and raise_invalid_exception(expected))
    return integer


def compute_integer(numeral, this_val=0, last_val=0, total=0):
    '''
    Recursively check the last character of a numeral string, adding or subtracting
    the value of the character depending on where it sits in numeral
    '''
    new_total = total + this_val if this_val >= last_val else total - this_val
    return new_total if len(numeral) is 0 \
        else compute_integer(numeral[:-1], INTEGER_MAPPING[numeral[-1]], this_val,
                             new_total)


def raise_zero_exception():
    raise ValueError("Romans had no notion of zero or negative numbers")


def raise_invalid_exception(expected):
    raise ValueError("That doesn't look like a correct Roman Numeral to me. "
                     "Did you mean {}?".format(expected))
