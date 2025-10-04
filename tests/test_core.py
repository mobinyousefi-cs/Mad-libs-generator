import pytest

from madlibs.core import MadLibEngine, StoryTemplate


def _engine():
    t = StoryTemplate(
        title="T",
        text="Hello {name}, eat {food}.",
        hints={"name": "person", "food": "meal"},
        tags={"test"},
        difficulty="beginner",
    )
    return MadLibEngine([t])


def test_fields_extraction():
    t = StoryTemplate(title="X", text="A {a} B {b} C {a}")
    assert t.fields() == ["a", "b"]  # unique, preserves first-seen order


def test_render_success():
    eng = _engine()
    out = eng.render("T", {"name": "Mobin", "food": "pizza"})
    assert "Mobin" in out and "pizza" in out


def test_missing_fields():
    eng = _engine()
    with pytest.raises(KeyError):
        eng.render("T", {"name": "Mobin"})  # missing 'food'


def test_invalid_characters():
    eng = _engine()
    with pytest.raises(ValueError):
        eng.render("T", {"name": "Mobin{", "food": "pizza"})
