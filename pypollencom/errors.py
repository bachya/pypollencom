"""Define errors."""


class PollenComError(Exception):
    """Define a base package error."""


class RequestError(PollenComError):
    """Define a generic request error."""
