"""Define generic fixtures to use anywhere."""

import pytest


@pytest.fixture(scope='session')
def bad_zip_code():
    """Define a password."""
    return 'bad_zip_code'


@pytest.fixture(scope='session')
def zip_code():
    """Define a password."""
    return '80238'
