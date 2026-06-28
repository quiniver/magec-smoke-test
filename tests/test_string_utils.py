"""Tests for src/string_utils.py"""

import pytest
from src.string_utils import reverse_string, is_palindrome, count_vowels


class TestReverseString:
    """Tests for the reverse_string() function."""

    def test_reverse_normal_string(self):
        assert reverse_string("hello") == "olleh"

    def test_reverse_single_character(self):
        assert reverse_string("a") == "a"

    def test_reverse_empty_string(self):
        assert reverse_string("") == ""

    def test_reverse_palindrome(self):
        # Reversing a palindrome should give the same string
        assert reverse_string("racecar") == "racecar"

    def test_reverse_with_spaces(self):
        assert reverse_string("hello world") == "dlrow olleh"

    def test_reverse_with_special_chars(self):
        assert reverse_string("a!b@c") == "c@b!a"

    def test_reverse_two_characters(self):
        assert reverse_string("ab") == "ba"

    def test_reverse_digits(self):
        assert reverse_string("12345") == "54321"


class TestIsPalindrome:
    """Tests for the is_palindrome() function."""

    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_simple_non_palindrome(self):
        assert is_palindrome("hello") is False

    def test_case_insensitive_palindrome(self):
        assert is_palindrome("Racecar") is True
        assert is_palindrome("RACECAR") is True
        assert is_palindrome("RaCeCaR") is True

    def test_case_insensitive_non_palindrome(self):
        assert is_palindrome("Hello") is False
        assert is_palindrome("HELLO") is False

    def test_empty_string_is_palindrome(self):
        assert is_palindrome("") is True

    def test_single_character_is_palindrome(self):
        assert is_palindrome("a") is True
        assert is_palindrome("A") is True

    def test_palindrome_with_spaces(self):
        # "A man a plan a canal Panama" -> "amanaplanacanalpanama"
        assert is_palindrome("A man a plan a canal Panama") is True

    def test_non_palindrome_with_spaces(self):
        assert is_palindrome("hello world") is False

    def test_palindrome_with_spaces_mixed_case(self):
        assert is_palindrome("Was It A Rat I Saw") is True

    def test_single_word_no_spaces(self):
        assert is_palindrome("level") is True
        assert is_palindrome("deed") is True

    def test_two_letter_palindrome(self):
        assert is_palindrome("aa") is True
        assert is_palindrome("ab") is False

    def test_special_characters_not_stripped(self):
        # Only spaces are removed, not other characters
        assert is_palindrome("a!a") is False
        assert is_palindrome("a a") is True


class TestCountVowels:
    """Tests for the count_vowels() function."""

    def test_basic_vowels(self):
        assert count_vowels("hello") == 2
        assert count_vowels("aeiou") == 5

    def test_no_vowels(self):
        assert count_vowels("bcdfg") == 0
        assert count_vowels("xyz") == 0

    def test_empty_string(self):
        assert count_vowels("") == 0

    def test_case_insensitive(self):
        assert count_vowels("AEIOU") == 5
        assert count_vowels("AeIoU") == 5

    def test_mixed_vowels_and_consonants(self):
        assert count_vowels("Programming") == 3
        assert count_vowels("Education") == 5

    def test_spaces_counted_correctly(self):
        assert count_vowels("a e i o u") == 5

    def test_numbers_and_special_chars(self):
        assert count_vowels("12345") == 0
        assert count_vowels("hello!@#world") == 3

    def test_all_uppercase(self):
        assert count_vowels("PYTHON") == 1

    def test_all_lowercase(self):
        assert count_vowels("python") == 1

    def test_y_is_not_vowel(self):
        assert count_vowels("sky") == 0
        assert count_vowels("yes") == 0
