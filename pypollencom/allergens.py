"""Define an API to get allergy information."""

from pypollencom.api import BaseAPI, raise_on_empty_data


class Allergens(BaseAPI):
    """Define an object that retrieves allergen data."""

    def __init__(self, zip_code):
        """Initialize."""
        super().__init__(zip_code)

    @raise_on_empty_data
    def current(self):
        """Get current allergen info."""
        return self.get('forecast/current/pollen').json()

    @raise_on_empty_data
    def extended(self):
        """Get extended allergen info."""
        return self.get('forecast/extended/pollen').json()

    @raise_on_empty_data
    def historic(self):
        """Get historic allergen info."""
        return self.get('forecast/historic/pollen').json()

    def outlook(self):
        """Get allergen outlook."""
        return self.get('forecast/outlook').json()
