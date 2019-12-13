# exercise from https://py.checkio.org/
# Your mission here is to create a function that gets a tuple and returns
# a tuple with 3 elements - the first, third
# and second to the last for the given array.


def easy_unpack(elements: tuple) -> tuple:
    return elements[0], elements[2], elements[-2]


if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
