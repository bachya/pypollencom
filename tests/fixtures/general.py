"""Define generic fixtures to use anywhere."""

import pytest


@pytest.fixture(scope='session')
def zip_code():
    """Define a password."""
    return '80238'
