"""Define a base object for interacting with the Xcel Energy® website."""

import requests

import pypollencom.const as const
import pypollencom.exceptions as exceptions


class BaseAPI(object):
    """Define a class that represents an API request."""

    def _get_data(self, endpoint):
        """Return JSON from a generic endpoint."""
        return self.get('{0}/{1}'.format(endpoint, self.zip_code)).json()

    @staticmethod
    def request(method_type, url, **kwargs):
        """Define a generic request."""
        kwargs.setdefault('headers', {})['Referer'] = const.POLLEN_BASE

        full_url = '{0}/{1}'.format(const.POLLEN_API_BASE_URL, url)
        method = getattr(requests, method_type)
        resp = method(full_url, **kwargs)

        # I don't think it's good form to make end users of pytile have to
        #  explicitly catch exceptions from a sub-library, so here, I wrap the
        # Requests HTTPError in my own:
        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError as exc_info:
            raise exceptions.HTTPError(str(exc_info)) from None

        return resp

    def get(self, url, **kwargs):
        """Define a generic GET request."""
        return self.request('get', url, **kwargs)
