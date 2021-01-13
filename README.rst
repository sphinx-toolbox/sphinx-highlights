##################
sphinx-highlights
##################

.. start short_desc

**Sphinx extention to display a selection of highlights from a Python library.**

.. end short_desc


.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos| |coveralls|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy| |pre_commit_ci|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/sphinx-highlights/latest?logo=read-the-docs
	:target: https://sphinx-highlights.readthedocs.io/en/latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/sphinx-toolbox/sphinx-highlights/workflows/Docs%20Check/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-highlights/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |actions_linux| image:: https://github.com/sphinx-toolbox/sphinx-highlights/workflows/Linux/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-highlights/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/sphinx-toolbox/sphinx-highlights/workflows/Windows/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-highlights/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/sphinx-toolbox/sphinx-highlights/workflows/macOS/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-highlights/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/sphinx-toolbox/sphinx-highlights/workflows/Flake8/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-highlights/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/sphinx-toolbox/sphinx-highlights/workflows/mypy/badge.svg
	:target: https://github.com/sphinx-toolbox/sphinx-highlights/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://requires.io/github/sphinx-toolbox/sphinx-highlights/requirements.svg?branch=master
	:target: https://requires.io/github/sphinx-toolbox/sphinx-highlights/requirements/?branch=master
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/sphinx-toolbox/sphinx-highlights/master?logo=coveralls
	:target: https://coveralls.io/github/sphinx-toolbox/sphinx-highlights?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/sphinx-toolbox/sphinx-highlights?logo=codefactor
	:target: https://www.codefactor.io/repository/github/sphinx-toolbox/sphinx-highlights
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/sphinx-highlights
	:target: https://pypi.org/project/sphinx-highlights/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/sphinx-highlights?logo=python&logoColor=white
	:target: https://pypi.org/project/sphinx-highlights/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/sphinx-highlights
	:target: https://pypi.org/project/sphinx-highlights/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/sphinx-highlights
	:target: https://pypi.org/project/sphinx-highlights/
	:alt: PyPI - Wheel

.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/sphinx-highlights?logo=anaconda
	:target: https://anaconda.org/domdfcoding/sphinx-highlights
	:alt: Conda - Package Version

.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/sphinx-highlights?label=conda%7Cplatform
	:target: https://anaconda.org/domdfcoding/sphinx-highlights
	:alt: Conda - Platform

.. |license| image:: https://img.shields.io/github/license/sphinx-toolbox/sphinx-highlights
	:target: https://github.com/sphinx-toolbox/sphinx-highlights/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/sphinx-toolbox/sphinx-highlights
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/sphinx-toolbox/sphinx-highlights/v0.1.0
	:target: https://github.com/sphinx-toolbox/sphinx-highlights/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/sphinx-toolbox/sphinx-highlights
	:target: https://github.com/sphinx-toolbox/sphinx-highlights/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2021
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/sphinx-highlights
	:target: https://pypi.org/project/sphinx-highlights/
	:alt: PyPI - Downloads

.. |pre_commit_ci| image:: https://results.pre-commit.ci/badge/github/sphinx-toolbox/sphinx-highlights/master.svg
	:target: https://results.pre-commit.ci/latest/github/sphinx-toolbox/sphinx-highlights/master
	:alt: pre-commit.ci status

.. end shields

Installation
--------------

.. start installation

``sphinx-highlights`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install sphinx-highlights

To install with ``conda``:

	* First add the required channels

	.. code-block:: bash

		$ conda config --add channels http://conda.anaconda.org/conda-forge
		$ conda config --add channels http://conda.anaconda.org/domdfcoding

	* Then install

	.. code-block:: bash

		$ conda install sphinx-highlights

.. end installation
