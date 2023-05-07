import pytest

from my_funcs.calculator import simple_calculator


@pytest.mark.parametrize("num_1, num_2, operation, expected_result", [(3, 3, "+", 6),
                                                                      (3, 3, "-", 0),
                                                                      (3, 3, "/", 1),
                                                                      (3, 3, "*", 9),

                                                                      (1, -5, "+", -4),
                                                                      (0, 10, "-", -10),
                                                                      (4, 2, "/", 2),
                                                                      (9, 0, "*", 0),
                                                                      ])
def test_simple_calculator_with_deco(num_1, num_2, operation, expected_result):
    result = simple_calculator(num_1, num_2, operation)
    assert result == expected_result
