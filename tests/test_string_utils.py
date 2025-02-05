# tests/test_string_utils.py
import pytest
from src.string_utils import StringUtils

class TestStringUtils:
    """
    Unit tests for string utils
    """
    def setup_method(self):
        self.utils = StringUtils()
    
    def test_reverse_string(self):
        assert self.utils.reverse_string("hello") == "olleh"
        assert self.utils.reverse_string("") == ""
        assert self.utils.reverse_string("a") == "a"
    
    def test_count_words(self):
        assert self.utils.count_words("hello world") == 2
        assert self.utils.count_words("") == 0
        assert self.utils.count_words("   ") == 0
        assert self.utils.count_words("one") == 1
    
    def test_capitalize_words(self):
        assert self.utils.capitalize_words("hello world") == "Hello World"
        assert self.utils.capitalize_words("") == ""
        assert self.utils.capitalize_words("a b c") == "A B C"
    
    def test_remove_duplicates(self):
        assert self.utils.remove_duplicates("hello") == "helo"
        assert self.utils.remove_duplicates("") == ""
        assert self.utils.remove_duplicates("aaa") == "a"
    
    def test_is_palindrome(self):
        assert self.utils.is_palindrome("A man, a plan, a canal: Panama")
        assert self.utils.is_palindrome("")
        assert self.utils.is_palindrome("a")
        assert not self.utils.is_palindrome("hello")