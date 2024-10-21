import pytest


def check_age(age: int):
    if age >= 18:  # Введите условие для проверки возраста
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'
    return result

@pytest.mark.parametrize(
    "age, expected",
    (
    (25, 'Доступ разрешён'),
    (10, 'Доступ запрещён'),
    (18, 'Доступ разрешён'),
    (17, 'Доступ запрещён')
    )
)
def test_check_age_with_params(age,expected):
    result = check_age(age)
    assert result == expected









