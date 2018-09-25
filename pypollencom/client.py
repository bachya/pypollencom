"""Define a client to interact with Pollen.com."""
from aiohttp import ClientSession, client_exceptions

from .allergens import Allergens
from .disease import Disease
from .errors import RequestError

API_BASE = 'https://www.pollen.com'
API_URL_SCAFFOLD = '{0}/api'.format(API_BASE)
API_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) ' \
    + 'AppleWebKit/537.36 (KHTML, like Gecko) ' \
    + 'Chrome/65.0.3325.181 Safari/537.36'


class Client:  # pylint: disable=too-few-public-methods
    """Define the client."""

    def __init__(self, zip_code: str, websession: ClientSession) -> None:
        """Initialize."""
        self._websession = websession
        self.zip_code = zip_code

        self.allergens = Allergens(self.request)
        self.disease = Disease(self.request)

    async def request(
            self,
            method: str,
            endpoint: str,
            *,
            headers: dict = None,
            params: dict = None,
            json: dict = None) -> dict:
        """Make a request against AirVisual."""
        url = '{0}/{1}/{2}'.format(API_URL_SCAFFOLD, endpoint, self.zip_code)

        if not headers:
            headers = {}
        headers.update({
            'Content-Type': 'application/json',
            'Referer': API_BASE,
            'User-Agent': API_USER_AGENT
        })

        async with self._websession.request(method, url, headers=headers,
                                            params=params, json=json) as resp:
            try:
                resp.raise_for_status()
                data = await resp.json(content_type=None)
                return data
            except client_exceptions.ClientError as err:
                raise RequestError(
                    'Error requesting data from {0}: {1}'.format(
                        endpoint, err)) from None
