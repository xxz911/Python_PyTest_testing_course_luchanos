from first_lesson import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5),
                                                   ])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("divisionable, divider, expected_exception", [(10, 0, ZeroDivisionError),
                                                                       (20, "2", TypeError)
                                                                       ])
def test_division_with_error(divisionable, divider, expected_exception):
    with pytest.raises(expected_exception):
        division(divisionable, divider)




