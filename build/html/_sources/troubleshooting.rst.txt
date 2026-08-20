Troubleshooting
===============

This guide helps you resolve common issues when using Lumache.

Common Issues and Solutions
----------------------------

InvalidKindError When Calling get_random_ingredients
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Problem**: You get an ``InvalidKindError`` when calling ``get_random_ingredients(kind='...')``.

**Solution**: Make sure you're using one of the valid ingredient kinds:

- ``'pasta'`` - for pasta types
- ``'sauce'`` - for sauce types
- ``'vegetables'`` - for vegetable types
- ``None`` - for default ingredients

.. code-block:: python

    from lumache import get_random_ingredients
    
    # ✓ Correct
    ingredients = get_random_ingredients(kind='pasta')
    
    # ✗ Incorrect
    # ingredients = get_random_ingredients(kind='invalid')


ImportError When Importing Lumache
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Problem**: ``ModuleNotFoundError: No module named 'lumache'``

**Solution**: Make sure Lumache is installed:

.. code-block:: console

    pip install lumache

Or if developing locally:

.. code-block:: console

    pip install -e .


Documentation Build Issues
---------------------------

Autodoc Not Finding Module
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Problem**: Sphinx autodoc can't find your Python modules.

**Solution**: Ensure ``conf.py`` has the correct path:

.. code-block:: python

    import sys
    import os
    sys.path.insert(0, os.path.abspath('..'))


Missing Generated Documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Problem**: Expected documentation pages aren't generated.

**Solution**: 

1. Verify the RST file exists and is included in ``toctree``
2. Check for syntax errors in RST files
3. Rebuild the documentation:

.. code-block:: console

    make clean
    make html


API Reference Issues
--------------------

Docstrings Not Appearing
^^^^^^^^^^^^^^^^^^^^^^^^^

**Problem**: Function docstrings don't appear in generated docs.

**Solution**: 

1. Ensure functions have proper docstrings
2. Check that ``sphinx.ext.autodoc`` is in ``extensions`` in ``conf.py``
3. Use proper ReST formatting in docstrings

.. code-block:: python

    def example_function(param1, param2):
        """
        Brief description.
        
        Args:
            param1: Description of param1
            param2: Description of param2
            
        Returns:
            Description of return value
        """
        pass


Type Hints Not Showing
^^^^^^^^^^^^^^^^^^^^^^

**Problem**: Type hints don't appear in documentation.

**Solution**: Enable type hints in ``conf.py``:

.. code-block:: python

    # In conf.py extensions
    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.autodoc',  # Make sure it's listed
    ]
    
    # Enable type hints display
    autodoc_typehints = 'description'


Code Examples
^^^^^^^^^^^^^

For troubleshooting code examples, use the ``:doctest:`` option:

.. code-block:: rst

    .. doctest::
    
        >>> from lumache import get_random_ingredients
        >>> ingredients = get_random_ingredients()
        >>> len(ingredients) > 0
        True


Performance Issues
-------------------

Slow Documentation Build
^^^^^^^^^^^^^^^^^^^^^^^^

**Problem**: Building documentation takes a long time.

**Solution**: 

1. Use ``-j`` for parallel builds:

.. code-block:: console

    make -j html

2. Disable features you don't need in ``conf.py``
3. Check for circular imports in Python modules


Build Size Too Large
^^^^^^^^^^^^^^^^^^^^

**Problem**: Generated HTML is very large.

**Solution**: 

1. Disable HTML search index if not needed
2. Remove unnecessary static files
3. Compress images


Getting Help
------------

.. tip::
   Check the official Sphinx documentation at https://www.sphinx-doc.org/

.. hint::
   Use ``sphinx-build -W`` to turn warnings into errors during development.

Common Sphinx Directives Reference
-----------------------------------

.. note::
   This creates an informational note.

.. warning::
   This creates a warning box.

.. caution::
   This creates a caution message.

.. attention::
   This creates an attention-grabbing message.

.. important::
   This highlights important information.

.. tip::
   This provides a helpful tip.

.. hint::
   This provides a subtle hint.

.. danger::
   This indicates dangerous operations.


FAQ
----------------

**Q: How do I add a new page to the documentation?**

A: Create a new ``.rst`` file and add it to the ``toctree`` directive in ``index.rst``.

**Q: Can I use Markdown instead of reStructuredText?**

A: Yes, install ``myst-parser`` and add ``'myst_parser'`` to extensions.

**Q: How do I customize the HTML theme?**

A: Modify the ``html_theme`` and related options in ``conf.py``.

**Q: How do I add syntax highlighting to code blocks?**

A: Use the ``.. code-block:: language`` directive (e.g., ``.. code-block:: python``).


Related Topics
--------------

* :doc:`usage`
* :doc:`examples`
* API Reference: :py:mod:`lumache`
