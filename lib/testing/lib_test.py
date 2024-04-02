import pytest
from lib.list_comprehension import return_evens, make_exclamation

def test_return_evens():
    assert return_evens([0, 1, 3, 5, 7, 8, 9]) == [0, 8]
    assert return_evens([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]
    assert return_evens([1, 3, 5, 7, 9]) == []

def test_make_exclamation():
    assert make_exclamation(["Hello", "I'm doing great", "Python is fun"]) == ["Hello!", "I'm doing great!", "Python is fun!"]
    assert make_exclamation(["Yes", "No", "Maybe"]) == ["Yes!", "No!", "Maybe!"]
    assert make_exclamation([]) == []

if __name__ == "__main__":
    pytest.main()
