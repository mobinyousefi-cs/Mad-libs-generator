#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Mad Libs Generator
File: core.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-04
Updated: 2025-10-04
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
Core engine for rendering Mad Libs stories. Provides a data model for templates and an engine
for prompting/validating inputs and producing final text.

Usage:
python -m madlibs  # see __main__.py
"""

from __future__ import annotations

from dataclasses import dataclass, field
from string import Formatter
from typing import Dict, Iterable, List, Mapping, Set


@dataclass(frozen=True)
class StoryTemplate:
    """Represents a Mad Lib story template."""

    title: str
    text: str  # uses `{placeholder}` format fields
    hints: Mapping[str, str] = field(default_factory=dict)
    tags: Set[str] = field(default_factory=set)
    difficulty: str = "beginner"

    def fields(self) -> List[str]:
        """Extract ordered unique placeholder names from the template."""
        seen: Set[str] = set()
        out: List[str] = []
        for _, field_name, _, _ in Formatter().parse(self.text):
            if field_name and field_name not in seen:
                seen.add(field_name)
                out.append(field_name)
        return out


class MadLibEngine:
    """Renders stories from a StoryTemplate with user-supplied values."""

    def __init__(self, templates: Iterable[StoryTemplate]):
        self._templates: Dict[str, StoryTemplate] = {t.title: t for t in templates}

    @property
    def titles(self) -> List[str]:
        return sorted(self._templates.keys())

    def get(self, title: str) -> StoryTemplate:
        if title not in self._templates:
            raise KeyError(f"Story not found: {title}")
        return self._templates[title]

    def required_fields(self, title: str) -> List[str]:
        return self.get(title).fields()

    def render(self, title: str, values: Mapping[str, str]) -> str:
        """Render a story with given mapping of placeholder -> string.

        Raises:
            KeyError if a required field is missing.
            ValueError if inputs contain disallowed characters (basic sanity).
        """
        tmpl = self.get(title)
        required = tmpl.fields()
        missing = [f for f in required if f not in values or values[f] is None or values[f] == ""]
        if missing:
            raise KeyError(f"Missing fields: {', '.join(missing)}")

        # Basic sanitization: avoid braces that break format, control chars.
        for k, v in values.items():
            if any(ch in v for ch in "{}"):
                raise ValueError(f"Invalid characters in value for '{k}'.")
            if any(ord(ch) < 32 and ch not in ("\n", "\t") for ch in v):
                raise ValueError(f"Control characters not allowed in value for '{k}'.")

        return tmpl.text.format(**values)
