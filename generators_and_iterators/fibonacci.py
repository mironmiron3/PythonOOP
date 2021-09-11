def fibonacci():
    list_of_created_nums = []
    yield 0
    list_of_created_nums.append(0)
    yield 1
    list_of_created_nums.append(1)

    index = 2
    while True:
        num = list_of_created_nums[index - 1] + list_of_created_nums[index - 2]
        index += 1
        list_of_created_nums.append(num)
        yield num

generator = fibonacci()
print(type(generator))
for i in range(100):
    print(next(generator))

