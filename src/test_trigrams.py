# -*- coding: utf-8 -*-
import pytest

SANITIZE_FUNC_PARAMS = [
    ('this is a test', [
        'this', 'is', 'a', 'test'
    ]),
    ('  test    multiple   whitespaces   ', [
        'test', 'multiple', 'whitespaces'
    ])
]


@pytest.mark.parametrize('string, sanitized_string_list', SANITIZE_FUNC_PARAMS)
def test_sanitize(string, sanitized_string_list):
    from trigrams import sanitize
    assert sanitize(string) == sanitized_string_list


PROCESS_TRIGRAMS_FUNC_PARAMS = [
    (['one', 'two', 'three'], {
        'one two': ['three']
    }),
    (['list', 'to', 'dict'], {
        'list to': ['dict']
    })
]


@pytest.mark.parametrize(
    'string_list, string_dict', PROCESS_TRIGRAMS_FUNC_PARAMS
)
def test_process_triagrams(string_list, string_dict):
    from trigrams import process_trigrams
    assert process_trigrams(string_list) == string_dict
