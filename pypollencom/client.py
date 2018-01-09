"""Define an Pollen.com client."""

import pypollencom.api as api
from pypollencom.allergens import Allergens
from pypollencom.disease import Disease


class Client(api.BaseAPI):
    """Define an Pollen.com client."""

    def __init__(self, zip_code):
        """Initialize."""
        super().__init__()
        self.zip_code = zip_code

        self.allergens = Allergens(zip_code)
        self.disease = Disease(zip_code)
