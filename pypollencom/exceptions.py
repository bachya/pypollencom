"""Define module exceptions."""


class BadZipCodeError(Exception):
    """Define an error when a bad ZIP code is used."""
    pass


class HTTPError(Exception):
    """Define a generic HTTP error (i.e., a wrapper for Requests)."""
    pass
