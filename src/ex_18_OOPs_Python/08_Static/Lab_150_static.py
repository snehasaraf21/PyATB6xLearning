class TestCount:
    count = 0
    def __init__(self):
        TestCount.count += 1

t1= TestCount()
t2= TestCount()
print(TestCount.count)

#each time an obj is created,count increases
#count is shared across all objects,
