#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Mad Libs Generator
File: gui.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-04
Updated: 2025-10-04
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
Tkinter GUI for the Mad Libs app. Choose a story, fill in fields, preview, and save.

Usage:
python -m madlibs.gui
"""

from __future__ import annotations

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from typing import Dict

from .core import MadLibEngine
from .templates import BUILT_IN_TEMPLATES


class MadLibsApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Mad Libs Generator")
        self.geometry("720x560")
        self.minsize(640, 520)

        self.engine = MadLibEngine(BUILT_IN_TEMPLATES)
        self._field_vars: Dict[str, tk.StringVar] = {}

        self._build_widgets()

    # --- UI construction -----------------------------------------------------
    def _build_widgets(self) -> None:
        container = ttk.Frame(self, padding=12)
        container.pack(fill="both", expand=True)

        # Story selector
        top = ttk.Frame(container)
        top.pack(fill="x", pady=(0, 8))

        ttk.Label(top, text="Story:").pack(side="left")
        self.story_var = tk.StringVar(value=self.engine.titles[0])
        self.story_combo = ttk.Combobox(
            top, textvariable=self.story_var, values=self.engine.titles, state="readonly"
        )
        self.story_combo.pack(side="left", padx=8)
        self.story_combo.bind("<<ComboboxSelected>>", lambda e: self._rebuild_fields())

        ttk.Button(top, text="Show Fields", command=self._show_fields).pack(side="left", padx=6)
        ttk.Button(top, text="Clear", command=self._clear_fields).pack(side="left", padx=6)

        # Dynamic fields area
        self.fields_frame = ttk.LabelFrame(container, text="Fill the blanks")
        self.fields_frame.pack(fill="x", pady=8)
        self._rebuild_fields()

        # Output area
        self.output = tk.Text(container, height=15, wrap="word")
        self.output.pack(fill="both", expand=True, pady=(8, 8))

        # Action buttons
        actions = ttk.Frame(container)
        actions.pack(fill="x")
        ttk.Button(actions, text="Generate", command=self._generate).pack(side="left")
        ttk.Button(actions, text="Save...", command=self._save).pack(side="left", padx=8)

        # Status
        self.status_var = tk.StringVar(value="Ready.")
        ttk.Label(container, textvariable=self.status_var, foreground="#555").pack(
            anchor="w", pady=(6, 0)
        )

    def _rebuild_fields(self) -> None:
        for child in self.fields_frame.winfo_children():
            child.destroy()
        self._field_vars.clear()

        title = self.story_var.get()
        tmpl = self.engine.get(title)
        fields = tmpl.fields()

        for i, name in enumerate(fields):
            row = ttk.Frame(self.fields_frame)
            row.pack(fill="x", pady=3)
            hint = tmpl.hints.get(name, "")
            ttk.Label(row, text=f"{name}:").pack(side="left", padx=(6, 8))
            var = tk.StringVar()
            ent = ttk.Entry(row, textvariable=var)
            ent.pack(side="left", fill="x", expand=True)
            if hint:
                ttk.Label(row, text=hint, foreground="#777").pack(side="left", padx=8)
            self._field_vars[name] = var

    # --- Actions -------------------------------------------------------------
    def _show_fields(self) -> None:
        tmpl = self.engine.get(self.story_var.get())
        msg = "Required fields:\n" + "\n".join(
            f"• {f}" + (f" — {tmpl.hints[f]}" if f in tmpl.hints else "") for f in tmpl.fields()
        )
        messagebox.showinfo("Fields", msg)

    def _clear_fields(self) -> None:
        for v in self._field_vars.values():
            v.set("")
        self.output.delete("1.0", tk.END)
        self.status_var.set("Cleared.")

    def _generate(self) -> None:
        try:
            values = {k: v.get().strip() for k, v in self._field_vars.items()}
            text = self.engine.render(self.story_var.get(), values)
        except Exception as exc:  # KeyError / ValueError surfaced to user
            messagebox.showerror("Error", str(exc))
            return
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, text)
        self.status_var.set("Story generated.")

    def _save(self) -> None:
        content = self.output.get("1.0", tk.END).strip()
        if not content:
            messagebox.showwarning("Nothing to save", "Generate a story first.")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Save Story",
        )
        if not path:
            return
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        self.status_var.set(f"Saved to: {path}")


def main() -> None:
    app = MadLibsApp()
    app.mainloop()


if __name__ == "__main__":
    main()
