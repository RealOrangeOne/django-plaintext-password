#!/usr/bin/env bash

export PATH=env/bin:${PATH}

set -ex


pytest --verbose --cov plaintext_password/ --cov-report term --cov-report html --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,ops --benchmark-group-by=func

if hash black 2>/dev/null;
then
    black plaintext_password tests setup.py --check
fi

ruff check plaintext_password tests setup.py

mypy plaintext_password tests setup.py
