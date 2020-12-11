from django.contrib.auth.hashers import check_password, make_password


def test_makes_plaintext_password():
    hashed_password = make_password("password", hasher="plaintext")
    assert hashed_password == "plaintext$$password"


def test_check_password():
    assert check_password("password", "plaintext$$password")


def test_check_password_with_unsafe_char():
    hashed_password = make_password("$password$", hasher="plaintext")
    assert check_password("$password$", hashed_password)
