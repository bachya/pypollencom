"""Define an object that retrieves disease data."""

import pypollencom.api as api
import pypollencom.exceptions as exceptions


class Disease(api.BaseAPI):
    """Define an API to get disease information."""

    def __init__(self, zip_code):
        """Initialize."""
        super().__init__()
        self.zip_code = zip_code

    def extended(self):
        """Get the usage information for a particular "premise"."""
        data = self._get_data('forecast/extended/cold')
        if data['Location']['periods']:
            return data
        else:
            raise exceptions.BadZipCodeError(
                'Bad ZIP Code: {0}'.format(self.zip_code))
