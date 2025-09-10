from challenge import reverse_string

def test_basic():
    assert reverse_string("Python") == "nohtyP"

def test_empty():
    assert reverse_string("") == ""

def test_single_char():
    assert reverse_string("A") == "A"

def test_palindrome():
    assert reverse_string("racecar") == "racecar"  # palindróm marad ugyanaz

def test_unicode():
    assert reverse_string("árvíztűrő tükörfúrógép") == "pégórúfröküt őrűztívrá"
