"""Define a set of tests for the usages API."""

# pylint: disable=wildcard-import,redefined-outer-name,unused-wildcard-import

import json

import pytest
import requests_mock

from pypollencom import Client
from pypollencom.const import POLLEN_API_BASE_URL
from pypollencom.exceptions import HTTPError
from tests.fixtures.general import *  # noqa
from tests.fixtures.disease import *  # noqa


def test_bad_zip_codes(bad_zip_code, empty_get_200):
    """Test all operations associated with the allergens module."""
    with requests_mock.Mocker() as mock:
        mock.get(
            '{0}/forecast/extended/cold/{1}'.format(
                POLLEN_API_BASE_URL,
                bad_zip_code),
            text=json.dumps(empty_get_200))

        with pytest.raises(HTTPError) as exc:
            client = Client(bad_zip_code)
            client.disease.extended()
            assert bad_zip_code in str(exc)


def test_disease_operations(extended_get_200, zip_code):
    """Test all operations associated with the allergens module."""
    with requests_mock.Mocker() as mock:
        mock.get(
            '{0}/forecast/extended/cold/{1}'.format(POLLEN_API_BASE_URL,
                                                    zip_code),
            text=json.dumps(extended_get_200))

        client = Client(zip_code)
        assert client.disease.extended() == extended_get_200
