import threading


def find_largest(numbers):
    largest = max(numbers)
    print(f"Largest value: {largest}")


def find_smallest(numbers):
    smallest = min(numbers)
    print(f"Smallest value: {smallest}")


user_values = input("Enter values separated by commas: ")
values_list = [int(x) for x in user_values.split(',')]

thread_largest = threading.Thread(target=find_largest, args=(values_list,))
thread_smallest = threading.Thread(target=find_smallest, args=(values_list,))

thread_largest.start()
thread_smallest.start()

thread_largest.join()
thread_smallest.join()

def foo2(args):
    print(args)

def foo(func, args):
    func(args)

foo(foo2, args=("name", 21))