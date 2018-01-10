"""Define an object that retrieves allergen data."""

import pypollencom.api as api
import pypollencom.exceptions as exceptions


class Allergens(api.BaseAPI):
    """Define an API to get overview information."""

    def __init__(self, zip_code):
        """Initialize."""
        super().__init__()
        self.zip_code = zip_code

    def current(self):
        """Get current allergen info."""
        data = self._get_data('forecast/current/pollen')
        if data['Location']['periods']:
            return data
        else:
            raise exceptions.BadZipCodeError(
                'Bad ZIP Code: {0}'.format(self.zip_code))

    def extended(self):
        """Get extended allergen info."""
        data = self._get_data('forecast/extended/pollen')
        if data['Location']['periods']:
            return data
        else:
            raise exceptions.BadZipCodeError(
                'Bad ZIP Code: {0}'.format(self.zip_code))

    def historic(self):
        """Get historic allergen info."""
        data = self._get_data('forecast/historic/pollen')
        if data['Location']['periods']:
            return data
        else:
            raise exceptions.BadZipCodeError(
                'Bad ZIP Code: {0}'.format(self.zip_code))

    def outlook(self):
        """Get allergen outlook."""
        try:
            return self._get_data('forecast/outlook')
        except exceptions.HTTPError:
            raise exceptions.BadZipCodeError(
                'Bad ZIP Code: {0}'.format(self.zip_code))
