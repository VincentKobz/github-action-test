from main import addition


def test_add_2():
    assert addition(1, 2) == 3


def test_add_3():
    assert addition(1, 5) == 6
