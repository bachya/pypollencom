"""Define a set of tests for the overview API."""

# pylint: disable=wildcard-import,redefined-outer-name,unused-wildcard-import

import json

import pytest
import requests_mock

from pypollencom import Client
from pypollencom.const import POLLEN_API_BASE_URL
from pypollencom.exceptions import HTTPError
from tests.fixtures.general import *  # noqa
from tests.fixtures.allergens import *  # noqa


def test_allergen_operations(current_get_200, extended_get_200,
                             historic_get_200, outlook_get_200, zip_code):
    """Test all operations associated with the allergens module."""
    with requests_mock.Mocker() as mock:
        mock.get(
            '{0}/forecast/current/pollen/{1}'.format(
                POLLEN_API_BASE_URL,
                zip_code),
            text=json.dumps(current_get_200))
        mock.get(
            '{0}/forecast/extended/pollen/{1}'.format(
                POLLEN_API_BASE_URL,
                zip_code),
            text=json.dumps(extended_get_200))
        mock.get(
            '{0}/forecast/historic/pollen/{1}'.format(
                POLLEN_API_BASE_URL,
                zip_code),
            text=json.dumps(historic_get_200))
        mock.get(
            '{0}/forecast/outlook/{1}'.format(
                POLLEN_API_BASE_URL,
                zip_code),
            text=json.dumps(outlook_get_200))

        client = Client(zip_code)
        assert client.allergens.current() == current_get_200
        assert client.allergens.extended() == extended_get_200
        assert client.allergens.historic() == historic_get_200
        assert client.allergens.outlook() == outlook_get_200


def test_bad_zip_codes(bad_zip_code, empty_get_200):
    """Test all operations associated with the allergens module."""
    with requests_mock.Mocker() as mock:
        mock.get(
            '{0}/forecast/current/pollen/{1}'.format(
                POLLEN_API_BASE_URL,
                bad_zip_code),
            text=json.dumps(empty_get_200))
        mock.get(
            '{0}/forecast/extended/pollen/{1}'.format(
                POLLEN_API_BASE_URL,
                bad_zip_code),
            text=json.dumps(empty_get_200))
        mock.get(
            '{0}/forecast/historic/pollen/{1}'.format(
                POLLEN_API_BASE_URL,
                bad_zip_code),
            text=json.dumps(empty_get_200))
        mock.get(
            '{0}/forecast/outlook/{1}'.format(
                POLLEN_API_BASE_URL,
                bad_zip_code),
            status_code=404)

        with pytest.raises(HTTPError) as exc:
            client = Client(bad_zip_code)
            client.allergens.current()
            assert bad_zip_code in str(exc)

        with pytest.raises(HTTPError) as exc:
            client = Client(bad_zip_code)
            client.allergens.extended()
            assert bad_zip_code in str(exc)

        with pytest.raises(HTTPError) as exc:
            client = Client(bad_zip_code)
            client.allergens.historic()
            assert bad_zip_code in str(exc)

        with pytest.raises(HTTPError) as exc:
            client = Client(bad_zip_code)
            client.allergens.outlook()
            assert bad_zip_code in str(exc)
