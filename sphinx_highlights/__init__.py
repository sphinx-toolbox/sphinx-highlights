#!/usr/bin/env python3
#
#  __init__.py
"""
Sphinx extention to display a selection of highlights from a Python library.
"""
#
#  Copyright © 2021 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#
#  format_parameter based on CPython.
#  Licensed under the Python Software Foundation License Version 2.
#  Copyright © 2001-2020 Python Software Foundation. All rights reserved.
#  Copyright © 2000 BeOpen.com. All rights reserved.
#  Copyright © 1995-2000 Corporation for National Research Initiatives. All rights reserved.
#  Copyright © 1991-1995 Stichting Mathematisch Centrum. All rights reserved.
#

# stdlib
import inspect
import itertools
import random
import re
from importlib import import_module
from types import FunctionType
from typing import AbstractSet, Iterator, List, Optional, Sequence, TypeVar, Union

# 3rd party
from docutils import nodes
from docutils.parsers.rst.directives import unchanged_required
from docutils.statemachine import ViewList
from domdf_python_tools.paths import PathPlus
from domdf_python_tools.stringlist import DelimitedList, StringList
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx_toolbox.more_autodoc.typehints import format_annotation
from sphinx_toolbox.utils import Purger, SphinxExtMetadata
from sphinxcontrib.default_values import format_default_value

__author__: str = "Dominic Davis-Foster"
__copyright__: str = "2021 Dominic Davis-Foster"
__license__: str = "MIT License"
__version__: str = "0.1.0"
__email__: str = "dominic@davis-foster.co.uk"

__all__ = [
		"SphinxHighlightsDirective",
		"copy_assets",
		"format_parameter",
		"format_signature",
		"setup",
		"get_random_sample",
		]

_T = TypeVar("_T")

sphinx_highlights_purger = Purger("all_sphinx_highlights")


def format_parameter(param: inspect.Parameter) -> str:
	"""
	Format an :class:`inspect.Parameter`, for insertion into the highlight panel.

	:param param:

	:return: The reStructuredText string.
	"""

	kind = param.kind
	formatted = param.name

	# Add annotation and default value
	if param.annotation is not inspect.Parameter.empty:
		formatted = f"{formatted}: {format_annotation(param.annotation)}"

	if param.default is not inspect.Parameter.empty:
		if param.annotation is not inspect.Parameter.empty:
			formatted = f"{formatted} = {format_default_value(param.default)}"
		else:
			formatted = f"{formatted}={format_default_value(param.default)}"

	if kind == inspect.Parameter.VAR_POSITIONAL:
		formatted = rf'\*{formatted}'
	elif kind == inspect.Parameter.VAR_KEYWORD:
		formatted = rf"\*\*{formatted}"

	return formatted


def format_signature(obj: Union[type, FunctionType]) -> StringList:
	"""
	Format the signature of the given object, for insertion into the highlight panel.

	:param obj:

	:return: A list of reStructuredText lines.
	"""

	signature: inspect.Signature = inspect.signature(obj)

	buf = StringList(".. parsed-literal::")
	buf.blankline()
	buf.indent_type = "    "
	buf.indent_size = 1

	if signature.return_annotation is not inspect.Signature.empty and not isinstance(obj, type):
		return_annotation = f") -> {format_annotation(signature.return_annotation)}"
	else:
		return_annotation = f")"

	total_length = len(obj.__name__) + len(return_annotation)

	arguments_buf: DelimitedList[str] = DelimitedList()

	param: inspect.Parameter
	for param in signature.parameters.values():
		arguments_buf.append(f"{format_parameter(param)}")
		total_length += len(arguments_buf[-1])

	if total_length <= 60:
		signature_buf = StringList(''.join([f"{obj.__name__}(", f"{arguments_buf:, }", return_annotation]))
	else:
		signature_buf = StringList([f"{obj.__name__}("])
		signature_buf.indent_type = "  "
		with signature_buf.with_indent_size(1):
			signature_buf.extend([f"{arguments_buf:,\n}" + ',', return_annotation])

	buf.extend(signature_buf)

	return buf


def get_random_sample(items: Union[Sequence[_T], AbstractSet[_T]]) -> List[_T]:
	"""
	Returns four random elements from ``items``.

	:param items:
	"""

	return random.sample(items, 4)


class SphinxHighlightsDirective(SphinxDirective):
	"""
	Provides the :rst:dir:`api-highlights` directive.
	"""

	has_content = True

	option_spec = {
			"colours": unchanged_required,
			"module": unchanged_required,
			"class": unchanged_required,
			}

	def delimited_get(self, option: str, default: str) -> Iterator[str]:
		"""
		Returns the value of the option with the given name,
		splitting the input at commas, semicolons and spaces.

		:param option: The option name.
		:param default: The default value, as a string separated by commas, spaces or semicolons.
		"""  # noqa: D400

		return filter(bool, re.split("[,; ]", self.options.get(option, default)))

	def run(self):
		# colours = itertools.cycle(self.delimited_get("colours", "#6ab0de"))
		colours = itertools.cycle(self.delimited_get("colours", "blue"))
		classes = list(self.delimited_get("class", "col-xl-6 col-lg-6 col-md-12 col-sm-12 col-xs-12 p-2"))

		content = StringList()
		content.append(".. panels::")
		content.indent_type = "    "
		content.indent_size = 1
		content.append(":container: container-xl pb-4 sphinx-highlights")
		content.blankline()

		for obj_name in get_random_sample(sorted(set(self.content))):
			if self.options.get("module", '') and obj_name.startswith('.'):
				obj_name = obj_name.replace('.', f"{self.options['module']}.", 1)

			name_parts = obj_name.split('.')
			module = import_module('.'.join(name_parts[:-1]))
			obj = getattr(module, name_parts[-1])

			role = ":py:obj:"

			if isinstance(obj, FunctionType):
				role = ":func:"
			elif isinstance(obj, type):
				role = ":class:"

			colour_class = f"highlight-{next(colours)}"
			content.append(f":column: {DelimitedList((*classes, colour_class)): }")

			if role == ":func:":
				content.append(f"{role}`{'.'.join(name_parts[1:])}() <.{obj_name}>`")
			else:
				content.append(f"{role}`{'.'.join(name_parts[1:])} <.{obj_name}>`")

			content.append('^' * len(content[-1]))
			content.blankline()
			# content.append(f".. function:: {name_parts[-1]} {stringify_signature(inspect.signature(obj))}")
			content.append(format_signature(obj))
			content.blankline()
			content.append(inspect.cleandoc(obj.__doc__ or '').split("\n\n")[0])
			content.blankline()
			content.append(f"See more in :mod:`{module.__name__}`.")
			content.append("---")

		content.pop(-1)

		targetid = f'sphinx-highlights-{self.env.new_serialno("sphinx-highlights"):d}'
		targetnode = nodes.target('', '', ids=[targetid])

		view = ViewList(content)
		body_node = nodes.paragraph(rawsource=str(content))
		self.state.nested_parse(view, self.content_offset, body_node)  # type: ignore

		sphinx_highlights_purger.add_node(self.env, body_node, targetnode, self.lineno)

		return [targetnode, body_node]


def copy_assets(app: Sphinx, exception: Optional[Exception] = None) -> None:
	"""
	Copy asset files to the output.

	:param app: The Sphinx application.
	:param exception: Any exception which occurred and caused Sphinx to abort.
	"""

	if exception:  # pragma: no cover
		return

	style = StringList()

	# if app.config.html_theme in {"domdf_sphinx_theme", "sphinx_rtd_theme"}:
	# 	header_colour = app.config.html_theme_options.get("style_nav_header_background", "#2980B9")
	#
	# 	style.blankline()
	# 	style.extend([
	# 			"div.sphinx-highlights div.card-header {",
	# 			f"    background-color: {header_colour}",
	# 			'}',
	# 			])

	style.blankline()
	style.extend([
			"div.sphinx-highlights div.highlight-blue div.card-header {",
			"    background-color: #6ab0de",
			'}',
			'',
			"div.sphinx-highlights div.highlight-orange div.card-header {",
			"    background-color: #f0b37e",
			'}',
			'',
			"div.sphinx-highlights div.highlight-green div.card-header {",
			"    background-color: #1abc9c",
			'}',
			'',
			"div.sphinx-highlights div.highlight-red div.card-header {",
			"    background-color: #f29f97",
			'}',
			'',
			])

	css_dir = PathPlus(app.builder.outdir) / "_static" / "css"
	css_dir.maybe_make(parents=True)
	css_file = css_dir / "sphinx_highlights.css"
	css_file.write_lines(style)


def env_get_outdated(app, env, added, changed, removed):
	return [node["docname"] for node in getattr(env, sphinx_highlights_purger.attr_name, ())]


def setup(app: Sphinx) -> SphinxExtMetadata:
	"""
	Setup :mod:`sphinx_highlights`.

	:param app: The Sphinx application.
	"""

	app.setup_extension("sphinx_panels")
	app.setup_extension("sphinx_toolbox.tweaks.sphinx_panels_tabs")
	app.add_directive("api-highlights", SphinxHighlightsDirective)
	app.add_css_file("css/sphinx_highlights.css")
	app.connect("build-finished", copy_assets)
	app.connect("env-get-outdated", env_get_outdated)
	app.connect("env-purge-doc", sphinx_highlights_purger.purge_nodes)

	return {
			"version": __version__,
			"parallel_read_safe": True,
			}
