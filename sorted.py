import doctest


def is_sorted(number_list):
    """
    Display the list of integers in non-decreasing order.

    A function that displays the list of integers in non-decreasing order.

    :param number_list: a list of integers
    :precondition: list must contain only integers
    :postcondition: displays the list of integers in non-decreasing order
    :return: True if list is sorted in non-decreasing order or False if it is not
    >>> is_sorted([1, 2, 3])
    True
    >>> is_sorted([3, 1, 5])
    False
    """

    if list == sorted(list):
        return True
    else:
        return False



def main():
    doctest.testmod(verbose=True)
    print(is_sorted([5, 4, 1]))


if __name__ == "__main__":
    main()