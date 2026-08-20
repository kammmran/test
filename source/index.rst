
Welcome to Lumache's documentation!
===================================

**Lumache** (/lu'make/) is a Python library for cooks and food lovers that
creates recipes mixing random ingredients. It pulls data from the `Open Food
Facts database <https://world.openfoodfacts.org/>`_ and offers a *simple* and
*intuitive* API.

.. note::
   This project is under active development.

.. warning::
   This library is still in beta. API changes may occur.

Features
--------

- **Random Recipe Generation**: Generate random pasta recipes
- **Ingredient Management**: Easy ingredient selection and management
- **Cooking Time Estimation**: Get estimated cooking times for different pasta types
- **Exception Handling**: Proper error handling with custom exceptions

Getting Started
---------------

To get started with Lumache, see the :doc:`usage` section.

For detailed API documentation, check the :doc:`api/modules` section.

Quick Example
^^^^^^^^^^^^^

.. code-block:: python

    from lumache import get_random_ingredients, make_pasta
    
    # Get random ingredients
    ingredients = get_random_ingredients()
    print(ingredients)
    
    # Create a pasta dish
    dish = make_pasta('spaghetti', 'tomato', ingredients)
    print(dish)

.. important::
   Make sure you have Python 3.6+ installed before using Lumache.

API Documentation
------------------

.. autosummary::
   :toctree: api
   :recursive:

   lumache

Table of Contents
------------------

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   usage
   api/modules
   examples
   troubleshooting


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`