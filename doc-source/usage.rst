=======
Usage
=======

``sphinx-highlights`` provides a single directive:


.. rst:directive:: api-highlights

	Shows 4 random highlights of the library.

	The objects to include in the highlights are given in the body of the directive. For example:

	.. code-block:: rest

		.. api-highlights::

			domdf_python_tools.stringlist.StringList
			domdf_python_tools.testing.check_file_regression
			domdf_python_tools.paths.PathPlus
			domdf_python_tools.iterative.groupfloats

	More than four objects can be listed. A random selection of those will be chosen when the documentation is built.

	.. rst:directive:option:: module
		:type: string

		The parent module of all of these objects.

		Allows the module name to be replaced with a dot (``.``). For example:

		.. code-block:: rest

			.. api-highlights::
				:module: domdf_python_tools

				.stringlist.StringList

	.. rst:directive:option:: colours
		:type: Comma- or space-separated list of strings.

		| The colours to use for the panel headers. Choose from "blue", "green", "red", or "orange".
		| Default "blue".

		.. versionchanged:: 0.2.0  If more than four colours are provided four will be chosen at random.

	.. rst:directive:option:: classes
		:type: Comma- or space-separated list of strings.

		| The classes to use for the panels.
		| Default ``col-xl-6 col-lg-6 col-md-12 col-sm-12 col-xs-12 p-2``.


Customising the colours
---------------------------

By default the only colours available are:

.. hlist::
	:columns: 4

	* .. rst-class:: highlight-blue

	      |nbsp| |nbsp| ``blue`` |nbsp| |nbsp|

	* .. rst-class:: highlight-green

	      |nbsp| |nbsp| ``green`` |nbsp| |nbsp|

	* .. rst-class:: highlight-red

	      |nbsp| |nbsp| ``red`` |nbsp| |nbsp|

	* .. rst-class:: highlight-orange

	      |nbsp| |nbsp| ``orange`` |nbsp| |nbsp|

Additional colours can be created by adding your own custom CSS to Sphinx:

.. code-block:: css

	div.sphinx-highlights div.highlight-purple div.card-header {
		background-color: #B452CD;
	}

where ``purple`` is the name of the colour to use in the ``colours`` option.

.. hlist::
	:columns: 4

	* .. rst-class:: highlight-purple

	      |nbsp| |nbsp| ``purple`` |nbsp| |nbsp|



.. seealso::

	https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html
	for more information on adding custom CSS.
