#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Mad Libs Generator
File: templates.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-04
Updated: 2025-10-04
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
A small collection of built-in story templates. Each template declares its placeholders via
`{placeholder}` fields and optional human-friendly hints.
"""

from __future__ import annotations

from .core import StoryTemplate

BUILT_IN_TEMPLATES = [
    StoryTemplate(
        title="Space Picnic",
        difficulty="beginner",
        tags={"space", "picnic", "funny"},
        hints={
            "noun": "A thing (e.g., rocket, comet)",
            "verb": "An action (present tense)",
            "adjective": "A describing word",
            "food": "Something edible",
            "adverb": "How an action happens (e.g., quickly)",
        },
        text=(
            "Today I packed my {adjective} {noun} to go on a picnic on the Moon. "
            "First, I will {verb} {adverb} across the craters, then snack on a {food} "
            "while watching Earth rise. If a friendly alien visits, I’ll offer a bite!"
        ),
    ),
    StoryTemplate(
        title="Dragon Interview",
        difficulty="intermediate",
        tags={"fantasy", "dragon"},
        hints={
            "profession": "Job title",
            "adjective": "A describing word",
            "verb_past": "Past-tense verb",
            "creature": "A mythical creature",
            "tool": "An object used for work",
        },
        text=(
            "I arrived for my interview as a {profession}, feeling very {adjective}. "
            "Then the door {verb_past} open and a {creature} walked in! "
            "It asked if I knew how to use a {tool}, and I said, 'Absolutely.' The job was mine!"
        ),
    ),
    StoryTemplate(
        title="Rainy-day Robot",
        difficulty="beginner",
        tags={"robot", "rain"},
        hints={
            "name": "A person's name",
            "adjective": "A describing word",
            "verb_ing": "Verb ending in -ing",
            "plural_noun": "A plural thing (e.g., gears)",
        },
        text=(
            "{name} built a {adjective} robot for rainy days. "
            "Instead of {verb_ing} outside, they collected {plural_noun} and played board games. "
            "It was the coziest storm ever!"
        ),
    ),
]
