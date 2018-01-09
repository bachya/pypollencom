"""Define a set of base API tests."""

# pylint: disable=wildcard-import,redefined-outer-name,unused-wildcard-import

import pytest
import requests_mock

import pypollencom
from tests.fixtures.general import *  # noqa


def test_api_exception(zip_code):
    """Test what happens some HTTP error occurs."""
    with requests_mock.Mocker() as mock:
        mock.get(
            '{0}/forecast/current/pollen/{1}'.format(
                pypollencom.const.POLLEN_API_BASE_URL,
                zip_code),
            status_code=404)

        with pytest.raises(pypollencom.exceptions.HTTPError) as exc_info:
            client = pypollencom.Client(zip_code)
            client.allergens.current()
            assert '404' in str(exc_info)
