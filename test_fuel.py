# This test is meant for the version of fuel.py found only in Problem_Set_5, because it had to be modified to allow pytest
# to be run successfuly (no interuptions for user input). The version of fuel.py found in Problem_Set_3 and github is a much 
# more user friendly program and should be prioritized, except when one wants to run this Unit Test code through pytest.

import modified_fuel
import pytest


def test_numerator():
    with pytest.raises(ValueError):
        modified_fuel.convert("a/5")

def test_denominator():
    with pytest.raises(ValueError):
        modified_fuel.convert("5/a")
    
def test_n_and_d():
    with pytest.raises(ValueError):
        modified_fuel.convert("a/b")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        modified_fuel.convert("5/0")

def test_fraction():
    assert modified_fuel.convert("3/4") == 75

def test_E():
    assert modified_fuel.gauge(1) == "E"

def test_F():
    assert modified_fuel.gauge(99) == "F"

def test_percent():
    assert modified_fuel.gauge(75) == f"percent = {75}%"