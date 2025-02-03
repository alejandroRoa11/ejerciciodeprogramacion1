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
        mean = sum(valid_numbers) / n
        valid_numbers.sort()
        L1=[]
        i = 0
        while i < len(valid_numbers) : 
            L1.append(valid_numbers.count(valid_numbers[i])) 
            i += 1
        d1 = dict(zip(valid_numbers, L1))
        d2={k for (k,v) in d1.items() if v == max(L1)}
        print("Mode(s) is/are :" + str(d2))
        variance = sum((num - mean) ** 2 for num in valid_numbers) / n
        std_deviation = variance ** 0.5
        print(mean)
        print(std_deviation)
        
        with open('output.txt', 'w') as file:
            file.write("hallexillo  bonillos")
        print("File 'output.txt' has been created and written successfully.")

        end = time.time()
        length = end - start
        print("tomó ", length, "segundos")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

#python3 /Users/alejandro/Desktop/statsFour/computeStatistics.py /Users/alejandro/Desktop/statsFour/archivo.txt