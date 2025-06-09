# stdlib
import random
from typing import Tuple, no_type_check

# 3rd party
import pytest
from bs4 import BeautifulSoup
from domdf_python_tools.paths import PathPlus
from domdf_python_tools.stringlist import StringList
from sphinx.application import Sphinx
from sphinx_toolbox.testing import HTMLRegressionFixture, LaTeXRegressionFixture


def test_build_example(app: Sphinx):
	app.build()
	app.build()


@no_type_check
def _get_alabaster_version() -> Tuple[int, int, int]:
	try:
		# 3rd party
		import alabaster._version as alabaster  # type: ignore[import-untyped]
	except ImportError:
		# 3rd party
		import alabaster  # type: ignore[import-untyped]

	return tuple(map(int, alabaster.__version__.split('.')))


@pytest.mark.sphinx("html", srcdir="test-root")
@pytest.mark.parametrize("page", ["index.html"], indirect=True)
def test_html_output(page: BeautifulSoup, html_regression: HTMLRegressionFixture):
	html_regression.check(page, jinja2=True, jinja2_namespace={"alabaster_version": _get_alabaster_version()})


@pytest.mark.sphinx("latex", srcdir="test-root")
def test_latex_output(
		app: Sphinx,
		latex_regression: LaTeXRegressionFixture,
		):
	random.seed("5678")

	assert app.builder is not None
	assert app.builder.name.lower() == "latex"
	app.build()

	output_file = PathPlus(app.outdir) / "sphinx-highlights-demo.tex"
	content = str(StringList(output_file.read_lines())).replace("\\sphinxAtStartPar\n", '')
	latex_regression.check(
			# re.sub(r"\\date{.*}", r"\\date{Mar 11, 2021}", content),
			content,
			jinja2=True,
			)
