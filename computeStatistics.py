import sys
import time

def main():
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        def is_float(string):
            try:
                float(string)
                return True
            except ValueError:
                return False

        start = time.time()
        with open(filename, 'r') as file:
            archivo = file.read()
        archivo = archivo.splitlines()
        valid_numbers = []
        invalid_data = []
        output = ""
        for line in archivo:
            if is_float(line.strip()):
                valid_numbers.append(float(line.strip()))
            else:
                invalid_data.append(line.strip())
        n = len(valid_numbers)
        if n == 0:
            print ("No se encontraron números en el archivo por cada línea")
        else:
            mean = sum(valid_numbers) / n
            valid_numbers.sort()
            L1=[]
            i = 0
            while i < len(valid_numbers) : 
                L1.append(valid_numbers.count(valid_numbers[i])) 
                i += 1
            d1 = dict(zip(valid_numbers, L1))
            d2={k for (k,v) in d1.items() if v == max(L1)}
            variance = sum((num - mean) ** 2 for num in valid_numbers) / n
            std_deviation = variance ** 0.5

            output = "Mean is: "+str(mean)+"\nStandard deviation is: "+str(std_deviation)+"\nMode(s) is/are :" + str(d2)
        end = time.time()
        length = end - start
        tiempo = "\ntomó "+str(length)+"segundos"

        with open('/Users/alejandro/Desktop/statsFour/StatisticsResults.txt', 'w') as file:
            file.write(output+tiempo)
        print(output+tiempo)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

#python3 /Users/alejandro/Desktop/statsFour/computeStatistics.py /Users/alejandro/Desktop/statsFour/archivo.txt
#python3 /Users/alejandro/Desktop/statsFour/computeStatistics.py /Users/alejandro/Desktop/codigoQualitySoftware/ArchivosDeApoyo/P1/TC1.txt
#python3 /Users/alejandro/Desktop/statsFour/computeStatistics.py /Users/alejandro/Desktop/codigoQualitySoftware/ArchivosDeApoyo/P1/TC2.txt
#python3 /Users/alejandro/Desktop/statsFour/computeStatistics.py /Users/alejandro/Desktop/codigoQualitySoftware/ArchivosDeApoyo/P1/TC3.txt
#python3 /Users/alejandro/Desktop/statsFour/computeStatistics.py /Users/alejandro/Desktop/codigoQualitySoftware/ArchivosDeApoyo/P1/TC4.txt
#python3 /Users/alejandro/Desktop/statsFour/computeStatistics.py /Users/alejandro/Desktop/codigoQualitySoftware/ArchivosDeApoyo/P1/TC5.txt
#python3 /Users/alejandro/Desktop/statsFour/computeStatistics.py /Users/alejandro/Desktop/codigoQualitySoftware/ArchivosDeApoyo/P1/TC6.txt
#python3 /Users/alejandro/Desktop/statsFour/computeStatistics.py /Users/alejandro/Desktop/codigoQualitySoftware/ArchivosDeApoyo/P1/TC7.txt