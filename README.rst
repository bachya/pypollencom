🌼 pypollencom: A Simple Python API for Pollen.com
==================================================

.. image:: https://travis-ci.org/bachya/pypollencom.svg?branch=master
  :target: https://travis-ci.org/bachya/pypollencom

.. image:: https://img.shields.io/pypi/v/pypollencom.svg
  :target: https://pypi.python.org/pypi/pypollencom

.. image:: https://img.shields.io/pypi/pyversions/pypollencom.svg
  :target: https://pypi.python.org/pypi/pypollencom

.. image:: https://img.shields.io/pypi/l/pypollencom.svg
  :target: https://github.com/bachya/pypollencom/blob/master/LICENSE

.. image:: https://codecov.io/gh/bachya/pypollencom/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/bachya/pypollencom

.. image:: https://api.codeclimate.com/v1/badges/71eb642c735e33adcdfc/maintainability
  :target: https://codeclimate.com/github/bachya/pypollencom

.. image:: https://img.shields.io/badge/SayThanks-!-1EAEDB.svg
  :target: https://saythanks.io/to/bachya

pypollencom is a simple Python library for allergen and disease data from
`Pollen.com <http://www.pollen.com/>`_.

🌼 PLEASE READ: 1.0.0 and Beyond
================================

Version 1.0.0 of pypollencom makes several breaking, but necessary changes:

* Moves the underlying library from
  `Requests <http://docs.python-requests.org/en/master/>`_ to
  `aiohttp <https://aiohttp.readthedocs.io/en/stable/>`_
* Changes the entire library to use :code:`asyncio`
* Makes 3.5 the minimum version of Python required

If you wish to continue using the previous, synchronous version of
pypollencom, make sure to pin version 1.1.2.

🌼 Installation
===============

.. code-block:: bash

  $ pip install pypollencom

🌼 Usage
========

.. code-block:: python

  import pypollencom

pyairvisual starts within an
`aiohttp <https://aiohttp.readthedocs.io/en/stable/>`_ :code:`ClientSession`:

.. code-block:: python

  import asyncio

  from aiohttp import ClientSession

  from pyairvisual import Client


  async def main() -> None:
      """Create the aiohttp session and run the example."""
      async with ClientSession() as websession:
          await run(websession)


  async def run(websession):
      """Run."""
      # YOUR CODE HERE

  asyncio.get_event_loop().run_until_complete(main())

Create a client:

.. code-block:: python

  client = pypollencom.Client(80012)

  # ZIP codes starting with 0 need to be provided as strings:
  client = pypollencom.Client('00544')

Then, get to it!

.. code-block:: python

  # Get current allergen information:
  client.allergens.current()

  # Get more information on the current allergen outlook:
  client.allergens.outlook()

  # Get extended forecast allergen information:
  client.allergens.extended()

  # Get historic allergen information:
  client.allergens.historic()

  # Get extended forecast cold and flu information:
  client.disease.extended()


🌼 Contributing
===============

#. `Check for open features/bugs <https://github.com/bachya/pypollencom/issues>`_
   or `initiate a discussion on one <https://github.com/bachya/pypollencom/issues/new>`_.
#. `Fork the repository <https://github.com/bachya/pypollencom/fork>`_.
#. Install the dev environment: :code:`make init`.
#. Enter the virtual environment: :code:`pipenv shell`
#. Code your new feature or bug fix.
#. Write a test that covers your new functionality.
#. Run tests: :code:`make test`
#. Build new docs: :code:`make docs`
#. Add yourself to AUTHORS.rst.
#. Submit a pull request!
