
# hm
Mnemonic tools


To install:	```pip install hm```

# Mnemonic Major System

The [major system](https://en.wikipedia.org/wiki/Mnemonic_major_system)
is a mnemonic technique used to aid in memorizing numbers.

It works as follows:

    >>> from hm import MajorSystem
    >>> m = MajorSystem()

The "Mnemonic Major System" (https://en.wikipedia.org/wiki/Mnemonic_major_system)
assigns a set of similar phonemes to each digit:

    >>> assert m.phones_for_num == {
    ...     0: {'S', 'Z'},
    ...     1: {'D', 'DH', 'T', 'TH'},
    ...     2: {'N'},
    ...     3: {'M'},
    ...     4: {'R'},
    ...     5: {'L'},
    ...     6: {'CH', 'JH', 'SH'},
    ...     7: {'G', 'K'},
    ...     8: {'F', 'V'},
    ...     9: {'B', 'P'}
    ... }

As a consequence these phonemes are mapped to numbers:

    >>> assert m.num_of_phone == {
    ...     'B': 9,
    ...     'CH': 6,
    ...     'D': 1,
    ...     'DH': 1,
    ...     'F': 8,
    ...     'G': 7,
    ...     'JH': 6,
    ...     'K': 7,
    ...     'L': 5,
    ...     'M': 3,
    ...     'N': 2,
    ...     'P': 9,
    ...     'R': 4,
    ...     'S': 0,
    ...     'SH': 6,
    ...     'T': 1,
    ...     'TH': 1,
    ...     'V': 8,
    ...     'Z': 0
    ... }

Any sentence has a corresponding phoneme sequence:

    >>> m.term_to_phones('wild cat')
    ['W', 'AY1', 'L', 'D', 'K', 'AE1', 'T']

The system doesn't contain all phonemes; only some of the consonant phonemes.
So if we only keep those phonemes that the system covers, we get:

    >>> m.term_to_mst_sequence('wild cat')
    ['L', 'D', 'K', 'T']

Which corresponds to a number.

    >>> m.term_to_nums('wild cat')
    [5, 1, 7, 1]

But really, the system is used to be able to create words (therefore images)
that correspond to a sequence of numbers, so that one can remember them:

    >>> m.terms_of_numstr['3214']  # doctest: +NORMALIZE_WHITESPACE
    ['hammontree', 'mahindra', 'manteer', 'mantra', 'mentor', 'minteer', 'mondry',
    'monetary', 'monteiro', 'monterey', 'montero', 'monterrey', 'montrouis',
    'montroy', 'montuori', 'omohundro']
