import pytest
import pynamer


@pytest.mark.parametrize("text, text_id", [('testerino12.test', 12), ('123test321.exe', 123), ('123test.py', 123), ('', -1)])
def test_extract_id(text, text_id):
    assert pynamer.extract_id(text) == text_id
