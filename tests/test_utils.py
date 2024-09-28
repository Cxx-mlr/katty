from katty.utils import is_prime, random_prime
import pytest

@pytest.mark.parametrize(
        ("number", "expected"),
        (
            (1, False), (2, True), (3, True),
            (4, False), (5, True),(6, False),
            (7, True), (8, False),(9, False),
            (10, False), (11, True), (12, False),
            (13, True), (14, False), (15, False)
        )
)
def test_is_prime(number: int, expected: bool):
    assert (is_prime(number) == expected)

def test_random_prime():
    for n in range(2, 1000):
        assert is_prime(random_prime(n))