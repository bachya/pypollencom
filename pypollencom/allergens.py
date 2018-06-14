"""Define an object to work with "Allergens" endpoints."""
from .decorators import raise_on_invalid_zip
from .errors import InvalidZipError, RequestError


class Allergens(object):
    """Define the "Allergens" object."""

    def __init__(self, request):
        """Initialize."""
        self._request = request

    @raise_on_invalid_zip
    async def current(self):
        """Get current allergy conditions."""
        return await self._request('get', 'forecast/current/pollen')

    @raise_on_invalid_zip
    async def extended(self):
        """Get extended allergen info."""
        return await self._request('get', 'forecast/extended/pollen')

    @raise_on_invalid_zip
    async def historic(self):
        """Get historic allergen info."""
        return await self._request('get', 'forecast/historic/pollen')

    async def outlook(self):
        """Get allergen outlook."""
        try:
            return await self._request('get', 'forecast/outlook')
        except RequestError as err:
            if '404' in str(err):
                raise InvalidZipError('No data returned for ZIP code')
            else:
                raise RequestError(err)
