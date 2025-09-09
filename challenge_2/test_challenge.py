# --- pytest tesztek ---

from challenge import char_at_index
def test_valid_index():
    assert char_at_index("Python", 0) == "P"
    assert char_at_index("Python", 5) == "n"

def test_out_of_range():
    assert char_at_index("Python", 6) == "Out of range."
    assert char_at_index("A", 2) == "Out of range."

def test_empty_string():
    assert char_at_index("", 0) == "String is empty."

def test_middle_index():
    assert char_at_index("Python", 2) == "t"

def test_unicode():
    assert char_at_index("árvíz", 1) == "r"
