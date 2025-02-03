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
        output = ""
        output2 = ''
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
            hexadecimal = ""
            n = number
            hex_digits = "0123456789abcdef"
            while n > 0:
                hexadecimal = hex_digits[n % 16] + hexadecimal
                n = n // 16
            print(f"Number: {number}, Binary: {binary}, Hexadecimal: {hexadecimal}")
            output = "Number: "+str(number)+" Binary: "+str(binary)+"Hexadecimal: "+str(hexadecimal)
            output2 = output2 + output+"\n"
        end = time.time()
        length = end - start
        tiempo = "\ntomó "+str(length)+"segundos"
        with open('/Users/alejandro/Desktop/statsFour/convertionResults.txt', 'w') as file:
            file.write(output2+tiempo)
        print(output+tiempo)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

#python3 /Users/alejandro/Desktop/statsFour/convertNumbers.py /Users/alejandro/Desktop/statsFour/archivo.txt

#python3 /Users/alejandro/Desktop/statsFour/convertNumbers.py /Users/alejandro/Desktop/codigoQualitySoftware/ArchivosDeApoyo/P2/TC1.txt
#python3 /Users/alejandro/Desktop/statsFour/convertNumbers.py /Users/alejandro/Desktop/codigoQualitySoftware/ArchivosDeApoyo/P2/TC2.txt
#python3 /Users/alejandro/Desktop/statsFour/convertNumbers.py /Users/alejandro/Desktop/codigoQualitySoftware/ArchivosDeApoyo/P2/TC3.txt
#python3 /Users/alejandro/Desktop/statsFour/convertNumbers.py /Users/alejandro/Desktop/codigoQualitySoftware/ArchivosDeApoyo/P2/TC4.txt