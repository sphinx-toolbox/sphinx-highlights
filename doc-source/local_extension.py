# 3rd party
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.ext import intersphinx


def handle_missing_xref(
		app: Sphinx,
		env: BuildEnvironment,
		node: nodes.Node,
		contnode: nodes.Node,
		):

	if not isinstance(node, nodes.Element):
		return

	if node.get("reftarget", '') in {"DataFrame", "Series"}:
		node.attributes["reftarget"] = f"pandas.{node.attributes['reftarget']}"
		del node.attributes["refspecific"]
		return intersphinx.missing_reference(app, env, node, contnode)


def setup(app: Sphinx):
	"""
	Setup Sphinx Extension.

	:param app: The Sphinx application.
	"""

	app.connect("missing-reference", handle_missing_xref, priority=400)
