"""Define an Pollen.com client."""

from pypollencom.allergens import Allergens
from pypollencom.disease import Disease


# pylint: disable=too-few-public-methods
class Client(object):
    """Define a Pollen.com client."""

    def __init__(self, zip_code):
        """Initialize."""
        self.zip_code = zip_code

        self.allergens = Allergens(zip_code)
        self.disease = Disease(zip_code)
