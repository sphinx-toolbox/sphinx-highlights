import sys

if sys.version_info >= (3, 10):
	# stdlib
	import types
	types.Union = types.UnionType

pytest_plugins = ("coincidence", )
