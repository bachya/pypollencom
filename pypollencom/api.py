"""Define a base object for interacting with the Pollen.com website."""

import requests

from pypollencom.const import POLLEN_BASE, POLLEN_API_BASE_URL
from pypollencom.exceptions import HTTPError


class BaseAPI(object):
    """Define a class that represents an API request."""

    def __init__(self, zip_code):
        """Initialize."""
        self.full_url = None
        self.zip_code = zip_code

    def request(self, method_type, url, **kwargs):
        """Define a generic request."""
        kwargs.setdefault('headers', {})['Referer'] = POLLEN_BASE

        self.full_url = '{0}/{1}/{2}'.format(POLLEN_API_BASE_URL, url,
                                             self.zip_code)
        method = getattr(requests, method_type)
        resp = method(self.full_url, **kwargs)

        # I don't think it's good form to make end users of pypollencom have to
        #  explicitly catch exceptions from a sub-library, so here, I wrap the
        # Requests HTTPError in my own:
        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError as exc_info:
            raise HTTPError(str(exc_info)) from None

        return resp

    def get(self, url, **kwargs):
        """Define a generic GET request."""
        return self.request('get', url, **kwargs)


def raise_on_empty_data(function):
    """Define a decorator to raise an exception on an invalid ZIP code."""

    def decorator(self, *args, **kwargs):
        """ Decorate! """
        data = function(self, *args, **kwargs)
        if data.get('Location', {}).get('periods', None):
            return data
        else:
            raise HTTPError('404 Client Error: Not Found for url: {0}'.format(
                self.full_url))

    return decorator
