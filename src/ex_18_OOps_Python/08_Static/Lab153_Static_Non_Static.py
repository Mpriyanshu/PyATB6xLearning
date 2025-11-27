class MathOperations:

    def div(self, a, b):
        return a / b

    @staticmethod
    def sum(a, b):
        return a + b

# NonStatic call by the refernce
t = MathOperations()
print(t.div(10,10))

# Static call directly
print(MathOperations.sum(10,10))
