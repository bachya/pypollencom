"""Define useful decorators."""
from .errors import InvalidZipError


def raise_on_invalid_zip(func):
    """Raise an exception when there's no data (via a bad ZIP code)."""

    async def decorator(*args, **kwargs):
        """Decorate."""
        data = await func(*args, **kwargs)
        if not data['Location']['periods']:
            raise InvalidZipError('No data returned for ZIP code')
        return data

    return decorator
