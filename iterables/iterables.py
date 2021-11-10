"""Iterator of words in sentence"""


class MultipleSentencesError(Exception):
    """Exception for cases when Sentence receive
    more than one sentence
    """
    ...


class Sentence:
    """Container
    methods: __init__, __repr__, word - laze iterator, __iter__, __getitem__
    attributes: text, _words (property words), _other_chars(chars)
    """
    def __init__(self, text: str):
        """Constructor"""
        self.text = text
        self._words = ''
        self._other_chars = ''
        self.index = 0

        for char in self.text:
            if char not in [',', ' ', '-', ':', '.', '!', '?']:
                self._words += char
            else:
                self._other_chars += char + ' '
                self._words += ' '

        if not isinstance(self.text, str):
            raise TypeError('Print only string.')
        if self.text[-1] not in ['.', '!', '?']:
            raise ValueError('Print only finished sentences.')
        for char in self.text[:-3]:
            if char in ['.', '!', '?']:
                raise MultipleSentencesError('Print only one sentence.')

    def __repr__(self):
        """Returns number of words and other_chars
        when object is printed
        """
        return f'Sentence(words = {len(self.words)}, other_chars = {len(self.other_chars)})'

    @property
    def other_chars(self):
        """Splits string from _other_chars"""
        return self._other_chars.split()

    @property
    def words(self):
        """Splits string from _words"""
        return self._words.split()

    def word(self):
        """Lazy iterator"""
        for word in self.words:
            yield word

    def __getitem__(self, item):
        """Return item by index"""
        return self.words[item]

    def __iter__(self):
        """Returns iterator class"""
        return SentenceIterator(self.words)


class SentenceIterator:
    """Iterator that follows protocol"""
    def __init__(self, text):
        """Constructor"""
        self.text = text
        self.index = 0

    def __next__(self):
        """Generate words"""
        if self.index < len(self.text):
            self.index += 1
            return self.text[self.index-1]
        raise StopIteration

    def __iter__(self):
        """Returns self"""
        return self


sentence_1 = Sentence('Hello,what about going to the club tonight?')
# print(sentence_1.words)
# print(sentence_1.other_chars)
# print(sentence_1)
# for x in sentence_1.word():
#     print(x)
# print(next(sentence_1.word()))
# iterator_1 = iter(sentence_1)
# print(next(iterator_1))
# print(next(iterator_1))
# print(next(iterator_1))
# print(next(iterator_1))
# print(next(iterator_1))
# print(next(iterator_1))
# print(next(iterator_1))
# print(next(iterator_1))
# print(next(iterator_1))
# print(sentence_1[4])
# print(sentence_1[:])
