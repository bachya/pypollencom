"""Define an object that retrieves allergen data."""

import pypollencom.api as api


class Allergens(api.BaseAPI):
    """Define an API to get overview information."""

    def __init__(self, zip_code):
        """Initialize."""
        super().__init__()
        self.zip_code = zip_code

    def current(self):
        """Get current allergen info."""
        return self._get_data('forecast/current/pollen')

    def extended(self):
        """Get extended allergen info."""
        return self._get_data('forecast/extended/pollen')

    def historic(self):
        """Get historic allergen info."""
        return self._get_data('forecast/historic/pollen')

    def outlook(self):
        """Get allergen outlook."""
        return self._get_data('forecast/outlook')
