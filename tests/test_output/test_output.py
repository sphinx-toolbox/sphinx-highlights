# stdlib
import random
import re

# 3rd party
import pytest
from bs4 import BeautifulSoup  # type: ignore
from coincidence.regressions import AdvancedFileRegressionFixture
from domdf_python_tools.paths import PathPlus
from domdf_python_tools.stringlist import StringList
from sphinx_toolbox.testing import HTMLRegressionFixture, LaTeXRegressionFixture, check_html_regression


def test_build_example(app):
	app.build()
	app.build()


@pytest.mark.sphinx("html", srcdir="test-root")
@pytest.mark.parametrize("page", ["index.html"], indirect=True)
def test_html_output(page: BeautifulSoup, html_regression: HTMLRegressionFixture):
	html_regression.check(page, jinja2=True)


@pytest.mark.sphinx("latex", srcdir="test-root")
def test_latex_output(
		app,
		latex_regression: LaTeXRegressionFixture,
		):
	random.seed("5678")

	assert app.builder.name.lower() == "latex"
	app.build()

	output_file = PathPlus(app.outdir / "sphinx-highlights-demo.tex")
	content = str(StringList(output_file.read_lines())).replace("\\sphinxAtStartPar\n", '')
	latex_regression.check(
			# re.sub(r"\\date{.*}", r"\\date{Mar 11, 2021}", content),
			content,
			jinja2=True,
			)
