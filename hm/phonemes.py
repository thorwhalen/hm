"""
Phoneme tools
"""

rooturl = 'http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/'
url_term_and_phones = rooturl + 'cmudict-0.7b'
url_phones = rooturl + 'cmudict-0.7b.phones'
url_symbols = rooturl + 'cmudict-0.7b.symbols'


def term_and_phones():
    return _text_to_term_and_phones(_get_cmu_raw_data_text())


def _get_cmu_raw_data_text(url=url_term_and_phones, encoding='latin1'):
    from pyckup import grab

    return grab(url).decode(encoding)


def _text_to_term_and_phones(text):
    for term, phones in map(
        methodcaller('split', sep=' ' * 2),
        filter(lambda x: not x.startswith(';;;'), text.splitlines()),
    ):
        yield term.lower(), phones.split(' ')


from functools import cached_property
from operator import methodcaller
from itertools import chain
from collections import Counter


class Phone:
    rooturl = 'http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/'
    url_term_and_phones = rooturl + 'cmudict-0.7b'
    url_phones = rooturl + 'cmudict-0.7b.phones'
    url_symbols = rooturl + 'cmudict-0.7b.symbols'
    encoding = 'latin1'

    def __init__(self, url_term_and_phones=None):
        self.url_term_and_phones = url_term_and_phones or self.url_term_and_phones

    @cached_property
    def tp(self):
        return dict(
            _text_to_term_and_phones(
                _get_cmu_raw_data_text(self.url_term_and_phones, self.encoding)
            )
        )

    @cached_property
    def phone_class(self):
        lines = _get_cmu_raw_data_text(self.url_phones).splitlines()
        return dict(map(methodcaller('split', sep='\t'), lines))

    @cached_property
    def phone_counts(self):
        return dict(Counter(chain.from_iterable(self.tp.values())).most_common())

    @cached_property
    def phones(self):
        # Note: url_phones contains
        return sorted(self.phone_counts)


class MST(Phone):
    """
    See:    https://en.wikipedia.org/wiki/Mnemonic_major_system

    """

    phones_for_num = {0: {'Z'}}
