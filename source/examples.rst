Examples and Recipes
====================

This section contains practical examples of using Lumache.

Recipe: Classic Spaghetti Carbonara
------------------------------------

Creating a traditional Italian carbonara recipe:

.. code-block:: python

    from lumache import make_pasta, estimate_cooking_time
    
    # Define carbonara ingredients
    carbonara_ingredients = ['guanciale', 'eggs', 'pecorino', 'black pepper']
    
    # Create the dish
    dish = make_pasta(
        pasta_type='spaghetti',
        sauce_type='cream',
        ingredients=carbonara_ingredients
    )
    
    # Get cooking time
    cooking_time = estimate_cooking_time('spaghetti')
    
    print(f"Dish: {dish['pasta']} {dish['sauce']}")
    print(f"Ingredients: {', '.join(dish['ingredients'])}")
    print(f"Cooking time: {cooking_time} minutes")


Recipe: Vegetarian Penne Arrabbiata
------------------------------------

Creating a spicy vegetarian pasta:

.. code-block:: python

    from lumache import make_pasta, get_random_ingredients
    
    # Get vegetable ingredients
    veggies = get_random_ingredients(kind='vegetables')
    
    # Create the dish
    dish = make_pasta(
        pasta_type='penne',
        sauce_type='tomato',
        ingredients=veggies
    )
    
    return dish


Batch Recipe Generation
-----------------------

Generate multiple recipes at once:

.. code-block:: python

    from lumache import get_random_ingredients, make_pasta
    
    pasta_types = ['spaghetti', 'penne', 'rigatoni']
    sauce_types = ['tomato', 'cream', 'pesto']
    
    recipes = []
    
    for pasta in pasta_types:
        for sauce in sauce_types:
            ingredients = get_random_ingredients()
            dish = make_pasta(pasta, sauce, ingredients)
            recipes.append(dish)
    
    return recipes


Advanced: Custom Recipe Generator
----------------------------------

Create a reusable recipe generator function:

.. code-block:: python

    from lumache import make_pasta, estimate_cooking_time, get_random_ingredients
    
    def generate_recipe(pasta_count=1, with_timing=True):
        """Generate pasta recipes with optional cooking times."""
        recipes = []
        
        for _ in range(pasta_count):
            pasta_type = 'spaghetti'
            ingredients = get_random_ingredients(kind='vegetables')
            
            dish = make_pasta(
                pasta_type=pasta_type,
                sauce_type='tomato',
                ingredients=ingredients
            )
            
            if with_timing:
                dish['cooking_time'] = estimate_cooking_time(pasta_type)
            
            recipes.append(dish)
        
        return recipes
    
    # Generate 5 recipes with timing
    recipes = generate_recipe(pasta_count=5, with_timing=True)


Testing Your Recipes
--------------------

Using doctest with Lumache:

.. code-block:: python

    def get_recipe_summary(dish):
        """
        Get a summary of the pasta dish.
        
        Examples:
            >>> dish = {'pasta': 'spaghetti', 'sauce': 'tomato', 'servings': 2}
            >>> summary = get_recipe_summary(dish)
            >>> 'spaghetti' in summary
            True
        """
        return f"{dish['pasta']} with {dish['sauce']}"


Common Patterns
---------------

Pattern 1: Ingredient Validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from lumache import InvalidKindError
    
    valid_kinds = ['pasta', 'sauce', 'vegetables']
    
    def safe_get_ingredients(kind):
        """Safely get ingredients with validation."""
        if kind not in valid_kinds:
            raise InvalidKindError(f"Kind '{kind}' not supported")
        return get_random_ingredients(kind=kind)


Pattern 2: Caching Results
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from functools import lru_cache
    from lumache import estimate_cooking_time
    
    @lru_cache(maxsize=32)
    def get_cached_cooking_time(pasta_type):
        """Get cooking time with caching."""
        return estimate_cooking_time(pasta_type)


Performance Tips
----------------

1. **Cache ingredient lookups**: Use memoization for repeated ingredient requests
2. **Batch operations**: Generate multiple recipes in a single loop
3. **Pre-seed random**: Set random seed for reproducible results

.. code-block:: python

    import random
    from lumache import get_random_ingredients
    
    # Seed for reproducibility
    random.seed(42)
    
    # Get deterministic ingredients
    ingredients = get_random_ingredients()


Related Topics
--------------

* :doc:`usage`
* :doc:`troubleshooting`
* API Reference: :py:mod:`lumache`
