"""Unit tests for dictionary functions."""
 

from exercises.ex06.dictionaries import invert, favorite_color, count


__author__ = "730466575"


def test_same_key_in_invert() -> None:
    a = {"string": "bean", "pinto": "bean"}
    assert invert(a) == KeyError("Two of the same key.")


def test_phrase_invert() -> None:
    a = {"hello": "there", "my": "friend"}
    assert invert(a) == {"there": "hello", "friend": "my"}  


def test_normal_invert() -> None:
    a = {"string": "bean", "blue": "bird"}
    assert invert(a) == {"bean": "string", "bird": "blue"}  


def test_all_different_colors() -> None:
    colors = {"Karl": "orange", "Daniel": "red", "James": "purple"}
    assert favorite_color(colors) == "orange"


def test_tie_colors() -> None:
    colors = {"Karl": "purple", "Daniel": "orange", "James": "purple", "Blake": "orange"}
    assert favorite_color(colors) == "purple"


def test_singal_popular_colors():
    colors = {"Karl": "red", "Daniel": "red", "James": "purple"}
    assert favorite_color(colors) == "red"


def test_all_different_count():
    classes = ["math", "science", "english"]
    assert count(classes) == {"math": 1, "science": 1, "english": 1}


def test_repeated_classes_count():
    classes = ["math", "science", "english", "science"]
    assert count(classes) == {"math": 1, "science": 2, "english": 1}


def test_no_classes_count():
    classes = []
    assert count(classes) == {}