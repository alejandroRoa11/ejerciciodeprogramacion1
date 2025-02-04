"""
This module contains a script to count the distinct words from a file
and their frequencies.
"""

import sys
import time


def main():
    """
    Main function to read a file, count distinct words and their frequencies,
    and save the results to an output file.
    """
    if len(sys.argv) != 2:
        print("Usage: python word_count.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        start = time.time()
        with open(filename, 'r', encoding='utf-8') as file:
            archivo = file.read()
        word_frequencies = {}
        output2 = "Distinct words and their frequencies:\n"
        current_word = ''
        for char in archivo:
            if char.isalnum():
                current_word += char.lower()
            else:
                if current_word != '':
                    if current_word in word_frequencies:
                        word_frequencies[current_word] += 1
                    else:
                        word_frequencies[current_word] = 1
                    current_word = ''
        if current_word != '':
            if current_word in word_frequencies:
                word_frequencies[current_word] += 1
            else:
                word_frequencies[current_word] = 1

        print("Distinct words and their frequencies:")
        for word, frequency in word_frequencies.items():
            print(f"{word}: {frequency}")

            output = f"{word}: {frequency}"
            output2 = output2 + output + "\n"
        end = time.time()
        length = end - start
        tiempo = f"\ntomó {length} segundos"
        print(tiempo)
        path = '/Users/alejandro/Desktop/statsFour/wordCountResultsTC5.txt'
        with open(path, 'w', encoding='utf-8') as file:
            file.write(output2 + tiempo)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except (FileNotFoundError, ValueError) as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
