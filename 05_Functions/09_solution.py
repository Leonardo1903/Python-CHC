def even_generator(limit):
    for i in range(2, limit + 1,2):
        yield i

limit = int(input("Enter the limit: "))
for num in even_generator(limit):
    print(num)