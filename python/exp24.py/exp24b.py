# Use NumPy to create an array of ten random numbers. Calculate and display the mean, median, and standard deviation.

import numpy as np


def main():
    random_numbers = np.random.rand(10)
    print("Random numbers: ", random_numbers)

    mean = np.mean(random_numbers)
    median = np.median(random_numbers)
    std_dev = np.std(random_numbers)

    print("Mean: ", mean)
    print("Median: ", median)
    print("Standard deviation: ", std_dev)


main()
