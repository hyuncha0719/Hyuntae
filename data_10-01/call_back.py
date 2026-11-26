# def callback(num):
#    # global count
#    num -= 1
#    if num == 0:
#        print("Counter reached zero,stopping the program.")
#       return
#    print("callback function called, count:", num)
#    callback(num)
#   print("callback function called, count:", num)

# callback(3)


def add_numbers(start, end):
    if end <= start:
        return 1
    else:
        return end + add_numbers(start,end-1)

print(add_numbers(1,10))

# def add_numbers(start, end):
#    foo = start + end
#    bar = foo * end
#    woo = bar / 2
#   print("woo:", woo)

# add_numbers(1, 1000000000)


def factorial(n):
    if n <= 1:
        return 1
    print("n:", n)
    foo = factorial(n - 1)
    print("n:", n)
    return n * foo

print(factorial(5))

def countdown(n):
    for i in range(n, 0, -1):
        print(i)
    print("발사!")

countdown(5)

def print_starts(n):
    if n <= 0:
        print("발사!")
        return
    print_starts(n - 1)
    print("*" * n)

print_starts(5)

def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:4}", end=" ")
        print()

multiplication_table(5)