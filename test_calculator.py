import calculator

def test_divide():
    assert calculator.divide(5, 0) == "Error: You cannot divide by zero."
    assert calculator.divide(7, 49) == (1 / 7)

def test_multiply():
    assert calculator.multiply(7, -1) == -7
    assert calculator.multiply(6, 6) == 36
    assert calculator.multiply(-9, -7) == 63

def test_add():
    assert calculator.add(1, 8) == 9
    assert calculator.add(0, 9) == 9
    assert calculator.add(9, -1) == 8

def test_subtract():
    assert calculator.subtract(7, 3) == 4
    assert calculator.subtract(7, -5) == 12
    assert calculator.subtract(0, 7) == -7
    
def main():
    test_add()
    test_divide()
    test_multiply()
    test_subtract()
    
if __name__ == "__main__":
    main()