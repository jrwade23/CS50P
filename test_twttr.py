from modified_twttr import shorten

def test_blank():
    assert shorten("") == ""

def test_argument():
    assert shorten("hello") == "hll"
    assert shorten("Hello") == "Hll"
    assert shorten("HELLO") == "HLL"