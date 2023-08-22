#!/usr/bin/env python3


def print_fibonacci(length):
    my_list = []

    # if empty and length longer than 0, start with 0
    if length > 0:
        my_list.append(0)

        # if length longer than 1, add 1 to sequence
        if length > 1:
            my_list.append(1)

            # if length longer than 2, start looping (at 2)
            if length > 2:
                i = 2

                # loop until we have met length parameter
                while i < length:
                    # append number that takes a position and the position behind it and add the values in those positions together
                    my_list.append(my_list[i - 2] + my_list[i - 1])

                    # increase i to move up a "position"
                    i += 1

    print(my_list)
