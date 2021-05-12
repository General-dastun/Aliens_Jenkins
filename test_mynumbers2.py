# Better version of test_mynumbers.py 
# Here we are combining different tests in one shot instead to having different functions as test_numbers.py

import mynumbers as mm
import pytest

@pytest.mark.parametrize("x,y, result",
                        [
                            (7,3,10),
                            (1.2,1.3,2.5),
                            ('h','i','hi')
                        ]
                        ) #any names to be used
# format: 1st argument, 2nd argument, result, iteratable list
def test_calc_total(x,y,result):
    assert mm.calc_total(x,y)==result

    assert mm.calc_total(2,1) is not str #no strings in results?
    assert type(mm.calc_total(2,1)) is not float #results is int type


def test_calc_multpl():
    result = mm.calc_multpl(2,3)
    assert result == 6 #value is correct?
    assert type(result) is int #results is int type
    assert result !=0 #non zero?
    assert (0 <= result <= 1000) #results in a range?
def test_print():
    mytext = mm.print('man')
    assert 'uh' not in mytext #results doesnt include a specific string?

