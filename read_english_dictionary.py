#!/usr/bin/env python3

import argparse
from typing import Iterator, List, Set

from itertools import filterfalse, combinations


def filter_by_letterset(letters: Set[str], words_set: Iterator[str]) \
        -> Iterator[str]:
    """
    Filters the words in the dictionary by the letter-set. So, the set
    {'h', 'o', 'w'} will match 'how' and 'who' but not 'whom'
    Args:
        letters: The set of letters to use to filter against the diction
        words_set: The supplied dictionary to filter

    Returns:
        An iterator for words that matched the letter-set
    """
    sz: int = len(letters)
    words_subset: Iterator[str] = filterfalse(lambda x: len(x) < sz, words_set)
    return filterfalse(lambda x: set(x) != letters, words_subset)


def combos(letters: str) -> List[Set[str]]:
    """
    Get all combinations of the 7-letter set, the smallest set will be of
    size 4 and the largest of size 7
    Args:
        letters: The string of 7-letters provided, the first of which is compulsory

    Returns:
        A list of all combinations of the 7-letter set, the smallest set will be of
    size 4 and the largest of size 7
    """
    x: List[Set[str]] = []
    compulsory: Set[str] = {letters[0]}
    for j in range(3, 7):
        x.extend([set(x).union(compulsory)
                  for x in combinations(letters[1:], j)])
    return x


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='7 letters please.')
    parser.add_argument('letters', type=str,
                        help='7-letter starting with the compulsory one ')
    args = parser.parse_args()

    ctr = 0
    with open('words_alpha.txt') as word_file:
        dictionary: List[str] = [x for x in word_file.read().split() if len(x) >= 4]

    for c in combos(args.letters):
        words_found = filter_by_letterset(c, dictionary)
        print(c)
        for w in words_found:
            ctr += 1
            print(f"{ctr}\t\t{w}")
