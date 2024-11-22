import calculator

def test_divide():
    assert calculator.divide(5, 0)
    assert calculator.divide(7, 49)

def test_multiply():
    assert calculator.multiply(7, -1)
    assert calculator.multiply(6, 6)
    assert calculator.multiply(-9, -7)
    assert calculator.multiply(0, 9)

def test_add():
    assert calculator.add(1, 8)
    assert calculator.add(0, 9)
    assert calculator.add(9, -1)

def test_subtract():
    assert calculator.subtract(7, 3)
    assert calculator.subtract(7, -5)
    assert calculator.subtract(0, 7)
    
def main():
    test_add()
    test_divide()
    test_multiply()
    test_subtract()
    
if __name__ == "__main__":
    main()