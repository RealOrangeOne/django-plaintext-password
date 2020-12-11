#!/usr/bin/env bash

export PATH=env/bin:${PATH}

set -ex


pytest --verbose --cov plaintext_password/ --cov-report term --cov-report html

if hash black 2>/dev/null;
then
    black plaintext_password tests setup.py --check
fi

flake8 plaintext_password tests setup.py

isort -rc -c plaintext_password tests setup.py

mypy plaintext_password tests setup.py
