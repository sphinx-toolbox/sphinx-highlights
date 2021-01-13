=======
Usage
=======


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

		The colours to use for the panel headers. Choose from "blue", "green", "red", or "orange". Default "blue".

	.. rst:directive:option:: classes
		:type: Comma- or space-separated list of strings.

		The classes to use for the panels. Default ``col-xl-6 col-lg-6 col-md-12 col-sm-12 col-xs-12 p-2``.
