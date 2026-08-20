Usage
=====



Basic Usage
-----------

Getting Random Ingredients
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients


Creating a Pasta Dish
^^^^^^^^^^^^^^^^^^^^^

To create a complete pasta dish, use the ``make_pasta()`` function:

.. autofunction:: lumache.make_pasta


Estimating Cooking Time
^^^^^^^^^^^^^^^^^^^^^^^

Get cooking time estimates for different pasta types:

.. autofunction:: lumache.estimate_cooking_time


API Reference
-------------

Complete Module Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: lumache
   :members:
   :undoc-members:
   :show-inheritance:


Exception Handling
------------------

Invalid Kind Error
^^^^^^^^^^^^^^^^^^^

The library raises ``InvalidKindError`` when an invalid ingredient kind is provided:

.. autoexception:: lumache.InvalidKindError


Detailed Examples
-----------------

Example 1: Simple Usage
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from lumache import get_random_ingredients
    
    # Get default random ingredients
    ingredients = get_random_ingredients()
    print(f"Ingredients: {ingredients}")


Example 2: Using Specific Ingredient Kinds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from lumache import get_random_ingredients
    
    # Get pasta ingredients
    pasta = get_random_ingredients(kind='pasta')
    
    # Get sauce ingredients
    sauce = get_random_ingredients(kind='sauce')
    
    # Get vegetable ingredients
    vegetables = get_random_ingredients(kind='vegetables')
    
    print(f"Pasta: {pasta}")
    print(f"Sauce: {sauce}")
    print(f"Vegetables: {vegetables}")


Example 3: Creating a Complete Dish
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from lumache import make_pasta, get_random_ingredients, estimate_cooking_time
    
    # Create a pasta dish
    dish = make_pasta(
        pasta_type='spaghetti',
        sauce_type='tomato',
        ingredients=['garlic', 'basil', 'olive oil']
    )
    
    # Get cooking time
    time = estimate_cooking_time('spaghetti')
    
    print(f"Dish: {dish}")
    print(f"Cooking time: {time} minutes")


Example 4: Error Handling
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from lumache import get_random_ingredients, InvalidKindError
    
    try:
        ingredients = get_random_ingredients(kind='invalid_kind')
    except InvalidKindError as e:
        print(f"Error: {e}")


Tips and Best Practices
-----------------------

.. tip::
   Use specific ingredient kinds to have more control over your recipes.

.. hint::
   Cooking times are approximate and may vary based on personal preference.

.. caution::
   Always validate ingredient kinds before calling functions.


Performance Notes
-----------------

.. note::
   The library uses Python's built-in ``random`` module for ingredient selection.
   For reproducible results, seed the random module before calling functions.


See Also
--------

* `Open Food Facts Database <https://world.openfoodfacts.org/>`_
* :py:mod:`random` module documentation
* :doc:`../examples`