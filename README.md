# 🌼 pypollencom: A Simple Python API for Pollen.com

[![Travis CI](https://travis-ci.org/bachya/pypollencom.svg?branch=master)](https://travis-ci.org/bachya/pypollencom)
[![PyPi](https://img.shields.io/pypi/v/pypollencom.svg)](https://pypi.python.org/pypi/pypollencom)
[![Version](https://img.shields.io/pypi/pyversions/pypollencom.svg)](https://pypi.python.org/pypi/pypollencom)
[![License](https://img.shields.io/pypi/l/pypollencom.svg)](https://github.com/bachya/pypollencom/blob/master/LICENSE)
[![Code Coverage](https://codecov.io/gh/bachya/pypollencom/branch/master/graph/badge.svg)](https://codecov.io/gh/bachya/pypollencom)
[![Maintainability](https://api.codeclimate.com/v1/badges/71eb642c735e33adcdfc/maintainability)](https://codeclimate.com/github/bachya/pypollencom/maintainability)
[![Say Thanks](https://img.shields.io/badge/SayThanks-!-1EAEDB.svg)](https://saythanks.io/to/bachya)

`pypollencom` is a simple Python library for allergen, asthma, and disease data
from [Pollen.com](http://www.pollen.com/).

# PLEASE READ: Version 2.0.0 and Beyond

Version 2.0.0 of `pypollencom` makes several breaking, but necessary changes:

* Moves the underlying library from
  [Requests](http://docs.python-requests.org/en/master/) to
  [aiohttp](https://aiohttp.readthedocs.io/en/stable/)
* Changes the entire library to use `asyncio`
* Makes 3.6 the minimum version of Python required

If you wish to continue using the previous, synchronous version of
`pypollencom`, make sure to pin version 1.1.2.

# Installation

```python
pip install pypollencom
```

# Usage

`pypollencom` starts within an
[aiohttp](https://aiohttp.readthedocs.io/en/stable/) `ClientSession`:

```python
import asyncio

from aiohttp import ClientSession

from pypollencom import Client


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
      # YOUR CODE HERE


asyncio.get_event_loop().run_until_complete(main())
```

Create a client and get to it:

```python
import asyncio

from aiohttp import ClientSession

from pypollencom import Client


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
      client = Client(80012, websession)

      # ZIP codes starting with 0 need to be provided as strings:
      client = Client('00544', websession)

      # Get current allergen information:
      await client.allergens.current()

      # Get more information on the current allergen outlook:
      await client.allergens.outlook()

      # Get extended forecast allergen information:
      await client.allergens.extended()

      # Get historic allergen information:
      await client.allergens.historic()

      # Get current asthma information:
      await client.asthma.current()

      # Get extended forecast asthma information:
      await client.asthma.extended()

      # Get historic asthma information:
      await client.asthma.historic()

      # Get extended forecast cold and flu information:
      await client.disease.extended()


asyncio.get_event_loop().run_until_complete(main())
```

# Contributing

1. [Check for open features/bugs](https://github.com/bachya/pypollencom/issues)
  or [initiate a discussion on one](https://github.com/bachya/pypollencom/issues/new).
2. [Fork the repository](https://github.com/bachya/pypollencom/fork).
3. Install the dev environment: `make init`.
4. Enter the virtual environment: `pipenv shell`
5. Code your new feature or bug fix.
6. Write a test that covers your new functionality.
7. Run tests and ensure 100% code coverage: `make coverage`
8. Add yourself to `AUTHORS.md`.
9. Submit a pull request!
