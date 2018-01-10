"""Define an API to get disease information."""

import pypollencom.api as api
import pypollencom.exceptions as exceptions


class Disease(api.BaseAPI):
    """Define an object that retrieves disease data."""

    def __init__(self, zip_code):
        """Initialize."""
        super().__init__()
        self.zip_code = zip_code

    def extended(self):
        """Get extended allergen info."""
        data = self._get_data('forecast/extended/cold')
        if data['Location']['periods']:
            return data
        else:
            raise exceptions.BadZipCodeError(
                'Bad ZIP Code: {0}'.format(self.zip_code))
