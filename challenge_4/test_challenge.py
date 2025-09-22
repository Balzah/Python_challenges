from challenge import first_and_last_three

def test_basic():
    assert first_and_last_three("Python") == "Python"  # Py(n)...hon

def test_exactly_three_chars():
    assert first_and_last_three("abc") == "abcabc"  # első 3 + utolsó 3 ugyanaz

def test_short_string():
    assert first_and_last_three("hi") == "hi"  # rövidebb mint 3

def test_empty_string():
    assert first_and_last_three("") == ""  # üres string

def test_unicode():
    assert first_and_last_three("abraka dabra") == "abrbra"  # első 3 + utolsó 3
