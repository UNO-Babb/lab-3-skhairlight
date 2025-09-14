#ApproxPi.py
#Name: Salsabiel Khair Allah
#Date: Sep.14
#Assignment: Lab 3
import math
import time

# PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
    realPi = math.pi

    # ask user for decimal precision (up to 10)
    digits = int(input("How many decimal points to compute (0 - 10): "))
    if digits < 0 or digits > 10:
        print("Please enter a value between 0 and 10.")
        return

    start = time.time()

    # calculate pi using the approximation technique
    pi_approx = 0.0
    sign = 1
    denominator = 1

    # loop until the level of precision is reached
    while round(pi_approx, digits) != round(realPi, digits):
        pi_approx += sign * (4 / denominator)
        sign *= -1
        denominator += 2

    end = time.time()

    elapsedTime = end - start
    print(f"Pi: {round(pi_approx, digits)}")
    print(f"Calculated in {elapsedTime} seconds.")

if __name__ == '__main__':
    main()

