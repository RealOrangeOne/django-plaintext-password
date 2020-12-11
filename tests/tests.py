import pytest
from django.contrib.auth.hashers import (
    check_password,
    get_hashers_by_algorithm,
    identify_hasher,
    make_password,
)
from hypothesis import given
from hypothesis.strategies import text

from plaintext_password import PlaintextPasswordHasher

PASSWORD = "password123"


@given(text())
def test_makes_plaintext_password(password):
    hashed_password = make_password(password, hasher="plaintext")
    assert hashed_password == f"plaintext$${password}"


@given(text())
def test_check_password(password):
    assert check_password(password, f"plaintext$${password}")


@pytest.mark.parametrize("password", {"$password$", "!password!"})
def test_check_password_with_unsafe_char(password):
    hashed_password = make_password(password, hasher="plaintext")
    assert check_password(password, hashed_password)


@given(text())
def test_end_to_end(password):
    hashed_password = make_password(password, hasher="plaintext")
    assert check_password(password, hashed_password)


def test_identify_hasher():
    assert isinstance(identify_hasher("plaintext$$password"), PlaintextPasswordHasher)


@pytest.mark.parametrize("hasher", get_hashers_by_algorithm().keys())
def test_make_password_performance(hasher, benchmark):
    benchmark(make_password, PASSWORD, hasher=hasher)


@pytest.mark.parametrize("hasher", get_hashers_by_algorithm().keys())
def test_check_password_performance(hasher, benchmark):
    encoded_password = make_password(PASSWORD, hasher=hasher)
    benchmark(check_password, PASSWORD, encoded_password)
