"""Define tests for the "Asthma" object."""
# pylint: disable=redefined-outer-name,unused-import

import json

import aiohttp
import pytest

from pypollencom import Client

from .const import TEST_ZIP
from .fixtures.asthma import *  # noqa


@pytest.mark.asyncio
async def test_endpoints(aresponses, event_loop, fixture_extended):
    """Test all endpoints."""
    aresponses.add(
        'www.asthmaforecast.com',
        '/api/forecast/extended/asthma/{0}'.format(TEST_ZIP), 'get',
        aresponses.Response(text=json.dumps(fixture_extended), status=200))

    async with aiohttp.ClientSession(loop=event_loop) as websession:
        client = Client(TEST_ZIP, websession)

        extended = await client.asthma.extended()
        assert len(extended['Location']['periods']) == 5
