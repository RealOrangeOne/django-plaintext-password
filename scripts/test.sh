#!/usr/bin/env bash

export PATH=env/bin:${PATH}
export PYTHONPATH=$PWD

set -ex


pytest --verbose --cov plaintext_password/ --cov-report term --cov-report html --benchmark-sort=mean --benchmark-columns=min,max,mean,stddev,ops --benchmark-group-by=func

ruff check plaintext_password tests setup.py
ruff format --check plaintext_password tests setup.py

mypy plaintext_password tests setup.py
