#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Mad Libs Generator
File: __init__.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-04
Updated: 2025-10-04
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
Package init for the Mad Libs project. Exposes high-level symbols.

Usage:
from madlibs.core import MadLibEngine
from madlibs.templates import BUILT_IN_TEMPLATES
"""
from .core import MadLibEngine, StoryTemplate  # noqa: F401
from .templates import BUILT_IN_TEMPLATES  # noqa: F401
