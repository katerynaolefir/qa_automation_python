class IteratorReverseList:

    def __init__(self, n):
        self.numbers = list(range(n))
        self.iterator_of_num = iter(reversed(self.numbers))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator_of_num)



print("Список у зворотному порядку:", end=" ")
for num in IteratorReverseList(20):
    print(num, end=" ")