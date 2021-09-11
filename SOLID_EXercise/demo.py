my_List = [1, 2, 3, 4]

a = (x** 2 for x in my_List)

while True:
    try:
        next(a)

    except StopIteration:
        break


