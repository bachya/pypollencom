"""Define tests for the "Supported" object."""
# pylint: disable=redefined-outer-name,unused-import

import json

import aiohttp
import pytest

from pypollencom import Client

from .const import TEST_ZIP


@pytest.fixture(scope='module')
def fixture_extended():
    """Return a /forecast/extended/cold/<ZIP> response."""
    return {
        "Type": "cold",
        "ForecastDate": "2018-06-12T00:00:00-04:00",
        "Location": {
            "ZIP":
                "80238",
            "City":
                "DENVER",
            "State":
                "CO",
            "periods": [{
                "Period": "2018-06-12T05:13:51.817",
                "Index": 2.4
            }, {
                "Period": "2018-06-13T05:13:51.817",
                "Index": 2.5
            }, {
                "Period": "2018-06-14T05:13:51.817",
                "Index": 2.5
            }, {
                "Period": "2018-06-15T05:13:51.817",
                "Index": 2.5
            }],
            "DisplayLocation":
                "Denver, CO"
        }
    }


@pytest.mark.asyncio
async def test_endpoints(aresponses, event_loop, fixture_extended):
    """Test all endpoints."""
    aresponses.add(
        'www.pollen.com',
        '/api/forecast/extended/cold/{0}'.format(TEST_ZIP), 'get',
        aresponses.Response(text=json.dumps(fixture_extended), status=200))

    async with aiohttp.ClientSession(loop=event_loop) as websession:
        client = Client(TEST_ZIP, websession)

        extended = await client.disease.extended()
        assert len(extended['Location']['periods']) == 4
