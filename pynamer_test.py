import pytest
import pynamer


@pytest.mark.parametrize("text, text_id", [('testerino12.test', 12),
                                           ('123t est321.exe', 123),
                                           ('123test.py', 123), ('', -1)])
def test_extract_id(text, text_id):
    assert pynamer.extract_id(text) == text_id


# @pytest.mark.parametrize("prefix, extensions", [
#     ('testPrefix', )
# ])
# def test_files_to_rename(prefix, extensions):
