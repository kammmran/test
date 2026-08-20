"""
Lumache Library - A delicious pasta recipe library.

This module provides utilities for creating pasta recipes with various
ingredients and cooking methods.

Example:
    >>> from lumache import get_random_ingredients
    >>> get_random_ingredients()
    ['shells', 'gorgonzola', 'parsley']
"""

import random


class InvalidKindError(Exception):
    """Exception raised when an invalid ingredient kind is provided."""
    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    Args:
        kind (str, optional): Optional "kind" of ingredients. 
            Valid options: 'pasta', 'sauce', 'vegetables'.
            Defaults to None (returns default ingredients).

    Returns:
        list: A list of ingredient strings.

    Raises:
        InvalidKindError: If the kind parameter is not None and
            not in the list of valid kinds.

    Examples:
        Get default ingredients:

        >>> get_random_ingredients()
        ['shells', 'gorgonzola', 'parsley']

        Get pasta ingredients:

        >>> ingredients = get_random_ingredients(kind='pasta')
        >>> len(ingredients) > 0
        True
    """
    
    if kind is None:
        return ["shells", "gorgonzola", "parsley"]

    valid_kinds = ['pasta', 'sauce', 'vegetables']
    if kind not in valid_kinds:
        raise InvalidKindError(
            f"Invalid kind '{kind}'. Must be one of {valid_kinds}")

    ingredients_map = {
        'pasta': ["penne", "linguine", "rigatoni", "fettuccine"],
        'sauce': ["tomato", "cream", "pesto", "seafood"],
        'vegetables': ["garlic", "onion", "basil", "mushroom", "zucchini"]
    }

    return random.sample(ingredients_map[kind], k=random.randint(1, 3))


def make_pasta(pasta_type, sauce_type, ingredients=None):
    """
    Create a pasta dish with specified components.

    Args:
        pasta_type (str): Type of pasta ('spaghetti', 'penne', etc.)
        sauce_type (str): Type of sauce ('tomato', 'cream', etc.)
        ingredients (list, optional): Additional ingredients to add.
            Defaults to None.

    Returns:
        dict: A dictionary containing the pasta dish details with keys:
            - 'pasta': pasta type
            - 'sauce': sauce type
            - 'ingredients': list of ingredients
            - 'servings': number of servings

    Example:
        >>> dish = make_pasta('spaghetti', 'tomato', ['garlic', 'basil'])
        >>> dish['pasta']
        'spaghetti'
    """

    if ingredients is None:
        ingredients = get_random_ingredients()

    return {
        'pasta': pasta_type,
        'sauce': sauce_type,
        'ingredients': ingredients,
        'servings': 2
    }


def estimate_cooking_time(pasta_type):
    """
    Estimate the cooking time for a given pasta type.

    Args:
        pasta_type (str): Type of pasta.

    Returns:
        int: Estimated cooking time in minutes.

    Note:
        Cooking times are approximate and may vary based on:
        - Water temperature
        - Altitude
        - Personal preference for pasta firmness
    """

    cooking_times = {
        'spaghetti': 9,
        'penne': 11,
        'rigatoni': 12,
        'fettuccine': 8,
        'linguine': 9

    }
    return cooking_times.get(pasta_type, 10)
