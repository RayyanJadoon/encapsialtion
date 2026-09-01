class myClass:

    __privateVariable = 37

    def __privateMeth(self):
        print("I'm inside a private class, myClass")

    def hello(self):
        print("Private variable:", myClass.__privateVariable)

obj = myClass()
obj.hello()
obj.__privateMeth()