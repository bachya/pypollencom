"""Define fixtures for disease data."""

import pytest


@pytest.fixture(scope='session')
def empty_get_200(bad_zip_code):
    """Define successful empty response."""
    return {
        "Type": "cold",
        "ForecastDate": "2018-01-09T00:00:00-05:00",
        "Location": {
            "ZIP": bad_zip_code,
            "periods": []
        }
    }


@pytest.fixture(scope='session')
def extended_get_200():
    """Define successful "extended" response."""
    return {
        "Type": "cold",
        "ForecastDate": "2018-01-09T00:00:00-05:00",
        "Location": {
            "ZIP":
            "80238",
            "City":
            "DENVER",
            "State":
            "CO",
            "periods": [{
                "Period": "2018-01-09T05:06:16.4",
                "Index": 4.7
            }, {
                "Period": "2018-01-10T05:06:16.4",
                "Index": 5.0
            }, {
                "Period": "2018-01-11T05:06:16.4",
                "Index": 5.2
            }, {
                "Period": "2018-01-12T05:06:16.4",
                "Index": 5.1
            }],
            "DisplayLocation":
            "Denver, CO"
        }
    }
