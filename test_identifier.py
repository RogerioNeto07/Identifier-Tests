from identifier import Identifier

def test_valid_identifier():
    id = Identifier()
    assert id.validate_identifier("abc") == True 
    assert id.validate_identifier("a1b2") == True
    assert id.validate_identifier("A1b2C3") == True 

def test_valid_limitValue_identifier():
    id = Identifier()
    assert id.validate_identifier("a") == True
    assert id.validate_identifier("banana") == True 

def test_invalid_empty_identifier():
    id = Identifier()
    assert id.validate_identifier("") == False

def test_invalid_startsWithNumber_identifier():
    id = Identifier()
    assert id.validate_identifier("1abc") == False

def test_invalid_specialCharacter_identifier():
    id = Identifier()
    assert id.validate_identifier("ab_c") == False

def test_invalid_hasMoreThanSix_identifier():
    id = Identifier()
    assert id.validate_identifier("abcdefg") == False
