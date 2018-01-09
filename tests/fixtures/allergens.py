"""Define fixtures for allergen data."""

import pytest


@pytest.fixture(scope='session')
def current_get_200():
    """Define successful "current" response."""
    return {
        "Type": "pollen",
        "ForecastDate": "2018-01-09T00:00:00-05:00",
        "Location": {
            "ZIP":
            "80238",
            "City":
            "DENVER",
            "State":
            "CO",
            "periods": [{
                "Triggers": [{
                    "LGID": 345,
                    "Name": "Mixed Trace",
                    "Genus": "Mixed Trace",
                    "PlantType": "Other"
                }],
                "Period":
                "0001-01-01T00:00:00",
                "Type":
                "Yesterday",
                "Index":
                1.3
            }, {
                "Triggers": [{
                    "LGID": 272,
                    "Name": "Juniper",
                    "Genus": "Juniperus",
                    "PlantType": "Tree"
                }],
                "Period":
                "0001-01-01T00:00:00",
                "Type":
                "Today",
                "Index":
                2.4
            }, {
                "Triggers": [{
                    "LGID": 272,
                    "Name": "Juniper",
                    "Genus": "Juniperus",
                    "PlantType": "Tree"
                }],
                "Period":
                "0001-01-01T00:00:00",
                "Type":
                "Tomorrow",
                "Index":
                0.7
            }],
            "DisplayLocation":
            "Denver, CO"
        }
    }


@pytest.fixture(scope='session')
def extended_get_200():
    """Define successful "extended" response."""
    return {
        "Type": "pollen",
        "ForecastDate": "2018-01-09T00:00:00-05:00",
        "Location": {
            "ZIP":
            "80238",
            "City":
            "DENVER",
            "State":
            "CO",
            "periods": [{
                "Period": "2018-01-09T12:02:18.503",
                "Index": 2.40
            }, {
                "Period": "2018-01-10T12:02:18.503",
                "Index": 0.70
            }, {
                "Period": "2018-01-11T12:02:18.503",
                "Index": 0.10
            }, {
                "Period": "2018-01-12T12:02:18.503",
                "Index": 1.40
            }, {
                "Period": "2018-01-13T12:02:18.503",
                "Index": 0.10
            }],
            "DisplayLocation":
            "Denver, CO"
        }
    }


@pytest.fixture(scope='session')
def historic_get_200():
    """Define successful "extended" response."""
    return {
        "Type": "pollen",
        "ForecastDate": "2018-01-09T00:00:00-05:00",
        "Location": {
            "ZIP":
            "80238",
            "City":
            "DENVER",
            "State":
            "CO",
            "periods": [{
                "Period": "2017-12-11T05:30:03",
                "Index": 0.10
            }, {
                "Period": "2017-12-12T05:30:04",
                "Index": 0.10
            }, {
                "Period": "2017-12-13T05:30:07",
                "Index": 0.10
            }, {
                "Period": "2017-12-14T05:30:01",
                "Index": 0.10
            }],
            "DisplayLocation":
            "Denver, CO"
        }
    }


@pytest.fixture(scope='session')
def outlook_get_200():
    """Define successful "extended" response."""
    return {
        "Market":
        "DENVER, CO",
        "ZIP":
        "80238",
        "TrendID":
        1,
        "Trend":
        "low",
        "Outlook":
        "The pollen levels for Tuesday will be increasing.",
        "Season":
        "Tree"
    }
