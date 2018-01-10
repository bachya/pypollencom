"""Define an API to get disease information."""

from pypollencom.api import BaseAPI, raise_on_empty_data


class Disease(BaseAPI):
    """Define an object that retrieves disease data."""

    def __init__(self, zip_code):
        """Initialize."""
        super().__init__(zip_code)

    @raise_on_empty_data
    def extended(self):
        """Get extended allergen info."""
        return self.get('forecast/extended/cold').json()
