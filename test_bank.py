from modifiied_bank import value

def test_hello():
    assert value("Hello, how are you?") == "$0"

def test_h():
    assert value("How's it going?") == "$20"

def test_noh():
    assert value("What's up?") == "$100"