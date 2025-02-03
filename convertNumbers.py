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
        archivo = archivo.splitlines()
        valid_numbers = []
        invalid_data = []
        for line in archivo:
            if line.strip().isdigit():
                valid_numbers.append(int(line.strip()))
            else:
                invalid_data.append(line.strip())
        n = len(valid_numbers)
        if n == 0:
            print ("No se encontraron números en el archivo por cada línea")

        for number in valid_numbers:
            binary = ""
            n = number
            while n > 0:
                binary = str(n % 2) + binary
                n = n // 2

            # Convert the number to hexadecimal
            hexadecimal = ""
            n = number
            hex_digits = "0123456789abcdef"
            while n > 0:
                hexadecimal = hex_digits[n % 16] + hexadecimal
                n = n // 16
            print(f"Number: {number}, Binary: {binary}, Hexadecimal: {hexadecimal}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

        end = time.time()
        length = end - start
        print("tomó ", length, "segundos")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

#python3 /Users/alejandro/Desktop/statsFour/convertNumbers.py /Users/alejandro/Desktop/statsFour/archivo.txt