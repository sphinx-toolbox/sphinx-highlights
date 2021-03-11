# stdlib
import random

# 3rd party
import pytest
from bs4 import BeautifulSoup  # type: ignore
from domdf_python_tools.paths import PathPlus
from domdf_python_tools.stringlist import StringList
from domdf_python_tools.testing import check_file_regression
from pytest_regressions.file_regression import FileRegressionFixture
from sphinx_toolbox.testing import check_html_regression


def test_build_example(app):
	app.build()
	app.build()


@pytest.mark.sphinx("html", srcdir="test-root")
@pytest.mark.parametrize("page", ["index.html"], indirect=True)
def test_html_output(page: BeautifulSoup, file_regression: FileRegressionFixture):
	check_html_regression(page, file_regression)


@pytest.mark.sphinx("latex", srcdir="test-root")
def test_latex_output(app, file_regression: FileRegressionFixture):
	random.seed("5678")

	assert app.builder.name.lower() == "latex"
	app.build()

	output_file = PathPlus(app.outdir / "sphinx-highlights-demo.tex")
	content = StringList(output_file.read_lines())
	check_file_regression(content, file_regression, extension=".tex")
