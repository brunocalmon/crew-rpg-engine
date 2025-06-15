from crew.utils import get_print

def test_get_print():
    assert get_print("test") == "Input: test"
