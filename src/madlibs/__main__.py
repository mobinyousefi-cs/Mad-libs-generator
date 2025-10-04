#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Mad Libs Generator
File: __main__.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-04
Updated: 2025-10-04
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
CLI entry-point. List stories, inspect required fields, and render a story using provided values.

Usage:
madlibs --list
madlibs --story "Space Picnic"
madlibs --story "Space Picnic" --set noun=rocket --set verb=zoom --set food="cheese sandwich"
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict

from .core import MadLibEngine
from .templates import BUILT_IN_TEMPLATES


def _parse_kv(pairs: list[str]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for item in pairs:
        if "=" not in item:
            raise argparse.ArgumentTypeError(f"Expected key=value, got '{item}'")
        k, v = item.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def main() -> None:
    parser = argparse.ArgumentParser(prog="madlibs", description="Mad Libs Generator (CLI)")
    parser.add_argument("--list", action="store_true", help="List available story titles")
    parser.add_argument("--story", type=str, help="Story title to use")
    parser.add_argument(
        "--set",
        metavar="key=value",
        action="append",
        default=[],
        help="Provide a placeholder value (repeatable)",
    )
    parser.add_argument("--show-fields", action="store_true", help="Show required fields and hints")
    parser.add_argument("--save", type=Path, help="Save the generated story to a file")
    parser.add_argument("--json", action="store_true", help="Output as JSON (for scripting)")

    args = parser.parse_args()
    engine = MadLibEngine(BUILT_IN_TEMPLATES)

    if args.list:
        for t in engine.titles:
            print(t)
        return

    if not args.story:
        parser.error("Please provide --story <title> or use --list")

    template = engine.get(args.story)

    if args.show-fields:
        fields = template.fields()
        print("Required fields:")
        for f in fields:
            hint = template.hints.get(f, "")
            print(f" - {f}" + (f"  ({hint})" if hint else ""))
        return

    values = _parse_kv(args.set)
    text = engine.render(args.story, values)

    if args.save:
        args.save.write_text(text, encoding="utf-8")

    if args.json:
        print(json.dumps({"title": args.story, "text": text}, ensure_ascii=False, indent=2))
    else:
        print(text)


if __name__ == "__main__":
    main()
