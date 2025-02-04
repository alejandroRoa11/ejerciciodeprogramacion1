"""
This module contains a script to convert numbers from a file
into their binary and hexadecimal representations.
"""

import sys
import time


def convert_number_to_binary_hex(number):
    """
    Converts a given number to its binary and hexadecimal representations.
    """
    binary = ""
    n = number
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2

    hexadecimal = ""
    n = number
    hex_digits = "0123456789abcdef"
    while n > 0:
        hexadecimal = hex_digits[n % 16] + hexadecimal
        n = n // 16

    return binary, hexadecimal


def main():
    """
    Main function to read numbers from a file and convert them
    to their binary and hexadecimal representations.
    """
    if len(sys.argv) != 2:
        print("Usage: python convert_numbers.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        start = time.time()
        with open(filename, 'r', encoding='utf-8') as file:
            archivo = file.read()
        archivo = archivo.splitlines()
        valid_numbers = []
        invalid_data = []
        output2 = ''

        for line in archivo:
            if line.strip().isdigit():
                valid_numbers.append(int(line.strip()))
            else:
                invalid_data.append(line.strip())

        n = len(valid_numbers)
        if n == 0:
            print("No se encontraron números en el archivo por cada línea")

        for number in valid_numbers:
            binary, hexadecimal = convert_number_to_binary_hex(number)
            print(f"Number: {number}, Binary: {binary}, Hexadecimal: {hexadecimal}")
            output = f"Number: {number} Binary: {binary} Hexadecimal: {hexadecimal}"
            output2 += output + "\n"

        end = time.time()
        length = end - start
        tiempo = f"\ntomó {length} segundos"
        path = '/Users/alejandro/Desktop/statsFour/convertionResultsTC5.txt'
        with open(path, 'w', encoding='utf-8') as file:
            file.write(output2 + tiempo)

        print(output + tiempo)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
