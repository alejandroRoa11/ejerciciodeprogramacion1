import sys
import time

def main():
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        start = time.time()
        with open(filename, 'r') as file:
            archivo = file.read()
        #archivo = archivo.splitlines()
        word_frequencies = {}
        # Initialize variables to process each word
        current_word = ''
        for char in archivo:
            # Check if the character is a letter or a number (part of a word)
            if char.isalnum():
                current_word += char.lower()
            else:
                if current_word != '':
                    # If the word is not already in the dictionary, add it
                    if current_word in word_frequencies:
                        word_frequencies[current_word] += 1
                    else:
                        word_frequencies[current_word] = 1

                    # Reset the current word
                    current_word = ''
        
        # Check the last word in the file
        if current_word != '':
            if current_word in word_frequencies:
                word_frequencies[current_word] += 1
            else:
                word_frequencies[current_word] = 1

        # Print the results
        print("Distinct words and their frequencies:")
        for word, frequency in word_frequencies.items():
            print(f"{word}: {frequency}")
        end = time.time()
        length = end - start
        print("tomó ", length, "segundos")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

#python3 /Users/alejandro/Desktop/statsFour/wordCount.py /Users/alejandro/Desktop/statsFour/archivo.txt