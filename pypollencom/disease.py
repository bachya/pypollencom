"""Define an object to work with "Disease" endpoints."""


class Disease(object):  # pylint: disable=too-few-public-methods
    """Define the "Disease" object."""

    def __init__(self, request):
        """Initialize."""
        self._request = request

    async def extended(self):
        """Get extended disease info."""
        return await self._request('get', 'forecast/extended/cold')
