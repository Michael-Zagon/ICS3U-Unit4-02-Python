#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Sep 2021
# This program multiplies each whole number that goes up to the users number


def main():
    # This function multiplies each whole number that goes up to the users number
    counter = 1
    the_product = 1

    # Input
    integer_a_s = input("Enter a positive number: ")
    print("")

    # Process and Output
    try:
        integer_a_i = int(integer_a_s)
        while counter <= integer_a_i:
            the_product = the_product * counter
            counter = counter + 1
        print(
            "The product of all positive numbers from 1 to {0} is {1}.".format(
                integer_a_s, the_product
            )
        )

    except Exception:
        print("Invalid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
