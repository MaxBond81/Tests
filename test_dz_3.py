import pytest


# На вход программе подаётся одно число n. Напишите программу, которая вернёт список [1, 2, 3, …, n].
def list_of_numbers(n: int) -> list:
    L = [k for k in range(1, n + 1)]
    return L


@pytest.mark.parametrize(
    "n, expected",
    (
    (0, []),
    (1, [1]),
    (3, [1,2,3]),
    (5, [1,2,3,4,5])
    )
)
def test_list_of_numbers(n,expected):
    result = list_of_numbers(n)
    assert result == expected
