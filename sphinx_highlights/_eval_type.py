#!/usr/bin/env python3
#
#  _eval_type.py
"""
Modified version of ``typing._eval_type`` which doesn't completely bail out
if it can't resolve a string annotation.
"""  # noqa: D400
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
#  _eval_type based on CPython.
#  Licensed under the Python Software Foundation License Version 2.
#  Copyright © 2001-2020 Python Software Foundation. All rights reserved.
#  Copyright © 2000 BeOpen.com. All rights reserved.
#  Copyright © 1995-2000 Corporation for National Research Initiatives. All rights reserved.
#  Copyright © 1991-1995 Stichting Mathematisch Centrum. All rights reserved.
#

# stdlib
import contextlib
import sys
import typing

__all__ = ["monkeypatcher"]

if sys.version_info >= (3, 9):  # pragma: no cover (<py39)

	def _eval_type(t, globalns, localns, recursive_guard=frozenset()):
		"""
		Evaluate all forward references in the given type t.

		For use of globalns and localns see the docstring for get_type_hints().
		recursive_guard is used to prevent prevent infinite recursion
		with recursive ForwardRef.
		"""

		if isinstance(t, typing.ForwardRef):
			return t._evaluate(globalns, localns, recursive_guard)

		if isinstance(t, (typing._GenericAlias, typing.GenericAlias)):  # noqa: TYP006
			ev_args_list = []

			for a in t.__args__:
				try:
					ev_args_list.append(_eval_type(a, globalns, localns, recursive_guard))
				except (NameError, TypeError, KeyError, AttributeError):
					ev_args_list.append(a)

			ev_args = tuple(ev_args_list)

			if ev_args == t.__args__:
				return t

			if isinstance(t, typing.GenericAlias):  # noqa: TYP006
				return typing.GenericAlias(t.__origin__, ev_args)  # noqa: TYP006
			else:
				return t.copy_with(ev_args)

		return t

elif sys.version_info >= (3, 7):  # pragma: no cover (py39+ or <py37)

	def _eval_type(t, globalns, localns):
		"""
		Evaluate all forward references in the given type t.

		For use of globalns and localns see the docstring for get_type_hints().
		"""

		if isinstance(t, typing.ForwardRef):
			return t._evaluate(globalns, localns)

		if isinstance(t, typing._GenericAlias):  # type: ignore[attr-defined]  # noqa: TYP006
			ev_args_list = []

			for a in t.__args__:
				try:
					ev_args_list.append(_eval_type(a, globalns, localns))
				except (NameError, TypeError, KeyError, AttributeError):
					ev_args_list.append(a)

			ev_args = tuple(ev_args_list)

			if ev_args == t.__args__:
				return t

			res = t.copy_with(ev_args)
			res._special = t._special
			return res

		return t


@contextlib.contextmanager
def monkeypatcher():
	"""
	Use the modified version of ``typing._eval_type`` for the scope of the :keyword:`with` block.
	"""

	original_eval_type = typing._eval_type  # type: ignore[attr-defined]  # noqa: TYP006

	try:
		typing._eval_type = _eval_type  # type: ignore[attr-defined]  # noqa: TYP006
		yield
	finally:
		typing._eval_type = original_eval_type  # type: ignore[attr-defined]  # noqa: TYP006
