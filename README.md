# django-plaintext-password

![CI](https://github.com/RealOrangeOne/django-plaintext-password/workflows/CI/badge.svg)

A Django password hasher to store passwords in plaintext.

## _"Should I use this in production?"_

Oh definitely not. Storing passwords in plaintext is a very *very* bad thing. Django's defaults are incredibly secure and should be used unless you have a good reason not to.

For more on why using this in production is a terrible idea, check out [How to store passwords](https://theorangeone.net/posts/how-to-store-passwords/).

When running deployment checks, this will throw a "CRITICAL" error if in use.

## Installation and usage

```
pip install django-plaintext-password
```

Then add `plaintext_password.PlaintextPasswordHasher` to [`PASSWORD_HASHERS`](https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-PASSWORD_HASHERS) in `settings.py`. To ensure it's used by default, make it the first or only item.

## How does it work?

By default, Django will store the password `password123` in a format similar to:

```
pbkdf2_sha256$216000$gd57n4OWJrXh$Xs/TqhwJICOxsLONGlKXorjuWccooiuJmJOUaxbwcOQ=
```

This is good for security as the password has been both salted and hashed before being saved into the database, making it almost impossible to retrieve the original password. This library however, stores the password as-is:

```
plaintext$$password123
```

This makes searching by password possible, as well as comparing users passwords and allowing you to email users their passwords if they forget them - neat!

In addition to storing the values directly in the database for easy retrieval, the comparison is done simply with `==`, rather than using [`secrets.compare_digest`](https://docs.python.org/3/library/secrets.html#secrets.compare_digest).

## Why?

Well, why not?

Although in all seriousness, If as part of your tests you're creating a large number of users, or just a couple users but you've got a lot of tests, you can get quite a performance improvement by simplifying the password hasher.

Unfortunately due to a limitation (and feature) with Django, it's not possible to store just the value directly, it must be prefixed with the algorithm.
