"""Define an API to get disease information."""

from pypollencom.api import BaseAPI, raise_on_empty_data


class Disease(BaseAPI):
    """Define an object that retrieves disease data."""

    @raise_on_empty_data
    def extended(self):
        """Get extended allergen info."""
        return self.get('forecast/extended/cold').json()
