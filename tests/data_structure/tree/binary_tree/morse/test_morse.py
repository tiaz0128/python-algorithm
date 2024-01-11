import pytest
from pytest import FixtureRequest

from src.data_structure.tree.binary_tree.morse.morse_tree import MorseCodeTree
from table import CODE_TABLE
import logging


@pytest.fixture(name="tree", scope="module")
def setup():
    logging.info("Creating tree fixture")
    return MorseCodeTree(CODE_TABLE)


@pytest.fixture(name="encode_inputs", params=[("SOS", ["...", "---", "..."])])
def setup_encode(request: FixtureRequest):
    return request.param


def test_morse_code_tree(tree, encode_inputs):
    raw_string, expected = encode_inputs

    morse_str = []

    # encode
    for ch in raw_string:
        code = tree.encode(ch)
        morse_str.append(code)

    assert morse_str == expected


@pytest.fixture(name="decode_input", params=[(["...", "---", "..."], "SOS")])
def setup_decode(request: FixtureRequest):
    return request.param


def test_decode(tree, decode_input):
    # given
    morse_str, expected = decode_input

    decoded_morse_lst = []

    # when
    for code in morse_str:
        ch = tree.decode(code)
        decoded_morse_lst.append(ch)

    # then
    assert "".join(decoded_morse_lst) == expected
