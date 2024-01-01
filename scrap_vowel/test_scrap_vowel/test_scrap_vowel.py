from scrap_vowel import shorten

def test_input():
    assert shorten("word") == "wrd"

def test_ucaseinput():
    assert shorten("Education") == "dctn"

def test_allvowels():
    assert shorten("AEIOUaeioupikx") == "pkx"
