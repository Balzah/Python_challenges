import challenge

def test():
    test_string = "string1"
    assert challenge.length_of_string(test_string) == 7

def test_empty():
    test_string = ""
    assert challenge.length_of_string(test_string) == 0