class IteratorEvenNum:

    def __init__(self, n):
        self.n = n
        self.iterator_of_num = (num for num in range(n + 1) if num % 2 == 0)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator_of_num)



print("Парні числа:", end=" ")
for num in IteratorEvenNum(20):
    print(num, end=" ")