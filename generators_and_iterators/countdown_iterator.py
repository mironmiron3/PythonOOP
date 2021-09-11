class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.current_num = self.count

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_num >= 0:
            value = self.current_num
            self.current_num -= 1
            return value
        raise StopIteration

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

