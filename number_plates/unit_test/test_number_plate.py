from number_plate import plate_regulation

def test_alphabets_plates():
        assert plate_regulation("ABCDE") == True


def test_alphanum_plates():
    assert plate_regulation("abc120") == True


def test_shorten_plates():

    assert plate_regulation("DRIVE") == True


def test_error():
     assert plate_regulation("P3INKMAN") == False



