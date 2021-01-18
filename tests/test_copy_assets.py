# 3rd party
from domdf_python_tools.paths import PathPlus
from pytest_regressions.file_regression import FileRegressionFixture
from sphinx_toolbox.testing import check_asset_copy

# this package
from sphinx_highlights import copy_assets


def test_copy_asset_files(tmp_pathplus: PathPlus, file_regression: FileRegressionFixture):
	check_asset_copy(copy_assets, "_static/css/sphinx_highlights.css", file_regression=file_regression)
