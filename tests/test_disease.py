"""Define a set of tests for the usages API."""

# pylint: disable=wildcard-import,redefined-outer-name,unused-wildcard-import

import json

import pytest
import requests_mock

import pypollencom
from pypollencom.const import POLLEN_API_BASE_URL
from tests.fixtures.general import *  # noqa
from tests.fixtures.disease import *  # noqa


def test_disease_operations(extended_get_200, zip_code):
    """Test all operations associated with the allergens module."""
    with requests_mock.Mocker() as mock:
        mock.get(
            '{0}/forecast/extended/cold/{1}'.format(
                POLLEN_API_BASE_URL,
                zip_code),
            text=json.dumps(extended_get_200))

        client = pypollencom.Client(zip_code)
        assert client.disease.extended() == extended_get_200
