"""Define an object to work with "Allergens" endpoints."""


class Allergens(object):
    """Define the "Allergens" object."""

    def __init__(self, request):
        """Initialize."""
        self._request = request

    async def current(self):
        """Get current allergy conditions."""
        return await self._request('get', 'forecast/current/pollen')

    async def extended(self):
        """Get extended allergen info."""
        return await self._request('get', 'forecast/extended/pollen')

    async def historic(self):
        """Get historic allergen info."""
        return await self._request('get', 'forecast/historic/pollen')

    async def outlook(self):
        """Get allergen outlook."""
        return await self._request('get', 'forecast/outlook')
