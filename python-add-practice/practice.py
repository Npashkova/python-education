"""Show examples for topics: generator, decorator, iterator and context manager"""
# Generator
import random


def randoms(minimum, maximum, amount):
    """Generator of numbers"""
    for _ in range(amount):
        yield random.randint(minimum, maximum)


print(next(randoms(5, 16, 3)))
for r in randoms(12, 24, 5):
    print(r)
print((randoms(5, 16, 3)))

generator = (x**8 for x in randoms(0, 10, 5))
print(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# Decorator


def my_decorator(other_func):
    """Wrapper to make all words uppercase"""
    def wrapper(argument):
        return other_func(argument).upper()
    return wrapper


@my_decorator
def rules(sentences):
    """Just get and return some sentence"""
    return sentences


print(rules('hello everybody.there are rules: ask questions.respect and listen to your classmates.\
respect and listen to the teacher.raise your hand to speak.be prepared for class.'))


def to_dict(other_func):
    """Convert func arguments to dictionary"""
    def wrapper(*args):
        dictionary = dict(other_func(*args))
        return f'New dictionary is: {dictionary}'
    return wrapper


@to_dict
def zipper(list_1, list_2):
    """Zip two lists"""
    return zip(list_1, list_2)


print(zipper([1, 2, 3, 4], ['Nastia', 'Vlad', 'Alex']))

# Iterator


class PowThree:
    """Iterator class that raise numbers to 3-d power"""
    def __init__(self, length):
        self.number = 1
        self.max = length

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > self.max:
            raise StopIteration
        result = self.number ** 3
        self.number += 1
        return result


number = PowThree(8)
# print(number)
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
for x in number:
    print(x)

# Context manager
with open('sample.txt', 'w') as opened_file:
    opened_file.write('This is a new information added.')
with open('sample.txt') as opened_file:
    opened_file.read()
print(opened_file)


class FileManager:
    """Creating context manager for file-opening"""
    def __init__(self, file_name, mode):
        self.file_obj = open(file_name, mode)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, ex_type, ex_value, ex_traceback):
        self.file_obj.close()


with FileManager('sample.txt', 'w') as file:
    file.write('This is a new information added. And some more')
print(file.closed)
with FileManager('sample.txt', 'r') as file:
    data = file.read()
print(data)
print(file.closed)

