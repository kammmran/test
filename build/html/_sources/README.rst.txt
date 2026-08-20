README
======

About Lumache
--------------

**Lumache** is a Python library designed for food enthusiasts and home cooks who want to
create pasta recipes with random ingredients. The project demonstrates comprehensive
Sphinx documentation practices.

Project Information
^^^^^^^^^^^^^^^^^^^

:Author: Kamran Heydarov
:Version: 4.2.1b0
:License: MIT
:Status: Development
:Python: 3.6+


Key Features
^^^^^^^^^^^^

✓ Random ingredient generation
✓ Pasta dish creation
✓ Cooking time estimation
✓ Custom exception handling
✓ Comprehensive documentation
✓ Type hints support


Installation
^^^^^^^^^^^^

Install Lumache using pip:

.. code-block:: console

    $ pip install lumache

Or install from source:

.. code-block:: console

    $ git clone https://github.com/yourusername/lumache.git
    $ cd lumache
    $ pip install -e .


Quick Start
^^^^^^^^^^^

.. code-block:: python

    from lumache import get_random_ingredients, make_pasta
    
    # Generate random ingredients
    ingredients = get_random_ingredients()
    
    # Create a pasta dish
    dish = make_pasta('spaghetti', 'tomato', ingredients)
    
    print(dish)


Requirements
^^^^^^^^^^^^

- Python 3.6 or higher
- No external dependencies for basic usage
- Optional: Sphinx for documentation building


Project Structure
^^^^^^^^^^^^^^^^^

.. code-block:: text

    lumache/
    ├── lumache.py           # Main module
    ├── source/
    │   ├── conf.py         # Sphinx configuration
    │   ├── index.rst       # Documentation home
    │   ├── usage.rst       # Usage guide
    │   ├── examples.rst    # Code examples
    │   ├── troubleshooting.rst  # Troubleshooting
    │   └── api/
    │       ├── modules.rst # API reference
    │       └── lumache.rst # Module docs
    ├── build/              # Generated documentation
    └── Makefile            # Build automation


Documentation
^^^^^^^^^^^^^^

Full documentation is available at:

- :doc:`usage` - Getting started and usage guide
- :doc:`examples` - Practical examples and recipes
- :doc:`api/modules` - Complete API reference
- :doc:`troubleshooting` - Problem solving guide


Sphinx Features Demonstrated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This project demonstrates:

- **autodoc**: Automatic documentation from Python docstrings
- **autosummary**: Summary tables of modules and classes
- **Code highlighting**: Syntax highlighting for code blocks
- **Cross-references**: Links between documentation pages
- **Directives**: Custom RST directives (note, warning, etc.)
- **Intersphinx**: Links to external documentation (e.g., Python docs)
- **Doctest**: Testing documentation examples
- **HTML themes**: Using the Furo theme


Building Documentation
^^^^^^^^^^^^^^^^^^^^^^

Build HTML documentation:

.. code-block:: console

    $ make html

Build PDF documentation (requires LaTeX):

.. code-block:: console

    $ make latexpdf

Build man pages:

.. code-block:: console

    $ make man

Clean build artifacts:

.. code-block:: console

    $ make clean


Contributing
^^^^^^^^^^^^

Contributions are welcome! Please ensure:

1. Code follows PEP 8 style guide
2. Docstrings use Google-style format
3. Tests pass before submitting
4. Documentation is updated


Testing
^^^^^^^

Run doctests from documentation:

.. code-block:: console

    $ sphinx-build -b doctest source build/doctest


License
^^^^^^^

This project is licensed under the MIT License. See LICENSE file for details.


Changelog
^^^^^^^^^

Version 4.2.1b0
"""""""""""""""
- Added comprehensive documentation
- Improved function docstrings
- Added examples and troubleshooting guides
- Beta release


Support
^^^^^^^

For issues, questions, or suggestions:

- Open an issue on GitHub
- Check the :doc:`troubleshooting` guide
- Review :doc:`examples` for common patterns


Links
^^^^^

- `GitHub Repository <https://github.com/yourusername/lumache>`_
- `Python Package Index <https://pypi.org/project/lumache/>`_
- `Sphinx Documentation <https://www.sphinx-doc.org/>`_


See Also
^^^^^^^^

- :doc:`usage` - Detailed usage instructions
- :doc:`examples` - Practical code examples
- :doc:`api/modules` - Complete API documentation
