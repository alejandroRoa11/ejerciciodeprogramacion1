"""
This module contains a script to compute statistics from a file.
The statistics computed include mean, standard deviation, and mode(s).
"""
import sys
import time


def is_float(string):
    """
    Checks if a string can be converted to a float.
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def compute_statistics(filename):
    """
    Computes statistics from a given file.
    """
    start = time.time()
    with open(filename, 'r', encoding='utf-8') as file:
        archivo = file.read()
    archivo = archivo.splitlines()
    valid_numbers = []
    for line in archivo:
        if is_float(line.strip()):
            valid_numbers.append(float(line.strip()))
    n = len(valid_numbers)
    if n == 0:
        return "No se encontraron números en el archivo por cada línea"
    mean = sum(valid_numbers) / n
    valid_numbers.sort()
    l1 = [valid_numbers.count(x) for x in valid_numbers]
    d1 = dict(zip(valid_numbers, l1))
    d2 = {k for k, v in d1.items() if v == max(l1)}
    variance = sum((num - mean) ** 2 for num in valid_numbers) / n
    std_deviation = variance ** 0.5

    output = (f"Mean is: {mean}\nStandard deviation is: {std_deviation}\n"
                f"Mode(s) is/are: {d2}")
    end = time.time()
    length = end - start
    tiempo = f"\ntomó {length} segundos"

    return output + tiempo


def main():
    """
    Main function to compute statistics from a file.
    """
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        output = compute_statistics(filename)
        path = '/Users/alejandro/Desktop/statsFour/StatisticsResultsTC7.txt'
        with open(path, 'w', encoding='utf-8') as file:
            file.write(output)
        print(output)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
