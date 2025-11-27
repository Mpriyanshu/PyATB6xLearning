class BaseCounter:
    count = 0

    def __init__(self):
        BaseCounter.count += 1

t1 = BaseCounter()
t2 = BaseCounter()
t3 = BaseCounter()
print(BaseCounter.count)