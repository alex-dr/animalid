"""Tests for the contents of the word lists."""
from collections import Counter
import itertools
import locale

import animalid

import pytest


LISTS_OF_WORDS = {
    "alloys": animalid.alloys,
    "animalids": animalid.animals,
    "colors": animalid.colors,
    "fabrics": animalid.fabrics,
    "origins": animalid.origins,
    "opinions": animalid.opinions,
    "shapes": animalid.shapes,
    "sizes": animalid.sizes,
}


@pytest.mark.parametrize("list_name, list_of_words", LISTS_OF_WORDS.iteritems())
def test_word_format(list_name, list_of_words):
    """All words are lower case letters and underscores."""
    valid_chars = "abcdefghijklmnopqrstuvwxyz_"
    invalid_words = [
        word for word in list_of_words if not all(char in valid_chars for char in word)
    ]
    assert not invalid_words, ("Invalid chars found in words {} from list {}").format(
        invalid_words, list_name
    )


@pytest.mark.parametrize("list_name, list_of_words", LISTS_OF_WORDS.iteritems())
def test_no_duplicate_words_within_files(list_name, list_of_words):
    """No words are duplicates within files."""
    counts = Counter(list_of_words)
    duplicates = [x for x, y in counts.iteritems() if y > 1]
    assert not duplicates, "Duplicate words {} found in list {}".format(
        duplicates, list_name
    )


def test_max_length():
    """No words over 20 characters long."""
    mega_list = list(itertools.chain(*LISTS_OF_WORDS.values()))
    overly_long_words = [word for word in mega_list if len(word) > 20]
    assert not overly_long_words, "Your words are too long!" "{}".format(
        overly_long_words
    )


@pytest.mark.xfail
@pytest.mark.parametrize("list_name, list_of_words", LISTS_OF_WORDS.iteritems())
def test_all_lists_sorted(list_name, list_of_words):
    """All lists are sorted alphabetically."""
    locale.setlocale(locale.LC_ALL, "C")
    assert sorted(list_of_words, cmp=locale.strcoll) == list_of_words
