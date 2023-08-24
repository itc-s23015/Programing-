def test_function():
    try:
        print("try")
        return
    except:
        print("except")
    else:
        print("else")
    finally:
        print("finally")


print(test_function())
