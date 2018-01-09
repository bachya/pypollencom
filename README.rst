pypollencom: A Simple Python API for Xcel Energy® Data
=================================================

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

Installation
============

.. code-block:: bash

  $ pip install pypollencom

Usage
=====

.. code-block:: python

  import pypollencom

  # Create a client:
  client = pypollencom.Client()

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


Contributing
============

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
