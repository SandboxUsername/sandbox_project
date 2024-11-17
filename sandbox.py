import pytest

@pytest.fixture
def a():
    print(1)
    yield
    print(2)

def x():
    return 123

def test_x(a):
    assert x() == 123