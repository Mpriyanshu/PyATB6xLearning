def before_after_ui_test(func):

    def wrapper():
        print("Before Running UI test")
        func()
        print("After Running UI test")
    return wrapper()









@before_after_ui_test
def test_ui():
    print("Hi, i am testing a UI test ")