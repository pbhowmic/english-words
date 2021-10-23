import argparse
from typing import Iterator, List, Set

from itertools import *
from itertools import filterfalse


def load_words(min_length: int, valid_words=None) -> Iterator[str]:
    """
    Load all the words in the dictionary and automatically rejects words of
    Returns:

    """
    return filterfalse(lambda x: len(x) < min_length, valid_words)


def filter_by_letterset(letters: Set[str], words_set: Iterator[str]) -> Iterator[str]:
    """
    Filters the words in the dictionary by the letter-set. For example,

    Args:
        letters:
        words_set:

    Returns:

    """
    sz: int = len(letters)
    words_subset: Iterator[str] = filterfalse(lambda x: len(x) < sz, words_set)
    return filterfalse(lambda x: set(x) != letters, words_subset)


def combos(letters: str) -> List[Set[str]]:
    """

    Args:
        letters:

    Returns:

    """
    x: list[set[str]] = []
    compulsory: set[str] = {letters[0]}
    for j in range(3, 7):
        x.extend([set(j).union(compulsory) for j in combinations(letters[1:], j)])
    return x


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='7 letters please.')
    parser.add_argument('letters', type=str,
                        help='7-letter starting with the cumpulsory one ')
    args = parser.parse_args()

    ctr = 0
    with open('words_alpha.txt') as word_file:
        dictionary: List[str] = word_file.read().split()

    for c in combos(args.letters):
        english_words = load_words(len(c), dictionary)
        print(c)
        words_found = filter_by_letterset(c, english_words)
        for w in words_found:
            ctr += 1
            print(f"{ctr}\t\t{w}")
