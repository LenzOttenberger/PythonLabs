import pytest
from contextlib import nullcontext
from task import count_words, find_unique, is_palindrome, are_anagrams, combine_dict

@pytest.mark.parametrize('text, res, expectation',
                         [
                             ("Hello my body!", 3, nullcontext()),
                             ("The grabbing hands grab all they can...", 7, nullcontext()),
                             (123, 0, pytest.raises(TypeError)),
                             ("Hello", 1, nullcontext()),
                         ])
def test_count_words(text, res, expectation):
    with expectation:
        assert count_words(text) == res
        
@pytest.mark.parametrize('lst, res, expectation',
                         [
                             ([1, 1, 1, 2, 3, 3, 4, 5, 5, 5, 8], [2, 4, 8], nullcontext()),
                             ([0, 0, 0, 0, 1, 0, 0, 0, 0, 3], [1, 3], nullcontext()),
                             (['a', 1, 3, 3, 'bbb'], ['a', 1, 'bbb'], nullcontext()),
                             (123, 0, pytest.raises(TypeError)),
                             ('asbccv', ['a', 's', 'b', 'v'], nullcontext())
                         ])
def test_find_unique(lst, res, expectation):
    with expectation:
        assert find_unique(lst) == res

@pytest.mark.parametrize('text, res, expectation',
                         [
                             ('aaabaaa', True, nullcontext()),
                             ('ababa', True, nullcontext()),
                             ([1, 1, 2, 1, 1], True, nullcontext()),
                             ('aaab', False, nullcontext()),
                             ('aabbaa', True, nullcontext()),
                             (123, 0, pytest.raises(TypeError))
                         ])
def test_is_palindrome(text, res, expectation):
    with expectation:
        assert is_palindrome(text) == res

@pytest.mark.parametrize('word1, word2, res, expectation',
                         [
                             ('aaabb', 'bbaaa', True, nullcontext()),
                             ('abyal', 'labay', True, nullcontext()),
                             ('aabb', 12, True, pytest.raises(TypeError)),
                             ('aaabb', 'bbbaa', False, nullcontext()),
                             ('bhsk', 'skbt', False, nullcontext())
                         ])
def test_are_anagrams(word1, word2, res, expectation):
    with expectation:
        assert are_anagrams(word1, word2) == res
        
@pytest.mark.parametrize('dct1, dct2, res, expectation',
                         [
                            (
                                {"a": 1},
                                {"b": 2},
                                {"a": 1, "b": 2},
                                nullcontext()
                            ),
                            (
                                {"a": 1},
                                {"a": 2},
                                {"a": 2},
                                nullcontext()
                            ),
                            (
                                {"a": {"x": 1}},
                                {"a": {"y": 2}},
                                {"a": {"x": 1, "y": 2}},
                                nullcontext()
                            ),
                            (
                                {"a": {"x": 1}},
                                {"a": 5},
                                {"a": 5},
                                nullcontext()
                            ),
                            (
                                123,
                                {"a": 1},
                                None,
                                pytest.raises(TypeError)
                            ),
                            (
                                {"a": 1},
                                "not a dict",
                                None,
                                pytest.raises(TypeError)
                            ),
                         ])
def test_combine_dict(dct1, dct2, res, expectation):
    with expectation:
        assert combine_dict(dct1, dct2) == res