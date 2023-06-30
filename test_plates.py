from modified_plates import is_valid

def test_alpha_numeric():
    assert is_valid("as_34") == False

def test_limits():
    assert is_valid("a") == False
    assert is_valid("ersdf355") == False

def test_start_letters():
    assert is_valid("23sdf")  == False

def test_end_numbers():
    assert is_valid("sdf32f") == False

def test_exceptions():
    assert is_valid("sd034") == False
    assert is_valid("srk f3") == False
    assert is_valid("sdf234") == True